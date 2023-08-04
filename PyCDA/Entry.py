from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component_Model import Component_Model

class Entry(Component_Model):
    """Entry"""
    def __init__(self, name: str, data: dict):
        pass

    @classmethod
    def as_dict(cls):
        """as_dict"""
        return {}
