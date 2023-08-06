from ..Core.Exceptions import InvalidGivenValue
from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .PatientRole import PatientRole

class RecordTarget(Component_Model):
    """RecordTarget"""
    def __init__(self, name: str, data: dict):
        self.name = name

        self.realmCode          = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId             = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId         = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.patientRole        = Element.Component(PatientRole, "patientRole", data, required=True, as_list=False)
        self.typeCode           = Element.Attribute("typeCode", data, fixed="RCT")
        self.contextControlCode = Element.Attribute("contextControlCOde", data, fixed="OP")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "relamCode"         : CS_CodedSimpleValue.to_dict(),
            "typeId"            : InfrastructureRootTypeId.to_dict(),
            "templateId"        : II_InstanceIdentifier.to_dict(),
            "patientRole"       : PatientRole.to_dict(),
            "typeCode"          : "",
            "contectControlCode": ""
        }
    