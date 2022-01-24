from sqlalchemy import Column, Text, Integer, UniqueConstraint

from pz5.model import DeclarativeBase, DBSession


__all__ = ["Library"]

class Library(DeclarativeBase):
	__tablename__ = "library"
	libId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(Text, nullable=False)
	address = Column(Text, nullable=False)
	city = Column(Text, nullable=False)

	UniqueConstraint(name, address, city)

	@staticmethod
	def checkIsExists(**kwargs):
		return DBSession.query(Library).\
			filter(Library.name == kwargs['msg']).\
			filter(Library.address == kwargs['address']).\
			filter(Library.city == kwargs['city']).\
				count() != 0

	@staticmethod
	def getById(id):
		return DBSession.query(Library).\
			filter(Library.libId == id).\
				one_or_none()

	@staticmethod
	def getAllIds():
		return list(
			map(lambda v: v.libId, DBSession.query(Library).all()))
