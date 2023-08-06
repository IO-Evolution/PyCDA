from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

class II_InstanceIdentifier(Component_Model):
    """II_InstanceIdentifier"""
    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")
        self.name      = name
        self.root      = Element.Attribute("root", data, required=True)
        self.extension = Element.Attribute("extension", data)

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "root"     : "",
            "extension": ""
        }
