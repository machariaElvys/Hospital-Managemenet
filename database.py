import sqlite3

def init_db():
    conn = sqlite3.connect('hospital_management.db')
    cursor = conn.cursor()

    # Create patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            contact TEXT NOT NULL,
            medical_history TEXT
        )
    ''')

    # Create doctors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')

    # Create appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY(patient_id) REFERENCES patients(id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(id)
        )
    ''')

    # Create rooms table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            room_number TEXT NOT NULL,
            allocated_to INTEGER,
            FOREIGN KEY(allocated_to) REFERENCES patients(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()