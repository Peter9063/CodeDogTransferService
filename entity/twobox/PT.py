# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PT(Base):
    __tablename__ = 'pt'

    pn = Column(String(50), primary_key=True, nullable=False, server_default=text("''"))
    pa = Column(String(50), primary_key=True, nullable=False, server_default=text("'P/A'"))
    mn = Column(String(255), nullable=False, server_default=text("''"))
    ACTIVE = Column(String(255), nullable=False, index=True, server_default=text("''"))
    onhand = Column(DECIMAL(20, 4), nullable=False, index=True, server_default=text("'0.0000'"))
    shp = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    rcv = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    wip = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    sip = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    sit = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    onloan = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    consigned = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    qa = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    ondemand = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    onorder = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    list_price = Column(DECIMAL(26, 10), nullable=False, server_default=text("'0.0000000000'"))
    avg_cost = Column(DECIMAL(26, 10), nullable=False, server_default=text("'0.0000000000'"))
    recosted = Column(Date)
    std_cost = Column(DECIMAL(26, 10), nullable=False, server_default=text("'0.0000000000'"))
    fi_cost = Column(DECIMAL(26, 10), nullable=False, server_default=text("'0.0000000000'"))
    pcode = Column(CHAR(1), nullable=False, server_default=text("''"))
    ccode = Column(CHAR(1), nullable=False, server_default=text("''"))
    ocode = Column(CHAR(1), nullable=False, server_default=text("''"))
    dcode = Column(CHAR(1), nullable=False, server_default=text("''"))
    ecode = Column(CHAR(1), nullable=False, server_default=text("''"))
    pv_preferred = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    pm_preferred_po = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    pm_preferred_so = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    po_unit = Column(String(10), nullable=False, server_default=text("''"))
    so_unit = Column(String(10), nullable=False, server_default=text("''"))
    lead_time = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    min_qty = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    max_qty = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    yr_usage = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    qtr_usage = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    ga = Column(String(20), nullable=False, server_default=text("'1401'"))
    pur_cost = Column(DECIMAL(18, 2), nullable=False, server_default=text("'0.00'"))
    last_out = Column(Date)
    last_in = Column(Date)
    pn_class = Column(CHAR(1))
    sto = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    cycle_count = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    last_count = Column(DateTime)
    pn_category = Column(CHAR(1))
    pn_category_times = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
