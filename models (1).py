
from sqlalchemy import Column,Integer,String

from database import Base



class WebhookEvent(Base):

    __tablename__="events"


    id=Column(
        Integer,
        primary_key=True
    )


    application=Column(
        String
    )


    event_type=Column(
        String
    )


    status=Column(
        String
    )



class FileMetadata(Base):

    __tablename__="files"


    id=Column(
        Integer,
        primary_key=True
    )


    filename=Column(
        String
    )


    location=Column(
        String
    )
