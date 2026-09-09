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

    # TODO 10: open the file, loop rows, build Patients via
    # Patient.from_csv_row, apply the two rules above.
    raise NotImplementedError

    return patients, errors


def write_clean_json(patients: list[Patient], out_path: Path) -> None:
    """Save the validated records as human-readable JSON (indent=2).

    HINT: out_path.parent.mkdir(exist_ok=True) creates reports/ if
    needed; use p.to_dict() for every patient.
    """
    # TODO 11
    raise NotImplementedError


def write_summary(patients: list[Patient], errors: list[str],
                  out_path: Path) -> dict:
    """Compute the business summary, save it as JSON, and return it.

    The summary dict must contain:
      valid_records          how many clean patients
      rejected_rows          how many error messages
      total_revenue          sum of all fees, rounded to 2 decimals
      revenue_by_department  {department: rounded total}
    """
    # TODO 12
    raise NotImplementedError
