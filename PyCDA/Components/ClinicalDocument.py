from ..Core.Component_Model import Component_Model
from ..Core import Elements as Element

from .CS_CodedSimpleValue import CS_CodedSimpleValue
from .InfrastructureRootTypeId import InfrastructureRootTypeId
from .II_InstanceIdentifier import II_InstanceIdentifier
from .CE_CodedWithEquivalents import CE_CodedWithEquivalents
from .ST_String import ST_String
from .TS_PointInTime import TS_PointInTime
from .INT_IntegerNumber import INT_IntegerNumber
from .RecordTarget import RecordTarget
from .Author import Author
from .DataEnterer import DataEnterer
from .Custodian import Custodian
from .InformationRecipient import InformationRecipient
from .LegalAuthenticator import LegalAuthenticator
from .Authenticator import Authenticator
from .InFulfillmentOf import InFulfillmentOf
from .DocumentationOf import DocumentationOf
from .RelatedDocument import RelatedDocument
from .Authorization import Authorization
from .Component1 import Component1
from .Component2 import Component2
from .Informant12 import Informant12
from .Participant1 import Participant1


class ClinicalDocument(Component_Model):
    """ClinicalDocument"""

    def __init__(self, name: str, data: dict):
        self.name                 = name
        self.realmCode            = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId               = Element.Component(InfrastructureRootTypeId, "typeId", data, required=True, as_list=False)
        self.templateId           = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                   = Element.Component(II_InstanceIdentifier, "id", data, required=True, as_list=False)
        self.code                 = Element.Component(CE_CodedWithEquivalents, "code", data, required=True, as_list=False)
        self.title                = Element.Component(ST_String, "title", data, as_list=False)
        self.effectiveTime        = Element.Component(TS_PointInTime, "effectiveTime", data, required=True, as_list=False)
        self.confidentialityCode  = Element.Component(CE_CodedWithEquivalents, "confidentialityCode", data, required=True, as_list=False)
        self.languageCode         = Element.Component(CS_CodedSimpleValue, "languageCode", data, as_list=False)
        self.setId                = Element.Component(II_InstanceIdentifier, "setId", data, as_list=False)
        self.versionNumber        = Element.Component(INT_IntegerNumber, "versionNumber", data, as_list=False)
        self.copyTime             = Element.Component(TS_PointInTime, "copyTime", data, as_list=False)
        self.recordTarget         = Element.Component(RecordTarget, "recordTarget", data, required=True)
        self.author               = Element.Component(Author, "author", data, required=True)
        self.dataEnterer          = Element.Component(DataEnterer, "dataEnterer", data, as_list=False)
        self.informant            = Element.Component(Informant12, "informant", data)
        
        self.custodian            = Element.Component(Custodian, "custodian", data, required=True, as_list=False)
        self.informationRecipient = Element.Component(InformationRecipient, "informationRecipient", data)
        self.legalAuthenticator   = Element.Component(LegalAuthenticator, "legalAuthenticator", data, as_list=False)
        self.authenticator        = Element.Component(Authenticator, "authenticator", data)
        self.participant          = Element.Component(Participant1, "participant", data)
        self.inFulfillmentOf      = Element.Component(InFulfillmentOf, "inFulfillmentOf", data)
        self.documentationOf      = Element.Component(DocumentationOf, "documentationOf", data)
        self.relatedDocument      = Element.Component(RelatedDocument, "relatedDocument", data)
        self.authorization        = Element.Component(Authorization, "authorization", data)
        self.componentOf          = Element.Component(Component1, "componentOf", data, as_list=False)
        self.component            = Element.Component(Component2, "component", data, required=True, as_list=False)
        self.classCode            = Element.Attribute("classCode", data, fixed="DOCCLIN")
        self.moodCode             = Element.Attribute("moodCode", data, fixed="EVN")

    @classmethod
    def to_dict(cls):
        """to_dict"""
        return {
            "realmCode"           : CS_CodedSimpleValue.to_dict_req(),
            "typeId"              : InfrastructureRootTypeId.to_dict_req(),
            "templateId"          : II_InstanceIdentifier.to_dict_req(),
            "id"                  : II_InstanceIdentifier.to_dict_req(),
            "code"                : CE_CodedWithEquivalents.to_dict_req(),
            "title"               : ST_String.to_dict_req(),
            "effectiveTime"       : TS_PointInTime.to_dict_req(),
            "confidentialityCode" : CE_CodedWithEquivalents.to_dict_req(),
            "languageCode"        : CS_CodedSimpleValue.to_dict_req(),
            "setId"               : II_InstanceIdentifier.to_dict_req(),
            "versionNumber"       : INT_IntegerNumber.to_dict_req(),
            "copyTime"            : TS_PointInTime.to_dict_req(),
            "recordTarget"        : RecordTarget.to_dict_req(),
            "author"              : Author.to_dict_req(),
            "dataEnterer"         : DataEnterer.to_dict_req(),
            "informant"           : Informant12.to_dict_req(),
            "custodian"           : Custodian.to_dict_req(),
            "informationRecipient": InformationRecipient.to_dict_req(),
            "legalAuthenticator"  : LegalAuthenticator.to_dict_req(),
            "authenticator"       : Authenticator.to_dict_req(),
            "participant"         : Participant1.to_dict_req(),
            "inFulfillmentOf"     : InFulfillmentOf.to_dict_req(),
            "documentationOf"     : DocumentationOf.to_dict_req(),
            "relatedDocument"     : RelatedDocument.to_dict_req(),
            "authorization"       : Authorization.to_dict_req(),
            "componentOf"         : Component1.to_dict_req(),
            "component"           : Component2.to_dict_req(),
            "classCode"           : "DOCCLIN",
            "moodCode"            : "EVN"
        }

    @classmethod
    def to_dict_req(cls):
        """to_dict"""
        return {
            "typeId"             : InfrastructureRootTypeId.to_dict_req(),
            "id"                 : II_InstanceIdentifier.to_dict_req(),
            "code"               : CE_CodedWithEquivalents.to_dict_req(),
            "effectiveTime"      : TS_PointInTime.to_dict_req(),
            "confidentialityCode": CE_CodedWithEquivalents.to_dict_req(),
            "recordTarget"       : RecordTarget.to_dict_req(),
            "author"             : Author.to_dict_req(),
            "custodian"          : Custodian.to_dict_req(),
            "component"          : Component2.to_dict_req()
        }
