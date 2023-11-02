import unittest
import my_module
import sys
import os

# Mendapatkan direktori tempat berkas test_my_module.py berada
current_dir = os.path.dirname(__file__)

# Mendapatkan direktori tempat my_module.py berada dan menambahkannya ke sys.path
# Ganti '..' dengan direktori yang sesuai
module_dir = os.path.join(current_dir, '..')
sys.path.append(module_dir)

# Sekarang Anda bisa mengimpor my_module
# my_module.py


def add(a, b):
    return a + b


# test_my_module.py


class testmymodule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_module.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
