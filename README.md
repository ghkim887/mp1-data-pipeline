# MP1 Data Pipeline

This command-line pipeline loads, validates, cleans, and saves tabular CSV data using a YAML configuration. The root `pipeline.py` coordinates the workflow and handles command-line arguments and validation or processing errors. The `src/data_loaders.py` module reads CSV, JSON, and YAML files, including the pipeline configuration. The `src/data_validator.py` module checks required columns, removes rows with invalid numeric values, and converts configured columns to numeric types. The `src/data_processor.py` module applies configured duplicate removal, missing-value handling, and IQR or Z-score outlier removal, then summarizes the cleaning results. The `src/data_output.py` module creates output directories and saves CSV files without an index, while `src/utils.py` provides logging setup and input-path validation. Configuration files live in `config/`, small test files live in `fixtures/`, and generated files in `output/` and the local `venv/` are excluded from Git.

## Setup (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Verified example with the existing fixture

```powershell
.\venv\Scripts\python.exe pipeline.py --input fixtures/sample.csv --output output/clean.csv --config config/config.yaml --verbose
```

The command validates and retains all five rows, saves `output/clean.csv`, and prints:

```text
Cleaning report:
{'rows_before': 5, 'rows_after': 5, 'rows_removed': 0, 'columns_before': 2, 'columns_after': 2, 'columns_removed': 0}
```

## Part 4 course fixture pending

The provided `sample_data.csv` was not available when this branch was prepared. The current configuration targets the existing `sample.csv` (`Student_ID`, `Score`). Before final submission, add the course file at `fixtures/sample_data.csv`, update the configuration using its actual column names, run the command below, and record its observed output here.

```powershell
.\venv\Scripts\python.exe pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```
