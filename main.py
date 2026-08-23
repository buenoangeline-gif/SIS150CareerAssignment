import unittest


class SmartLight:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def change_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
        else:
            raise ValueError("Brightness must be between 0 and 100.")


# Create an object and test it manually
my_light = SmartLight()

my_light.turn_on()
my_light.change_brightness(80)

print("Light on:", my_light.is_on)
print("Brightness:", my_light.brightness)

my_light.turn_off()
print("Light on:", my_light.is_on)


# Unit tests
class TestSmartLight(unittest.TestCase):

    def test_turn_on(self):
        light = SmartLight()
        light.turn_on()
        self.assertTrue(light.is_on)

    def test_turn_off(self):
        light = SmartLight()
        light.turn_on()
        light.turn_off()
        self.assertFalse(light.is_on)

    def test_change_brightness(self):
        light = SmartLight()
        light.change_brightness(50)
        self.assertEqual(light.brightness, 50)

    def test_invalid_brightness(self):
        light = SmartLight()

        with self.assertRaises(ValueError):
            light.change_brightness(150)


if __name__ == "__main__":
    unittest.main()