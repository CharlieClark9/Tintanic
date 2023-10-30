import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")
    global records, headings

    with open(file_path) as file:
        reader = csv.reader(file)
        headings = next(reader)
        for record in reader:
            records.append(record)
        num_records = len(records)
    print("Done")
    return num_records

def run():
    file_path = "C:\\Users\\charl\\Documents\\AMy Files\\Visual Studio\\Python\\Titanic\\titanic.csv"
    num_records = load_data(file_path)
    print(f"Successfully loaded {num_records} records.")


run()
