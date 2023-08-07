from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .ON_OrganisationName import ON_OrganisationName
from .TEL_TelecomincationAddress import TEL_TelecomincationAddress
from .AD_PostalAddress import AD_PostalAddress
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents

# IMPORT CIRCOLARI
import sys
if "PyCDA.Components.OrganizationPartOf" not in sys.modules:
    from .OrganizationPartOf import OrganizationPartOf


class Organization(Component_Model):
    """Organization"""

    def __init__(self, name: str, data: dict):
        self.name                      = name
        self.realmCode                 = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId                    = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId                = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                        = Element.Component(II_InstanceIdentifier, "id", data)
        self._name                     = Element.Component(ON_OrganisationName, "name", data)
        self.telecom                   = Element.Component(TEL_TelecomincationAddress, "telecom", data)
        self.addr                      = Element.Component(AD_PostalAddress, "addr", data)
        self.standardIndustryClassCode = Element.Component(CE_CodedWithEquivalents, "standardIndustryClassCode", data, as_list=False)
        self.asOrganizationPartOf      = Element.Component(OrganizationPartOf, "asOrganizationPartOf", data, as_list=False)
        self.classCode                 = Element.Attribute("classCode", data, fixed="ORG")
        self.determinerCode            = Element.Attribute("determinerCode", data, fixed="INSTANCE")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"                : CS_CodedSimpleValue.to_dict(),
            "typeId"                   : InfrastructureRootTypeId.to_dict(),
            "templateId"               : II_InstanceIdentifier.to_dict(),
            "id"                       : II_InstanceIdentifier.to_dict(),
            "name"                     : ON_OrganisationName.to_dict(),
            "telecom"                  : TEL_TelecomincationAddress.to_dict(),
            "addr"                     : AD_PostalAddress.to_dict(),
            "standardIndustryClassCode": CE_CodedWithEquivalents.to_dict(),
            "asOrganizationPartOf"     : "RICORSIONE",
            "classCode"                : "ORG",
            "determinerCode"           : "INSTANCE"
        }
