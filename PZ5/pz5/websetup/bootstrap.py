# -*- coding: utf-8 -*-
"""Setup the PZ5 application"""
from __future__ import print_function, unicode_literals
import transaction
import datetime
from pz5 import model


def bootstrap(command, conf, vars):
	"""Place any commands to setup pz5 here"""

	model.DBSession.add(model.LiteratyreType(typeName="test"))
	model.DBSession.add(
		model.Library(name='Test', address='test address', city='test city'))
	model.DBSession.add(
		model.Stuff(lastName='Name', position='pos', education='education',
					salary=100, birthDate=datetime.date.today(),
					hireDate=datetime.date.today(), libId=1))
	model.DBSession.add(model.Fond(name='Test', libId=1))
	model.DBSession.add(
		model.FondRefuel(source="123", publisher="2", amount="10",
						 publishDate=datetime.date.today(),
						 refuelDate=datetime.date.today(), fondId=1, stuffId=1,
						 litType="test"))

	model.DBSession.flush()
	transaction.commit()
	# <websetup.bootstrap.before.auth

	# <websetup.bootstrap.after.auth>
