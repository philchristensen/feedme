# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from zope.interface import implements

from modu.web import resource, app

from feedme.model import feed
from feedme.util import feeder

def rss_filter(match):
	return dict(
		title		= match.group(1),
		link		= match.group(2),
		description	= match.group(3),
		guid		= match.group(4),
	)

class Resource(resource.Resource):
	implements(resource.IContent)
	def prepare_content(self, req):
		"""
		@see: L{modu.web.resource.IContent.prepare_content()}
		"""
		if not(req.postpath):
			app.raise404()
		
		req.store.ensure_factory('feed', model_class=feed.Feed)
		f = req.store.load_one('feed', url_code=req.postpath[0])
		if not(f):
			app.raise404()
		
		self.rss = feeder.generate_feed(req, f, filter_func=rss_filter)
	
	def get_content(self, req):
		"""
		@see: L{modu.web.resource.IResource.get_response()}
		"""
		return self.rss.to_xml('UTF-8')
	
	def get_content_type(self, req):
		"""
		@see: L{modu.web.resource.IContent.get_content_type()}
		"""
		return 'application/rss+xml; charset=UTF-8'
