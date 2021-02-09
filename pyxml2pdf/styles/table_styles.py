from pathlib import PurePath
from typing import Dict, List, Tuple, Union

from reportlab.lib import colors  # type: ignore
from reportlab.lib.pagesizes import mm  # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, StyleSheet1  # type: ignore
from reportlab.pdfbase.pdfmetrics import (
    registerFont,
    registerFontFamily,  # type: ignore
)
from reportlab.pdfbase.ttfonts import TTFont  # type: ignore

from input.properties import columns, font, fontsize  # type: ignore
from .cell_formattings import CellFormattingCommands


class TableStyle:
    """ Create a collection of styling information about the table to create

    Beautiful colors are:
        *   aliceblue (nicht mit azure)
        *   azure (nicht mit aliceblue)
        *   honeydew
        * ...
    """

    _column_widths: List[float]
    _table_width: float
    _custom_styles: Dict[str, Union[Tuple[str, ...], StyleSheet1]] = {}

    def __init__(self):
        self._custom_styles["heading"] = [
            CellFormattingCommands.valign_middle,
            CellFormattingCommands.background(colors.honeydew),
            CellFormattingCommands.box(colors.black),
            CellFormattingCommands.inner_grid(colors.black),
            CellFormattingCommands.align_center,
        ]

        self._custom_styles["normal"] = [
            CellFormattingCommands.align_left,
            CellFormattingCommands.valign_middle,
            CellFormattingCommands.box(colors.black),
            CellFormattingCommands.inner_grid(colors.black),
            CellFormattingCommands.leftpadding_reduce,
            CellFormattingCommands.rightpadding_reduce,
        ]

        self._custom_styles["sub_heading"] = self._custom_styles["normal"]

        self._custom_styles["sub_heading"] = self._custom_styles["normal"]

        # Extract the column widths from properties.
        self._column_widths = [float(column["width"]) * mm for column in columns]

        # Set the resulting tables' styling with all the customization of
        # margins, fonts, fontsizes, etc...

        # Get custom_styles for all headings, texts, etc. from sample
        custom_styles = getSampleStyleSheet()
        # Overwrite the sample styles according to our needs.
        custom_styles.get("Normal").fontSize = fontsize["normal"]
        custom_styles.get("Normal").leading = custom_styles["Normal"].fontSize * 1.2
        custom_styles.get("Normal").fontName = "normal_font"
        custom_styles.get("Italic").fontSize = custom_styles["Normal"].fontSize
        custom_styles.get("Italic").leading = custom_styles["Italic"].fontSize * 1.2
        custom_styles.get("Italic").fontName = "italic_font"
        custom_styles.get("Heading1").fontSize = fontsize["table_heading"]
        custom_styles.get("Heading1").alignment = 1
        custom_styles.get("Heading1").leading = custom_styles["Heading1"].fontSize * 1.2
        custom_styles.get("Heading1").fontName = "bold_font"
        custom_styles.get("Heading2").fontSize = fontsize["column_heading"]
        custom_styles.get("Heading2").alignment = 1
        custom_styles.get("Heading2").leading = custom_styles["Heading2"].fontSize * 1.2
        custom_styles.get("Heading2").fontName = "bold_font"
        self._custom_styles["stylesheet"] = custom_styles

        # Register font with reportlab.
        self._init_font_family()

    @staticmethod
    def _init_font_family():
        """Register the desired font with :py:mod:`reportlab`

        This ensures that `<i></i>` and `<b></b>` as cell content work well.
        """
        # Set root of fonts to the folder containing this file.
        path_to_fonts = PurePath(__file__).parent.joinpath("fonts")

        # Finally lead and register fonts with reportlab.
        registerFont(TTFont("normal_font", path_to_fonts.joinpath(font["normal"])))
        registerFont(TTFont("bold_font", path_to_fonts.joinpath(font["bold"])))
        registerFont(TTFont("italic_font", path_to_fonts.joinpath(font["italic"])))
        registerFont(
            TTFont("bolditalic_font", path_to_fonts.joinpath(font["bolditalic"]))
        )
        registerFontFamily(
            "custom_font",
            normal="normal_font",
            bold="bold_font",
            italic="italic_font",
            boldItalic="bolditalic_font",
        )

    @property
    def column_widths(self):
        """Return the column widths for the tables

        :returns: the list of column widths in mm
        :rtype: List[float]
        """
        return self._column_widths

    @property
    def table_width(self) -> float:
        """Return the full table width

        :returns: the sum of all column widths in mm
        """
        # Return table width unless not yet initialized, then initialize and return.
        try:
            return self._table_width
        except AttributeError:
            self._table_width = sum(set(self._column_widths))
            return self._table_width

    @property
    def custom_styles(self) -> Dict[str, Union[Tuple[str, ...], StyleSheet1]]:
        """Return the custom styles and stylesheet for the tables

        :returns: the custom styles and stylesheet in the Form
            ::
                custom_styles = {
                    "heading": List[Styles],
                    "normal": List[Styles],
                    "sub_heading": List[Styles],
                    "stylesheet": StyleSheet1
                }
        """
        return self._custom_styles
