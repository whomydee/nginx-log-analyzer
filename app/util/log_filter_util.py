from datetime import datetime
from typing import List

from app.dto.util.time_range_dto import TimeRangeDto
from app.util.info_extraction_util import InfoExtractionUtil


class LogFilterUtil:
    @staticmethod
    def get_date_time_in_comparable_format(
        date_time_as_string: str, format: str = "%d/%b/%Y:%H:%M:%S"
    ):
        return datetime.strptime(date_time_as_string, format)

    @staticmethod
    def get_logs_within_timeframe(logs_to_filter: List[str], time_range: TimeRangeDto):
        logs_within_timeframe = []

        start_time = LogFilterUtil.get_date_time_in_comparable_format(
            time_range.start_time
        )
        end_time = LogFilterUtil.get_date_time_in_comparable_format(time_range.end_time)

        for single_line_log in logs_to_filter:
            time_stamp = InfoExtractionUtil.get_timestamp_from_single_line_text(
                single_line_log
            )
            if time_stamp:
                time_stamp_as_string = (
                    InfoExtractionUtil.get_timestamp_from_single_line_text(
                        single_line_log
                    )[0]
                )
                time_stamp = LogFilterUtil.get_date_time_in_comparable_format(
                    time_stamp_as_string
                )

                if start_time <= time_stamp <= end_time:
                    logs_within_timeframe.append(single_line_log)

        return logs_within_timeframe
