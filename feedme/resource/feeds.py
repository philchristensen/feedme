# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.web import resource, app

from feedme.model import page

class Resource(resource.Resource):
	implements(resource.IContent)
	def prepare_content(self, req):
		"""
		@see: L{modu.web.resource.IContent.prepare_content()}
		"""
	
	def get_content(self, req):
		"""
		@see: L{modu.web.resource.IResource.get_response()}
		"""
	
	def get_content_type(self, req):
		"""
		@see: L{modu.web.resource.IContent.get_content_type()}
		"""
		return 'application/rss+xml'
