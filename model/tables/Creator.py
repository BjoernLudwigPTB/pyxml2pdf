from typing import List, Tuple, Union

from reportlab.platypus import Table


class Creator:
    @staticmethod
    def create_fixedwidth_table(elements, widths, style):
        """Create a table with specified column widths

        Create a table from specified elements with fixed column widths and a specific
        style.

        :param List[List[reportlab.platypus.Flowable]] elements: the cell values
            wrapped by a List representing the columns wrapped by a list representing
            the lines of the table
        :param Union[float, List[float]] widths: the column widths
        :param List[Tuple[Union[str, Tuple[int]]]] style: the style in which the table
            shall appear
        :returns Table: table containing all specified elements in fixed width columns
        """
        table = Table(elements, colWidths=widths)
        table.setStyle(style)

        return table
