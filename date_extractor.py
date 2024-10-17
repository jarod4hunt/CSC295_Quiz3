from dateutil.parser import parse
import re

def extract_dates_from_text(text):
    # Use a regex to find potential date-like patterns
    date_candidates = re.findall(r'\b[\w\s\-,]+\b', text)
    dates = []

    for candidate in date_candidates:
        try:
            # Attempt to parse the candidate as a date
            parsed_date = parse(candidate, fuzzy=True)
            dates.append(parsed_date)
        except ValueError:
            # Skip if the candidate isn't a valid date
            pass

    return dates

if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        content = f.read()
        dates = extract_dates_from_text(content)
        print("Extracted Dates:")
        for date in dates:
            print(date.strftime("%Y-%m-%d"))