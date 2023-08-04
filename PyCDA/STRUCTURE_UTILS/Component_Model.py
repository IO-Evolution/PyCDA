"""Component Class Model"""
from abc import ABC, abstractmethod

class Component_Model(ABC):
    """Component_Model"""
    name: str
    value: str

    @abstractmethod
    def to_dict(self):
        """to_dict"""
