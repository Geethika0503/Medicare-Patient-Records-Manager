"""Reading raw CSV data and writing clean outputs (Module 8 skills)."""

import csv
import json
from pathlib import Path

from clinic.models import Patient
from clinic.validators import InvalidRecordError


def load_patients(csv_path: Path) -> tuple[list[Patient], list[str]]:
    """Read the raw CSV and return (clean_patients, error_messages).

    Rules:
    - A bad row must NEVER crash the program: catch InvalidRecordError,
      append "line <n>: <message>" to errors, and continue.
    - Skip duplicate patient_ids (keep the first; log the duplicate).
    HINT: enumerate(csv.DictReader(f), start=2) numbers the data lines
    the way they appear in the file (line 1 is the header).
    """
    patients: list[Patient] = []
    errors: list[str] = []
    seen_ids: set[str] = set()
with csv_path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for line_no, row in enumerate(reader, start=2):
        patient_id = row["patient_id"].strip()

        if patient_id in seen_ids:
            errors.append(f"line {line_no}: duplicate patient_id '{patient_id}'")
            continue

        try:
            patient = Patient.from_csv_row(row)
            patients.append(patient)
            seen_ids.add(patient_id)
        except InvalidRecordError as e:
            errors.append(f"line {line_no}: {e}")

    return patients, errors


def write_clean_json(patients: list[Patient], out_path: Path) -> None:
    """Save the validated records as human-readable JSON (indent=2).

    HINT: out_path.parent.mkdir(exist_ok=True) creates reports/ if
    needed; use p.to_dict() for every patient.
    """

    out_path.parent.mkdir(parents=True, exist_ok=True)

    data = [p.to_dict() for p in patients]

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def write_summary(
    patients: list[Patient],
    errors: list[str],
    out_path: Path
) -> dict:
    """Compute the business summary, save it as JSON, and return it.

    The summary dict must contain:
        valid_records
        rejected_rows
        total_revenue
        revenue_by_department
    """

    revenue_by_department = {}

    for patient in patients:
        department = patient.department
        revenue_by_department[department] = (
            revenue_by_department.get(department, 0)
            + patient.consultation_fee
        )

    summary = {
        "valid_records": len(patients),
        "rejected_rows": len(errors),
        "total_revenue": round(
            sum(p.consultation_fee for p in patients), 2
        ),
        "revenue_by_department": {
            department: round(total, 2)
            for department, total in revenue_by_department.items()
        },
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    return summary
