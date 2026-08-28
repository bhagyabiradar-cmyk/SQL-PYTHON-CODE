import sqlite3

# Connect to database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

# Insert products
products = [
    (1, "Laptop", "Electronics", 55000, 10),
    (2, "Mouse", "Electronics", 800, 25),
    (3, "Keyboard", "Electronics", 1500, 15),
    (4, "Chair", "Furniture", 4500, 8),
    (5, "Table", "Furniture", 7000, 5)
]

cursor.executemany("""
INSERT OR IGNORE INTO products
VALUES (?, ?, ?, ?, ?)
""", products)

# Display all products
print("ALL PRODUCTS")
cursor.execute("SELECT * FROM products")

for row in cursor.fetchall():
    print(row)

# Products costing more than 5000
print("\nPRODUCTS ABOVE 5000")
cursor.execute("""
SELECT name, price
FROM products
WHERE price > 5000
""")

for row in cursor.fetchall():
    print(row)

# Find total inventory value
print("\nTOTAL INVENTORY VALUE")
cursor.execute("""
SELECT SUM(price * quantity)
FROM products
""")

print(cursor.fetchone()[0])

# Find most expensive product
print("\nMOST EXPENSIVE PRODUCT")
cursor.execute("""
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 1
""")

print(cursor.fetchone())

# Update product quantity
cursor.execute("""
UPDATE products
SET quantity = quantity + 5
WHERE name = 'Mouse'
""")

conn.commit()

print("\nMouse quantity updated successfully!")

conn.close()