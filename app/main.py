import os

from app.service.info_extraction_service import InfoExtractionService
from app.service.ip_details_provider_service import IpDetailsProviderService
from logs_to_analyze import log_base_path


log_file_location = os.path.join(log_base_path, "frontendlog.txt")

with open(log_file_location, 'r') as file:
    log_file_contents = file.read().split("\n")


ip_extraction_service = InfoExtractionService()
ip_details_service = IpDetailsProviderService()

for single_line_log in log_file_contents:
    extracted_ips = ip_extraction_service.get_ip_from_single_line_text(single_line_log)
    for ip_address in extracted_ips:
        ip_details = ip_details_service.get_detail_info(ip_address)
    # print(extracted_ips)
