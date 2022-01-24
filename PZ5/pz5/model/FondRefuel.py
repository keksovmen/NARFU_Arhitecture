from sqlalchemy import Column, Text, Integer, Date, ForeignKey

from pz5.model import DeclarativeBase, DBSession


__all__ = ["FondRefuel"]

class FondRefuel(DeclarativeBase):
	__tablename__ = "fond_refuel"
	refuelId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	source = Column(Text, nullable=False)
	publisher = Column(Text, nullable=False)
	amount = Column(Integer, default=0)
	publishDate = Column(Date, nullable=False)
	refuelDate = Column(Date, nullable=False)

	fondId = Column(Integer, ForeignKey("fond.fondId"), nullable=False)
	stuffId = Column(Integer, ForeignKey("stuff.stuffId"), nullable=False)
	litType = Column(Integer, ForeignKey("literatyre_type.typeName"), nullable=False)


	@staticmethod
	def checkIsExists(**kwargs):
		return False

	@staticmethod
	def getById(id):
		return DBSession.query(FondRefuel).\
			filter(FondRefuel.refuelId == id).\
				one_or_none()

	@staticmethod
	def getAllIds():
		return list(
			map(lambda v: v.refuelId, DBSession.query(FondRefuel).all()))
