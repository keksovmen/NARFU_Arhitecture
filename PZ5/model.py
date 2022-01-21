import mysql.connector
from datetime import date, time, datetime


def getConnection():
	return mysql.connector.connect(user='narfu',
							password='1234', 
							host='192.168.0.100',
							database='arhitecture')


class LiteratyreType:
	def __init__(self, name):
		self.name = name
	
	@property
	def info(self):
		return f"{self.name}"
	
	@staticmethod
	def addLiteratyreType(name):
		con = getConnection()
		c = con.cursor()
		c.execute("INSERT INTO literatyre_type "
				"(literatyre_type_name) VALUES(%s)"
				"ON DUPLICATE KEY UPDATE "
				"literatyre_type_name=literatyre_type_name",
					[name])
		con.commit()
		con.close()
	
	@staticmethod
	def deleteLiteratyreType(name):
		con = getConnection()
		c = con.cursor()
		c.execute("DELETE FROM literatyre_type "
					"WHERE literatyre_type_name=(%s)",
					[name])
		con.commit()
		con.close()
		
	@staticmethod
	def updateLiteratyreType(oldName, newName):
		con = getConnection()
		c = con.cursor()
		c.execute("UPDATE literatyre_type SET "
					"literatyre_type_name=%(newName)s "
					"WHERE literatyre_type_name=%(oldName)s",
					{"newName": newName, "oldName": oldName})
		con.commit()
		con.close()
		
	@staticmethod
	def getLiteratyreTypes():
		con = getConnection()
		c = con.cursor()
		result = []
		c.execute("SELECT * from literatyre_type")
		for row in c:
			result.append(LiteratyreType(row[1]))
		con.close()
		return result

class Library:
	def __init__(self, libId, name, address, city):
		self.libId = libId
		self.name = name
		self.address = address
		self.city = city
	
	@property
	def info(self):
		return f"{self.libId} | {self.name} | " \
				f"{self.address} | {self.city}"
	
	@staticmethod
	def addLibrary(name, address, city):
		con = getConnection()
		c = con.cursor()
		c.execute("INSERT INTO library "
				"(library_name, "
				"library_address, "
				"library_city) "
				"VALUES(%(name)s, %(address)s, %(city)s)",
					{"name": name,
					"address": address,
					"city": city})
		con.commit()
		con.close()
	
	@staticmethod
	def deleteLibrary(libId):
		con = getConnection()
		c = con.cursor()
		c.execute("DELETE FROM library "
					"WHERE library_id=(%s)",
					[libId])
		con.commit()
		con.close()
		
	@staticmethod
	def updateLibrary(libId, name, address, city):
		con = getConnection()
		c = con.cursor()
		c.execute("UPDATE library SET "
					"library_name=%(name)s, "
					"library_address=%(address)s, "
					"library_city=%(city)s "
					"WHERE library_id=%(libId)s",
					{"libId": libId, "name": name,
					"address": address, "city": city})
		con.commit()
		con.close()
		
	@staticmethod
	def getLibraries():
		con = getConnection()
		c = con.cursor()
		result = []
		c.execute("SELECT * from library")
		for row in c:
			result.append(Library(row[0], row[1],
								row[2], row[3]))
		con.close()
		return result

