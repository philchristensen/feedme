# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import urllib2, simplejson, os.path

from zope.interface import implements

from modu.web import resource, app

from feedme.model import feed

def generate_json_test(pattern, text):
	matches = feed.get_feed_matches(text, pattern)
	return simplejson.dumps(dict(
		pattern	= pattern,
		source	= text,
		matches	= [
			dict(
				groups	= m.groups(),
				named_groups = m.groupdict(),
			) for m in matches
		]
	))

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
			
			base_url = os.path.dirname(url)
			text = feed.fix_urls(result.read(), base_url)
			
			self.content_type = "application/json; charset=UTF-8"
			self.content = generate_json_test(pattern, text)
		else:
			req.store.ensure_factory('feed', model_class=feed.Feed)
			f = req.store.load_one('feed', url_code=req.postpath[0])
			if not(f):
				app.raise404()
		
			self.content_type = 'application/rss+xml; charset=UTF-8'
			self.content = f.to_xml(req)
		
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
