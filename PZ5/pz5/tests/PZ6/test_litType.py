# -*- coding: utf-8 -*-
"""
Functional test suite for the root controller.

This is an example of how functional tests can be written for controllers.

As opposed to a unit-test, which test a small unit of functionality,
functional tests exercise the whole application and its WSGI stack.

Please read https://webtest.readthedocs.io/ for more information.

"""

import collections

from nose.tools import ok_
from pz5.tests import TestController


class TestLiteratyreTypeController(TestController):

	def test_index(self):
		response = self.app.get('/litType/')
		response.mustcontain("<td>test")

	def test_create(self):
		self.app.post(
			"/litType/create", {"typeName": "Name"})
		response = self.app.get('/litType/')
		response.mustcontain("<td>Name")

	def test_delete(self):
		self.app.get('/litType/delete?idName=test')
		response = self.app.get('/litType/')
		ok_("<td>test" not in response)

	def test_edit(self):
		self.app.post('/litType/edit?idName=test', collections.OrderedDict(
			{"typeName": "EditName"}))
		response = self.app.get('/litType/')
		response.mustcontain("<td>EditName")
