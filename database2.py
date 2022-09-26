class Patient:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.patient_id = ''
        self.age = ''
        self.tests = []
        x = 5

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name, patient_last_name, patient_id,
                         patient_age):
    new_patient = {"first name": patient_first_name,
                   "last name": patient_last_name,
                   "id": patient_id,
                   "age": patient_age,
                   "test": []}
    return new_patient


def main():
    # x = Patient()
    # x.first_name = 'David'
    # x.last_name = "Ward"
    # print(x.last_name)
    # y = Patient()
    # y.first_name = 'Edward'
    # y.last_name = 'Smith'
    # print(y.last_name)
    # exit()
    db = {}
    db[1] = create_patient_entry("Ann", "Ables", 1, 30)
    db[2] = create_patient_entry("Bob", "Boyles", 2, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print(finder(db, 2))
    print(test(db, 3, "HDL", 100))
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])