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
    (1, "Laptop", "Electronics", 55000, 5),
    (2, "Mouse", "Electronics", 800, 20),
    (3, "Keyboard", "Electronics", 1500, 15),
    (4, "Chair", "Furniture", 4500, 8),
    (5, "Table", "Furniture", 7000, 3)
]

cursor.executemany("""
INSERT OR IGNORE INTO products
VALUES (?, ?, ?, ?, ?)
""", products)

# Display all products
print("PRODUCT INVENTORY")
cursor.execute("SELECT * FROM products")

for product in cursor.fetchall():
    print(product)

# Products with price above 2000
print("\nProducts above ₹2000:")

cursor.execute("""
SELECT name, price
FROM products
WHERE price > 2000
ORDER BY price DESC
""")

for product in cursor.fetchall():
    print(product)

# Products with low stock
print("\nLow Stock Products:")

cursor.execute("""
SELECT name, quantity
FROM products
WHERE quantity < 10
""")

for product in cursor.fetchall():
    print(product)

# Calculate total inventory value
cursor.execute("""
SELECT SUM(price * quantity)
FROM products
""")

total_value = cursor.fetchone()[0]

print("\nTotal Inventory Value: ₹", total_value)

# Find the most expensive product
cursor.execute("""
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 1
""")

expensive = cursor.fetchone()

print("Most Expensive Product:", expensive)

# Close connection
conn.commit()
conn.close()