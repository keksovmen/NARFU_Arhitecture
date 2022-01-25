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


class TestLibraryController(TestController):

	def test_index(self):
		response = self.app.get('/lib/')
		response.mustcontain("<td>Test", "<td>test address", "<td>test city")

	def test_create(self):
		self.app.post(
			"/lib/create/", collections.OrderedDict(
				{"name": "Name", "address": "Address", "city": "City"}))
		response = self.app.get('/lib/')
		response.mustcontain("<td>Name", "<td>Address", "<td>City")

	def test_delete(self):
		self.app.get('/lib/delete?libId=1')
		response = self.app.get('/lib/')
		ok_("<td>Test" not in response)

	def test_edit(self):
		self.app.post('/lib/edit?libId=1', collections.OrderedDict(
			{"name": "EditName", "address": "EditAddress", "city": "EditCity"}))
		response = self.app.get('/lib/')
		response.mustcontain("<td>EditName", "<td>EditAddress", "<td>EditCity")
