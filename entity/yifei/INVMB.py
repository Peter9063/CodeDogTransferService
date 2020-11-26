# coding: utf-8
from sqlalchemy import CHAR, Column, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class INVMB(Base):
    __tablename__ = 'INVMB'

    COMPANY = Column(CHAR(10, 'Chinese_PRC_BIN'))
    CREATOR = Column(CHAR(10, 'Chinese_PRC_BIN'))
    USR_GROUP = Column(CHAR(10, 'Chinese_PRC_BIN'))
    CREATE_DATE = Column(CHAR(17, 'Chinese_PRC_BIN'))
    MODIFIER = Column(CHAR(10, 'Chinese_PRC_BIN'))
    MODI_DATE = Column(CHAR(17, 'Chinese_PRC_BIN'))
    FLAG = Column(Numeric(3, 0))
    MB001 = Column(CHAR(20, 'Chinese_PRC_BIN'), primary_key=True )
    MB002 = Column(String(60, 'Chinese_PRC_BIN'), index=True)
    MB003 = Column(String(60, 'Chinese_PRC_BIN'))
    MB004 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB005 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB006 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB007 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB008 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB009 = Column(String(255, 'Chinese_PRC_BIN'))
    MB010 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB011 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB012 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB013 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB014 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB015 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB016 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB017 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB018 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB019 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB020 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB021 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB022 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB023 = Column(Numeric(4, 0), server_default=text("(0)"))
    MB024 = Column(Numeric(4, 0), server_default=text("(0)"))
    MB025 = Column(CHAR(1, 'Chinese_PRC_BIN'), index=True, server_default=text("('')"))
    MB026 = Column(CHAR(2, 'Chinese_PRC_BIN'), index=True, server_default=text("('')"))
    MB027 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB028 = Column(String(255, 'Chinese_PRC_BIN'))
    MB029 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB030 = Column(CHAR(8, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB031 = Column(CHAR(8, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB032 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB033 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB034 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB035 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB036 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB037 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB038 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB039 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB040 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB041 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB042 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB043 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB044 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB045 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB046 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB047 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB048 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB049 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB050 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB051 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB052 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB053 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB054 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB055 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB056 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB057 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB058 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB059 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB060 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB061 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB062 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB063 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB064 = Column(Numeric(17, 6), server_default=text("(0)"))
    MB065 = Column(Numeric(16, 2), server_default=text("(0)"))
    MB066 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB067 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB068 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB069 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB070 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB071 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB072 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB073 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB074 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB075 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB076 = Column(Numeric(3, 0), server_default=text("(0)"))
    MB077 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB078 = Column(Numeric(3, 0), server_default=text("(0)"))
    MB079 = Column(Numeric(3, 0), server_default=text("(0)"))
    MB080 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB081 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB082 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB083 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB084 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB085 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB086 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB087 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB088 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB089 = Column(Numeric(17, 6), server_default=text("(0)"))
    MB090 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB091 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB092 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB093 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB094 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB095 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB096 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB100 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB101 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB102 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB103 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB104 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB105 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB106 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB107 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB108 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB109 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('y')"))
    MB110 = Column(CHAR(20, 'Chinese_PRC_BIN'), index=True, server_default=text("('')"))
    MB111 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB112 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB113 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB114 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB115 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB116 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB117 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB118 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('1')"))
    MB119 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB120 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB121 = Column(CHAR(30, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB122 = Column(CHAR(30, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB123 = Column(CHAR(30, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB124 = Column(CHAR(30, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB125 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB126 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('4')"))
    MB127 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB128 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB129 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB130 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB131 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB132 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB133 = Column(CHAR(20, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB134 = Column(String(255, 'Chinese_PRC_BIN'))
    MB135 = Column(String(255, 'Chinese_PRC_BIN'))
    MB136 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB137 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB138 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB139 = Column(CHAR(8, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB140 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB141 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB142 = Column(CHAR(12, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB143 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB144 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB145 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB146 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB147 = Column(Numeric(4, 0), server_default=text("(0)"))
    MB148 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB149 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB150 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB151 = Column(Numeric(8, 0), server_default=text("(0)"))
    MB152 = Column(Numeric(8, 0), server_default=text("(0)"))
    MB179 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB180 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB181 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB182 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB183 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB184 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB185 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB186 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB187 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB188 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB189 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB190 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB191 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB192 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB193 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB194 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB195 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB196 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB197 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB198 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB199 = Column(CHAR(60, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB401 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB402 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB403 = Column(Numeric(5, 4), server_default=text("(0)"))
    MB404 = Column(Numeric(17, 8), server_default=text("(0)"))
    MB405 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB406 = Column(CHAR(3, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB407 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('0')"))
    MB408 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB409 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB410 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB411 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('3')"))
    MB412 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB413 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('1')"))
    MB414 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB415 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB416 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB417 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB418 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB419 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB420 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB421 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('2')"))
    MB422 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB423 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('1')"))
    MB424 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB425 = Column(Numeric(2, 0), server_default=text("('1')"))
    MB426 = Column(Numeric(2, 0), server_default=text("('1')"))
    MB427 = Column(Numeric(2, 0), server_default=text("('1')"))
    MB428 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB429 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB430 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB431 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB432 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB433 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB434 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB435 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('1')"))
    MB436 = Column(CHAR(8, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB437 = Column(String(30, 'Chinese_PRC_BIN'))
    MB438 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB439 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB440 = Column(Numeric(16, 6), server_default=text("(0)"))
    MB441 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB442 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('2')"))
    MB443 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB444 = Column(CHAR(4, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB445 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB446 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB447 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB448 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB449 = Column(Numeric(7, 4), server_default=text("(0)"))
    MB450 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB451 = Column(CHAR(8, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB452 = Column(Numeric(16, 6), server_default=text("(0)"))
    MBD01 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MBD02 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MBE01 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB453 = Column(CHAR(30, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB454 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MBH01 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MBH02 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MBH03 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB455 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB456 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB457 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB458 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB459 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB460 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB461 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB462 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB463 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB464 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB465 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB466 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB467 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB468 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB469 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB470 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB471 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB472 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB473 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB474 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MB475 = Column(CHAR(6, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MBL01 = Column(Numeric(2, 0), server_default=text("(0)"))
    MBL02 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('')"))
    MBL03 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MBL04 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB476 = Column(Numeric(2, 0), server_default=text("(0)"))
    MB477 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB478 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB479 = Column(CHAR(1, 'Chinese_PRC_BIN'), server_default=text("('N')"))
    MB480 = Column(CHAR(10, 'Chinese_PRC_BIN'), server_default=text("('')"))
    UDF01 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF02 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF03 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF04 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF05 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF06 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF51 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF52 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF53 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF54 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF55 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF56 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF07 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF08 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF09 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF10 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF11 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF12 = Column(String(255, 'Chinese_PRC_BIN'))
    UDF57 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF58 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF59 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF60 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF61 = Column(Numeric(16, 6), server_default=text("(0)"))
    UDF62 = Column(Numeric(16, 6), server_default=text("(0)"))
