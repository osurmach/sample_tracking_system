from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from tracking_system.database import Base
from tracking_system.enums import QCStatus, SampleStatus


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_uuid = Column(String, unique=True, index=True)

    samples = relationship('Sample', back_populates='order')


class Sample(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True)
    sample_uuid = Column(String, unique=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    sequence = Column(String)
    plate_id = Column(Integer)
    well = Column(String(3))
    qc_1 = Column(Float)
    qc_2 = Column(Float)
    qc_3 = Column(Enum(QCStatus))
    status = Column(Enum(SampleStatus), default=SampleStatus.ORDERED)

    order = relationship('Order', back_populates='samples')
