import datetime
class Appointment:
	def __init__(self, note_text, appt_date, vet=None, animal=None, id=None):
		self.note_text = note_text
		self.appt_date = appt_date
		self.vet = vet
		self.animal = animal
		self.id = id
		
	def get_note_text(self):
		return self.note_text

	def get_appt_date(self):
		if isinstance(self.appt_date, datetime.date):
			self.appt_date = self.appt_date.strftime('%d/%m/%Y')
		return self.appt_date

	def get_vet(self):
		return self.vet.get_name()

	def get_animal(self):
		return self.animal.get_name()

	def get_id(self):
		return self.id

	def get_headings(self):
		return ["Appt Date", "Animal", "Notes", "Vet"]

