import argparse
import re
import csv
from datetime import datetime
from collections import Counter
from colorama import Fore, Style

def parse_arguments():
    parser = argparse.ArgumentParser(description='Log File Analyzer')
    parser.add_argument('--files', nargs='+', required=True, help='List of log files to analyze')
    parser.add_argument('--top-errors', type=int, default=5, help='Show top N frequent error messages')
    parser.add_argument('--since', help='Filter logs since date (YYYY-MM-DD)')
    parser.add_argument('--output', default='summary_report.txt', help='Output summary file (txt or csv)')
    return parser.parse_args()

def analyze_log(file_path, since_date=None):
    error_pattern = re.compile(r'error', re.IGNORECASE)
    warning_pattern = re.compile(r'warning', re.IGNORECASE)
    failed_login_pattern = re.compile(r'failed login', re.IGNORECASE)

    error_counter = Counter()
    warning_count = 0
    failed_login_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
            lines = log_file.readlines()
            if not lines:
                print(f"⚠️ Warning: {file_path} is empty, skipping.")
                return error_counter, warning_count, failed_login_count

            for line in lines:
                if since_date:
                    parts = line.split()
                    if parts:
                        try:
                            log_date = datetime.strptime(parts[0], '%Y-%m-%d')
                            if log_date < since_date:
                                continue
                        except ValueError:
                            print(f"⚠️ Skipping line with malformed date: {line.strip()}")
                            continue

                if error_pattern.search(line):
                    error_counter[line.strip()] += 1
                if warning_pattern.search(line):
                    warning_count += 1
                if failed_login_pattern.search(line):
                    failed_login_count += 1

    except FileNotFoundError:
        print(f"❌ Error: File not found — {file_path}")
    except Exception as e:
        print(f"❌ Error reading file {file_path}: {e}")

    return error_counter, warning_count, failed_login_count

def print_summary(error_counter, warning_count, failed_login_count, top_n):
    print(Fore.YELLOW + f"Warnings Found: {warning_count}" + Style.RESET_ALL)
    print(Fore.RED + f"Failed Logins Found: {failed_login_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"\nTop {top_n} Errors:" + Style.RESET_ALL)
    for i, (error, count) in enumerate(error_counter.most_common(top_n), 1):
        print(f"{i}. {error} — {count} times")

def export_summary_to_txt(error_counter, warning_count, failed_login_count, top_n, output_file):
    with open(output_file, 'w') as f:
        f.write(f"Warnings Found: {warning_count}\n")
        f.write(f"Failed Logins Found: {failed_login_count}\n\n")
        f.write(f"Top {top_n} Errors:\n")
        for i, (error, count) in enumerate(error_counter.most_common(top_n), 1):
            f.write(f"{i}. {error} — {count} times\n")
    print(f"\nSummary exported to {output_file}")

def export_summary_to_csv(error_counter, top_n, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Rank', 'Error Message', 'Count'])
        for i, (error, count) in enumerate(error_counter.most_common(top_n), 1):
            writer.writerow([i, error, count])
    print(f"\nSummary exported to {output_file}")

def main():
    args = parse_arguments()
    since_date = datetime.strptime(args.since, '%Y-%m-%d') if args.since else None

    combined_error_counter = Counter()
    total_warning_count = 0
    total_failed_login_count = 0

    for file_path in args.files:
        print(f"Analyzing {file_path}...")
        error_counter, warning_count, failed_login_count = analyze_log(file_path, since_date)
        combined_error_counter.update(error_counter)
        total_warning_count += warning_count
        total_failed_login_count += failed_login_count

    print_summary(combined_error_counter, total_warning_count, total_failed_login_count, args.top_errors)

    if args.output.endswith('.csv'):
        export_summary_to_csv(combined_error_counter, args.top_errors, args.output)
    else:
        export_summary_to_txt(combined_error_counter, total_warning_count, total_failed_login_count, args.top_errors, args.output)

if __name__ == "__main__":
    main()