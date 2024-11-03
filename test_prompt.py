import unittest

from prompt import *

class PromptTest(unittest.TestCase):
    def test_prompt_image(self):
        self.assertEqual(prompt_image(0), "https://zkbauuiquqlwlibhhuoy.supabase.co/storage/v1/object/public/location-images/Aldrich-Park_1600.jpg")

    # def test_prompt_images(self):
    #     self.assertEqual(prompt_images(), ["https://zkbauuiquqlwlibhhuoy.supabase.co/storage/v1/object/public/location-images/Aldrich-Park_1600.jpg"])
    
if __name__ == "__main__":
    unittest.main()
