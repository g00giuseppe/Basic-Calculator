import unittest

from app import addizione, divisione, moltiplicazione, potenza, radice_quadrata, sottrazione

class TestCalcolatrice(unittest.TestCase):

  def test_addizione(self):
    self.assertEqual(addizione(1, 2), 3)
    self.assertEqual(addizione(-1, -2), -3)

  def test_sottrazione(self):
    self.assertEqual(sottrazione(3, 2), 1)
    self.assertEqual(sottrazione(-2, -1), -1)

  def test_moltiplicazione(self):
    self.assertEqual(moltiplicazione(2, 3), 6)
    self.assertEqual(moltiplicazione(-2, -3), 6)

  def test_divisione(self):
    self.assertEqual(divisione(6, 2), 3)
    with self.assertRaises(ZeroDivisionError):
      divisione(1, 0)

if __name__ == '__main__':
  unittest.main()
