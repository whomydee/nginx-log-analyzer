from pydantic.main import BaseModel

from app.dto.util.time_range_dto import TimeRangeDto


class TimeFrameWiseHitDto(BaseModel):
    timeframe: TimeRangeDto
    hit_count: int
