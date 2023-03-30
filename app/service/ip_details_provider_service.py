from typing import List
from loguru import logger

from ip2geotools.databases.noncommercial import DbIpCity

from app.dto.service.ip_details_dto import IpDetailsDto


class IpDetailsProviderService:
    @staticmethod
    def get_detail_info(ip_address: str) -> IpDetailsDto:

        response = DbIpCity.get(ip_address, api_key='free')

        ip_details = IpDetailsDto(city=response.city, country=response.country)
        logger.debug(f"City: {ip_details.city} - Country: {ip_details.country}")

        return ip_details
