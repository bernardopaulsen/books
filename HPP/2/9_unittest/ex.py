import unittest

@profile
def some_fn(nbr):
    return nbr * 2

class TestCase(unittest.TestCase):
    def test(self):
        result = some_fn(2)
        self.assertEquals(result, 4)