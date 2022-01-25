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


class TestStuffController(TestController):

	def test_index(self):
		response = self.app.get('/stuff/')
		response.mustcontain("<td>Name", "<td>pos", "<td>education")

	def test_create(self):
		self.app.post(
			"/stuff/create/", collections.OrderedDict(
				{"lastName": "Name", "position": "position", "education": "ed",
				 "salary": "100", "birthDate": "01.01.1990",
				 "hireDate": "01.01.2020",
				 "libId": "1"}))
		response = self.app.get('/stuff/')
		response.mustcontain("<td>Name", "<td>position", "<td>100")

	def test_delete(self):
		self.app.get('/stuff/delete?stuffId=1')
		response = self.app.get('/stuff/')
		ok_("<td>Name" not in response)

	def test_edit(self):
		self.app.post('/stuff/edit?stuffId=1', collections.OrderedDict(
			{"lastName": "EditName", "position": "position", "education": "ed",
			 "salary": "500", "birthDate": "01.01.1990",
			 "hireDate": "01.01.2020",
			 "libId": "1"}))
		response = self.app.get('/stuff/')
		response.mustcontain("<td>EditName", "<td>position", "<td>500")
