# Users Guide — Excel File Splitter

## Overview

This tool splits a large Excel file (`.xlsx`) into 40 smaller files of roughly equal size. Each output file preserves the original column headers.

## Prerequisites

- Python 3
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/taimoure67/JKReed.git
   cd JKReed
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This installs `pandas` and `openpyxl`.

## Usage

Run the script with the path to your Excel file:

```bash
python split_excel.py <path_to_excel_file>
```

For example:

```bash
python split_excel.py Taimour_21.xlsx
```

## Output

The script creates an `output/` directory next to your input file containing up to 40 files named sequentially:

```
output/
  part_01.xlsx
  part_02.xlsx
  ...
  part_40.xlsx
```

Each file contains an equal portion of the rows from the original file. If the total number of rows doesn't divide evenly by 40, the last file will contain fewer rows. If there are fewer rows than 40, only as many files as needed are created.

## Configuration

To change the number of output files, edit the `NUM_SPLITS` variable at the top of `split_excel.py`:

```python
NUM_SPLITS = 40  # Change this to your desired number of splits
```

## Example

```
$ python split_excel.py Taimour_21.xlsx
Reading 'Taimour_21.xlsx'...
Total rows: 800
  Created part_01.xlsx (20 rows)
  Created part_02.xlsx (20 rows)
  ...
  Created part_40.xlsx (20 rows)

Done. 40 files saved to 'output/'
```

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| `Error: File 'xyz.xlsx' not found.` | The file path is incorrect or the file doesn't exist | Double-check the file path and ensure the file is in the expected location |
| `Error: The Excel file has no data rows.` | The spreadsheet has headers but no data | Verify the file contains data rows below the header |
| `ModuleNotFoundError: No module named 'pandas'` | Dependencies aren't installed | Run `pip install -r requirements.txt` |
| `Usage: python split_excel.py <path_to_excel_file>` | No file argument was provided | Pass the path to your Excel file as a command-line argument |
