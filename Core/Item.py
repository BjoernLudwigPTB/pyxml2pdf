from xml.etree.ElementTree import Element
import xml


class Item:

    _item: Element

   def __init__(self):
       """

       :param self:
       :type self:
       """
       self._item = Element()
