import os

class Doctor:
    def __init__(self, doctor_ID="123", name="Andy", specialization="heart", working_Time="9-18", qualification="MD", room_Number="456"):
        self.doctor_ID = doctor_ID
        self.name = name
        self.specialization = specialization
        self.working_Time = working_Time
        self.qualification = qualification
        self.room_Number = room_Number

    def get_doctor_id(self):
        return self.doctor_ID

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_Time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_Number
    
    def set_doctor_id(self, new_id):
        self.doctor_ID = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_Time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_Number = new_room_number

    def __str__(self):
        return f'{self.doctor_ID}_{self.name}_{self.specialization}_{self.working_Time}_{self.qualification}_{self.room_Number}'

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)

    def enter_dr_info(self):
        doctorId = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctors speciality: ")
        working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        return Doctor(doctorId, name, specialization, working_time, qualification, room_number)

    def read_doctors_file(self):
        if os.path.exists('doctors.txt'):
            with open('doctors.txt', 'r') as file:
                for line in file:
                    doctor_id, name, specialization, working_time, qualification, room_number = line.strip().split('_')
                    doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
                    self.doctors.append(doctor)
        else:
            print("doctors.txt file not found. Starting with an empty list.")
            
    def search_doctor_by_id(self):
        doctor_id = input("Enter the doctor ID: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system")
    
    def search_doctor_by_name(self):
        name = input("Enter the doctor name: ")
        for doctor in self.doctors:
            if doctor.get_name().lower() == name.lower():
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")
    
    def display_doctor_info(self, doctor):
        print("{:7}{:15}{:15}{:15}{:15}{:15}".format("ID", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
        print("{:7}{:15}{:15}{:15}{:15}{:15}".format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def edit_doctor_info(self):
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        doctor = next((d for d in self.doctors if d.get_doctor_id() == doctor_id), None)
        if doctor:
            doctor.set_name(input("Enter new name: "))
            doctor.set_specialization(input("Enter new Specialists in: "))
            doctor.set_working_time(input("Enter new Timing: "))
            doctor.set_qualification(input("Enter new Qualification: "))
            doctor.set_room_number(input("Enter new Room number: "))
            self.write_list_of_doctors_to_file()
            print(f'Doctor whose ID is {doctor.get_doctor_id()} has been edited')
        else:
            print("Can't find the doctor with the same ID on the system")

    def display_doctors_list(self):
        print("{:7}{:15}{:15}{:15}{:15}{:15}".format("ID", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
        for doctor in self.doctors:
            print("{:7}{:15}{:15}{:15}{:15}{:15}".format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def write_list_of_doctors_to_file(self):
        with open('doctors.txt', 'w') as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + '\n')

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open('doctors.txt', 'a') as file:
            file.write(self.format_dr_info(new_doctor) + '\n')
        print(f'Doctor whose ID is {new_doctor.get_doctor_id()} has been added')

class Patient:
    def __init__(self, pid="7896", pname="John", disease="COVID", gender="Male", age="23"):
        self.pid = pid
        self.pname = pname
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid
    
    def get_pname(self):
        return self.pname
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_pname(self, new_pname):
        self.pname = new_pname

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f'{self.pid}_{self.pname}_{self.disease}_{self.gender}_{self.age}'

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return f'{patient.get_pid()}_{patient.get_pname()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}'

    def enter_patient_info(self):
        pid = input("Enter Patient id: ")
        pname = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        return Patient(pid, pname, disease, gender, age)

    def read_patients_file(self):
        if os.path.exists('patients.txt'):
            with open('patients.txt', 'r') as file:
                for line in file:
                    pid, pname, disease, gender, age = line.strip().split('_')
                    self.patients.append(Patient(pid, pname, disease, gender, age))
        else:
            print("patients.txt file not found. Starting with an empty list.")

    def search_patient_by_id(self):
        pid = input("Enter the Patient Id: ")
        for patient in self.patients:
            if patient.get_pid() == pid:
                self.display_patient_info(patient)
                return
        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        print(f'\nID   Name                   Disease         Gender          Age')
        print(f'{patient.get_pid():<4} {patient.get_pname():<22} {patient.get_disease():<15} {patient.get_gender():<15} {patient.get_age()}')

    def edit_patient_info_by_id(self):
        pid = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == pid:
                new_name = input("Enter new Name: ")
                new_disease = input("Enter new disease: ")
                new_gender = input("Enter new gender: ")
                new_age = input("Enter new age: ")
                patient.set_pname(new_name)
                patient.set_disease(new_disease)
                patient.set_gender(new_gender)
                patient.set_age(new_age)
                self.write_list_of_patients_to_file()
                print(f"\nPatient whose ID is {pid} has been edited.")
                return
        print("Cannot find the patient...")

    def display_patients_list(self):
        print("\nID   Name                   Disease         Gender          Age")
        for patient in self.patients:
            print(f'{patient.get_pid():<4} {patient.get_pname():<22} {patient.get_disease():<15} {patient.get_gender():<15} {patient.get_age()}')

    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + '\n')

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open('patients.txt', 'a') as file:
            file.write(self.format_patient_info_for_file(new_patient) + '\n')
        print(f"\nPatient whose ID is {new_patient.get_pid()} has been added.")

class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Managment system ")
            print("Select from the following options, or select 3 to stop:")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.display_doctors_menu()
            elif choice == '2':
                self.display_patients_menu()
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1. Display doctors list")
            print("2. Search doctor by ID")
            print("3. Search doctor by name")
            print("4. Add new doctor")
            print("5. Edit doctor information")
            print("6. Return to main menu")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.doctor_manager.display_doctors_list()
            elif choice == '2':
                self.doctor_manager.search_doctor_by_id()
            elif choice == '3':
                self.doctor_manager.search_doctor_by_name()
            elif choice == '4':
                self.doctor_manager.add_dr_to_file()
            elif choice == '5':
                self.doctor_manager.edit_doctor_info()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_patients_menu(self):
        while True:
            print("\nPatients Menu:")
            print("1. Display patients list")
            print("2. Search patient by ID")
            print("3. Add new patient")
            print("4. Edit patient information")
            print("5. Return to main menu")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.patient_manager.display_patients_list()
            elif choice == '2':
                self.patient_manager.search_patient_by_id()
            elif choice == '3':
                self.patient_manager.add_patient_to_file()
            elif choice == '4':
                self.patient_manager.edit_patient_info_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    management = Management()
    management.display_menu()
