import unittest
from temperature import Temperature

class mytestTemp(unittest.TestCase):
    def testCelsius(self):
        test_celsius = Temperature(celsius=30)
        self.assertEqual(test_celsius.kelvin, 303.15)
    
    def testFahrenheit(self):
        test_fahrenheit = Temperature(fahrenheit=90)
        self.assertEqual(test_fahrenheit.kelvin, 305.37)

    def testCelsius2(self):
        test_celsius2 = Temperature(celsius=20)
        self.assertEqual(test_celsius2.kelvin, 293.15)

    def testFahrenheit(self):
        test_fahrenheit2 = Temperature(fahrenheit=100)
        self.assertEqual(test_fahrenheit2.kelvin, 310.92777777777775)

if __name__ == '__main__':
    unittest.main()