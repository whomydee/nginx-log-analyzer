from unittest import TestCase

from parameterized import parameterized

from app.dto.service.ip_details_dto import IpDetailsDto
from app.service.ip_details_provider_service import IpDetailsProviderService


class TestIpDetailsProviderService(TestCase):
    @parameterized.expand([
        ("103.89.239.47", IpDetailsDto(city="Biñan", country="PH")),
        ("66.240.236.109", IpDetailsDto(city="San Diego (Kearny Mesa)", country="US"))

    ])
    def test__get_detail_info__given_ip_address__return_correct_city_and_country(self, ip_address: str, expected_ip_details: IpDetailsDto):
        ip_details_provider_service = IpDetailsProviderService()
        actual_ip_details = ip_details_provider_service.get_detail_info(ip_address)

        self.assertEqual(actual_ip_details, expected_ip_details)
