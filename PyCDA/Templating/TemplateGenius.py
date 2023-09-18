from enum import Enum

from .DBManager import DBManager
from ..Components.ClinicalDocument import ClinicalDocument


class DOC_TYPE(Enum):
    LDO = 1
    VPS = 2
    RML = 3
    RR = 4
    CV = 5
    SV = 6
    PS = 7
    RSA = 8


class TemplateGenius:
    def __init__(self):
        self.db = DBManager()

    def fetch_static_data(self, doc_type: DOC_TYPE) -> list:
        query = f"SELECT PATH, VALUE FROM STATIC_DATA WHERE DOC_TYPE={doc_type.value}"
        print(query)
        return self.db.fetch(query)

    def _rectify(self, data: dict, path: str):
        for item in data.keys():
            if isinstance(data[item], dict):
                self._rectify(data[item], path + item)
            elif isinstance(data[item], str):
                if data[item][0] != "[":
                    print(f"{path}.{item}\t{data[item]}")

    def generate_template(self, doc_type: DOC_TYPE):
        template_data = self.fetch_static_data(doc_type)
        general_template = ClinicalDocument.to_dict_req()
        for element in template_data:
            value = element[1]
            element = element[0].split(".")
            cursor = general_template
            for path in element:
                try:
                    if isinstance(cursor[path], dict):
                        cursor = cursor[path]
                    else:
                        cursor[path] = value
                except:
                    cursor[path] = value
        return general_template
