# Section 1: Variables and types

student_name = "Jason"
teams_coached = 4
weekly_study_hours =19.5
learning_python = True

print(student_name, type(student_name))
print(teams_coached, type(teams_coached))
print(weekly_study_hours, type(weekly_study_hours))
print(learning_python, type(learning_python))

#Section 2: User Input and age

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

age = 2026 - birth_year
print(f"Hello {name}! Your approximate age is {age}.")

#Section 3: Numbers and f-strings

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

product = first_number * second_number

print(f"{first_number} multiplied by {second_number} = {product}.")

# Section 4: Formatted receipt

item = "Notebook"
price = 4.99
quantity = 3
total = price * quantity

print("\n--- RECEIPT ---")
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")

# Section 5: Profile card

profile_name = input("\nWhat is your name? ")
hometown = input("What is your hometown? ")
favorite_hobby = input("What is your favorite hobby? ")
fun_fact = input("Share a fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))

profile_age = 2026 - profile_birth_year

print("\n--- PROFILE CARD ---")
print(f"Name: {profile_name}")
print(f"Hometown: {hometown}")
print(f"Hobby: {favorite_hobby}")
print(f"Fun Fact: {fun_fact}")
print(f"Age: {profile_age}")
