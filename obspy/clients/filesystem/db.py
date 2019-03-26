# -*- coding: utf-8 -*-
"""
SQLAlchemy ORM definitions (database layout) for tsindex.db.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

import datetime

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint


Base = declarative_base()


def get_tsindex_table(table_name='tsindex'):

    class TSIndexTable(Base):
        """
        DB table containing tsindex.
        """
        __tablename__ = table_name
        __table_args__ = (
            PrimaryKeyConstraint('network', 'station',
                                 'location', 'channel',
                                 'quality', 'version',
                                 'starttime', 'endtime'),
            {'keep_existing': True}
        )

        network = Column(String)
        station = Column(String)
        location = Column(String)
        channel = Column(String)
        quality = Column(String(1))
        version = Column(Integer)
        starttime = Column(String)
        endtime = Column(String)
        samplerate = Column(Float)
        filename = Column(String)
        byteoffset = Column(Integer)
        bytes = Column(Integer)
        hash = Column(String)
        timeindex = Column(String)
        timespans = Column(String)
        timerates = Column(String)
        format = Column(String)
        filemodtime = Column(String)
        updated = Column(String)
        scanned = Column(String)

        def __repr__(self):
            return "<TSIndexTable('%s %s %s %s %s %s %s')>" % \
                    (self.network, self.station, self.location,
                     self.channel, self.starttime, self.endtime,
                     self.filemodtime)
    return TSIndexTable


def get_tsindex_summary_table(table_name='tsindex_summary'):

    class TSIndexSummaryTable(Base):
        """
        DB table containing tsindex.
        """
        __tablename__ = table_name
        __table_args__ = (
            PrimaryKeyConstraint('network', 'station',
                                 'location', 'channel',
                                 'earliest', 'latest'),
            {'keep_existing': True}
        )

        network = Column(String)
        station = Column(String)
        location = Column(String)
        channel = Column(String)
        earliest = Column(String)
        latest = Column(String)
        updt = Column(String,
                      default=datetime.datetime.utcnow)

        def __repr__(self):
            return "<TSIndexSummaryTable('%s %s %s %s %s %s %s')>" % \
                    (self.network, self.station, self.location,
                     self.channel, self.earliest, self.latest, self.updt)
    return TSIndexSummaryTable
