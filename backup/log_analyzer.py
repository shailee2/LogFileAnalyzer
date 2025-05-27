import argparse
import re
from collections import Counter
from colorama import Fore, Style

def parse_arguments():
    parser = argparse.ArgumentParser(description='Log File Analyzer')
    parser.add_argument('--file', required=True, help='Path to the log file')
    parser.add_argument('--top-errors', type=int, default=5, help='Show top N frequent error messages')
    return parser.parse_args()

def analyze_log(file_path):
    error_pattern = re.compile(r'error', re.IGNORECASE)
    warning_pattern = re.compile(r'warning', re.IGNORECASE)
    failed_login_pattern = re.compile(r'failed login', re.IGNORECASE)

    error_counter = Counter()
    warning_count = 0
    failed_login_count = 0

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
        for line in log_file:
            if error_pattern.search(line):
                error_counter[line.strip()] += 1
            if warning_pattern.search(line):
                warning_count += 1
            if failed_login_pattern.search(line):
                failed_login_count += 1

    return error_counter, warning_count, failed_login_count

def print_summary(error_counter, warning_count, failed_login_count, top_n):
    print(Fore.YELLOW + f"Warnings Found: {warning_count}" + Style.RESET_ALL)
    print(Fore.RED + f"Failed Logins Found: {failed_login_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"\nTop {top_n} Errors:" + Style.RESET_ALL)
    for i, (error, count) in enumerate(error_counter.most_common(top_n), 1):
        print(f"{i}. {error} — {count} times")

def main():
    args = parse_arguments()
    error_counter, warning_count, failed_login_count = analyze_log(args.file)
    print_summary(error_counter, warning_count, failed_login_count, args.top_errors)

if __name__ == "__main__":
    main()
