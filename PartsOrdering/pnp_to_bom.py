"""
Convert KiCad pick-and-place CSVs in a directory to a consolidated BOM.

Usage:
    python pnp_to_bom.py <csv_dir> [output_csv]

    csv_dir     - directory containing KiCad PnP CSV files
    output_csv  - output path (default: <csv_dir>/ProjectBom.csv)

Groups rows by (Value, Package) across all input files and emits a
Quantity column with the total count.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path


def load_pnp_csvs(csv_dir: Path) -> list[dict]:
    rows = []
    for path in sorted(csv_dir.glob("*.csv")):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    return rows


def build_bom(rows: list[dict]) -> list[dict]:
    counts: dict[tuple, int] = defaultdict(int)
    for row in rows:
        key = (row["Val"].strip(), row["Package"].strip())
        counts[key] += 1

    bom = [
        {"Value": val, "Package": pkg, "Quantity": qty}
        for (val, pkg), qty in sorted(counts.items())
    ]
    return bom


def write_bom(bom: list[dict], output_path: Path) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Value", "Package", "Quantity"])
        writer.writeheader()
        writer.writerows(bom)


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    csv_dir = Path(sys.argv[1])
    if not csv_dir.is_dir():
        print(f"Error: '{csv_dir}' is not a directory")
        sys.exit(1)

    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else csv_dir / "ProjectBom.csv"

    rows = load_pnp_csvs(csv_dir)
    if not rows:
        print(f"No CSV files found in '{csv_dir}'")
        sys.exit(1)

    bom = build_bom(rows)
    write_bom(bom, output_path)

    total_parts = sum(r["Quantity"] for r in bom)
    print(f"Wrote {len(bom)} unique parts ({total_parts} total) to '{output_path}'")


if __name__ == "__main__":
    main()
