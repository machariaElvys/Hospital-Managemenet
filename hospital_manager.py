import sqlite3

def connect_db():
    return sqlite3.connect('hospital_management.db')

# Patient Management
def add_patient(name, age, contact, medical_history):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO patients (name, age, contact, medical_history) VALUES (?, ?, ?, ?)', 
                   (name, age, contact, medical_history))
    conn.commit()
    conn.close()

def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return patients

def update_patient(patient_id, name, age, contact, medical_history):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE patients SET name = ?, age = ?, contact = ?, medical_history = ? WHERE id = ?', 
                   (name, age, contact, medical_history, patient_id))
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()

# Doctor Management
def add_doctor(name, specialization, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO doctors (name, specialization, contact) VALUES (?, ?, ?)', 
                   (name, specialization, contact))
    conn.commit()
    conn.close()

def view_doctors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doctors')
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def update_doctor(doctor_id, name, specialization, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE doctors SET name = ?, specialization = ?, contact = ? WHERE id = ?', 
                   (name, specialization, contact, doctor_id))
    conn.commit()
    conn.close()

def delete_doctor(doctor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM doctors WHERE id = ?', (doctor_id,))
    conn.commit()
    conn.close()

# Appointment Management
def schedule_appointment(patient_id, doctor_id, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (patient_id, doctor_id, date) VALUES (?, ?, ?)', 
                   (patient_id, doctor_id, date))
    conn.commit()
    conn.close()

def view_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT a.id, p.name, d.name, a.date, a.status FROM appointments a '
                   'JOIN patients p ON a.patient_id = p.id '
                   'JOIN doctors d ON a.doctor_id = d.id')
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def update_appointment(appointment_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE appointments SET status = ? WHERE id = ?', (status, appointment_id))
    conn.commit()
    conn.close()

def cancel_appointment(appointment_id):
    update_appointment(appointment_id, 'Cancelled')

# Room Management
def allocate_room(room_number, allocated_to=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rooms (room_number, allocated_to) VALUES (?, ?)', 
                   (room_number, allocated_to))
    conn.commit()
    conn.close()

def view_rooms():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms')
    rooms = cursor.fetchall()
    conn.close()
    return rooms

def update_room(room_id, room_number, allocated_to):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE rooms SET room_number = ?, allocated_to = ? WHERE id = ?', 
                   (room_number, allocated_to, room_id))
    conn.commit()
    conn.close()

def release_room(room_id):
    update_room(room_id, None, None)