# Healthcare Data Governance and Cleaning

**EdVyro Healthcare & Pharmacy Data Analytics — Milestone 2**

## Objective
Create a privacy-aware data dictionary and clean de-identified patient records using reproducible validation rules.

## Requirements covered
- [x] Classify fields and document why the sample is de-identified.
- [x] Validate ranges and types.
- [x] Check missing values.
- [x] Check duplicate patient IDs.
- [x] Apply cleaning rules without inventing clinical values.
- [x] Produce a clean dataset.
- [x] Produce a data dictionary.
- [x] Produce an exception log.
- [x] Include reproducible Python cleaning code.
- [x] Keep source and cleaned datasets separate.

## Project structure

```text
data/
  healthcare_patients_sample_SYNTHETIC.csv
  healthcare_patients_cleaned.csv
documentation/
  data_dictionary.md
  data_validation_report.md
  exception_log.csv
scripts/
  clean_healthcare_data.py
notebook/
  analysis_notes.md
evidence/
  submission_checklist.md
```

## Key result
Input records: **35**  
Cleaned records: **34**  
Duplicate patient IDs detected: **1**  
Exceptions logged: **8**

## Privacy and governance
The project uses fictional/de-identified training data. No real patient identifiers are intentionally included. Invalid or missing clinical information is not guessed or filled with invented medical values.

## Reproducibility
Run:

```bash
python scripts/clean_healthcare_data.py
```

The script creates/updates:
- `data/healthcare_patients_cleaned.csv`
- `documentation/exception_log.csv`

## Source-data note
The official EdVyro raw CSV could not be retrieved into this workspace because its endpoint is served as a raw CSV and is not accessible through the current file environment. The included source is therefore explicitly labelled **SYNTHETIC**.

**Before final EdVyro submission, replace `healthcare_patients_sample_SYNTHETIC.csv` with the official EdVyro `healthcare_patients_sample.csv`, rename it accordingly, run the script, and commit the resulting outputs.**

This note is intentional: the project should not falsely claim that a generated dataset is EdVyro's supplied dataset.
