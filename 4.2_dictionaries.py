"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Information about a laptop.
# 2. Process: The program stores the laptop information in a dictionary. It reads one field, changes one field, removes one field, and then displays all the remaining fields and their values
# 3. Out: The laptop information displayed as field-value pairs.
# 4. My object, my five fields, and why those: I chose a laptop because it is a common object in the IT field. The dictionary stores information such as its brand, model, processor, RAM, storage, and price.




# Your code below


laptop = {
    "brand": "Dell",
    "model": "Inspiron 15",
    "processor": "Intel Core i5",
    "RAM": "16 GB",
    "storage": "512 GB SSD",
    "price": 700
}

# Read one field
print("Laptop model:", laptop["model"])

# Change one field
laptop["RAM"] = "32 GB"

# Remove one field
del laptop["storage"]

# Display every field with its value
print("\nLaptop information:")

for field, value in laptop.items():
    print(field, ":", value)