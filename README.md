# RapidCenter

## Overview
RapidCenter is a Python-based program designed to efficiently manage and analyze data storage on Windows systems. It utilizes advanced algorithms to gather, analyze, and report on storage data, helping users identify critical usage levels and manage their storage resources effectively.

## Features
- **Storage Information Gathering**: Collects detailed information about all disk partitions and their usage.
- **Critical Usage Analysis**: Identifies partitions with critical usage levels (above 90%).
- **Storage Management**: Provides insights for managing storage effectively based on analysis.
- **Report Generation**: Saves a storage report in JSON format for further analysis or record-keeping.

## Requirements
- Python 3.x
- `psutil` library

## Installation
To install the required library, you can use pip:

```bash
pip install psutil
```

## Usage
1. Clone this repository or download the `rapid_center.py` file.
2. Run the program using Python:

```bash
python rapid_center.py
```

3. The program will output the current storage analysis and save a report as `storage_report.json`.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with any enhancements or bug fixes.

## Contact
For any inquiries or support, please contact the project maintainer.