from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents
from .BL_Boolean import BL_Boolean


class LanguageCommunication(Component_Model):
    """LanguageCommunication"""

    def __init__(self, name: str, data: dict):
        self.name                 = name
        self.realmCode            = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId               = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId           = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.languageCode         = Element.Component(CS_CodedSimpleValue, "languageCode", data, as_list=False)
        self.modeCode             = Element.Component(CE_CodedWithEquivalents, "modeCode", data, as_list=False)
        self.proficiencyLevelCode = Element.Component(CE_CodedWithEquivalents, "proficiencyLevelCode", data, as_list=True)
        self.preferenceInd        = Element.Component(BL_Boolean, "preferenceInd", data, as_list=False)

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"           : CS_CodedSimpleValue.to_dict_req(),
            "typeId"              : InfrastructureRootTypeId.to_dict_req(),
            "templateId"          : II_InstanceIdentifier.to_dict_req(),
            "languageCode"        : CS_CodedSimpleValue.to_dict_req(),
            "modeCode"            : CE_CodedWithEquivalents.to_dict_req(),
            "proficiencyLevelCode": CE_CodedWithEquivalents.to_dict_req(),
            "preferenceInd"       : BL_Boolean.to_dict_req()
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {}
