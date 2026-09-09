"""The Patient class — the OOP heart of the project.

Two OOP ideas to demonstrate (only two, on purpose):
1. ENCAPSULATION — consultation_fee guarded by @property (Module 6).
2. FACTORY CLASSMETHOD — Patient.from_csv_row() builds a validated
   Patient from a messy CSV row (Module 5 + Module 8 together).
"""

from clinic import validators


class Patient:
    """One validated patient visit record."""

    def __init__(self, patient_id: str, name: str, age: int,
                 department: str, consultation_fee: float, visit_date: str):
        # TODO 5: store all six values on self.
        # Assign consultation_fee normally — it must go through the setter.
        raise NotImplementedError

    # ----- encapsulation: a guarded attribute -----
    @property
    def consultation_fee(self) -> float:
        # TODO 6: return the private attribute self._consultation_fee
        raise NotImplementedError

    @consultation_fee.setter
    def consultation_fee(self, value: float):
        # TODO 7: raise ValueError if value < 0, else store it
        # in self._consultation_fee
        raise NotImplementedError

    # ----- factory: build a Patient from one raw CSV row (a dict) -----
    @classmethod
    def from_csv_row(cls, row: dict) -> "Patient":
        """Validate and convert one csv.DictReader row into a Patient.

        Use the validators module for name / age / department / fee;
        .strip() is enough for patient_id and visit_date.
        Let InvalidRecordError bubble up to the caller (storage handles it).
        """
        # TODO 8: return cls(...) with all six cleaned values
        raise NotImplementedError

    def to_dict(self) -> dict:
        """Return a plain dict — the shape JSON and CSV writers need."""
        # TODO 9: six keys matching the CSV header names
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Patient({self.patient_id}, {self.name}, {self.department})"


if __name__ == "__main__":
    # Self-test (Module 7 pattern) — works once TODOs 5-7 are done
    demo = Patient("P999", "Test Person", 30, "General", 500.0, "2026-08-12")
    print("Self-test:", demo)
