"""This module contains a class :class:`XMLTable` to collect the XML's content."""

from typing import List

from reportlab.platypus import Table  # type:ignore


class XMLTable:
    """An :class:`XMLTable` contains a subset of the xml file's content in a Table

    Contains all XML tags which match the desired content specified in :attr:`content`.
    Every XML tag listed has at least one subtag from each of the lists in
    :attr:`content`.

    :param str title: Name of the table
    :param List[List[str]] include_filters: nested list of criteria to collect in table
    """

    def __init__(self, title: str, include_filters: List[List[str]]):
        """Initialize a table containing a subset of the XML data"""
        self._rows = []  # type: List[Table]
        self._title = title  # type: str
        self._include_filters = include_filters  # type: List[List[str]]

    def append(self, row: Table):
        """Append a row to the end of the table

        :param row: a single row that should be appended to the table
        """
        self.rows.append(row)

    def extend(self, rows: List[Table]):
        """Append a a list of rows to the end of the table

        :param rows: a list of rows that should be appended to the table
        """
        self.rows.extend(rows)

    @property
    def rows(self) -> List[Table]:
        """List[Table]: The list of rows as Table objects"""
        return self._rows

    @rows.setter
    def rows(self, value: List[Table]):
        self._rows = value

    @property
    def title(self) -> str:
        """str: Name of the table"""
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def include_filters(self) -> List[List[str]]:
        """List[List[str]]: include_filters to match XML contents for including"""
        return self._include_filters

    @include_filters.setter
    def include_filters(self, value: List[List[str]]):
        self._include_filters = value
