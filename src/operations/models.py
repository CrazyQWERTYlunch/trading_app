from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, func

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP, default=func.now()),
    Column("type", String),
)