import re
from datetime import datetime


class Account:
    id = 0
    usernames = []

    def __init__(self, username, password, email=None):
        if username not in Account.usernames:
            Account.id += 1
            Account.usernames.append(username)
            self.username = username
            self.password = password
            self.email = email
            self.id = Account.id
            self.is_online = False
        else:
            raise ValueError

    def login(self, username):
        entered_password = input(f'Parolni kiriting: ')  # Asking for password
        if self.username == username and self.password == entered_password:
            self.is_online = True
            print(f'{self.username} {datetime.now()} da saytga kirdi.')
        else:
            print('Login yoki parol noto\'g\'ri')

    def logout(self):
        if self.is_online:
            self.is_online = False
            print(f'{self.username} saytdan chiqdi.')
        else:
            print('Siz hali saytga kirmadingiz... login methodi orqali saytga kiring.')

    def validate_password(self, password):
        if len(password) < 8:
            print('Parol 8 tadan kam bo`lmasligi kerak.')
            return False
        if not re.search(r"[A-Z]", password):
            print('Parol katta harfni o`z ichiga olishi kerak.')
            return False
        if not re.search(r"\d", password):
            print('Parol raqamni o`z ichiga olishi kerak.')
            return False
        return True

    def change_password(self):
        if self.is_online:
            password = input('Eski parolni kiriting: ')
            if self.password == password:
                new_password = input('Yangi parolni kiriting: ')
                while not self.validate_password(new_password):
                    new_password = input('Yangi parolni kiriting: ')
                self.password = new_password
                print('Parol muvaffaqiyatli o‘zgartirildi.')
            else:
                print('Parol noto‘g‘ri kiritildi.')
        else:
            print('Siz oldin saytga kiring!')


# Example usage
user1 = Account('user1', 'Password1')
user2 = Account('user2', 'Abcd123user', 'example@gamil.com')

# Login and change password
user1.login('user1')
user1.change_password()
user1.logout()
