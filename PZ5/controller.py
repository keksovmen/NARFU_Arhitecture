import model
from view import View

class BaseController:
	def handleInput(self, choice):
		pass
	
	def showMenu(self):
		pass

class BaseModelController(BaseController):
	def handleInput(self, choice):
		if choice == 1:
			self._add_()
		elif choice == 2:
			self._delete_()
		elif choice == 3:
			self._update_()
		elif choice == 4:
			self._show_()
		elif choice == 5:
			return MenuController()
		return self
	
	def showMenu(self):
		View.showSpecificMenu(self._getModelTitle_())
	
	def _add_(self):
		pass
	
	def _delete_(self):
		pass
	
	def _update_(self):
		pass
	
	def _show_(self):
		pass
	
	def _getModelTitle_(self):
		pass
	
	def _createObjectFromInput_(self):
		pass

class LiteratyreTypeController(BaseModelController):
	def _add_(self):
		obj = self._createObjectFromInput_()
		model.LiteratyreType.addLiteratyreType(obj.name)
	
	def _delete_(self):
		name = View.getData("name")
		model.LiteratyreType.deleteLiteratyreType(name)
	
	def _update_(self):
		oldName = View.getData("old name")
		obj = self._createObjectFromInput_()
		model.LiteratyreType.updateLiteratyreType(oldName, obj.name)
	
	def _show_(self):
		data = model.LiteratyreType.getLiteratyreTypes()
		View.showLitTypes(data)
	
	def _getModelTitle_(self):
		return "LiteratyreType"
	
	def _createObjectFromInput_(self):
		name = View.getData("name")
		return model.LiteratyreType(name)

class LibraryController(BaseModelController):
	def _add_(self):
		obj = self._createObjectFromInput_()
		model.Library.addLibrary(obj.name, obj.address, obj.city)
	
	def _delete_(self):
		libId = View.getData("library ID")
		model.Library.deleteLibrary(libId)
	
	def _update_(self):
		libId = View.getData("library ID")
		obj = self._createObjectFromInput_()
		model.Library.updateLibrary(libId, obj.name,
									obj.address, obj.city)
	
	def _show_(self):
		data = model.Library.getLibraries()
		View.showLibraries(data)
	
	def _getModelTitle_(self):
		return "Library"
	
	def _createObjectFromInput_(self):
		name = View.getData("name")
		address = View.getData("address")
		city = View.getData("city")
		return model.Library(0, name, address, city)

class StuffController(BaseModelController):
	def _add_(self):
		obj = self._createObjectFromInput_()
		model.Stuff.addStuff(obj.libId, obj.lastName, 
								obj.position, obj.birth, 
								obj.hire, obj.education,
								obj.salary)
	
	def _delete_(self):
		stuffId = View.getData("stuff ID")
		model.Stuff.deleteStuff(stuffId)
	
	def _update_(self):
		stuffId = View.getData("stuff ID")
		obj = self._createObjectFromInput_()
		model.Stuff.updateStuff(stuffId, obj.libId, 
								obj.lastName, obj.position, 
								obj.birth, obj.hire, 
								obj.education, obj.salary)
	
	def _show_(self):
		data = model.Stuff.getStuff()
		View.showStuff(data)
	
	def _getModelTitle_(self):
		return "Stuff"
	
	def _createObjectFromInput_(self):
		lastName = View.getData("last name")
		libId = View.getData("library ID")
		position = View.getData("position")
		birth = View.getData("birth date")
		hire = View.getData("hire date")
		education = View.getData("education date")
		salary = View.getData("salary date")
		return model.Stuff(libId, 0, lastName, 
							position, birth, hire,
							education, salary)

class FondController(BaseModelController):
	def _add_(self):
		obj = self._createObjectFromInput_()
		model.Fond.addFond(obj.libId, obj.name, 
								obj.books, obj.magazines, 
								obj.papers, obj.dictionaries,
								obj.dissertations, obj.referats)
	
	def _delete_(self):
		fondId = View.getData("fond ID")
		model.Fond.deleteFond(fondId)
	
	def _update_(self):
		fondId = View.getData("fond ID")
		obj = self._createObjectFromInput_()
		model.Fond.addFond(obj.libId, fondId, obj.name, 
								obj.books, obj.magazines, 
								obj.papers, obj.dictionaries,
								obj.dissertations, obj.referats)
	
	def _show_(self):
		data = model.Fond.getFonds()
		View.showFond(data)
	
	def _getModelTitle_(self):
		return "Fond"
	
	def _createObjectFromInput_(self):
		libId = View.getData("library ID")
		name = View.getData("name")
		books = View.getData("books")
		magazines = View.getData("magazines")
		papers = View.getData("papers")
		dictionaries = View.getData("dictionaries")
		dissertations = View.getData("dissertations")
		referats = View.getData("referats")
		return model.Fond(libId, 0, name, books,
							magazines, papers, dictionaries,
							dissertations, referats)

class FondRefuelController(BaseModelController):
	def _add_(self):
		obj = self._createObjectFromInput_()
		model.FondRefuel.addFondRefuel(obj.fondId, obj.stuffId, 
										obj.litId, obj.refuelDate, 
										obj.source, obj.publisher,
										obj.publishDate, obj.amount)
	
	def _delete_(self):
		refuelId = View.getData("refuel ID")
		model.FondRefuel.deleteFondRefuel(refuelId)
	
	def _update_(self):
		refuelId = View.getData("refuel ID")
		obj = self._createObjectFromInput_()
		model.FondRefuel.addFondRefuel(refuelId, obj.fondId, obj.stuffId, 
										obj.litId, obj.refuelDate, 
										obj.source, obj.publisher,
										obj.publishDate, obj.amount)
	
	def _show_(self):
		data = model.FondRefuel.getFondRefuels()
		View.showFondRefuel(data)
	
	def _getModelTitle_(self):
		return "FondRefuel"
	
	def _createObjectFromInput_(self):
		fondId = View.getData("fond ID")
		stuffId = View.getData("stuff ID")
		litId = View.getData("literature type ID")
		whenDate = View.getData("when date")
		source = View.getData("source")
		publisher = View.getData("publisher")
		publishDate = View.getData("publish date")
		amount = View.getData("amount")
		return model.FondRefuel(fondId, stuffId, litId, 0,
								whenDate, source, publisher,
								publishDate, amount)

class MenuController(BaseController):
	def handleInput(self, choice):
		if choice == 1:
			return LiteratyreTypeController()
		elif choice == 2:
			return LibraryController()
		elif choice == 3:
			return FondController()
		elif choice == 4:
			return FondRefuelController()
		elif choice == 5:
			return StuffController()
		elif choice == 6:
			return None
		else:
			return self
	
	def showMenu(self):
		View.showMasterMenu()
	

class Main:
	def run(self):
		controller = MenuController()
		while controller:
			controller.showMenu()
			choice = int(View.getData("choice option"))
			controller = controller.handleInput(int(choice))
	

if __name__ == "__main__":
	main = Main()
	main.run()