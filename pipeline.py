"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input fixtures/sample_data.csv --config config/config.yaml --output output/clean.csv
"""

import argparse
import logging
import sys
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)


logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Data processing pipeline")
    parser.add_argument("--input", "-i", required=True, help="Path to the input file")
    parser.add_argument("--config", required=True, help="Path to a YAML configuration file")
    parser.add_argument("--output", "-o", required=True, help="Path to the output file")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    return parser.parse_args()


def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(
        f"Arguments parsed: input={args.input}, config={args.config}, output={args.output}"
    )
    if not validate_input(args.input):
        sys.exit(1)
    if not validate_input(args.config):
        sys.exit(1)
    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)
    try:
        validation = config["validation"]
        required_columns = validation["required_columns"]
        numeric_columns = validation["numeric_columns"]
    except (KeyError, TypeError):
        logger.error("Configuration must provide validation.required_columns and validation.numeric_columns")
        sys.exit(1)
    before_validation = len(data)
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)
    logger.info(f"Validation complete: {before_validation} → {len(data)} rows")
    original = data.copy()
    try:
        cleaned = process_data(data, config)
    except ValueError:
        sys.exit(1)
    report = create_cleaning_report(original, cleaned)
    logger.info(f"Processing complete: {len(original)} → {len(cleaned)} rows")
    output_path = save_data(cleaned, args.output)
    logger.info(f"Saved cleaned data to {output_path}")
    print("Cleaning report:")
    print(report)


if __name__ == "__main__":
    main()
