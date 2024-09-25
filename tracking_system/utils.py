from sqlalchemy.orm import Session

from tracking_system.database import SessionLocal
from tracking_system.db import samples_manager as SamplesManager
from tracking_system.enums import QCStatus, SampleStatus
from tracking_system.schemas import Sample, SampleProcessed


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_samples(db: Session, samples: list[Sample]) -> list[int]:
    sample_uuids = (sample.sample_uuid for sample in samples)
    return SamplesManager.get_samples_uuids(db, sample_uuids)

def get_sample_status(sample: SampleProcessed) -> SampleStatus:
    status = SampleStatus.PROCESSED \
        if sample.qc_1 >= 10.0 and sample.qc_2 >= 5.0 and sample.qc_3.value.lower() == QCStatus.PASS.value.lower() \
        else SampleStatus.FAILED
    return status

def process_sample_statuses(samples):
    result = list()
    for sample in samples:
        result.append({'sample_uuid': sample.sample_uuid, 'status': sample.status.value})
    return result

def process_samples(samples):
    result = [sample.sample_uuid for sample in samples]
    return result

