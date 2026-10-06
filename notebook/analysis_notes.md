# Analysis Notebook Notes

## 1. Load and inspect
The dataset was loaded as a tabular CSV and profiled before any transformation.

## 2. Quality checks
- Row count: 35
- Column count: 7
- Duplicate IDs: 1
- Exceptions: 8
- Missing values were profiled column-by-column.

## 3. Validation philosophy
Healthcare data cleaning must separate:
- **Missing**: no value is available.
- **Impossible/invalid**: a value violates the validation rule.
- **Duplicate**: an identifier repeats when uniqueness is expected.

No missing or invalid clinical values were replaced with guessed values.

## 4. Cleaning outcome
The cleaned dataset contains 34 unique patient IDs. Subsequent duplicate records were excluded; invalid/missing fields were set to missing and recorded in the exception log.

## 5. Interpretation
The output is suitable for demonstrating data-quality workflow and governance. It is not suitable for clinical decision-making.
