from hospital_manager import (
    add_patient, view_patients, update_patient, delete_patient,
    add_doctor, view_doctors, update_doctor, delete_doctor,
    schedule_appointment, view_appointments, update_appointment, cancel_appointment,
    allocate_room, view_rooms, update_room, release_room
)

def display_menu():
    print("\nHospital Management System")
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Room Management")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def patient_management():
    print("\nPatient Management")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        contact = input("Enter contact: ")
        medical_history = input("Enter medical history: ")
        add_patient(name, age, contact, medical_history)
        print("Patient added successfully!")
    
    elif choice == '2':
        patients = view_patients()
        for patient in patients:
            print(patient)
    
    elif choice == '3':
        patient_id = int(input("Enter patient ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        contact = input("Enter new contact: ")
        medical_history = input("Enter new medical history: ")
        update_patient(patient_id, name, age, contact, medical_history)
        print("Patient updated successfully!")
    
    elif choice == '4':
        patient_id = int(input("Enter patient ID to delete: "))
        delete_patient(patient_id)
        print("Patient deleted successfully!")

def doctor_management():
    print("\nDoctor Management")
    print("1. Add Doctor")
    print("2. View Doctors")
    print("3. Update Doctor")
    print("4. Delete Doctor")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter name: ")
        specialization = input("Enter specialization: ")
        contact = input("Enter contact: ")
        add_doctor(name, specialization, contact)
        print("Doctor added successfully!")
    
    elif choice == '2':
        doctors = view_doctors()
        for doctor in doctors:
            print(doctor)
    
    elif choice == '3':
        doctor_id = int(input("Enter doctor ID to update: "))
        name = input("Enter new name: ")
        specialization = input("Enter new specialization: ")
        contact = input("Enter new contact: ")
        update_doctor(doctor_id, name, specialization, contact)
        print("Doctor updated successfully!")
    
    elif choice == '4':
        doctor_id = int(input("Enter doctor ID to delete: "))
        delete_doctor(doctor_id)
        print("Doctor deleted successfully!")

def appointment_management():
    print("\nAppointment Management")
    print("1. Schedule Appointment")
    print("2. View Appointments")
    print("3. Update Appointment Status")
    print("4. Cancel Appointment")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        schedule_appointment(patient_id, doctor_id, date)
        print("Appointment scheduled successfully!")
    
    elif choice == '2':
        appointments = view_appointments()
        for appointment in appointments:
            print(f"ID: {appointment[0]}, Patient: {appointment[1]}, Doctor: {appointment[2]}, Date: {appointment[3]}, Status: {appointment[4]}")
    
    elif choice == '3':
        appointment_id = int(input("Enter appointment ID to update: "))
        status = input("Enter new status (Scheduled, Completed, Cancelled): ")
        update_appointment(appointment_id, status)
        print("Appointment status updated successfully!")
    
    elif choice == '4':
        appointment_id = int(input("Enter appointment ID to cancel: "))
        cancel_appointment(appointment_id)
        print("Appointment cancelled successfully!")

def room_management():
    print("\nRoom Management")
    print("1. Allocate Room")
    print("2. View Rooms")
    print("3. Update Room")
    print("4. Release Room")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        room_number = input("Enter room number: ")
        patient_id = int(input("Enter patient ID (or leave blank): ") or 0)  # Optional
        allocate_room(room_number, patient_id if patient_id else None)
        print("Room allocated successfully!")
    
    elif choice == '2':
        rooms = view_rooms()
        for room in rooms:
            print(f"Room ID: {room[0]}, Room Number: {room[1]}, Allocated To Patient ID: {room[2]}")
    
    elif choice == '3':
        room_id = int(input("Enter room ID to update: "))
        room_number = input("Enter new room number: ")
        patient_id = int(input("Enter new allocated patient ID (or leave blank): ") or 0)  # Optional
        update_room(room_id, room_number, patient_id if patient_id else None)
        print("Room updated successfully!")
    
    elif choice == '4':
        room_id = int(input("Enter room ID to release: "))
        release_room(room_id)
        print("Room released successfully!")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            patient_management()
        elif choice == '2':
            doctor_management()
        elif choice == '3':
            appointment_management()
        elif choice == '4':
            room_management()
        elif choice == '5':
            print("Thank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()