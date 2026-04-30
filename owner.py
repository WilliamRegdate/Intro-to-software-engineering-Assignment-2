""" owner.py
Contains the Owner class
"""
from pet import Pet
import utils


class Owner:
    """Owners have a name and a list of pets"""
    def __init__(self, name):
        """ Owner __init__    
        Initializes an empty list of pets.    
        :param name: Name of the owner 
        """
        self.name = name
        self.pets = []

    def add_pet(self, pet_name, species):
        """ Creates a new pet for this owner.
        
        :param name: name of pet
        :param species: species of pet
        """
        self.pets.append(Pet(pet_name, self, species))

    
    def find_pet(self, pet_name):
        return utils.find_by_name(pet_name, self.pets)