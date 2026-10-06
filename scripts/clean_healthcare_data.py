"""
Reproducible healthcare data cleaning script.
Usage:
    python scripts/clean_healthcare_data.py

The script reads data/healthcare_patients_sample.csv if present.
For the included training package, the synthetic source file is used.
It never invents clinical values.
"""
from pathlib import Path
import csv
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SOURCE = DATA / "healthcare_patients_sample.csv"
if not SOURCE.exists():
    SOURCE = DATA / "healthcare_patients_sample_SYNTHETIC.csv"
OUTPUT = DATA / "healthcare_patients_cleaned.csv"
LOG = ROOT / "documentation" / "exception_log.csv"

HEADERS = ["patient_id","age","sex","diagnosis","blood_pressure","record_date","status"]
VALID_SEX = {"Male","Female","Unknown"}
VALID_STATUS = {"Active","Stable","Inactive"}
VALID_DIAGNOSES = {"Hypertension","Diabetes","Asthma","Arthritis","Migraine","Anemia"}

with SOURCE.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

cleaned, exceptions, seen = [], [], set()

for source_row, r in enumerate(rows, start=2):
    pid = r.get("patient_id", "")
    if pid in seen:
        exceptions.append([source_row,pid,"duplicate_patient_id",
                           "Duplicate patient ID; subsequent row excluded.",
                           "No clinical value invented."])
        continue
    seen.add(pid)

    age = r.get("age","")
    if age:
        try:
            a = int(age)
            if not 0 <= a <= 120:
                exceptions.append([source_row,pid,"invalid_age_range",
                                   f"Age {age} outside 0–120.","Set to NA."])
                age = ""
        except ValueError:
            exceptions.append([source_row,pid,"invalid_age_type",
                               f"Age '{age}' is not an integer.","Set to NA."])

    sex = r.get("sex","")
    if sex not in VALID_SEX:
        if sex:
            exceptions.append([source_row,pid,"invalid_sex_category",
                               f"Unexpected sex '{sex}'.","Set to NA."])
        sex = ""

    diagnosis = r.get("diagnosis","")
    if diagnosis and diagnosis not in VALID_DIAGNOSES:
        exceptions.append([source_row,pid,"unexpected_diagnosis",
                           f"Unexpected diagnosis '{diagnosis}'.","Set to NA."])

    bp = r.get("blood_pressure","")
    if bp:
        try:
            s, d = map(int, bp.split("/"))
            if not (60 <= s <= 250 and 30 <= d <= 150):
                raise ValueError
        except ValueError:
            exceptions.append([source_row,pid,"invalid_blood_pressure",
                               f"Invalid BP '{bp}'.","Set to NA."])
            bp = ""

    date = r.get("record_date","")
    if date:
        try:
            datetime.strptime(date,"%Y-%m-%d")
        except ValueError:
            exceptions.append([source_row,pid,"invalid_record_date",
                               f"Invalid date '{date}'.","Set to NA."])
            date = ""

    status = r.get("status","")
    if status not in VALID_STATUS:
        if status:
            exceptions.append([source_row,pid,"invalid_status",
                               f"Unexpected status '{status}'.","Set to NA."])
        status = ""

    cleaned.append([pid,age,sex,diagnosis,bp,date,status])

with OUTPUT.open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(HEADERS); w.writerows(cleaned)

with LOG.open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["source_row","patient_id","exception_type","observation","cleaning_action"])
    w.writerows(exceptions)

print(f"Input: {SOURCE}")
print(f"Output: {OUTPUT}")
print(f"Rows in: {len(rows)} | Rows out: {len(cleaned)}")
print(f"Exceptions logged: {len(exceptions)}")
