from sqlalchemy import Column, Text

from pz5.model import DeclarativeBase, DBSession


__all__ = ["LiteratyreType"]

class LiteratyreType(DeclarativeBase):
    __tablename__ = "literatyre_type"

    typeName = Column(Text, primary_key=True, nullable=False)

    @staticmethod
    def checkIsExists(**kwargs):
        return DBSession.query(LiteratyreType).\
            filter(LiteratyreType.typeName == kwargs['typeName']).\
                   count() != 0

    @staticmethod
    def getById(id):
        return DBSession.query(LiteratyreType).\
            filter(LiteratyreType.typeName == id).\
                   one_or_none()

    @staticmethod
    def getAllIds():
        return list(map(lambda v: v.typeName, DBSession.query(LiteratyreType).all()))
