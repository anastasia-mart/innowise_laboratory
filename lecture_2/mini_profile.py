def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

print("Добро пожаловать в генератор мини-профилей!")

user_name = input("Enter your full name: ")
birth_year = int(input("Enter your birth year: "))
current_age = 2025 - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

print("\n---\nProfile Summary:")
print(f"Name: {user_name}")
print(f"Age: {current_age}")
print(f"Life Stage: {life_stage}")

if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
