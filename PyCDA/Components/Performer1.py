from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model


class Performer1(Component_Model):
    """Performer1"""

    def __init__(self, name: str, data: dict):
        pass

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {}

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {}
