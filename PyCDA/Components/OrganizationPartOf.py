from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents
from .IVL_TS_IntervalOfTime import IVL_TS_IntervalOfTime

# IMPORT CIRCOLARI
import sys
if "PyCDA.Components.Organization" not in sys.modules:
    from .Organization import Organization


class OrganizationPartOf(Component_Model):
    """OrganizationPartOf"""

    def __init__(self, name: str, data: dict):
        self.name              = name
        self.realmCode         = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId            = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId        = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                = Element.Component(II_InstanceIdentifier, "id", data)
        self.code              = Element.Component(CE_CodedWithEquivalents, "code", data, as_list=False)
        self.statusCode        = Element.Component(CS_CodedSimpleValue, "statusCode", data, as_list=False)
        self.effectiveTime     = Element.Component(IVL_TS_IntervalOfTime, "effectiveTime", data, as_list=False)
        self.wholeOrganization = Element.Component(Organization, "wholeOrganization", data, as_list=False)
        self.classCode         = Element.Attribute("classCode", data, fixed="PART")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"        : CS_CodedSimpleValue.to_dict_req(),
            "typeId"           : InfrastructureRootTypeId.to_dict_req(),
            "templateId"       : II_InstanceIdentifier.to_dict_req(),
            "id"               : II_InstanceIdentifier.to_dict_req(),
            "code"             : CE_CodedWithEquivalents.to_dict_req(),
            "statusCode"       : CS_CodedSimpleValue.to_dict_req(),
            "effectiveTime"    : IVL_TS_IntervalOfTime.to_dict_req(),
            "wholeOrganization": Organization.to_dict_req(),
            "classCode"        : "PART"
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {}
