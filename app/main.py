import os

from app.service.ip_extraction_service import IpExtractionService
from logs_to_analyze import log_base_path


log_file_location = os.path.join(log_base_path, "frontendlog.txt")

with open(log_file_location, 'r') as file:
    log_file_contents = file.read().split("\n")


ip_extraction_service = IpExtractionService()

for single_line_log in log_file_contents:
    extracted_ips = ip_extraction_service.get_ip_from_single_line_text(single_line_log)
    print(extracted_ips)
