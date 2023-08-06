from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

class Person(Component_Model):
    """Person"""
    def __init__(self, name: str, data: dict):
        pass

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {}
    