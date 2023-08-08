from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .EN_GenericName import EN_GenericName
from .AD_PostalAddress import AD_PostalAddress


class Place(Component_Model):
    """Place"""

    def __init__(self, name: str, data: dict):
        self.name           = name
        self.realmCode      = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId         = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId     = Element.Component(II_InstanceIdentifier, "templateId", data)
        self._name          = Element.Component(EN_GenericName, "name", data, as_list=False)
        self.addr           = Element.Component(AD_PostalAddress, "addr", data, as_list=False)
        self.classCode      = Element.Attribute("classCode", data, fixed="PLC")
        self.determinerCode = Element.Attribute("determinerCode", data, fixed="INSTANCE")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"     : CS_CodedSimpleValue.to_dict_req(),
            "typeId"        : InfrastructureRootTypeId.to_dict_req(),
            "templateId"    : II_InstanceIdentifier.to_dict_req(),
            "name"          : EN_GenericName.to_dict_req(),
            "addr"          : AD_PostalAddress.to_dict_req(),
            "classCode"     : "",
            "determinerCode": ""
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {}
