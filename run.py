import os
import sys
from typing import Dict

from loguru import logger
from datetime import datetime
import argparse

from app.util.info_extraction_util import InfoExtractionUtil
from app.util.log_filter_util import LogFilterUtil
from logs_to_analyze import log_base_path


logger.remove(0)
logger.add(sys.stderr, level="INFO")


def store_hit_record(ip_wise_hits: Dict, ip_address: str, status_code: int) -> Dict:
    if ip_address in ip_wise_hits:
        if status_code in ip_wise_hits[ip_address]:
            ip_wise_hits[ip_address][status_code] += 1
        else:
            ip_wise_hits[ip_address][status_code] = 1
    else:
        ip_wise_hits[ip_address] = {}
        ip_wise_hits[ip_address][status_code] = 1

    return ip_wise_hits


def get_filtered_ip_wise_hits(ip_wise_hits: Dict[str, Dict[int, int]], min_hit_count) -> Dict[str, Dict[int, int]]:
    filtered_ip_wise_hits = {}

    for ip_address, status_code_wise_hit_count in ip_wise_hits.items():
        total_hit_for_ip = 0
        for status_code, hit_count in status_code_wise_hit_count.items():
            total_hit_for_ip += hit_count

        if total_hit_for_ip >= min_hit_count:
            filtered_ip_wise_hits[ip_address] = status_code_wise_hit_count

    return filtered_ip_wise_hits


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Nginx Access Log Analytics")

    min_start_time = datetime.min.strftime('%d/%b/%Y:%H:%M:%S')
    max_end_time = datetime.max.strftime('%d/%b/%Y:%H:%M:%S')

    parser.add_argument("--start-time", nargs='?', type=str, default=min_start_time,
                        help="--start-time 15/Mar/2023:12:00:00")
    parser.add_argument("--end-time", nargs='?', type=str, default=max_end_time,
                        help="--end-time 15/Mar/2023:17:35:00")
    parser.add_argument("--min-hit-count", nargs='?', type=int, default=1, help="--min-hit-count 5")
    parser.add_argument("--status-code-wise", nargs='?', type=bool, default=False, help="--status-code-wise True")
    parser.add_argument("--timestamp", nargs='?', type=bool, default=False, help="--timestamp True")
    args = parser.parse_args()

    if args.start_time == min_start_time and args.end_time == max_end_time:
        logger.info(f"Fetching Entire Log")
    elif args.start_time == min_start_time:
        logger.info(f"Fetching Logs from the Beginning to {args.end_time}")
    elif args.end_time == max_end_time:
        logger.info(f"Fetching Logs from {args.start_time} to the End of File")
    else:
        logger.info(f"Fetching Logs from {args.start_time} to {args.end_time}")

    log_file_location = os.path.join(log_base_path, "frontendlog.txt")

    with open(log_file_location, 'r') as file:
        log_file_contents = file.read().split("\n")

    filtered_log_file_contents = LogFilterUtil.get_logs_within_timeframe(log_file_contents, args)

    ip_wise_hits = {}
    ip_wise_access_timestamp = {}
    total_hit_count = len(filtered_log_file_contents)

    for single_line_log in filtered_log_file_contents:
        extracted_ip = InfoExtractionUtil.get_ip_from_single_line_text(single_line_log)[0]
        status_code = InfoExtractionUtil.get_status_code_from_single_line_text(single_line_log)

        ip_wise_hits = store_hit_record(ip_wise_hits, extracted_ip, status_code)

        event_timestamp = InfoExtractionUtil.get_timestamp_from_single_line_text(single_line_log)[0]

        if extracted_ip not in ip_wise_access_timestamp:
            ip_wise_access_timestamp[extracted_ip] = [event_timestamp]
        else:
            ip_wise_access_timestamp[extracted_ip].append(event_timestamp)

    ip_wise_hits = {k: dict(sorted(v.items(), key=lambda x: x[1], reverse=True)) for k, v in ip_wise_hits.items()}
    ip_wise_hits = dict(sorted(ip_wise_hits.items(), key=lambda x: sum(x[1].values()), reverse=True))

    filtered_ip_wise_hits = get_filtered_ip_wise_hits(ip_wise_hits, args.min_hit_count)

    print(f"Printing IPs with a Minimum Hit of {args.min_hit_count}")
    for ip_address, status_code_wise_hit_count in filtered_ip_wise_hits.items():
        print("IP: " + "\033[91m" + f"{ip_address}" + "\033[0m")
        total_hit_for_ip = 0

        for status_code, hit_count in status_code_wise_hit_count.items():
            if args.status_code_wise:
                print("Status Code " + "\033[92m" + f"{status_code}: " + "\033[0m" + f"{hit_count} hits")
            total_hit_for_ip += hit_count
        print("Total Hit: " + "\033[92m" + f"{total_hit_for_ip}" + "\033[0m")
        if args.timestamp:
            for timestamp in ip_wise_access_timestamp[ip_address]:
                print(f"Access Timestamp: {timestamp}")
        print("==============================")
    print(f"Total Hits from All IP: {total_hit_count} Hits.")