class Fond:
	def __init__(self, libId, fondId, name,
				books, magazines,
				papers, dictionaries,
				dissertations, referats):
		self.fondId = fondId
		self.libId = libId
		self.name = name
		self.books = books
		self.magazines = magazines
		self.papers = papers
		self.dictionaries = dictionaries
		self.dissertations = dissertations
		self.referats = referats
	
	@property
	def info(self):
		return f"{self.fondId} | {self.libId} | " \
				f"{self.name} | {self.books} | " \
				f"{self.magazines} | {self.papers} | " \
				f"{self.dictionaries} | {self.dissertations} | " \
				f"{self.referats}"
	
	@staticmethod
	def addFond(libId, name,
				books=0, magazines=0,
				papers=0, dictionaries=0,
				dissertations=0, referats=0):
		con = getConnection()
		c = con.cursor()
		c.execute("INSERT INTO fond "
				"(library_library_id, "
				"fond_name, fond_books, "
				"fond_magazines, "
				"fond_papers, "
				"fond_dictinaries, "
				"fond_dissertations, "
				"fond_referats) "
				"VALUES(%(libId)s, %(name)s, "
				"%(books)s, %(magazines)s, %(papers)s, "
				"%(dictionaries)s, %(dissertations)s, "
				"%(referats)s)",
					{"libId": libId,
					"name": name,
					"books": books,
					"magazines": magazines,
					"papers": papers,
					"dictionaries": dictionaries,
					"dissertations": dissertations,
					"referats": referats})
		con.commit()
		con.close()
	
	@staticmethod
	def deleteFond(fondId):
		con = getConnection()
		c = con.cursor()
		c.execute("DELETE FROM fond "
					"WHERE fond_id=(%s)",
					[fondId])
		con.commit()
		con.close()
		
	@staticmethod
	def updateFond(fondId, 
				libId, name,
				books, magazines,
				papers, dictionaries,
				dissertations, referats):
		con = getConnection()
		c = con.cursor()
		c.execute("UPDATE fond SET "
					"library_library_id=%(libId)s, "
					"fond_name=%(name)s, "
					"fond_books=%(books)s, "
					"fond_magazines=%(magazines)s, "
					"fond_papers=%(papers)s, "
					"fond_dictinaries=%(dictionaries)s, "
					"fond_dissertations=%(dissertations)s, "
					"fond_referats=%(referats)s "
					"WHERE fond_id=%(fondId)s",
					{"fondId": fondId,
					"libId": libId,
					"name": name,
					"books": books,
					"magazines": magazines,
					"papers": papers,
					"dictionaries": dictionaries,
					"dissertations": dissertations,
					"referats": referats})
		con.commit()
		con.close()
		
	@staticmethod
	def getFonds():
		con = getConnection()
		c = con.cursor()
		result = []
		c.execute("SELECT * from fond")
		for row in c:
			result.append(Fond(row[0], row[1],
								row[2], row[3],
								row[4], row[5],
								row[6], row[7],
								row[8]
								))
		con.close()
		return result

class Stuff:
	def __init__(self, libId, stuffId,
				lastName, position,
				birthDate, hireDate,
				education, salary):
		self.libId = libId
		self.stuffId = stuffId
		self.lastName = lastName
		self.position = position
		self.birthDate = birthDate
		self.hireDate = hireDate
		self.education = education
		self.salary = salary
	
	@property
	def info(self):
		return f"{self.stuffId} | {self.libId} | " \
				f"{self.lastName} | {self.position} | " \
				f"{self.birthDate} | {self.hireDate} | " \
				f"{self.education} | {self.salary} | "
	
	@staticmethod
	def addStuff(libId,
				lastName, position,
				birthDate, hireDate,
				education=None, salary=0):
		con = getConnection()
		c = con.cursor()
		c.execute("INSERT INTO stuff"
				"(library_library_id, "
				"stuff_lastName, "
				"stuff_position, "
				"stuff_birthDate, "
				"stuff_hireDate, "
				"stuff_education, "
				"stuff_salary) "
				"VALUES(%(libId)s, %(name)s, "
				"%(pos)s, %(birth)s, %(hire)s, "
				"%(ed)s, %(salary)s)",
					{"libId": libId,
					"name": lastName,
					"pos": position,
					"birth": birthDate,
					"hire": hireDate,
					"ed": education,
					"salary": salary})
		con.commit()
		con.close()
	
	@staticmethod
	def deleteStuff(stuffId):
		con = getConnection()
		c = con.cursor()
		c.execute("DELETE FROM stuff "
					"WHERE stuff_id=(%s)",
					[stuffId])
		con.commit()
		con.close()
		
	@staticmethod
	def updateStuff(stuffId,
					libId,
					lastName, position,
					birthDate, hireDate,
					education, salary):
		con = getConnection()
		c = con.cursor()
		c.execute("UPDATE stuff SET "
					"library_library_id=%(libId)s, "
					"stuff_lastName=%(name)s, "
					"stuff_position=%(pos)s, "
					"stuff_birthDate=%(birth)s, "
					"stuff_hireDate=%(hire)s, "
					"stuff_education=%(ed)s, "
					"stuff_salary=%(salary)s "
					"WHERE stuff_id=%(stuffId)s",
					{"stuffId": stuffId,
					"libId": libId,
					"name": lastName,
					"pos": position,
					"birth": birthDate,
					"hire": hireDate,
					"ed": education,
					"salary": salary})
		con.commit()
		con.close()
		
	@staticmethod
	def getStuff():
		con = getConnection()
		c = con.cursor()
		result = []
		c.execute("SELECT * from stuff")
		for row in c:
			result.append(Stuff(row[0], row[1],
								row[2], row[3],
								row[4], row[5],
								row[6], row[7]))
		con.close()
		return result

