"""Component Class Model"""
from abc import ABC, abstractmethod

class Component_Model:
    """Component_Model"""
    name : str
    value: str

    @classmethod
    @abstractmethod
    def as_dict(cls):
        """to_dict"""
