# import xml.etree.ElementTree as ET
from lxml import etree as ET

from .DICTfactory import DICTfactory


class XMLfactory:
    """FACTORY"""

    def __init__(self, document):
        self.root_name = "ClinicalDocument"
        self.data = DICTfactory(document)
        self.data = self.data.to_dict()

    def dict_to_xml(self):
        """dict_to_xml"""
        root = ET.Element(self.root_name)

        self._dict_to_xml(root, self.data)
        ET.indent(root, space="\t", level=0)
        return ET.tostring(root, encoding='utf-8').decode()

    def _dict_to_xml(self, node, data: dict):
        for key, value in data.items():
            print(key, value)
            if isinstance(value, dict):
                if "_text" in value and len(value) == 1:
                    subnode = ET.SubElement(node, key)
                    subnode.text = str(value["_text"])
                else:
                    subnode = ET.Element(key)
                    node.append(subnode)
                    self._dict_to_xml(subnode, value)
            elif key.startswith("__"):
                node.set(key[2:], value)
            elif isinstance(value, list):
                for el in value:
                    subnode = ET.Element(key)
                    node.append(subnode)
                    self._dict_to_xml(subnode, el)
            else:
                subnode = ET.SubElement(node, key)
                subnode.text = f"dato di {key}"

    def save_dict_to_xml(self, filename: str):
        """save_dict_to_xml"""
        xml_string = self.dict_to_xml()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_string)
