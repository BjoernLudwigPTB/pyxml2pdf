"""This module contains the class :class:`XMLTableStyle` to style the result"""

from pathlib import PurePath
from typing import Dict, List, Tuple, Union

from reportlab.lib.colors import black, Color, honeydew  # type: ignore
from reportlab.lib.pagesizes import mm  # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, StyleSheet1  # type: ignore
from reportlab.pdfbase.pdfmetrics import (  # type: ignore
    registerFont,
    registerFontFamily,
)
from reportlab.pdfbase.ttfonts import TTFont  # type: ignore
from reportlab.platypus import TableStyle  # type: ignore

from pyxml2pdf.input.properties import columns, font, fontsize  # type: ignore

LineFormattingCommand = Tuple[str, Tuple[int, int], Tuple[int, int], float, Color]
CellFormattingCommand = Tuple[
    str, Tuple[int, int], Tuple[int, int], Union[Color, float, str]
]


class XMLTableStyle:
    """Create a collection of styling information about the table to create

    Beautiful colors are:
        *   aliceblue (not with azure)
        *   azure (not with aliceblue)
        *   honeydew
        * ...
    """

    # Prepare a reusable constant for assigning settings to all cells of an area.
    FULL_ROW = (
        (0, 0),
        (-1, -1),
    )  # type: Tuple[Tuple[int, int], Tuple[int, int]]

    # Set important defaults for the table.
    LINE_THICKNESS = 0.25  # type: float
    LINE_COLOR = black  # type: Color
    BACKGROUND_COLOR = honeydew  # type: Color
    PADDING = 3  # type: int

    ALIGN_CENTER = ("ALIGN", *FULL_ROW, "CENTER")  # type: CellFormattingCommand
    VALIGN_MIDDLE = ("VALIGN", *FULL_ROW, "MIDDLE")  # type: CellFormattingCommand
    VALIGN_TOP = ("VALIGN", *FULL_ROW, "TOP")  # type: CellFormattingCommand
    ALIGN_LEFT = ("ALIGN", *FULL_ROW, "LEFT")  # type: CellFormattingCommand
    LEFTPADDING_REDUCE = (
        "LEFTPADDING",
        *FULL_ROW,
        PADDING,
    )  # type: CellFormattingCommand
    RIGHTPADDING_REDUCE = (
        "RIGHTPADDING",
        *FULL_ROW,
        PADDING,
    )  # type: CellFormattingCommand
    BACKGROUND = (
        "BACKGROUND",
        *FULL_ROW,
        BACKGROUND_COLOR,
    )  # type: CellFormattingCommand
    BOX = ("BOX", *FULL_ROW, 0.25, LINE_COLOR)  # type: LineFormattingCommand
    INNERGRID = (
        "INNERGRID",
        *FULL_ROW,
        LINE_THICKNESS,
        LINE_COLOR,
    )  # type: LineFormattingCommand

    def __init__(self):
        """Initialise font and cell formatting"""
        self._font = font

        # Set the resulting tables' styling with all the customization of
        # margins, fonts, fontsizes, etc...

        # Get custom_styles for all headings, texts, etc. from sample
        custom_stylesheet = getSampleStyleSheet()
        # Overwrite the sample styles according to our needs.
        custom_stylesheet.get("Normal").fontSize = fontsize.normal
        custom_stylesheet.get("Normal").leading = (
            custom_stylesheet["Normal"].fontSize * 1.2
        )
        custom_stylesheet.get("Normal").fontName = "normal_font"
        custom_stylesheet.get("Italic").fontSize = custom_stylesheet["Normal"].fontSize
        custom_stylesheet.get("Italic").leading = (
            custom_stylesheet["Italic"].fontSize * 1.2
        )
        custom_stylesheet.get("Italic").fontName = "italic_font"
        custom_stylesheet.get("Heading1").fontSize = fontsize.table_heading
        custom_stylesheet.get("Heading1").alignment = 1
        custom_stylesheet.get("Heading1").leading = (
            custom_stylesheet["Heading1"].fontSize * 1.2
        )
        custom_stylesheet.get("Heading1").fontName = "bold_font"
        custom_stylesheet.get("Heading2").fontSize = fontsize.column_heading
        custom_stylesheet.get("Heading2").alignment = 1
        custom_stylesheet.get("Heading2").leading = (
            custom_stylesheet["Heading2"].fontSize * 1.2
        )
        custom_stylesheet.get("Heading2").fontName = "bold_font"

        self._custom_styles: Dict[str, Union[StyleSheet1, TableStyle]] = {
            "heading": TableStyle(
                [
                    self.VALIGN_MIDDLE,
                    self.BACKGROUND,
                    self.BOX,
                    self.ALIGN_CENTER,
                ]
            ),
            "stylesheet": custom_stylesheet,
        }

        self._custom_styles.update(
            dict.fromkeys(
                ["normal", "sub_heading"],
                TableStyle(
                    [
                        self.ALIGN_LEFT,
                        self.VALIGN_MIDDLE,
                        self.BOX,
                        self.INNERGRID,
                        self.LEFTPADDING_REDUCE,
                        self.RIGHTPADDING_REDUCE,
                    ]
                ),
            )
        )

        # Extract the column widths from properties.
        self._column_widths = [
            float(column.width) * mm for column in columns
        ]  # type: List[float]

        # Set full table width.
        self._table_width = sum(self._column_widths)  # type: float

        # Register font with reportlab.
        self._init_font_family()

    def _init_font_family(self):
        """Register the desired font with :py:mod:`reportlab`

        This ensures that `<i></i>` and `<b></b>` as cell content work well.
        """
        # Set root of fonts to the folder containing this file.
        path_to_fonts = PurePath(__file__).parent.joinpath("fonts")

        # Finally lead and register fonts with reportlab.
        registerFont(TTFont("normal_font", path_to_fonts.joinpath(self._font.normal)))
        registerFont(TTFont("bold_font", path_to_fonts.joinpath(self._font.bold)))
        registerFont(TTFont("italic_font", path_to_fonts.joinpath(self._font.italic)))
        registerFont(
            TTFont("bolditalic_font", path_to_fonts.joinpath(self._font.bolditalic))
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
        """List[float]: Return the column widths for the tables in mm."""
        return self._column_widths

    @property
    def table_width(self) -> float:
        """float: Return the sum of all column widths in mm."""
        return self._table_width

    @property
    def custom_styles(self) -> Dict[str, Union[StyleSheet1, TableStyle]]:
        """Dict[str, TableStyle]: Return the custom styles"""
        return self._custom_styles
