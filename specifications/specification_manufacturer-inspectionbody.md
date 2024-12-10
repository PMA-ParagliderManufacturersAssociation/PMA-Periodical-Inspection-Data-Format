## Manufacturer to Inspection Body Specification

### Manufacturer to Inspection Body Specification

- **From:** Paraglider manufacturer  
- **To:** Inspection body  
- **Specification Version:** 1.0  
- **Document Version:** 1.0  

#### Units
All units must adhere to the standards described in the PMA standard.

#### Info
This specification defines the JSON format for data exchanged from manufacturers to inspection bodies. This format includes the manufacturer's information, inspection protocols, and line details required for conducting inspections.


---
#### General 

| Field                        | Type        | Description                                                                 |
|------------------------------|-------------|-----------------------------------------------------------------------------|
| `PMA_file_format`            | `string`    | Version of the PMA file format standard                                     |
| `manufacturer`               | `string`    | Name of the paraglider manufacturer                                                   |
| `model`                      | `string`    | Model name of the paraglider                                                |
| `size`                       | `string`    | Paraglider Size                                                            |
| `weight_min`                 | `integer`   | Minimum of the paraglider weight range (in kg)                                       |
| `weight_max`                 | `integer`   | Maximum of the paraglider weight range (in kg)                                   |
| `inspection_interval`        | `string`    | Recommended inspection interval (e.g., time or usage hours)                |
| `inspection_protocol`        | `string`    | Protocol details, including deviations from PMA standards                  |
| `standard_version`           | `string`    | Which version of the standard to use during the inspection   |

---

#### Line Details

| Field                        | Type        | Description                                                                 |
|------------------------------|-------------|-----------------------------------------------------------------------------|
| `line_details`               | `array`     | Array of objects describing the details of individual lines                |
| - `name`                     | `string`    | Name of the line                                                           |
| - `material`                 | `string`    | Material of the line ( core material in case of sheathed lines)                                                      |
| - `color`                    | `string`    | Color of the line                                                          |
| - `construction_details`     | `string` or `null` | Construction details (e.g., reinforcements)                          |
| - `sewn_length`              | `integer`   | Sewn length of the line (in mm)                                            |
| - `minimum_strength`         | `number`    | Minimum strength of the line                                               |
| - `value_new       `         | `number`    | Strength of the line when new                                              |
| - `parent`                   | `string` or `null` | Name of the parent line (or `null` if it has no parent)              |

---

#### Total Line Lengths

| Field                        | Type        | Description                                                                 |
|------------------------------|-------------|-----------------------------------------------------------------------------|
| `total_line_lengths`         | `array`     | Array of objects representing the total length of main lines               |
| - `name`                     | `string`    | Name of the main line                                                      |
| - `total_length`             | `integer`   | Total length of the line (in mm)                                           |

---

#### Additional Comments

| Field                        | Type        | Description                                                                 |
|------------------------------|-------------|-----------------------------------------------------------------------------|
| `comment`                    | `string`    | Any additional comments or notes                                           |

---
