from ..Core import Elements as Element
from ..Core.Component_Model import Component_Model

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .PN_PersonName import PN_PersonName
from .TS_PointInTime import TS_PointInTime
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents
from .Guardian import Guardian
from .BirthPlace import BirthPlace
from .LanguageCommunication import LanguageCommunication


class Patient(Component_Model):
    """Patient"""

    def __init__(self, name: str, data: dict):
        self.name                     = name
        self.realmCode                = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId                   = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId               = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                       = Element.Component(II_InstanceIdentifier, "id", data, as_list=False)
        self.name_                    = Element.Component(PN_PersonName, "name", data)
        self.administrativeGenderCode = Element.Component(CE_CodedWithEquivalents, "administrativeGenderCode", data, as_list=False)
        self.birthTime                = Element.Component(TS_PointInTime, "birthTime", data, as_list=False)
        self.maritalStatusCode        = Element.Component(CE_CodedWithEquivalents, "maritalStatusCode", data, as_list=True)
        self.religiousAfflitionCode   = Element.Component(CE_CodedWithEquivalents, "religiousAfflitionCode", data, as_list=True)
        self.raceCode                 = Element.Component(CE_CodedWithEquivalents, "raceCode", data, as_list=True)
        self.ethnicGroupCode          = Element.Component(CE_CodedWithEquivalents, "ethnicGroupCode", data, as_list=True)
        self.guardian                 = Element.Component(Guardian, "guardian", data)
        self.birthplace               = Element.Component(BirthPlace, "birthplace", data, as_list=False)
        self.languageCommunication    = Element.Component(LanguageCommunication, "languageCommunication", data)
        self.classCode                = Element.Attribute("classCode", data, fixed="PSN")
        self.determinerCode           = Element.Attribute("determinerCode", data, fixed="INSTANCE")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"               : CS_CodedSimpleValue.to_dict_req(),
            "typeId"                  : InfrastructureRootTypeId.to_dict_req(),
            "templateId"              : II_InstanceIdentifier.to_dict_req(),
            "id"                      : II_InstanceIdentifier.to_dict_req(),
            "name"                    : PN_PersonName.to_dict_req(),
            "administrativeGenderCode": CE_CodedWithEquivalents.to_dict_req(),
            "birthTime"               : TS_PointInTime.to_dict_req(),
            "maritalStatusCode"       : CE_CodedWithEquivalents.to_dict_req(),
            "religiousAfflitionCode"  : CE_CodedWithEquivalents.to_dict_req(),
            "raceCode"                : CE_CodedWithEquivalents.to_dict_req(),
            "ethnicGroupCode"         : CE_CodedWithEquivalents.to_dict_req(),
            "guardian"                : Guardian.to_dict_req(),
            "birthplace"              : BirthPlace.to_dict_req(),
            "languageCommunication"   : LanguageCommunication.to_dict_req(),
            "classCode"               : "",
            "determinerCode"          : ""
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {}
