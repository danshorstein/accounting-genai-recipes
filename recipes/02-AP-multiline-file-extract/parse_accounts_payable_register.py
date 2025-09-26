from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List

import pandas as pd
from pypdf import PdfReader

DATE_PATTERN = re.compile(r"^\d{2}/\d{2}/\d{4}$")
AMOUNT_PATTERN = re.compile(r"^-?[\d,]+\.\d{2}$")


def extract_data_lines(pdf_path: Path) -> List[str]:
    lines: List[str] = []
    reader = PdfReader(pdf_path.open("rb"))
    for page in reader.pages:
        page_lines = page.extract_text().splitlines()
        if "PO #" not in page_lines:
            continue
        start_idx = page_lines.index("PO #") + 1
        for raw in page_lines[start_idx:]:
            text = raw.strip()
            if not text:
                continue
            if text.startswith("*** GRAND TOTAL ***"):
                return lines
            lines.append(text)
    return lines


def parse_accounts_payable_register(pdf_path: Path) -> pd.DataFrame:
    lines = extract_data_lines(pdf_path)
    records = []
    i = 0
    total = len(lines)
    while i < total:
        date_filed = lines[i]
        if not DATE_PATTERN.fullmatch(date_filed):
            raise ValueError(f"Unexpected line {date_filed!r} at index {i}")
        i += 1
        if i >= total:
            raise ValueError("Unexpected end of data after date filed")
        apv_number = lines[i]
        i += 1

        pre_amount: List[str] = []
        while i < total and not AMOUNT_PATTERN.fullmatch(lines[i]):
            pre_amount.append(lines[i])
            i += 1
        if not pre_amount:
            raise ValueError(f"Missing payee/appropriation before amount at index {i}")

        payee = pre_amount[0]
        appropriation = " ".join(pre_amount[1:]).strip()

        if i >= total:
            raise ValueError("Unexpected end of data before amount")
        amount_text = lines[i]
        i += 1
        if i >= total:
            raise ValueError("Unexpected end of data before check number")
        check_number = lines[i]
        i += 1

        description_parts: List[str] = []
        while i < total and not DATE_PATTERN.fullmatch(lines[i]):
            description_parts.append(lines[i])
            i += 1
        description = " ".join(description_parts).strip()

        if i >= total:
            raise ValueError("Unexpected end of data before check date")
        check_date = lines[i]
        i += 1
        if i >= total:
            raise ValueError("Unexpected end of data before appropriation code")
        appropriation_code = lines[i]
        i += 1

        trailing: List[str] = []
        while i < total and not DATE_PATTERN.fullmatch(lines[i]):
            trailing.append(lines[i])
            i += 1
        po_number = " ".join(trailing).strip() or None

        records.append(
            {
                "date_filed": date_filed,
                "apv_number": apv_number,
                "payee": payee,
                "appropriation": appropriation,
                "amount": amount_text,
                "check_number": check_number,
                "description": description,
                "check_date": check_date,
                "appropriation_code": appropriation_code,
                "po_number": po_number,
            }
        )

    df = pd.DataFrame(records)
    if not df.empty:
        df["amount"] = df["amount"].str.replace(",", "", regex=False).astype(float)
        df["date_filed"] = pd.to_datetime(df["date_filed"], format="%m/%d/%Y", errors="coerce")
        df["check_date"] = pd.to_datetime(df["check_date"], format="%m/%d/%Y", errors="coerce")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse an AP register PDF into a DataFrame")
    parser.add_argument("pdf", type=Path, help="Path to the accounts payable register PDF")
    parser.add_argument("--csv", type=Path, help="Optional path to write the parsed rows as CSV")
    args = parser.parse_args()

    df = parse_accounts_payable_register(args.pdf)
    print(df.head().T)
    if args.csv:
        df.to_csv(args.csv, index=False)
    print(f'Total amounts were {df["amount"].sum():.2f}')


if __name__ == "__main__":
    main()
