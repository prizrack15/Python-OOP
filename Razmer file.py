class File:
    def __init__(self, size_in_bytes):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f'{self._size_in_bytes} B'
        elif 1023 < self._size_in_bytes < 1048577:
            return f'{self._size_in_bytes/1024:.2f} KB'
        elif 1048577 < self._size_in_bytes < 1073741824:
            return f'{self._size_in_bytes / (1024 ** 2):.2f} MB'
        elif self._size_in_bytes > 1073741823:
            return f'{self._size_in_bytes / (1024 ** 3):.2f} GB'

    @size.setter
    def size(self, value):
        self._size_in_bytes = value

file = File(5)
assert file.size == "5 B"
file.size = 1023
assert file.size == "1023 B"
file.size = 1024
assert file.size == "1.00 KB"

file_1 = File(1500000)
assert file_1._size_in_bytes == 1500000
assert file_1.size == "1.43 MB"

file_2 = File(1500)
assert file_2.size == "1.46 KB"


file_3 = File(2789326322)
assert file_3.size == "2.60 GB"
file_3.size = 1073741824
assert file_3.size == "1.00 GB"

print('Good')