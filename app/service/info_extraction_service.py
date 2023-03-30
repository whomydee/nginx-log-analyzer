import re
from typing import List

from loguru import logger


class InfoExtractionService:
    @staticmethod
    def get_ip_from_single_line_text(single_line_text: str) -> List[str]:
        regex_pattern_for_ip = re.compile(r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        ip_addresses = regex_pattern_for_ip.findall(single_line_text)

        logger.debug(f"Found IP: {ip_addresses}")

        return ip_addresses





