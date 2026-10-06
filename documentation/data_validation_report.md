# Data Validation & Cleaning Report

## 1. Scope
This report documents reproducible validation checks for the supplied educational dataset used in this project.

> **Important source note:** The included CSV is a synthetic training substitute because the EdVyro-hosted raw CSV could not be retrieved in this workspace. Replace it with the official EdVyro `healthcare_patients_sample.csv` before final submission if your EdVyro dashboard requires the exact supplied file.

## 2. Dataset profile
- Input rows: **35**
- Cleaned rows: **34**
- Input columns: **7**
- Duplicate patient IDs detected: **1**
- Logged exceptions: **8**

## 3. Validation checks

| Check | Result | Action |
|---|---|---|
| Field types | Checked | Invalid values converted to missing and logged |
| Age range | Checked against 0–120 | Invalid age set to NA |
| Blood pressure format/range | Checked | Invalid readings set to NA |
| Date format | Checked as YYYY-MM-DD | Invalid date set to NA |
| Missing values | Profiled before/after | No clinical values invented |
| Duplicate patient IDs | Checked | Subsequent duplicate record excluded |
| Category values | Checked | Unexpected categories set to NA |
| Clinical value invention | Prohibited | No diagnosis/measurement/date guessed |

## 4. Missing-value profile

### Before cleaning
- patient_id: 0
- age: 1
- sex: 0
- diagnosis: 1
- blood_pressure: 0
- record_date: 1
- status: 0

### After cleaning
- patient_id: 0
- age: 2
- sex: 1
- diagnosis: 1
- blood_pressure: 1
- record_date: 2
- status: 0

## 5. Cleaning methodology
1. Read the source CSV without modifying the raw copy.
2. Validate identifiers and detect duplicate patient IDs.
3. Validate numeric age range.
4. Validate allowed categorical values.
5. Validate blood-pressure structure and numeric bounds.
6. Validate record dates.
7. Convert invalid/missing values to NA/blank and log the exception.
8. Exclude only the subsequent duplicate patient record.
9. Save the cleaned dataset separately.
10. Keep an exception log so every transformation is auditable.

## 6. Data-quality interpretation
The cleaning process intentionally does **not** infer missing diagnoses, ages, dates, or measurements. This avoids introducing false clinical information.

## 7. Limitations
- This is fictional/de-identified educational data.
- Validation thresholds are quality-control rules for this exercise, not clinical decision rules.
- The results must not be used for patient diagnosis or treatment.
