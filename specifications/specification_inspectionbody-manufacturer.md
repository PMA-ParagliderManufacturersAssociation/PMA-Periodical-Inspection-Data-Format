## Inspection Report JSON Format Specification

### Inspection Body to Manufacturer Specification

- **From:** Inspection body  
- **To:** Paraglider manufacturer  
- **Specification Version:** 1.0  
- **Document Version:** 1.0  

#### Units
All units must adhere to the standards described in the PMA standard.

#### Info
This specification defines the JSON format for data exchanged from inspection bodies to manufacturers. This format includes the inspection results.

---

#### General Structure

| Field                              | Type                   | Description                                                    |
|------------------------------------|------------------------|----------------------------------------------------------------|
| `PMA_file_format`            | `string`    | Version of the PMA file format standard                                     |
| `manufacturer`               | `string`    | Name of the paraglider manufacturer                                                   |
| `model`                      | `string`    | Model name of the paraglider                                                |
| `size`                       | `string`    | Paraglider Size                                                            |
| `standard_version`                 | `string`               | Which version of the standard was used during the inspection   |
| `serial_number`                    | `string`               | Unique serial number of the inspected glider                   |
| `inspection_date`                  | `string (datetime)`    | Date and time of inspection (ISO 8601)                         |
| `_comment`                         | `string`               | Optional comment              |

---

#### Visual Inspection 

| Field                                  | Type         | Description                             |
|----------------------------------------|--------------|-----------------------------------------|
| `visual_inspection_stickers`           | `string`     | Sticker inspection result               |
| `visual_inspection_upper_surface`      | `string`     | Upper surface condition                 |
| `visual_inspection_lower_surface`      | `string`     | Lower surface condition                 |
| `visual_inspection_internal_structure` | `string`     | Internal structure condition            |
| `visual_inspection_line_attachment_points` | `string` | Line attachment point condition         |
| `visual_inspection_lines`              | `string`     | Lines inspection result                 |
| `visual_inspection_risers`             | `string`     | Risers inspection result                |

---

#### Fabric Porosity 

| Field                     | Type         | Description                                  |
|---------------------------|--------------|----------------------------------------------|
| `porosimeter_model`       | `string`     | Model of the porosimeter used                |
| `porosity_upper`          | `array`      | Array of objects representing porosity measurements for the upper surface |
| - `panel`                 | `string`     | Panel number for the measurement             |
| - `value`                 | `integer`    | Porosity value for the panel                 |
| `porosity_lower`          | `array`      | Array of objects representing porosity measurements for the lower surface |
| - `panel`                 | `string`     | Panel number for the measurement             |
| - `value`                 | `integer`    | Porosity value for the panel  

---

#### Fabric Tear Strength 

| Field                         | Type       | Description                                     |
|-------------------------------|------------|-------------------------------------------------|
| `tear_strength_upper`         | `array`    | Array of objects representing tear strength measurements for the upper surface |
| - `panel`                     | `string`   | Panel number for the measurement               |
| - `result`                    | `string` or `integer` | Tear strength result, which can be a descriptive status (`"Good"`, `"Acceptable"`, `"Fail"`) or a numeric value (e.g., `750`, `1200`) |
| `tear_strength_lower`         | `array`    | Array of objects representing tear strength measurements for the lower surface |
| - `panel`                     | `string`   | Panel number for the measurement               |
| - `result`                    | `string` or `integer` | Tear strength result, which can be a descriptive status (`"Good"`, `"Acceptable"`, `"Fail"`) or a numeric value (e.g., `750`, `1200`) |

---

#### Line Strength 

| Field                | Type      | Description                                  |
|----------------------|-----------|----------------------------------------------|
| `line_strengths`     | `array`   | Array of objects, each with `name` and `value` or default minimum strength if unavailable |
| - `name`             | `string`  | Line identifier name                         |
| - `value`            | `integer` | Measured strength value of the line          |

---

#### Line Geometry

| Field                     | Type      | Description                                |
|---------------------------|-----------|--------------------------------------------|
| `total_line_geometry`     | `array`   | Array of objects, each with `name` and `total_length` or default minimum length if unavailable |
| - `name`                  | `string`  | Line identifier name                       |
| - `total_length`          | `integer` | Total length of the line                   |

---

#### Additional Comments

| Field            | Type       | Description                      |
|------------------|------------|----------------------------------|
| `modifications`  | `string`   | Comments on any modifications    |
| `comment`        | `string`   | General comments about the inspection |
