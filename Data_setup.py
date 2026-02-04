import sqlite3

def create_table():
    conn = sqlite3.connect('campus_cart.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            location TEXT NOT NULL,       
            seller_name TEXT NOT NULL,    
            contact TEXT NOT NULL,
            description TEXT              
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()