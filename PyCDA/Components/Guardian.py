from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents
from .AD_PostalAddress import AD_PostalAddress
from .TEL_TelecomincationAddress import TEL_TelecomincationAddress
from .Person import Person
from .Organization import Organization

class Guardian(Component_Model):
    """Guardian"""
    def __init__(self, name: str, data: dict):
        # self.realmCode            = Element.Component()
        # self.typeId               = Element.Component()
        # self.templateId           = Element.Component()
        # self.id                   = Element.Component()
        # self.code                 = Element.Component()
        # self.addr                 = Element.Component()
        # self.telecom              = Element.Component()
        # self.guardianPerson       = Element.Component()
        # self.guardianOrganization = Element.Component()
        # self.classCode            = Element.Attribute()
        pass

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"           : CS_CodedSimpleValue.to_dict(),
            "typeId"              : InfrastructureRootTypeId.to_dict(),
            "templateId"          : II_InstanceIdentifier.to_dict(),
            "id"                  : II_InstanceIdentifier.to_dict(),
            "code"                : CE_CodedWithEquivalents.to_dict(),
            "addr"                : AD_PostalAddress.to_dict(),
            "telecom"             : TEL_TelecomincationAddress.to_dict(),
            "guardianPerson"      : Person.to_dict(),
            "guardianOrganization": Organization.to_dict(),
            "classCode"           : ""
        }
    