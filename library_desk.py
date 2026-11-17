# College Library Desk

# Taking member details
name = input("Enter member name: ")
age = int(input("Enter age: "))
books = int(input("Enter borrowed books: "))
student = input("Are you a student? (yes/no): ").lower() == "yes"

fine = 0.0
books += 1
has_a = 'a' in name.lower()

eligible = (student is True) and (age > 17) and (books < 5)

# Display summary
print("\n--- Library Membership Summary ---")
print("Name:", name)
print("Age:", age)
print("Books Borrowed:", books)
print("Fine:", fine)
print("Student:", "Yes" if student else "No")
print("Contains letter 'a':", has_a)
print("Eligible:", "eligible" if eligible else "Not Eligible")