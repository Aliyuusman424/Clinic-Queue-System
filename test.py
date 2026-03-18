from models import Patient, ClinicQueue

clinic = ClinicQueue()

p1 = Patient("Ali")
p2 = Patient("Zainab")

clinic.add_patient(p1)
clinic.add_patient(p2)

for p in clinic.get_all_patients():
    print(p.get_details())