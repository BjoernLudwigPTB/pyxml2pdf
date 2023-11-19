"""This module contains the class :class:`XMLTableStyle` to style the result"""

from pathlib import PurePath
from typing import Dict, List, Tuple, Union

from reportlab.lib.colors import black, Color, honeydew  # type: ignore
from reportlab.lib.pagesizes import mm  # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # type: ignore
from reportlab.pdfbase.pdfmetrics import (  # type: ignore
    registerFont,
    registerFontFamily,
)
from reportlab.pdfbase.ttfonts import TTFont  # type: ignore
from reportlab.platypus import TableStyle  # type: ignore

from pyxml2pdf.input.properties import COLUMNS, FONT, FONTSIZE  # type: ignore

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
    FULL_ROW: Tuple[Tuple[int, int], Tuple[int, int]] = ((0, 0), (-1, -1))

    # Set important defaults for the table.
    LINE_THICKNESS: float = 0.25
    LINE_COLOR: Color = black
    BACKGROUND_COLOR: Color = honeydew
    PADDING: int = 3

    ALIGN_CENTER: CellFormattingCommand = ("ALIGN", *FULL_ROW, "CENTER")
    VALIGN_MIDDLE: CellFormattingCommand = ("VALIGN", *FULL_ROW, "MIDDLE")
    VALIGN_TOP: CellFormattingCommand = ("VALIGN", *FULL_ROW, "TOP")
    ALIGN_LEFT: CellFormattingCommand = ("ALIGN", *FULL_ROW, "LEFT")
    LEFTPADDING_REDUCE: CellFormattingCommand = ("LEFTPADDING", *FULL_ROW, PADDING)
    RIGHTPADDING_REDUCE: CellFormattingCommand = ("RIGHTPADDING", *FULL_ROW, PADDING)
    BACKGROUND: CellFormattingCommand = ("BACKGROUND", *FULL_ROW, BACKGROUND_COLOR)
    BOX: LineFormattingCommand = ("BOX", *FULL_ROW, 0.25, LINE_COLOR)
    INNERGRID: LineFormattingCommand = (
        "INNERGRID",
        *FULL_ROW,
        LINE_THICKNESS,
        LINE_COLOR,
    )

    def __init__(self):
        """Initialise font and cell formatting"""
        self._font = FONT

        # Set the resulting tables' styling with all the customization of
        # margins, fonts, fontsizes, etc...

        # Get custom_styles for all headings, texts, etc. from sample
        custom_stylesheet = getSampleStyleSheet()
        # Overwrite the sample styles according to our needs.
        custom_stylesheet.get("Normal").fontSize = FONTSIZE.normal
        custom_stylesheet.get("Normal").leading = (
            custom_stylesheet["Normal"].fontSize * 1.2
        )
        custom_stylesheet.get("Normal").fontName = "normal_font"
        custom_stylesheet.get("Italic").fontSize = custom_stylesheet["Normal"].fontSize
        custom_stylesheet.get("Italic").leading = (
            custom_stylesheet["Italic"].fontSize * 1.2
        )
        custom_stylesheet.get("Italic").fontName = "italic_font"
        custom_stylesheet.get("Heading1").fontSize = FONTSIZE.table_heading
        custom_stylesheet.get("Heading1").alignment = 1
        custom_stylesheet.get("Heading1").leading = (
            custom_stylesheet["Heading1"].fontSize * 1.2
        )
        custom_stylesheet.get("Heading1").fontName = "bold_font"
        custom_stylesheet.get("Heading2").fontSize = FONTSIZE.column_heading
        custom_stylesheet.get("Heading2").alignment = 1
        custom_stylesheet.get("Heading2").leading = (
            custom_stylesheet["Heading2"].fontSize * 1.2
        )
        custom_stylesheet.get("Heading2").fontName = "bold_font"

        self._custom_styles: Dict[str, Union[ParagraphStyle, TableStyle]] = {
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
        self._column_widths: List[float] = [
            float(column.width) * mm for column in COLUMNS
        ]

        # Set full table width.
        self._table_width: float = sum(self._column_widths)

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
    def custom_styles(self) -> Dict[str, Union[ParagraphStyle, TableStyle]]:
        """Dict[str, TableStyle]: Return the custom styles"""
        return self._custom_styles
