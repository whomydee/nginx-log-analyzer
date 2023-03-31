from pydantic import BaseModel


class TimeRangeDto(BaseModel):
    start_time: str
    end_time: str
