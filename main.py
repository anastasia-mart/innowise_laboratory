from colorama import init, Fore, Back, Style

# Инициализируем colorama
init()

print("🎯 ОТЛАДКА: Программа запущена")
print("🎯 ОТЛАДКА: Colorama инициализирована")

# Выводим цветной Hello World
print(f"{Fore.RED}>{Back.YELLOW}Hello World!{Style.RESET_ALL}")
print("🎯 ОТЛАДКА: Первая цветная строка выполнена")

print(f"{Fore.GREEN}Hello World in Green!{Style.RESET_ALL}")
print("🎯 ОТЛАДКА: Вторая цветная строка выполнена")

print(f"{Fore.BLUE}>{Style.BRIGHT}Hello World in Bright Blue!{Style.RESET_ALL}")
print("🎯 ОТЛАДКА: Третья цветная строка выполнена")

print(f"{Fore.MAGENTA}>{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")
print("🎯 ОТЛАДКА: Все цветные строки выполнены")
print("🎯 ОТЛАДКА: Программа завершена успешно!")