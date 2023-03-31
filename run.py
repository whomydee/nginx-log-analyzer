import os
import sys

from loguru import logger
from datetime import datetime
import argparse

from app.util.info_extraction_util import InfoExtractionUtil
from app.util.log_filter_util import LogFilterUtil
from logs_to_analyze import log_base_path

logger.remove(0)
logger.add(sys.stderr, level="INFO")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Nginx Access Log Analytics")

    min_start_time = datetime.min.strftime('%d/%b/%Y:%H:%M:%S')
    max_end_time = datetime.max.strftime('%d/%b/%Y:%H:%M:%S')

    parser.add_argument("--start-time", nargs='?', type=str, default=min_start_time, help="Start Time in UTC [Format: 15/Mar/2023:12:00:00]")
    parser.add_argument("--end-time", nargs='?', type=str, default=max_end_time, help="End Time in UTC [Format: 15/Mar/2023:17:35:00]")
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

    for single_line_log in filtered_log_file_contents:
        extracted_ips = InfoExtractionUtil.get_ip_from_single_line_text(single_line_log)
        event_timestamp = InfoExtractionUtil.get_timestamp_from_single_line_text(single_line_log)
        print(f"IP: {extracted_ips[0]} - Time: {event_timestamp[0]}")
