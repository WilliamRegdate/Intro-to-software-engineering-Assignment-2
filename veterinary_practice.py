""" veterinary_practice.py
Contains the VeterinaryPractice class
"""
from medication import Medication
from owner import Owner
import utils


class VeterinaryPractice:
    """ Holds the data required for the Veterinary Practice application and allows:
        - pets to be registered
        - appointments for pets to be created and attended
        - medications to be stocked
        - prescriptions to be created, prepared and collected.

        NOTE: in a real systems, use data storage rather than a set of lists and an MVC architecture.
    """

    def __init__(self):
        """ Initialise empty lists to store the VeterinaryPractice data """
        self.owners = []
        self.medications = []
        self.prescriptions = []
        self.appointments = []

    def register_pet(self, pet_name, owner_name, species):
        """ Registers a pet with the vets. 
            If the owner does not exist, a new owner is created.
        
        :param pet_name (string): The name of the pet
        :param owner_name (string): The name of a new or existing owner
        :param species (string): The pet's species
        """
        owner = self.find_owner(owner_name)
        if owner == None:
            owner = Owner(owner_name)
            self.owners.append(owner)

        owner.add_pet(pet_name, species)

    def create_appointment(self, appointment):
        """ Adds the appointment and returns the appointment ID (the ID is list index)"""
        self.appointments.append(appointment)

        return len(self.appointments) - 1

    def attend_appointment(self, appointment_id):
        """Attend an appointment and return notes or an error message."""
        appointment = self.find_appointment(appointment_id)

        if appointment is None:
            return "Unrecognized appointment ID"

        appointment.attend_appointment()
        return appointment.get_notes()
     

    def stock_medication(self, medication_name, amount):
        """ Find the medication by the given name or, if it does not exist, creates the medication.
            Updates the amount of mediation that is in stock.
            
        :param medication_name: The name of the medication to be created/updated.
        :param amount: The amount to increase the stock by.
        """
        existing_medication = self.find_medication(medication_name)

        if existing_medication is None:
            existing_medication = Medication(medication_name, amount)
            self.medications.append(existing_medication)
        else:
            existing_medication.restock(amount)

    def create_prescription(self, pet, medication, dosage):
        """ Create a prescription for a pet.
        
        :param pet (Pet): The pet to create the prescription for
        :param medication (Medication): The medication the prescription is for
        :param dosage (int): The amount of medication to be given

        :returns the prescription ID (the ID is list index)
        """
        prescription = pet.create_prescription(medication, dosage)
        self.prescriptions.append(prescription)

        return len(self.prescriptions) - 1    
        
    def prepare_prescription_for_collection(self, prescription_id):
        """Prepare a prescription for collection."""
        prescription = self.find_prescription(prescription_id)

        if prescription is None:
            return "Unrecognized prescription ID"

        if prescription.prepareForCollection():
            return "Prescription prepared"

        return "Prescription is not ready for preparation"
        
    
    def collect_prescription(self, prescription_id):
        """Collect a prescription."""
        prescription = self.find_prescription(prescription_id)

        if prescription is None:
            return "Unrecognized prescription ID"

        if prescription.collect():
            return "Prescription collected"

        return "Prescription is not ready for collection"
    

    #===================================
    # Basic access methods

    def has_owners(self):
        return len(self.owners) > 0

    def has_medications(self):
        return len(self.medications) > 0

    def has_prescriptions(self):
        return len(self.prescriptions) > 0

    def find_owner(self, owner_name):
        return utils.find_by_name(owner_name, self.owners)

    def find_medication(self, name):
        return utils.find_by_name(name, self.medications)

    def find_prescription(self, prescription_id):
        if prescription_id < len(self.prescriptions):
            return self.prescriptions[prescription_id]
        return None

    def find_appointment(self, appointment_id):
        if appointment_id < len(self.appointments):
            return self.appointments[appointment_id]
        return None
    

# EOF    
#------