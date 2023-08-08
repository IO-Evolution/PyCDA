from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model


class CS_CodedSimpleValue(Component_Model):
    """CS_CodedSimpleValue"""

    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.code = Element.Attribute("code", data, required=True)

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "code": ""
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {
            "code": ""
        }
