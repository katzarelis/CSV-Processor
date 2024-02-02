# CSV Processor

A Python script for combining and processing data from CSV files.

## Features

Reads CSV files with a unique identifier ('id' field).
Combines data from two CSV files, summing scores for matching 'id' values.
Saves the combined data into a new CSV file.
Retrieves the combined score for a given name.
## Usage

The CSVProcessor class provides the following methods:

### read_csv(file_path)

Reads data from a CSV file and returns a dictionary with 'id' as keys and 'score' as values.

### combine_and_save()

Combines data from two CSV files, sums the scores for matching 'id' values, and saves the result in a new CSV file.

### get_score_by_name(name)

Retrieves the 'id' and 'score' for a given name from the combined data.

## Additional Information

- **Supported CSV Format:** Ensure your CSV files have a header row with 'id' and 'score' columns, and values are in an appropriate numerical format for score calculation.

- **Error Handling:** Consider adding error handling to gracefully handle potential issues like file read errors or invalid data types.

- **Unit Tests:** Implement unit tests to ensure the script's functionality and catch any issues during development.
