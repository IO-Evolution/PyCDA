from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

class TS_PointInTime(Component_Model):
    """TS_PointInTime"""
    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name  = name
        self.value = Element.Attribute("value", data, required=True)

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "value": ""
        }
    