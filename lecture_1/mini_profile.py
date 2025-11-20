def generate_profile(age):
    """Определяет жизненную стадию по возрасту."""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

print("Добро пожаловать в генератор мини-профилей!")

# Получаем основную информацию
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Собираем хобби
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

# Обрабатываем данные
life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Выводим результат
print("\n---\nProfile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies']}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")
