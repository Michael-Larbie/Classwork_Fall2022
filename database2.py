def create_patient_entry(patient_first_name, patient_last_name, patient_id,
                         patient_age):
    new_patient = {"first name": patient_first_name,
                   "last name": patient_last_name,
                   "id": patient_id,
                   "age": patient_age,
                   "test": []}
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob", "Boyles", 2, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    print(finder(db,2))
    print(test(db, 3, "HDL", 100))
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))


def directory(db):
    for i in db:
        print(i)
        print("Name: {}, Id: {}, Age: {}".format(i['first name'],
                                                 i['id'],
                                                 i["age"]))


def finder(db, id_no):
    for i in db:
        if i['id'] == id_no:
            return i
    return False


def test(db, id_no, tname, tvalue):
    patient = finder(db, id_no)
    patient["test"].append((tname, tvalue))
    return patient


def get_full_name(patient):
    full_name = "{} {}".format(patient["first name"], patient['last name'])
    return full_name


def adult_or_minor(patient):
    if patient["age"] >= 18:
        return "adult"
    else:
        return "minor"


if __name__ == "__main__":
    main()
