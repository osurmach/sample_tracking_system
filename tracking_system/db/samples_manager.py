from sqlalchemy.orm import Session

from tracking_system.enums import SampleStatus
from tracking_system.models import Sample
from tracking_system.schemas import SampleCreate, SampleProcessed
from tracking_system.utils import update_sample_status


def get_samples_uuids(db: Session, sample_uuids: list[int]) -> list[str]:
    return db.query(Sample).with_entities(Sample.sample_uuid).filter(Sample.sample_uuid.in_(sample_uuids)).all()


def get_samples(db: Session, status: SampleStatus) -> list[Sample]:
    return db.query(Sample).filter(Sample.status == status).all()


def create_sample(db: Session, sample: SampleCreate, order_id: int):
    db_sample = Sample(sample_uuid=sample.sample_uuid, sequence=sample.sequence, order_id=order_id)
    db.add(db_sample)
    db.commit()


def update_processed_sample(db: Session, sample: SampleProcessed):
    sample_status = update_sample_status(sample)
    db.query(Sample).filter(Sample.sample_uuid == sample.sample_uuid).update({
        'plate_id': sample.plate_id,
        'well': sample.well,
        'qc_1': sample.qc_1,
        'qc_2': sample.qc_2,
        'qc_3': sample.qc_3,
        'status': sample_status
    })
    db.commit()


def update_shipped_sample(db: Session, sample_uuid: str):
    db.query(Sample).filter(Sample.sample_uuid == sample_uuid).update({
        'status': SampleStatus.SHIPPED
    })
    db.commit()


def get_sample_status(db: Session, order_id: int):
    return db.query(Sample).with_entities(Sample.sample_uuid, Sample.status).filter(Sample.order_id == order_id).all()
