"""
Inspection to Manufacturer JSON Validator
-----------------------------------------

This script validates JSON data against the "Inspection to Manufacturer Specification."
It ensures the data complies with the schema defined in the external JSON schema file.

Author: Fred
Version: 1.0
Date: 07/12/024

Usage:
    1. Place the schema file (`inspectionbody-manufacturer.schema.json`) in the same directory as this script.
    2. Prepare the JSON data to validate in the `example_data` variable or load it from a file.
    3. Run the script:
       $ python validate_inspection_to_manufacturer.py
    4. The script will output whether the JSON data is valid or describe validation errors.

Dependencies:
    - Python 3.7 or higher
    - jsonschema library (install using `pip install jsonschema`)

Schema File:
    The schema is stored in `inspectionbody-manufacturer.schema.json`.

Example Output:
    - "JSON data is valid." (if the JSON data complies with the schema)
    - "Validation Error: [error description]" (if the JSON data does not comply with the schema)
"""

import json
from jsonschema import validate, ValidationError, SchemaError


# Load the schema from an external file
def load_schema(schema_file):
    with open(schema_file, "r") as file:
        return json.load(file)


# Path to the schema file
schema_path = "inspectionbody-manufacturer.schema.json"

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
    "PMA_file_format": "2023.3.0",
    "manufacturer": "BestGlider",
    "model": "Tornado",
    "size": "ML",
    "standard_version": "PMA 2022",
    "serial_number": "TOR_21147_H",
    "inspection_date": "2022-03-15T14:25:00Z",
    "_comment": "Inspection results",
    "visual_inspection_stickers": "OK",
    "visual_inspection_upper_surface": "OK",
    "visual_inspection_lower_surface": "OK",
    "visual_inspection_internal_structure": "OK",
    "visual_inspection_line_attachment_points": "OK",
    "visual_inspection_lines": "Damaged",
    "visual_inspection_risers": "Used",
    "porosimeter_model": "JDC mk2",
    "porosity_upper": [{"panel": "4", "value": 157}],
    "porosity_lower": [{"panel": "7", "value": 57}],
    "tear_strength_upper": [{"panel": "4_1", "result": "OK"}],
    "tear_strength_lower": [{"panel": "7_2", "result": 1600}],
    "line_strengths": [{"name": "AR1", "value": 178}],
    "total_line_geometry": [{"name": "A1", "total_length": 7254}],
    "modifications": "None",
    "comment": "General comments",
}

# Validate the example data
validate_json(example_data)
