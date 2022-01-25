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


class TestFondController(TestController):

	def test_index(self):
		response = self.app.get('/fond/')
		response.mustcontain("<td>Test", "<td>0", "<td>1")

	def test_create(self):
		self.app.post(
			"/fond/create/", collections.OrderedDict(
				{"name": "Name", "books": "300", "magazines": "200",
				 "papers": "100", "dictinaries": "500", "dissertations": "500",
				 "referats": "300", "libId": "1"}))
		response = self.app.get('/fond/')
		response.mustcontain("<td>Name", "<td>300", "<td>500")

	def test_delete(self):
		self.app.get('/fond/delete?fondId=1')
		response = self.app.get('/fond/')
		ok_("<td>123" not in response)

	def test_edit(self):
		self.app.post('/fond/edit?fondId=1', collections.OrderedDict(
			{"name": "EditName", "books": "0", "magazines": "200",
			 "papers": "100", "dictinaries": "500", "dissertations": "500",
			 "referats": "300", "libId": "1"}))
		response = self.app.get('/fond/')
		response.mustcontain("<td>EditName", "<td>0", "<td>1")
