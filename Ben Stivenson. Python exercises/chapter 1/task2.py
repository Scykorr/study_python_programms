"""Упражнение 2. Приветствие"""
def print_hello(user_name: str) -> None:
    print(f'Здравствуйте, {user_name}!')

if __name__ == '__main__':
    user_name = input('Введите своё имя: ')
    print_hello(user_name=user_name)