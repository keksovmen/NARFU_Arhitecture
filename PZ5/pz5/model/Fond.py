from sqlalchemy import Column, Text, Integer, ForeignKey

from pz5.model import DeclarativeBase, DBSession


__all__ = ["Fond"]

class Fond(DeclarativeBase):
	__tablename__ = "fond"
	fondId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(Text, nullable=False)
	books = Column(Integer, default=0)
	magazines = Column(Integer, default=0)
	papers = Column(Integer, default=0)
	dictinaries = Column(Integer, default=0)
	dissertations = Column(Integer, default=0)
	referats = Column(Integer, default=0)
	libId = Column(Integer, ForeignKey("library.libId"), nullable=False)


	@staticmethod
	def checkIsExists(**kwargs):
		return False

	@staticmethod
	def getById(id):
		return DBSession.query(Fond).\
			filter(Fond.fondId == id).\
				one_or_none()

	@staticmethod
	def getAllIds():
		return list(
			map(lambda v: v.fondId, DBSession.query(Fond).all()))
