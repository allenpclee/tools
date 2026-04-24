# Speed Test Logger User Manual

`sptest.py` is a Python script that runs periodic internet speed tests and logs the download and upload speeds to a CSV file.

## Features
- **Periodic Testing**: Automatically runs speed tests at scheduled intervals.
- **Robust Error Handling**: Automatically retries on network failures with exponential backoff.
- **Continuous Logging**: Appends results immediately to a CSV file to prevent data loss in case of a crash or interruption.
- **Customizable**: Allows configuration of output file, intervals, and test counts via command-line arguments.
- **Graceful Exit**: Can be safely stopped anytime by pressing `Ctrl+C`.

## Prerequisites
- Python 3.x
- `speedtest-cli` library

To install the required library, run:
```bash
pip install speedtest-cli
```

## Usage

By default, running the script with no arguments will perform 96 tests at 15-minute intervals (totaling 24 hours) and log the results to `sptest.csv`.

```bash
python sptest.py
```

### Command-Line Arguments

You can customize the behavior using the following arguments:

- `-o`, `--output`: Specify the output CSV file name. (Default: `sptest.csv`)
- `-i`, `--interval`: Time between each speed test in minutes. (Default: `15`)
- `-c`, `--count`: Total number of tests to run. (Default: `96`)
- `-h`, `--help`: Display the help message.

### Examples

**1. Run tests every 30 minutes for 48 hours:**
```bash
python sptest.py --interval 30 --count 96
```

**2. Save results to a specific file, e.g., `weekend_tests.csv`:**
```bash
python sptest.py --output weekend_tests.csv
```

**3. Run a quick stress test (10 tests, 5 minutes apart):**
```bash
python sptest.py -i 5 -c 10
```

## Output Format

The output is a standard CSV file with the following columns:
- **Timestamp**: Date and time of the test (Format: `YYYY-MM-DD HH:MM:SS`)
- **Download (Mbps)**: Download speed in Megabits per second
- **Upload (Mbps)**: Upload speed in Megabits per second

If a test fails after the maximum number of retries, it will log "N/A" for the speed values.
