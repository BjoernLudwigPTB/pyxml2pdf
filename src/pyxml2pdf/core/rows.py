"""This module contains the base class to create table rows

Specifically it contains a class :class:`XMLCell` for unified styled cells and
a class :class:`XMLRow` for xml extracted data.
"""
from typing import cast, List, Set, Type

import defusedxml  # type: ignore
from reportlab.lib.styles import StyleSheet1  # type: ignore
from reportlab.platypus import Paragraph, Table  # type: ignore

from pyxml2pdf.input.properties import (
    columns,
    filter_xmltag,
    identifier_xmltag,
)  # type: ignore
from pyxml2pdf.styles.table_styles import XMLTableStyle
from pyxml2pdf.tables.builder import TableBuilder

# Monkeypatch standard library xml vulnerabilities.
defusedxml.defuse_stdlib()
from xml.etree.ElementTree import Element

__all__ = ["XMLCell", "XMLRow"]


class XMLCell(Paragraph):
    """This class represents the text of type reportlab.platypus.Paragraph in a cell

    It inherits from :class:`reportlab.platypus.Paragraph` and ensures the
    unified styling of all table cells.

    :py:class:`reportlab.platypus.Paragraph` is solely used with one
    certain style, which is supposed to be set as a class attribute during runtime.

    :param str text: the text to write into row
    """

    _style: StyleSheet1

    def __init__(self, text: str):
        super().__init__(text, self.style)

    @property
    def style(self) -> StyleSheet1:
        """StyleSheet1: The one for all stylesheet to style all cells."""
        return self._style

    @style.setter
    def style(self, value: StyleSheet1):
        self._style = value


class XMLRow(Element):
    """A wrapper class for :py:class:`xml.etree.ElementTree.Element`

    :py:class:`xml.etree.ElementTree.Element` is augmented with the table row
    representation and the attributes and methods to manipulate everything
    according to the final tables needs. A :py:class:`XMLRow` can only be initialized
    with an object of type :py:class:`xml.etree.ElementTree.Element`.

    :param xml.etree.ElementTree.Element element: the element to build the instance from
    """

    _table_builder: TableBuilder = TableBuilder()
    _table_style: XMLTableStyle = XMLTableStyle()

    _criteria: Set[str]
    _identifier: str
    _cell_styler: Type[XMLCell] = XMLCell

    def __init__(self, element):
        # Call Element constructor and extend ourselves by extending all children
        # tags to create an underlying copy of element.
        super().__init__(element.tag, element.attrib)
        self.extend(list(element))
        # Initialize needed objects especially for table creation.
        self._cell_styler.style = self._table_style.custom_styles["stylesheet"][
            "Normal"
        ]
        # Initialize definitely needed instance variables.
        self._criteria = self._init_criteria()
        self._identifier = self._concatenate_tags_content(identifier_xmltag)
        self._mandatory_columns = self._init_full_row()

    def _init_criteria(self):
        """Initialize the list of criteria from the according xml tag's content"""
        criteria: str = self._concatenate_tags_content([filter_xmltag])
        return set(criteria.split(", "))

    def _concatenate_tags_content(
        self, cell_tags: List[str], separator: str = " - "
    ) -> str:
        """Form one string from the texts of a set of XML tags's to fill a cell

        Form a string of the content for all desired XML tags by
        concatenating them together with a separator. This is especially necessary,
        since :py:mod:`reportlab.platypus.Paragraph` cannot handle `None`s as texts but
        handles as well the concatenation of XML tags' content, if `cell_tags`
        has more than one element. So we ensure the result to be at least an empty
        string.

        :param cell_tags: list of all tags for which the
            descriptive texts is wanted, even if it is just one
        :param separator: the separator in between the concatenated texts
        :returns: concatenated, separated texts of all tags for the current cell
        """
        return separator.join(
            [cast(str, self.findtext(tag)) for tag in cell_tags if self.findtext(tag)]
        )

    def _init_full_row(self) -> List[XMLCell]:
        """Initialize the single table row containing all information from the XML input

        Extract interesting information from specified row tag's subtags and
        connect them into a nicely formatted row of a table.

        :return: the columns of any table representation
        :rtype: List[XMLCell]
        """
        table_columns = [
            self._cell_styler(self._concatenate_tags_content(column.tag))
            for column in columns
        ]
        self._full_row = self._table_builder.create_fixedwidth_table([table_columns])
        return table_columns

    def get_full_row(self, subtable_title: str = None) -> Table:
        """Return a table row with all the row's information

        This ensures, that in subclasses we can override this function and after
        handing over the full information, the reduced version with a reference to
        the subtable containing the full version can be created via a decorator.

        See :class:`Event` for an example implementation of this pattern.

        :param subtable_title: the title of the subtable in which the row will
            be integrated
        :returns: a table row with all the event's information
        """
        return self._full_row

    @property
    def criteria(self) -> Set[str]:
        """Return the event's criteria

        :returns: a list of the event's criteria
        :rtype: Set[str]
        """
        return self._criteria

    @property
    def identifier(self) -> str:
        """Return the identifier of the event

        :returns: identifier
        :rtype: str
        """
        return self._identifier

    def get_table_row(self, subtable_title: str) -> Table:
        """Return the table row representation of the XML tag

        This is the API of :py:class:`XMLRow` for getting the
        table row representation of the event. It allows for reacting to the
        distribution of the XML tags content by creating a shorter version
        referencing the main subtable. See :meth:`get_full_row` for details.

        :param str subtable_title: the title of the subtable in which the row will
            be integrated
        :returns: a table row representation of the XML tag's content
        :rtype: Table
        """
        # We check if the reduced row was produced before, which means in turn,
        # that :meth:`get_table_row` was called at least once before. Otherwise we call
        # :meth:`get_full_row` which automatically triggers the creation of the
        # reduced row for later uses.
        try:
            return self._reduced_row
        except AttributeError:
            return self.get_full_row(subtable_title)
