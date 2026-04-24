import speedtest
import time
import csv
import random
import argparse
import sys
from datetime import datetime

def run_speed_test(max_retries=5, delay=60):
    for attempt in range(max_retries):
        try:
            st = speedtest.Speedtest()
            print("Running download test...")
            download_speed = st.download() / 1_000_000
            print("Running upload test...")
            upload_speed = st.upload() / 1_000_000

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return current_time, download_speed, upload_speed
        except Exception as e:
            print(f"Error occurred: {e}")
            if attempt < max_retries - 1:
                wait_time = delay * (2 ** attempt) + random.uniform(0, 10)
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached. Skipping this test.")
                return datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None, None

def main():
    parser = argparse.ArgumentParser(description="A script to run periodic internet speed tests and log them to a CSV file.")
    parser.add_argument("-o", "--output", default="sptest.csv", help="Output CSV file name (default: sptest.csv)")
    parser.add_argument("-i", "--interval", type=int, default=15, help="Interval between tests in minutes (default: 15)")
    parser.add_argument("-c", "--count", type=int, default=96, help="Number of tests to run (default: 96, which is 24 hours at 15 min interval)")
    
    args = parser.parse_args()
    
    output_file = args.output
    interval_seconds = args.interval * 60
    total_tests = args.count

    # Initialize CSV with headers if it doesn't exist
    try:
        with open(output_file, "a", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                csv_writer.writerow(["Timestamp", "Download (Mbps)", "Upload (Mbps)"])
    except IOError as e:
        print(f"Failed to access output file {output_file}: {e}")
        sys.exit(1)

    print(f"Starting speed test. Logging to {output_file}.")
    print(f"Running {total_tests} tests at {args.interval}-minute intervals.")
    print("Press Ctrl+C to stop.")

    try:
        for i in range(total_tests):
            time_str, download, upload = run_speed_test()
            
            with open(output_file, "a", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                if download is not None and upload is not None:
                    csv_writer.writerow([time_str, f"{download:.2f}", f"{upload:.2f}"])
                    print(f"Test {i+1}/{total_tests} completed: {time_str}, Down: {download:.2f} Mbps, Up: {upload:.2f} Mbps")
                else:
                    csv_writer.writerow([time_str, "N/A", "N/A"])
                    print(f"Test {i+1}/{total_tests} failed: {time_str}")

            if i < total_tests - 1:
                print(f"Waiting for {args.interval} minutes...")
                time.sleep(interval_seconds)
                
    except KeyboardInterrupt:
        print("\nSpeed test interrupted by user. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
    