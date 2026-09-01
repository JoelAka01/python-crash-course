from pathlib import Path

path = Path('guest_book.txt')
names = []

user_name = input("Enter your name: ")
while user_name:
    names.append(user_name)
    path.write_text('\n'.join(names) + '\n')  
    user_name = input("Enter your name: ")
