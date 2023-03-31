import os

from app.dto.util.time_range_dto import TimeRangeDto
from app.util.info_extraction_util import InfoExtractionUtil
from app.service.ip_details_provider_service import IpDetailsProviderService
from app.util.log_filter_util import LogFilterUtil
from logs_to_analyze import log_base_path


log_file_location = os.path.join(log_base_path, "frontendlog.txt")

with open(log_file_location, 'r') as file:
    log_file_contents = file.read().split("\n")


ip_details_service = IpDetailsProviderService()

for single_line_log in log_file_contents:
    extracted_ips = InfoExtractionUtil.get_ip_from_single_line_text(single_line_log)
    for ip_address in extracted_ips:
        ip_details = ip_details_service.get_detail_info(ip_address)
    event_timestamp = InfoExtractionUtil.get_timestamp_from_single_line_text(single_line_log)
    print(extracted_ips)