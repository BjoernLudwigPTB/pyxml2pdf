"""This is the set of parameters for interpretation the XML input and formatting"""

from typing import List, NamedTuple, Tuple

#: The XML tag, which will be represented by one row in the table.
rows_xmltag = "kurs"  # type: str

#: The XML tag, which will be used to identify the row for error message printing.
identifier_xmltag = [
    "TerminDatumVon1",
    "TerminDatumBis1",
    "TerminDatumVon2",
    "TerminDatumBis2",
    "TerminDatumVon3",
    "TerminDatumBis3",
]  # type: List[str]

#: The table title is displayed as the content of the very first cell in full table
#: width.
table_title = "Ausbildungs- und Fahrtenprogramm 2021"  # type: str

Column = NamedTuple("Column", [("label", str), ("tag", List[str]), ("width", float)])
#: The specification for the table columns. The desired column headings are specified
#: as 'label' and the XML tags containing the content to be displayed in the table
#: columns are specified as 'tag'. By default, the content of each tag is transferred
#: to one cell. If several tags are to be merged within one cell, nested lists can be
#: used here. All tags listed here, which finally shall be displayed in the columns of
#: one and the same row, must each belong to one parent tag `rows_xmltag'. The column
#: widths are specified with 'width' in mm.
columns = [
    Column(label="Art", tag=["Kursart"], width=7.2),
    Column(
        label="Datum",
        tag=[
            "TerminDatumVon1",
            "TerminDatumBis1",
            "TerminDatumVon2",
            "TerminDatumBis2",
            "TerminDatumVon3",
            "TerminDatumBis3",
        ],
        width=11.5,
    ),
    Column(label="Ort", tag=["Ort1"], width=18.7),
    Column(label="Leitung", tag=["Kursleiter"], width=14.5),
    Column(
        label="Beschreibung",
        tag=["Bezeichnung", "Bezeichnung2", "Beschreibung"],
        width=60.9,
    ),
    Column(label="Zielgruppe", tag=["Zielgruppe"], width=18),
    Column(
        label="Voraussetzungen<br/>a) persönliche | b) " "materielle | c) finanzielle",
        tag=["Voraussetzung", "Ausruestung", "Kurskosten", "Leistungen"],
        width=47,
    ),
]  # type: List[Column]

#: The XML tag used to select the respective rows for the subtables.
subtables_xmltag = "Kategorie"  # type: str

SubtableSetting = NamedTuple(
    "SubtableSetting", [("label", str), ("include", List[List[str]])]
)
#: The subtables headings and `subtables_xmltag`'s content on which to decide what
#: tags should be included. All tags from the XML file which are supposed to be
#: listed in the respective subtable should match at least one of each of the sublists
#: include-filters. There will be one subtable for each set of label and
#: include-filters, as long as at least one element is found for the subtable.
subtable_settings = (
    SubtableSetting(
        label="Wandern im Hoch- und Mittelgebirge",
        include=[["Hochgebirge", "Mittelgebirge"], ["Wandern"]],
    ),
    SubtableSetting(
        label="Klettern und Bouldern im Mittelgebirge",
        include=[["Mittelgebirge"], ["Klettern", "Bouldern", "Höhle"]],
    ),
    SubtableSetting(
        label="Ausbildung, Wandern und Klettern in Berlin",
        include=[["in Berlin"], ["Ausbildung", "Wandern", "Klettern"]],
    ),
    SubtableSetting(
        label="Mountainbiken", include=[["Mountainbiken"], ["Mountainbiken"]]
    ),
    SubtableSetting(
        label="Ski, Bergsteigen, Hochtouren und Klettern im Hochgebirge",
        include=[
            ["Hochgebirge"],
            ["Bergsteigen", "Hochtouren", "Höhle", "Klettern", "Klettersteig", "Ski"],
        ],
    ),
    SubtableSetting(
        label="Veranstaltungen für Familien", include=[["Familie"], ["Familie"]]
    ),
    SubtableSetting(
        label="Jugendgruppen und -events", include=[["Jugend"], ["Jugend"]]
    ),
)  # type: Tuple[SubtableSetting, ...]

Font = NamedTuple(
    "Font", [("normal", str), ("italic", str), ("bold", str), ("bolditalic", str)]
)
#: Fonts for the table.
font = Font(
    normal="NewsGothicBT-Roman.ttf",
    italic="NewsGothicBT-Italic.ttf",
    bold="NewsGothicBT-Bold.ttf",
    bolditalic="NewsGothicBT-BoldItalic.ttf",
)  # type: Font

FontSize = NamedTuple(
    "FontSize", [("normal", float), ("table_heading", float), ("column_heading", float)]
)
#: Set the font size for the table. 'normal' applies to all text except table and
#: column headings, where 'table_heading' applies to the very first line of the whole
#: table and additionally the first line of all subtables.
fontsize = FontSize(normal=6.5, table_heading=12, column_heading=6.5,)  # type: FontSize
