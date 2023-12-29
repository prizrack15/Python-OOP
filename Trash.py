class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File) == False:
            print('В корзину добавлять можно только файл')
        else:
            Trash.content.append(file)
            file.in_trash = True

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for i in Trash.content:
            File.remove(i)
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for i in Trash.content:
            File.restore_from_trash(i)
        Trash.content = []
        print('Корзина пуста')


class File:

    def __init__(self, name):
        self.is_deleted = False
        self.in_trash = False
        self.name = name

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted == True:
            return print(f'ErrorReadFileDeleted({self.name})')
        if self.in_trash == True:
            return print(f'ErrorReadFileTrashed({self.name})')
        if self.is_deleted == False and self.in_trash == False:
            return print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted == True:
            return print(f'ErrorWriteFileDeleted({self.name})')
        if self.in_trash == True:
            return print(f'ErrorWriteFileTrashed({self.name})')
        if self.is_deleted == False and self.in_trash == False:
            return print(f'Записали значение {content} в файл {self.name}')


f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content

Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()
