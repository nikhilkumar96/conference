from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Date, Time
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Conference(Base):
    __tablename__ = 'conference'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    talks = relationship('Talk', backref="under")


class Talk(Base):
    __tablename__ = 'talk'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    duration = Column(String)
    date = Column(Date)
    time = Column(Time)
    conference_id = Column(Integer, ForeignKey('conference.id'))
    speakers = relationship("Speaker", backref="speaker_for")
    participants = relationship("Participant", backref="participant_for")
    # conf = relationship("Conf", backref=backref('talk'))


class Speaker(Base):
    __tablename__ = 'speaker'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    talk_id = Column(Integer, ForeignKey('talk.id'))
    # speakerof = relationship("Speakerof", backref=backref('speaker'))


class Participant(Base):
    __tablename__ = 'participant'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    talk_id = Column(Integer, ForeignKey('talk.id'))
    # participantof = relationship("Participantof", backref=backref('participant'))