class FondRefuel:
	def __init__ (self, 
					fondId, stuffId, litId,
					refuelId,
					refuelDate, source,
					publisher, publishDate,
					amount):
		self.fondId = fondId
		self.stuffId = stuffId
		self.litId = litId
		self.refuelId = refuelId
		self.refuelDate = refuelDate
		self.source = source
		self.publisher = publisher
		self.publishDate = publishDate
		self.amount = amount
	
	@property
	def info(self):
		return f"{self.refuelId} | {self.fondId} | " \
				f"{self.stuffId} | {self.litId} | " \
				f"{self.refuelDate} | {self.source} | " \
				f"{self.publisher} | {self.publishDate} | " \
				f"{self.amount}"
	
	@staticmethod
	def addFondRefuel(fondId, stuffId, litId,
						refuelDate, source,
						publisher, publishDate,
						amount):
		con = getConnection()
		c = con.cursor()
		c.execute("INSERT INTO fond_refuel"
				"(fond_fond_id, "
				"stuff_stuff_id, "
				"literatyre_type_id, "
				"fond_refuel_date, "
				"fond_refuel_source, "
				"fond_refuel_publisher, "
				"fond_refuel_publishDate, "
				"fond_refuel_amount) "
				"VALUES(%(fondId)s, %(stuffId)s, %(litId)s, "
				"%(when)s, %(source)s, "
				"%(publisher)s, %(publishDate)s, "
				"%(amount)s)",
					{"fondId": fondId,
					"stuffId": stuffId,
					"litId": litId,
					"when": refuelDate,
					"source": source,
					"publisher": publisher,
					"publishDate": publishDate,
					"amount": amount})
		con.commit()
		con.close()
	
	@staticmethod
	def deleteFondRefuel(refuelId):
		con = getConnection()
		c = con.cursor()
		c.execute("DELETE FROM fond_refuel "
					"WHERE fond_refuel_id=(%s)",
					[refuelId])
		con.commit()
		con.close()
		
	@staticmethod
	def updateFondRefuel(refuelId,
					fondId, stuffId, litId,
					refuelDate, source,
					publisher, publishDate,
					amount):
		con = getConnection()
		c = con.cursor()
		c.execute("UPDATE fond_refuel SET "
					"fond_fond_id=%(fondId)s, "
					"stuff_stuff_id=%(stuffId)s, "
					"literatyre_type_id=%(litId)s, "
					"fond_refuel_date=%(when)s, "
					"fond_refuel_source=%(source)s, "
					"fond_refuel_publisher=%(publisher)s, "
					"fond_refuel_publishDate=%(pD)s ,"
					"fond_refuel_amount=%(amount)s "
					"WHERE fond_refuel_id=%(refuelId)s",
					{"fondId": fondId,
					"stuffId": stuffId,
					"litId": litId,
					"when": refuelDate,
					"source": source,
					"publisher": publisher,
					"pD": publishDate,
					"amount": amount,
					"refuelId": refuelId})
		con.commit()
		con.close()
		
	@staticmethod
	def getFondRefuels():
		con = getConnection()
		c = con.cursor()
		result = []
		c.execute("SELECT * from fond_refuel")
		for row in c:
			result.append(FondRefuel(row[0], row[1],
								row[2], row[3],
								row[4], row[5],
								row[6], row[7],
								row[8]))
		con.close()
		return result

	
	
	
# LiteratyreType.addLiteratyreType("test")
# LiteratyreType.updateLiteratyreType("test", "test3")
# LiteratyreType.deleteLiteratyreType("test")
# for i in LiteratyreType.getLiteratyreTypes():
	# print(i.info)

# Library.addLibrary("test", "asd", "la")
# Library.deleteLibrary(6)
# Library.updateLibrary(1, "New name", "New address", "New city")
# for i in Library.getLibraries():
	# print(i.info)	

# Fond.addFond(1, "pyFond")
# Fond.deleteFond(2)
# Fond.updateFond(1, 2, "name", 10, 10, 10, 10, 10, 10)
# for i in Fond.getFonds():
	# print(i.info)	

# Stuff.addStuff(2, 'name', 'position', date(1960, 4, 30), date(1970, 10, 30), 'ed', 1000)
# Stuff.updateStuff(3, 1, 'o', 'p', datetime.now(), datetime.now(), 'e', 0)
# Stuff.deleteStuff(2)
# for i in Stuff.getStuff():
	# print(i.info)

# FondRefuel.addFondRefuel(1, 1, 1, datetime.now(), "source", "publisher", datetime.now(), 100)
# FondRefuel.updateFondRefuel(1, 1, 1, 1, datetime.now(), "asd", "dsa", datetime.now(), 50)
# FondRefuel.deleteFondRefuel(2)
# for i in FondRefuel.getFondRefuels():
	# print(i.info)
