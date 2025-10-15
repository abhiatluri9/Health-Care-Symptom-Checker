import sqlite3

conn = sqlite3.connect("symptom_history.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    result TEXT
)
""")
conn.commit()

def save_query(symptom: str, result: dict):
    cursor.execute("INSERT INTO history (symptom, result) VALUES (?, ?)", (symptom, str(result)))
    conn.commit()
