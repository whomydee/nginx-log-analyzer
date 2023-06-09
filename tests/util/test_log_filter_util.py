from typing import List
from unittest import TestCase

from parameterized import parameterized

from app.dto.util.time_range_dto import TimeRangeDto
from app.util.log_filter_util import LogFilterUtil


class TestLogFilterUtil(TestCase):
    log_to_test = [
        '202.74.246.195 - - [06/Mar/2023:06:57:23 +0000] "GET /logo192.png HTTP/1.1" 200 5347 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:57:24 +0000] "GET /logo512.png HTTP/1.1" 200 9664 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:57:27 +0000] "GET /static/js/2.1a21d93d.chunk.js.map HTTP/1.1" 200 5942822 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:26 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/css/2.f33e5aa3.chunk.css HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/css/main.b1efeaa0.chunk.css HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/js/2.1a21d93d.chunk.js HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/js/main.042ebd2a.chunk.js HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:28 +0000] "GET /static/media/spinner.4a75f64d.gif HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:28 +0000] "GET /avc-backend/patients?count=50 HTTP/1.1" 502 497 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:30 +0000] "GET /static/css/main.b1efeaa0.chunk.css.map HTTP/1.1" 200 60011 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:31 +0000] "GET /static/js/main.042ebd2a.chunk.js.map HTTP/1.1" 200 318527 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:32 +0000] "GET /static/css/2.f33e5aa3.chunk.css.map HTTP/1.1" 200 743332 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:34 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:35 +0000] "GET /static/css/main.b1efeaa0.chunk.css.map HTTP/1.1" 200 60011 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:35 +0000] "GET /static/css/2.f33e5aa3.chunk.css.map HTTP/1.1" 200 743332 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:36 +0000] "GET /avc-backend/patients?count=50 HTTP/1.1" 502 497 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:37 +0000] "GET /static/js/main.042ebd2a.chunk.js.map HTTP/1.1" 200 318527 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:38 +0000] "GET /static/js/2.1a21d93d.chunk.js.map HTTP/1.1" 200 5942822 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:41 +0000] "GET /static/js/2.1a21d93d.chunk.js.map HTTP/1.1" 200 5942822 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '198.199.116.50 - - [06/Mar/2023:07:03:31 +0000] "GET /owa/auth/logon.aspx?url=https%3a%2f%2f1%2fecp%2f HTTP/1.1" 200 2333 "-" "Mozilla/5.0 zgrab/0.x" "-"',
        '202.74.246.195 - - [06/Mar/2023:07:15:01 +0000] "GET /something/1698 HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:07:15:01 +0000] "GET /static/css/main.b1efeaa0.chunk.css HTTP/1.1" 304 0 "https://something.something.something/something/1234" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:07:15:01 +0000] "GET /static/js/2.1a21d93d.chunk.js HTTP/1.1" 304 0 "https://something.something.something/something/1234" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:07:15:02 +0000] "GET /static/js/main.042ebd2a.chunk.js HTTP/1.1" 304 0 "https://something.something.something/something/1234" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
    ]
    expected_logs_after_filter = [
        '202.74.246.195 - - [06/Mar/2023:06:58:26 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/css/2.f33e5aa3.chunk.css HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/css/main.b1efeaa0.chunk.css HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/js/2.1a21d93d.chunk.js HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:27 +0000] "GET /static/js/main.042ebd2a.chunk.js HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:28 +0000] "GET /static/media/spinner.4a75f64d.gif HTTP/1.1" 304 0 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:28 +0000] "GET /avc-backend/patients?count=50 HTTP/1.1" 502 497 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:30 +0000] "GET /static/css/main.b1efeaa0.chunk.css.map HTTP/1.1" 200 60011 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:31 +0000] "GET /static/js/main.042ebd2a.chunk.js.map HTTP/1.1" 200 318527 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:32 +0000] "GET /static/css/2.f33e5aa3.chunk.css.map HTTP/1.1" 200 743332 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:34 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:35 +0000] "GET /static/css/main.b1efeaa0.chunk.css.map HTTP/1.1" 200 60011 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:35 +0000] "GET /static/css/2.f33e5aa3.chunk.css.map HTTP/1.1" 200 743332 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:36 +0000] "GET /avc-backend/patients?count=50 HTTP/1.1" 502 497 "https://raf-optimizer-demo.infolytx.net/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:37 +0000] "GET /static/js/main.042ebd2a.chunk.js.map HTTP/1.1" 200 318527 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:38 +0000] "GET /static/js/2.1a21d93d.chunk.js.map HTTP/1.1" 200 5942822 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '202.74.246.195 - - [06/Mar/2023:06:58:41 +0000] "GET /static/js/2.1a21d93d.chunk.js.map HTTP/1.1" 200 5942822 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"',
        '198.199.116.50 - - [06/Mar/2023:07:03:31 +0000] "GET /owa/auth/logon.aspx?url=https%3a%2f%2f1%2fecp%2f HTTP/1.1" 200 2333 "-" "Mozilla/5.0 zgrab/0.x" "-"',
    ]

    @parameterized.expand(
        [
            (
                log_to_test,
                TimeRangeDto(
                    start_time="06/Mar/2023:06:58:00", end_time="06/Mar/2023:07:15:00"
                ),
            )
        ]
    )
    def test__get_logs_within_timeframe__given_log__return_logs_within_timeframe(
        self, logs: List[str], time_range: TimeRangeDto
    ):
        actual_logs_after_filter = LogFilterUtil.get_logs_within_timeframe(
            logs, time_range
        )

        self.assertEqual(actual_logs_after_filter, self.expected_logs_after_filter)
        self.assertNotEqual(len(self.log_to_test), len(actual_logs_after_filter))
