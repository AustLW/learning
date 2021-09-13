
class Patient:
    age = None
    first_name = None
    last_name = None
    new_patient = None

    def __init__(self, first_name, last_name, is_patient, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.new_patient = is_patient

    def print_patient_info(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old")

austin = Patient(
    first_name='Austin',
    last_name='Winegar',
    is_patient=False,
    age=36
)
austin.print_patient_info()

class VetPatient(Patient):
    def __init__(self, first_name, last_name, age, is_patient, owner):
        super(Patient).__init__(
            first_name=first_name,
            last_name=last_name,
            age=age,
            is_patient=is_patient
        )
        self.owner = owner

    def print_patient_info(self):
        print(f'Nori is owned by {self.owner}')

Nori = VetPatient(
    first_name='Nori',
    last_name='Dassow',
    age=5,
    is_patient=True,
    owner="matt dassow"
)

Nori.print_patient_info()
# if new_patient == True:
#     print("New Patient")
# else:
#     print("Current Patient")
# print(first_name,",",last_name,"-", "Age:", age)
