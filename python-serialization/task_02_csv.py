#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data = []
        # Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Use DictReader to turn each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        # Open the JSON file for writing
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            # Serialize the list of dictionaries to JSON
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # Return False if the specified CSV file does not exist
        return False
    except Exception:
        # Return False for any other unexpected errors
        return False
