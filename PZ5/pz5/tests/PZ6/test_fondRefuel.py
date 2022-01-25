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


class TestFondRefuelController(TestController):

	def test_index(self):
		response = self.app.get('/fr/')
		response.mustcontain("<td>123", "<td>2", "<td>10")

	def test_create(self):
		self.app.post(
			"/fr/create/", collections.OrderedDict(
				{"source": "source", "publisher": "publisher", "amount": "1",
				 "fondId": "1", "publishDate": "01.01.1990",
				 "refuelDate": "01.01.2020",
				 "stuffId": "1", "litType" : "test"}))
		response = self.app.get('/fr/')
		response.mustcontain("<td>source", "<td>publisher", "<td>test")

	def test_delete(self):
		self.app.get('/fr/delete?refuelId=1')
		response = self.app.get('/stuff/')
		ok_("<td>123" not in response)

	def test_edit(self):
		self.app.post('/fr/edit?refuelId=1', collections.OrderedDict(
			{"source": "EditSource", "publisher": "EditPublisher", "amount": "1",
				 "fondId": "1", "publishDate": "01.01.1990",
				 "refuelDate": "01.01.2020",
				 "stuffId": "1", "litType" : "test"}))
		response = self.app.get('/fr/')
		response.mustcontain("<td>EditSource", "<td>EditPublisher", "<td>test")
