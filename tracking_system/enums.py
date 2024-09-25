import enum


class QCStatus(enum.Enum):
    FAIL = 'FAIL'
    PASS = 'PASS'


class SampleStatus(enum.Enum):
    ORDERED = 'ORDERED'
    SHIPPED = 'SHIPPED'
    PROCESSED = 'PROCESSED'
    FAILED = 'FAILED'

