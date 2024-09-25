import uuid
from sqlalchemy.orm import Session

from tracking_system.models import Order


def create_order(db: Session) -> Order:
    db_order = Order(order_uuid=str(uuid.uuid4()))
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order_id(db: Session, order_uuid: str) -> int:
    return db.query(Order).with_entities(Order.id).filter(Order.order_uuid == order_uuid).first()
