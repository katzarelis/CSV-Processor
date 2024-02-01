import csv

class CSVProcessor:
    def __init__(self, file1, file2, output_file):
        """
        Initialize CSVProcessor
        """
        self.file1 = file1
        self.file2 = file2
        self.output_file = output_file

    def read_csv(self, file_path):
        """
        Read data from a CSV file and return a dictionary with id as keys and score as values.

        Returns dictionary with id as keys and score as values.
        """
        data_dict = {}
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Create a nested dictionary for each 'id' with 'name' and 'score' fields
                data_dict[row['id']] = {'name': row.get('name', None), 'score': data_dict.get(row['id'], 0) + int(row['score'])}
        return data_dict
    
    def combine_and_save(self):
        """
        Combine data from two CSV files, summing the scores, and save the result in a new CSV file.
        """
        data1 = self.read_csv(self.file1)
        data2 = self.read_csv(self.file2)

        combined_data = {}

        # Explicitly handle combination of data from file1
        for id, info in data1.items():
            combined_data[id] = {'score': info['score'], 'name': info.get('name', None)}

        # Explicitly handle combination of data from file2
        for id, info in data2.items():
            if id in combined_data:
                combined_data[id]['score'] += info['score']
            else:
                combined_data[id] = {'score': info['score'], 'name': info['name']}

        # Sort combined data by 'id' before saving
        sorted_combined_data = sorted(combined_data.items(), key=lambda x: int(x[0]))

        with open(self.output_file, 'w', newline='') as csv_file:
            fieldnames = ['id', 'name', 'score']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for key, value in sorted_combined_data:
                csv_writer.writerow({'id': key, 'name': value['name'], 'score': value['score']})


    def get_score_by_name(self, name):
        """
        Retrieve the id and score for a given name from the combined data.

        Returns tuple or None. A tuple containing (id, score) if the name is found, else None.
        """
        combined_data = self.read_csv(self.output_file)
        for id, info in combined_data.items():
            # Compare the 'name' field during the search
            if info.get('name') == name:
                return id, info['score']
        return None

# Example usage
processor = CSVProcessor('file1.csv', 'file2.csv', 'output.csv')
processor.combine_and_save()

# Test 
name_to_search = 'John'
result = processor.get_score_by_name(name_to_search)

if result:
    print(f"Score for {name_to_search}: {result[1]}")
else:
    print(f"{name_to_search} not found.")

# Test 
name_to_search = 'Maria'
result = processor.get_score_by_name(name_to_search)

if result:
    print(f"Score for {name_to_search}: {result[1]}")
else:
    print(f"{name_to_search} not found.")
