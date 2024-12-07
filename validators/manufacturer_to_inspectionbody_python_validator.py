"""
Manufacturer to Inspection Body JSON Validator
------------------------------------------------

This script validates JSON data against the "Manufacturer to Inspection Body Specification."
It ensures the data complies with the schema defined in the external JSON schema file.

Author: Fred
Version: 1.0
Date: 07/12/2024

Usage:
    1. Place the schema file (`manufacturer_to_inspection_schema.json`) in the same directory as this script.
    2. Prepare the JSON data to validate in the `example_data` variable or load it from a file.
    3. Run the script:
       $ python validate_json.py
    4. The script will output whether the JSON data is valid or describe validation errors.

Dependencies:
    - Python 3.7 or higher
    - jsonschema library (install using `pip install jsonschema`)

Schema File:
    The schema is stored in `manufacturer_to_inspection_schema.json`.

Example Output:
    - "JSON data is valid." (if the JSON data complies with the schema)
    - "Validation Error: [error description]" (if the JSON data does not comply with the schema)

"""

# %%
import json
from jsonschema import validate, ValidationError, SchemaError


# Load the schema from an external file
def load_schema(schema_file):
    with open(schema_file, "r") as file:
        return json.load(file)


# Path to the schema file
schema_path = "manufacturer_to_inspection_schema.json"

# Load the schema
schema = load_schema(schema_path)


# Function to validate JSON data
def validate_json(data):
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid.")
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
    except SchemaError as e:
        print(f"Schema Error: {e.message}")


# Example JSON data for validation
example_data = {
    "_comment": "Template Manufacturer to Inspection Body",
    "PMA_file_format": "2023.3.0",
    "manufacturer": "BestGlider",
    "model": "Tornado",
    "size": "ML",
    "weight_min": 80,
    "weight_max": 95,
    "inspection_interval": "3 years or 150hr",
    "inspection_protocol": "according to PMA standard",
    "line_details": [
        {
            "name": "AR1",
            "material": "8000U_320",
            "color": "Red",
            "construction_details": "loop externally reinforced",
            "sewn_length": 3254,
            "minimum_strength": 150,
            "parent": None,
        },
        {
            "name": "AM1",
            "material": "8000U_190",
            "color": "Red",
            "construction_details": "loop reinforced",
            "sewn_length": 1542,
            "minimum_strength": 98.7,
            "parent": "AR1",
        },
    ],
    "total_line_lengths": [
        {"name": "A1", "total_length": 7254},
        {"name": "A2", "total_length": 7235},
    ],
    "comment": "Any comments",
}

# Validate the example data
validate_json(example_data)

# %%
