class AppointmentDecorator:
    def __init__(self, appointment):
        self.appointment = appointment

    def attend_appointment(self):
        self.appointment.attend_appointment()

    def get_notes(self):
        return self.appointment.get_notes()

class VaccinationDecorator(AppointmentDecorator):
    def attend_appointment(self):
        super().attend_appointment()
        print("Enter Vaccination notes: ")
        vaccination_notes = input()
        self.appointment.get_notes().append(f"vaccination={vaccination_notes}")

class SurgeryDecorator(AppointmentDecorator):
    def attend_appointment(self):
        super().attend_appointment()
        print("Enter surgery notes: ")
        surgery_notes = input()
        self.appointment.get_notes().append(f"surgery notes={surgery_notes}")