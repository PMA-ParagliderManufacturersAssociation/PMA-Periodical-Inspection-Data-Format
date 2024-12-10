![alt text](asset/PMALogo-500w-600dpi.png)

# PMA Periodical Inspection Data Format

This repository defines the standard JSON data exchange formats between paragliding inspection bodies and manufacturers, as specified by the Paragliding Manufacturer Association (PMA). These formats ensure uniformity and reliability in assessing the airworthiness of used paragliders.

## Overview

The JSON format supports bidirectional data exchange:
- **Manufacturer → Inspection Body:** Manufacturer information needed for the inspection.
    * [Specifications](specifications/specification_manufacturer-inspectionbody.md)
    * [Simplified example](examples/exemple_manufacturer-InspectionBody.json)
    * [Jalidator and JSON schema](validators/manufacturer_to_inspectionbody_python_validator.py)
    * [Scripts](scripts/TODO.txt)
- **Inspection Body → Manufacturer:** Detailed reports of inspection results. 
    * [Specifications](specifications/specification_inspectionbody-manufacturer.md)
    * [Simplified example](examples/exemple_InspectionBody_manufacturer.json)
    * [Validator and JSON schema](validators/inspectionbody_to_manufacturer_python_validator)
    * [Scripts](scripts/TODO.txt)



## Contributions

We welcome any proposals or improvements to the PMA Data Exchange Standard. Your feedback and suggestions help us refine the standard to better meet the needs of the paragliding community. Feel free to submit issues or pull requests.

## References
- [PMA website](https://www.p-m-a.info)
- [PMA Standard "Periodical Inspection of Paragliders"](https://www.p-m-a.info) 
