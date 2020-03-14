from input.properties import (
    columns,
    rows_xmltag,
    subtables,
    subtables_xmltag,
    table_title,
)


def test_rows_xmltag():
    # Check type of `rows_xmltag`.
    assert isinstance(rows_xmltag, str)


def test_table_title():
    # Check type of `table_title`.
    assert isinstance(table_title, str)


def test_columns():
    # Check types and shape `columns`.
    assert isinstance(columns, list)
    for column in columns:
        assert isinstance(column, dict)
        for key in column:
            assert isinstance(key, str)
        assert "label" in column
        assert isinstance(column["label"], str)
        assert "tag" in column
        assert isinstance(column["tag"], list)
        for tag in column["tag"]:
            assert isinstance(tag, str)
        assert "width" in column
        assert float(column["width"])


def test_subtables_xmltag():
    # Check type of `subtables_xmltag`.
    assert isinstance(subtables_xmltag, str)


def test_subtables():
    # Check types and shape `subtables`.
    assert isinstance(subtables, list)
    for subtable in subtables:
        assert isinstance(subtable, dict)
        for key in subtable:
            assert isinstance(key, str)
        assert "label" in subtable
        assert isinstance(subtable["label"], str)
        assert "content" in subtable
        assert isinstance(subtable["content"], list)
        for criteria_list in subtable["content"]:
            assert isinstance(criteria_list, list)
            for criteria in criteria_list:
                assert isinstance(criteria, str)
