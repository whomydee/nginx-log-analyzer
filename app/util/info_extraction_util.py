import re
from typing import List

from loguru import logger


class InfoExtractionUtil:
    @staticmethod
    def get_ip_from_single_line_text(single_line_text: str) -> List[str]:
        regex_pattern_for_ip = re.compile(r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        ip_addresses = regex_pattern_for_ip.findall(single_line_text)

        logger.debug(f"Found IP: {ip_addresses}")

        return ip_addresses

    @staticmethod
    def get_timestamp_from_single_line_text(single_line_text: str) -> List[str]:
        regex_pattern_for_timestamp = re.compile(r'\[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2})')
        timestamp = regex_pattern_for_timestamp.findall(single_line_text)

        logger.debug(f"Timestamp (UTC): {timestamp}")

        return timestamp




