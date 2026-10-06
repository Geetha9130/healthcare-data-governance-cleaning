# Data Dictionary — Healthcare Patient Records

## Dataset purpose
Educational healthcare data-governance exercise using fictional/de-identified patient records.

## Privacy classification

| Field | Type | Classification | Description | Validation |
|---|---|---|---|---|
| patient_id | String | Indirect/controlled identifier | Synthetic record identifier used to detect duplicate records. | Required, unique in cleaned data |
| age | Integer | Sensitive demographic | Patient age in years. | 0–120; invalid/missing values are not imputed |
| sex | Categorical | Sensitive demographic | Recorded sex category in the educational sample. | Male/Female/Unknown |
| diagnosis | Categorical | Clinical/sensitive | Synthetic diagnosis label. | Must match supplied validation vocabulary |
| blood_pressure | String | Clinical/sensitive | Synthetic blood-pressure reading in systolic/diastolic form. | Numeric components; reasonable validation range |
| record_date | Date | Temporal | Date associated with the synthetic record. | YYYY-MM-DD |
| status | Categorical | Operational/clinical context | Record status. | Active/Stable/Inactive |

## Why the sample is treated as de-identified

- No real patient names are present.
- No phone numbers, email addresses, home addresses, Aadhaar numbers, insurance numbers, or medical record numbers are included.
- `patient_id` values are synthetic study identifiers rather than direct identity attributes.
- The dataset is explicitly used as fictional/de-identified training data.
- The project does not attempt to re-identify any person.

## Governance principle

Cleaning must improve structural quality without creating unsupported clinical facts. Missing or impossible clinical values are therefore retained as missing/NA after being logged, rather than being guessed or statistically invented.
