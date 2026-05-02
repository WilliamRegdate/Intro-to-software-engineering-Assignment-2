"""observer.py
contains the Observer class 
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass