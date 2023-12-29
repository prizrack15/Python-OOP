from string import ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if isinstance(value, str) == False:
            raise TypeError
        if '@' not in value or value.count('@') > 1:
            raise ValueError
        if '.' not in value or value.index('.') < (value.index('@')):
            raise ValueError
        else:
            self.__login = value

    @staticmethod
    def is_include_digit(kek):
        return any([i.isdigit() for i in kek])

    @staticmethod
    def is_include_all_register(value):
        lol1 = False
        lol2 = False
        if any([i.isupper() for i in value]):
            lol1 = True
        if any([i.islower() for i in value]):
            lol2 = True
        return (lol1 and lol2)

    @staticmethod
    def is_include_only_latin(argh):
        for i in range(len(argh)):
            if argh[i].isdigit():
                continue
            elif argh[i] not in ascii_letters:
                return False

    @staticmethod
    def check_password_dictionary(value):
        b = 0
        with open('easy_passwords.txt') as f:
            f = f.read().splitlines()
            for i in f:
                if i == value:
                    b += 1
            if b == 0:
                return False
            else:
                return True

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pas):
        if isinstance(new_pas, str) == False:
            raise TypeError("Пароль должен быть строкой")
        if len(new_pas) < 5 or len(new_pas) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if self.is_include_digit(new_pas) == False:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not self.is_include_all_register(new_pas):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if self.is_include_only_latin(new_pas):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(new_pas):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = new_pas


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')

