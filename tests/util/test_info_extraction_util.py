from unittest import TestCase

from parameterized import parameterized

from app.util.info_extraction_util import InfoExtractionUtil


class TestInfoExtractionUtil(TestCase):
    @parameterized.expand(
        [
            (
                '202.74.246.195 - - [06/Mar/2023:06:55:50 +0000] "GET /something/something HTTP/1.1" 502 497 "https://something.something.something/'
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                "-",
                ["202.74.246.195"],
            ),
            (
                '52.224.243.156 - - [06/Mar/2023:12:57:35 +0000] "GET /enviroments/.env.production HTTP/1.1" 301 169 "-'
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
                "-",
                ["52.224.243.156"],
            ),
        ]
    )
    def test__get_ip_from_single_line_text__given_single_line_log__extract_correct_ips(
        self, single_line_text, expected_extracted_ips
    ):
        actual_extracted_ips = InfoExtractionUtil.get_ip_from_single_line_text(
            single_line_text
        )

        self.assertEqual(actual_extracted_ips, expected_extracted_ips)

    @parameterized.expand(
        [
            (
                '202.74.246.195 - - [06/Mar/2023:06:55:50 +0000] "GET /something/something HTTP/1.1" 502 497 "https://something.something.something/'
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                "-",
                ["06/Mar/2023:06:55:50"],
            ),
            (
                '52.224.243.156 - - [06/Mar/2023:12:57:35 +0000] "GET /enviroments/.env.production HTTP/1.1" 301 169 "-'
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
                "-",
                ["06/Mar/2023:12:57:35"],
            ),
        ]
    )
    def test__get_timestamp_from_single_line_text__given_single_line_log__extract_correct_timestamp(
        self, single_line_text, expected_extracted_ips
    ):
        actual_extracted_ips = InfoExtractionUtil.get_timestamp_from_single_line_text(
            single_line_text
        )

        self.assertEqual(actual_extracted_ips, expected_extracted_ips)
