from pydantic import BaseModel

from tracking_system.enums import QCStatus, SampleStatus


class SampleBase(BaseModel):
    sample_uuid: str

class SampleCreate(SampleBase):
    sequence: str

class SampleToMake(SampleBase):
    sequence: str

class SampleToShip(SampleBase):
    plate_id: int
    well: str

class SampleProcessed(SampleBase):
    plate_id: int
    well: str
    qc_1: float
    qc_2: float
    qc_3: QCStatus

class SampleShipped(SampleBase):
    pass

class SampleState(SampleBase):
    status: SampleStatus

class Sample(SampleCreate):
    plate_id: int
    well: str
    qc_1: float
    qc_2: float
    qc_3: QCStatus
    status: SampleStatus

class SampleUUIDs(BaseModel):
    repeat_sample_uuids: list[str]

class OrderBase(BaseModel):
    order_uuid: str

class OrderState(BaseModel):
    sample_statuses: list[SampleState]

class Order(OrderBase):
    samples: list[Sample] = []

    class Config:
        orm_mode = True


