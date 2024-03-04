import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Alert(Base):
    __tablename__ = "alerts"
    alert_id = sa.Column(sa.Integer(), autoincrement=True, primary_key=True)
    data_item = sa.Column(sa.String(), nullable=False)
    operator = sa.Column(sa.String(), nullable=False)
    value = sa.Column(sa.Double(), nullable=False)
    last_modified = sa.Column(
        sa.TIMESTAMP(), server_default=sa.text("(now() at time zone 'utc')")
    )


class Borrower(Base):
    __tablename__ = "borrowers"

    borrower_id = sa.Column(sa.Integer(), autoincrement=True, primary_key=True)
    name = sa.Column(sa.String(), nullable=False)
    last_modified = sa.Column(
        sa.TIMESTAMP(), server_default=sa.text("(now() at time zone 'utc')")
    )
    total_revenue = sa.Column(sa.Double(), nullable=True)
    ebitda = sa.Column(sa.Double(), nullable=True)
    dscr = sa.Column(sa.Double(), nullable=True)
    debt_to_ebitda = sa.Column(sa.Double(), nullable=True)
