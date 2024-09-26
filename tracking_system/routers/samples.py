from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from tracking_system.db import samples_manager as SamplesManager
from tracking_system.enums import SampleStatus
from tracking_system.schemas import SampleToMake, SampleToShip, SampleProcessed, SamplesShipped
from tracking_system.utils import get_db

router = APIRouter(prefix='/sample', tags=['sample'])


@router.get('')
def get_samples(status: str, db: Session = Depends(get_db)):
    if status.lower() == SampleStatus.ORDERED.value.lower():
        db_samples = SamplesManager.get_samples(db, SampleStatus.ORDERED)
        samples_to_make = [SampleToMake(sample_uuid=db_sample.sample_uuid, sequence=db_sample.sequence) for db_sample in
                           db_samples]
        return {'samples_to_make': samples_to_make if len(samples_to_make)<=96 else samples_to_make[:96]}
    elif status.lower() == SampleStatus.PROCESSED.value.lower():
        db_samples = SamplesManager.get_samples(db, SampleStatus.PROCESSED  )
        samples_to_ship = [SampleToShip(sample_uuid=db_sample.sample_uuid, plate_id=db_sample.plate_id,
                                        well=db_sample.well)
                           for db_sample in db_samples]
        return {'samples_to_ship': samples_to_ship}


@router.put('/update/processed')
def update_processed_orders(samples_made: Annotated[list[SampleProcessed], Body(embed=True)], db: Session = Depends(get_db)):
    for sample in samples_made:
        SamplesManager.update_processed_sample(db, sample)
    return {'message: Success'}


@router.put('/update/shipped')
def update_shipped_orders(samples: SamplesShipped, db: Session = Depends(get_db)):
    for sample in samples.samples_shipped:
        SamplesManager.update_shipped_sample(db, sample)
    return {'message: Success'}