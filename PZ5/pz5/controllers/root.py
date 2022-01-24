# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from pz5.model import DBSession

from pz5.lib.base import BaseController
from pz5.controllers.error import ErrorController

from pz5.controllers.litTypeController import LiteratureTypeController
from pz5.controllers.libraryController import LibraryController
from pz5.controllers.stuffController import StuffController
from pz5.controllers.fondController import FondController
from pz5.controllers.fondRefuelController import FondRefuelController


__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the PZ5 application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()
    litType = LiteratureTypeController()
    lib = LibraryController()
    stuff = StuffController()
    fond = FondController()
    fr = FondRefuelController()


    def _before(self, *args, **kw):
        tmpl_context.project_name = "pz5"

    @expose('pz5.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')
    @expose('pz5.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('pz5.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('pz5.templates.data')
    @expose('json')
    def data(self, **kw):
        """
        This method showcases how you can use the same controller
        for a data page and a display page.
        """
        return dict(page='data', params=kw)
