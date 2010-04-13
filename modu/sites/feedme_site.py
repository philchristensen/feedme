# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import os.path
import pkg_resources as pkg

from zope.interface import classProvides

from twisted import plugin

from modu.web import app, static
from modu.editable import resource
from modu.editable.datatypes import fck

from feedme.resource import index, feeds

def admin_site_stylesheet_callback(req):
	return req.get_path('regex-test-styles.css')

class Site(object):
	classProvides(plugin.IPlugin, app.ISite)
	base_domain = 'localhost'
	
	def initialize(self, application):
		application.base_domain = self.base_domain
		application.db_url = 'MySQLdb://feedme:jufGhosh@localhost/feedme'
		application.template_dir = 'feedme', 'template'
		application.admin_site_stylesheet = admin_site_stylesheet_callback
		
		import feedme
		application.compiled_template_root = '/tmp/modu/feedme'
		if not(os.path.exists(application.compiled_template_root)):
			os.makedirs(application.compiled_template_root)
		
		application.activate('/assets', static.FileResource, pkg.resource_filename('modu.assets', ''))
		
		import feedme.itemdefs
		application.activate('/admin', resource.AdminResource, default_path='admin/listing/page', itemdef_module=feedme.itemdefs)
		
		application.activate('/fck', fck.FCKEditorResource)

		application.activate('/', index.Resource)
		application.activate('/feeds', feeds.Resource)

class LiveSite(Site):
	classProvides(plugin.IPlugin, app.ISite)
	base_domain = 'feedmeweirdthings.com'
