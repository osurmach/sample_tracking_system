from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from typing import Annotated
from sqlalchemy.orm import Session

from tracking_system.db import orders_manager as OrdersManager
from tracking_system.db import samples_manager as SamplesManager
from tracking_system.schemas import OrderBase, SampleCreate
from tracking_system.utils import get_db, process_sample_statuses, process_samples, validate_samples


router = APIRouter(prefix='/orders', tags=['orders'])


@router.post('/new', response_model=OrderBase)
def create_order(order: Annotated[list[SampleCreate], Body(embed=True)], db: Session = Depends(get_db)):
    samples = validate_samples(db, order)
    if samples:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={'repeat_sample_uuids': process_samples(samples)})
    else:
        db_order = OrdersManager.create_order(db)
        for sample in order:
            SamplesManager.create_sample(db, sample, db_order.id)
        return OrderBase(order_uuid=db_order.order_uuid)


@router.post('/status')
def get_status(
        order_uuid_to_get_sample_statuses_for: Annotated[str, Body(embed=True)],
        db: Session = Depends(get_db)):
    order_id = OrdersManager.get_order_id(db, order_uuid_to_get_sample_statuses_for)[0]
    samples = SamplesManager.get_sample_status(db, order_id)
    return JSONResponse(content={'sample_statuses': process_sample_statuses(samples)})

