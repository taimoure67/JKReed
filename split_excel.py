import sys
import os
import math
import pandas as pd


NUM_SPLITS = 40


def split_excel(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    print(f"Reading '{input_file}'...")
    df = pd.read_excel(input_file, engine="openpyxl")
    total_rows = len(df)
    print(f"Total rows: {total_rows}")

    if total_rows == 0:
        print("Error: The Excel file has no data rows.")
        sys.exit(1)

    chunk_size = math.ceil(total_rows / NUM_SPLITS)
    output_dir = os.path.join(os.path.dirname(input_file) or ".", "output")
    os.makedirs(output_dir, exist_ok=True)

    files_created = 0
    for i in range(NUM_SPLITS):
        start = i * chunk_size
        end = min(start + chunk_size, total_rows)
        if start >= total_rows:
            break
        chunk = df.iloc[start:end]
        filename = f"part_{i + 1:02d}.xlsx"
        filepath = os.path.join(output_dir, filename)
        chunk.to_excel(filepath, index=False, engine="openpyxl")
        files_created += 1
        print(f"  Created {filename} ({len(chunk)} rows)")

    print(f"\nDone. {files_created} files saved to '{output_dir}/'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_excel.py <path_to_excel_file>")
        sys.exit(1)
    split_excel(sys.argv[1])
