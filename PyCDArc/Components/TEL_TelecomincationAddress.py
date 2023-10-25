from .IVL_TS_IntervalOfTime import IVL_TS_IntervalOfTime
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model
from ..Core.Exceptions import InvalidGivenValue, InvalidNullFlavor


class TEL_TelecomincationAddress(Component_Model):
    """TEL_TelecomincationAddress"""

    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.value = Element.Attribute("value", data, required=True, nullable=True)
        self.use = Element.Attribute("use", data, nullable=True)
        self.useablePeriod = Element.Component(IVL_TS_IntervalOfTime, "useablePeriod", data, as_list=False)

        self.nullFlavor = Element.Attribute("nullFlavor", data)
        self.check_null_flavor()

    def check_null_flavor(self):
        if self.value is not None:
            self.nullFlavor = None

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "value": "",
            "use": "",
            "useablePeriod": IVL_TS_IntervalOfTime.to_dict(),
            "nullFlavor": ""
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {
            "value": ""
        }
