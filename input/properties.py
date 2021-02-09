# The XML tag, which will be represented by one row in the table.
rows_xmltag = "kurs"

# The table title is displayed as the content of the very first cell in full table
# width.
table_title = "Ausbildungs- und Fahrtenprogramm 2020"

# The specification for the table columns. The desired column headings are specified
# as 'label' and the XML tags containing the content to be displayed in the table
# columns are specified as 'tag'. By default, the content of each tag is transferred
# to one cell. If several tags are to be merged within one cell, nested lists can be
# used here. All tags listed here, which finally shall be displayed in the columns of
# one and the same row, must each belong to one parent tag `rows_xmltag'. The column
# widths are specified with 'width' in mm.
columns = [
    {"label": "Art", "tag": ["Kursart"], "width": 7.2},
    {
        "label": "Datum",
        "tag": [
            "TerminDatumVon1",
            "TerminDatumBis1",
            "TerminDatumVon2",
            "TerminDatumBis2",
            "TerminDatumVon3",
            "TerminDatumBis3",
        ],
        "width": 11.5,
    },
    {"label": "Ort", "tag": ["Ort1"], "width": 18.7},
    {"label": "Leitung", "tag": ["Kursleiter"], "width": 14.5},
    {
        "label": "Beschreibung",
        "tag": ["Bezeichnung", "Bezeichnung2", "Beschreibung"],
        "width": 60.9,
    },
    {"label": "Zielgruppe", "tag": ["Zielgruppe"], "width": 18},
    {
        "label": "Voraussetzungen<br/>a) persönliche | b) "
        "materielle | c) finanzielle",
        "tag": ["Voraussetzung", "Ausruestung", "Kurskosten", "Leistungen"],
        "width": 47,
    },
]
# The XML tag used to select the respective rows for the subtables.
subtables_xmltag = "Kategorie"

# The subtables headings and criteria, i.e. the `subtables_xmltag`'s content,
# which all elements from the XML input should match to be listed in the according
# subtable. There will be one subtable for each set of title and criteria, as long as
# at least one element is found for the subtable. To _match_ the criteria,
# the element's `subtables_xmltag`'s content needs to contain at least one of the
# list elements of each of the nested lists, given here.
subtables = [
    {
        "label": "Wandern im Hoch- und Mittelgebirge",
        "content": [["Hochgebirge", "Mittelgebirge"], ["Wandern"]],
    },
    {
        "label": "Klettern und Bouldern im Mittelgebirge",
        "content": [["Mittelgebirge"], ["Klettern", "Bouldern", "Höhle"]],
    },
    {
        "label": "Ausbildung, Wandern und Klettern in Berlin",
        "content": [["in Berlin"], ["Ausbildung", "Wandern", "Klettern"]],
    },
    {"label": "Mountainbiken", "content": [["Mountainbiken"], ["Mountainbiken"]]},
    {
        "label": "Ski, Bergsteigen, Hochtouren und Klettern im Hochgebirge",
        "content": [
            ["Hochgebirge"],
            ["Bergsteigen", "Hochtouren", "Höhle", "Klettern", "Klettersteig", "Ski"],
        ],
    },
    {"label": "Veranstaltungen für Familien", "content": [["Familie"], ["Familie"]]},
    {"label": "Jugendgruppen und -events", "content": [["Jugend"], ["Jugend"]]},
]

# Set font for the table.
font = {
    "normal": "NewsGothicBT-Roman.ttf",
    "italic": "NewsGothicBT-Italic.ttf",
    "bold": "NewsGothicBT-Bold.ttf",
    "bolditalic": "NewsGothicBT-BoldItalic.ttf",
}

# Set the font size for the table. 'normal' applies to all text except table and
# column headings, where 'table_heading' applies to the very first line of the whole
# table and additionally the first line of all subtables.
fontsize = {"normal": 6.5, "table_heading": 12, "column_heading": 6.5}
