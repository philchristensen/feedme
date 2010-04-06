# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import urllib2

from modu.persist import storable

from feedme.util import feeder

class Feed(storable.Storable):
	def __init__(self):
		super(Feed, self).__init__('feed')
	
	def get_origin_page(self):
		result = urllib2.urlopen(self.origin_url)
		return result.read()
	
	def extract_items(self):
		text = self.get_origin_page()
		return feeder.get_feed_matches(text, self.item_match)
	
	def get_items(self, cached=False):
		return [self.convert_match(x) for x in self.extract_items()]
	
	def convert_match(self, match):
		info = dict(
			title		= match.expand(self.title_pattern),
			link		= match.expand(self.link_pattern),
			description	= match.expand(self.body_pattern),
			guid		= match.expand(self.link_pattern),
		)
		return rss.RSSItem(pubDate=datetime.datetime.now(), **info)
