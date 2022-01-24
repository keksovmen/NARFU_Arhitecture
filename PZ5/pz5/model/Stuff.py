from sqlalchemy import Column, Text, Integer, Date, ForeignKey

from pz5.model import DeclarativeBase, DBSession


__all__ = ["Stuff"]

class Stuff(DeclarativeBase):
	__tablename__ = "stuff"
	stuffId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	lastName = Column(Text, nullable=False)
	position = Column(Text, nullable=False)
	education = Column(Text, nullable=False)
	salary = Column(Integer, nullable=False)
	birthDate = Column(Date, nullable=False)
	hireDate = Column(Date, nullable=False)
	libId = Column(Integer, ForeignKey("library.libId"), nullable=False)


	@staticmethod
	def checkIsExists(**kwargs):
		return False
		# return DBSession.query(Stuff).\
		# 	filter(Stuff.msg == kwargs['msg']).\
		# 	filter(Stuff.address == kwargs['address']).\
		# 	filter(Stuff.city == kwargs['city']).\
		# 		count() != 0

	@staticmethod
	def getById(id):
		return DBSession.query(Stuff).\
			filter(Stuff.stuffId == id).\
				one_or_none()

	@staticmethod
	def getAllIds():
		return list(
			map(lambda v: v.stuffId, DBSession.query(Stuff).all()))
