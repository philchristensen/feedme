# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import urllib2

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
		
		if(req.postpath[0] == 'test'):
			url = req.data.get('url', None).value
			pattern = req.data.get('pattern', None).value
			
			if not(url and pattern):
				app.raise400('Missing parameters.')
			
			try:
				result = urllib2.urlopen(url)
			except Exception, e:
				app.raise400('Invalid URL: %s' % e)
			
			text = result.read()
			
			self.content_type = "application/json; charset=UTF-8"
			self.content = feeder.generate_json_test(pattern, text)
		else:
			req.store.ensure_factory('feed', model_class=feed.Feed)
			f = req.store.load_one('feed', url_code=req.postpath[0])
			if not(f):
				app.raise404()
		
			self.content_type = 'application/rss+xml; charset=UTF-8'
			self.content = feeder.generate_feed(req, f, filter_func=rss_filter)
		
	def get_content(self, req):
		"""
		@see: L{modu.web.resource.IResource.get_response()}
		"""
		return self.content
	
	def get_content_type(self, req):
		"""
		@see: L{modu.web.resource.IContent.get_content_type()}
		"""
		return self.content_type
