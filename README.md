# LogFileAnalyzer

**LogFileAnalyzer** is a Python-based tool designed to automate the parsing, analysis, and summarization of system log files. It helps users extract key metrics and generate concise summaries for quick diagnostics and reporting.

## Features

- Parses log files with varying formats and handles edge cases (e.g., missing/invalid data).
- Generates structured reports in CSV and TXT formats.
- Includes unit tests for core functionality.
- Modular design with easy-to-extend components.

## Project Structure

LogFileAnalyzer/<br>
│ <br>
├── log_analyzer.py # Core logic for parsing and analyzing logs <br>
├── setup.py # Setup script for packaging (optional) <br>
├── report.txt # Sample output report <br>
│ <br>
├── sample_logs/ # Example logs for testing <br>
│ ├── sample_log.txt <br>
│ ├── bad_date_log.txt <br>
│ └── empty_log.txt <br>
│ <br>
├── outputs/ # Auto-generated analysis outputs <br>
│ ├── combined_summary.csv <br>
│ └── combined_summary.txt <br>
│ <br>
└── backup/ # Backup and test-related files <br>
├── log_analyzer.py <br>
└── tests/ <br>
└── test_log_analyzer.py <br>

## Getting Started

1. **Install dependencies (if any)**  
   *(No external libraries needed for basic usage.)*

2. **Run the Analyzer**

```bash
python log_analyzer.py

```
This reads from the sample_logs/ directory and writes results to outputs/.

3. **Run unit tests**

```bash
python -m unittest backup/tests/test_log_analyzer.py
```

## Use Cases
- System administrators parsing server logs.
- Developers debugging timestamped output files.
- Automation of recurring diagnostics and reporting.
