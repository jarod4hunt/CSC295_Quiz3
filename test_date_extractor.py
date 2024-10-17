import unittest
from date_extractor import extract_dates_from_text

class TestDateExtractor(unittest.TestCase):
    def test_extract_dates(self):
        with open("sample.txt", "r") as f:
            text = f.read()
        
        result = extract_dates_from_text(text)

        # Expected dates in the format (Year, Month, Day)
        expected_dates = [
            "2023-09-15",
            "2024-10-20",
            "2023-10-15"
        ]
        extracted_dates = [date.strftime("%Y-%m-%d") for date in result]

        self.assertEqual(extracted_dates, expected_dates)

if __name__ == '__main__':
    unittest.main()