import sqlite3

# Connect to database
conn = sqlite3.connect("shopping.db")
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL,
    stock INTEGER
)
""")

# Insert products
products = [
    (1, "Laptop", "Electronics", 55000, 10),
    (2, "Mouse", "Electronics", 800, 25),
    (3, "Keyboard", "Electronics", 1500, 15),
    (4, "Backpack", "Accessories", 1200, 20),
    (5, "Headphones", "Electronics", 2500, 12)
]

cursor.executemany("""
INSERT OR REPLACE INTO products
(id, name, category, price, stock)
VALUES (?, ?, ?, ?, ?)
""", products)

# Display all products
print("All Products:")
cursor.execute("SELECT * FROM products")

for product in cursor.fetchall():
    print(product)

# Electronics products
print("\nElectronics Products:")
cursor.execute("""
SELECT name, price
FROM products
WHERE category = ?
""", ("Electronics",))

for product in cursor.fetchall():
    print(product)

# Products below ₹2000
print("\nProducts Below ₹2000:")
cursor.execute("""
SELECT name, price
FROM products
WHERE price < ?
""", (2000,))

for product in cursor.fetchall():
    print(product)

# Update stock
cursor.execute("""
UPDATE products
SET stock = stock - ?
WHERE name = ?
""", (2, "Laptop"))

# Find most expensive product
cursor.execute("SELECT MAX(price) FROM products")
highest_price = cursor.fetchone()[0]

print("\nHighest Product Price:", highest_price)

# Calculate average price
cursor.execute("SELECT AVG(price) FROM products")
average_price = cursor.fetchone()[0]

print("Average Product Price:", round(average_price, 2))

# Count total products
cursor.execute("SELECT COUNT(*) FROM products")
total_products = cursor.fetchone()[0]

print("Total Products:", total_products)

conn.commit()
conn.close()