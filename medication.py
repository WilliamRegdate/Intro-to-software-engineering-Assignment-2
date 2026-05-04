""" medication.py
Contains the Medication class.
"""


class Medication:
    def __init__(self, name, amount_in_stock):
        """ Medication __init__
        
        :param name (string): the name of the medication
        :param amount_in_stock: how much of this medication is in stock
        """
        self._observers = []
        self.name = name
        self.amount_in_stock = amount_in_stock

    def restock(self, amount):
        """ Increases the stock by a given amount.

        :param amount (int): The amount to increase the stock by
        """
        self.amount_in_stock += amount
        self.notify_observers()

    
    def reduce_stock(self, amount):
        self.amount_in_stock -= amount
        self.notify_observers()


    def has_enough_stock(self, dosage):
        """ Checks if there is enough stock for the given dosage.

        :param dosage (int): The dosage to be checked.
        :returns True or False
        """
        return self.amount_in_stock >= dosage
    
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()