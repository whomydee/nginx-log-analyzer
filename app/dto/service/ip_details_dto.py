from pydantic import BaseModel


class IpDetailsDto(BaseModel):
    city: str
    country: str
