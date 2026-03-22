import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        stock INTEGER
    )
""")

cursor.executemany("INSERT INTO products VALUES (?,?,?,?,?)", [
    (1, "Laptop",     "Electronics", 999.99,  45),
    (2, "Desk Chair", "Furniture",   249.99,  12),
    (3, "Monitor",    "Electronics", 399.99,  30),
    (4, "Keyboard",   "Electronics",  79.99, 100),
    (5, "Bookshelf",  "Furniture",   149.99,   8),
    (6, "Webcam",     "Electronics",  59.99,  55),
])

conn.commit()
conn.close()
print("Database created successfully!")