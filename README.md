# MP1 Data Pipeline

This command-line pipeline loads, validates, cleans, and saves tabular CSV data using a YAML configuration. The root `pipeline.py` coordinates the workflow and handles command-line arguments and validation or processing errors. The `src/data_loaders.py` module reads CSV, JSON, and YAML files, including the pipeline configuration. The `src/data_validator.py` module checks required columns, removes rows with invalid numeric values, and converts configured columns to numeric types. The `src/data_processor.py` module applies configured duplicate removal, missing-value handling, and IQR or Z-score outlier removal, then summarizes the cleaning results. The `src/data_output.py` module creates output directories and saves CSV files without an index, while `src/utils.py` provides logging setup and input-path validation. Configuration files live in `config/`, small test files live in `fixtures/`, and generated files in `output/` and the local `venv/` are excluded from Git.

## Setup (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the complete pipeline

```powershell
.\venv\Scripts\python.exe pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

The supplied course fixture contains 100 rows and five columns: `record_id`, `name`, `rating`, `category`, and `status`. The configuration requires all five columns, validates numeric values in `rating`, and removes rating outliers using IQR with a threshold of 1.5. The verified run removes two rows with invalid numeric ratings, two duplicate rows, two rows with missing values, and two outlier rows, saving 92 rows to `output/clean.csv`.

```text
Cleaning report:
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```

The cleaning report starts after numeric validation, so its 98 starting rows exclude the two invalid numeric rows. For another compatible CSV, change the input path and the required, numeric, and outlier column names in the YAML configuration. The earlier fixtures remain available for loader testing, but their different schemas require a matching validation configuration.
