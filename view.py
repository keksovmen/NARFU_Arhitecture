

class View:
	"""
		@data must be iterable and 
			items must have info property
	"""
	
	@staticmethod
	def showData(heading, data):
		print(heading)
		for i in data:
			print(i.info)
	
	@staticmethod
	def showLitTypes(data):
		View.showData(f"in database {len(data)} "
					f"LiteratyreTypes, they are:",
					data)
	
	@staticmethod
	def showLibraries(data):
		View.showData(f"in database {len(data)} "
					f"Library, they are:",
					data)
	
	@staticmethod
	def showStuff(data):
		View.showData(f"in database {len(data)} "
					f"Stuff, they are:",
					data)
	
	@staticmethod
	def showFond(data):
		View.showData(f"in database {len(data)} "
					f"Fond, they are:",
					data)
	
	@staticmethod
	def showFondRefuel(data):
		View.showData(f"in database {len(data)} "
					f"FondRefuel, they are:",
					data)
	
	@staticmethod
	def getData(msg):
		return input('enter ' + msg + ': ')
	
	@staticmethod
	def showMasterMenu():
		print("what do you want to interact with?\n"
			"\t (1) Literature Type\n"
			"\t (2) Library\n"
			"\t (3) Fond\n"
			"\t (4) Fond Refuel\n"
			"\t (5) Stuff\n"
			"\t (6) Quit\n"
			)
	
	@staticmethod
	def showSpecificMenu(objName):
		print(f"what do you want to do with {objName}?\n"
			"\t (1) Add\n"
			"\t (2) Delete\n"
			"\t (3) Update\n"
			"\t (4) Show\n"
			"\t (5) Go Back\n")