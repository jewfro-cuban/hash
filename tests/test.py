import unittest
from hash.hashtable import HashTable

class TestHash(unittest.TestCase):
    def test_set(self):
        h = HashTable()
        h[20] = 123
        self.assertEqual(h.items(), '[ [20,123] ]')

    def test_pop(self):
        h = HashTable()
        h[20] = 'use'
        h[23] = 123
        self.assertEqual(h.pop(20), 'use')
        self.assertEqual(h.pop(23), 123)
    
    def test_get(self):
        h = HashTable()
        h[20] = 'use'
        self.assertEqual(h.get(20), 'use')
        self.assertEqual(h.get(12), None)

if __name__ == '__main__':
    unittest.main()
