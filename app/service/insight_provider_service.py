import datetime

from typing import List

from app.dto.service.timeframe_wise_hit_dto import TimeFrameWiseHitDto
from app.dto.util.time_range_dto import TimeRangeDto
from app.util.info_extraction_util import InfoExtractionUtil
from app.util.log_filter_util import LogFilterUtil


class InsightProviderService:
    def get_timeframes_by_hit_count(self, logs: List[str], time_interval_in_minutes: int, top_k: int = 3) -> \
    List[TimeFrameWiseHitDto]:

        count_of_hits = 0
        timeframe_wise_hit = []

        for single_line_log in logs:

            if not count_of_hits:
                interval_start_time = LogFilterUtil.get_date_time_in_comparable_format(
                    InfoExtractionUtil.get_timestamp_from_single_line_text(single_line_log)[0]
                )

                interval_end_time = interval_start_time + datetime.timedelta(minutes=time_interval_in_minutes)

            event_timestamp = LogFilterUtil.get_date_time_in_comparable_format(
                InfoExtractionUtil.get_timestamp_from_single_line_text(single_line_log)[0]
            )
            if interval_start_time <= event_timestamp <= interval_end_time:
                count_of_hits += 1
            else:
                timeframe = TimeRangeDto(start_time=interval_start_time.strftime('%d/%b/%Y:%H:%M:%S'),
                                         end_time=interval_end_time.strftime('%d/%b/%Y:%H:%M:%S'))
                timeframe_wise_hit.append(TimeFrameWiseHitDto(timeframe=timeframe, hit_count=count_of_hits))

                interval_start_time = interval_end_time
                interval_end_time = interval_start_time + datetime.timedelta(minutes=time_interval_in_minutes)

                count_of_hits = 1

        timeframe_wise_hit = sorted(timeframe_wise_hit, key= lambda x: x.hit_count, reverse=True)

        return timeframe_wise_hit[0: top_k]
