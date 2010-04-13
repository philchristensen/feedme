# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import urllib2, dateutil.parser, re, datetime, sys, os.path, urlparse
import PyRSS2Gen as rss

from modu.persist import storable

import hashlib

find_re = re.compile(r'\bhref\s*=\s*("[^"]*"|\'[^\']*\'|[^"\'<>=\s]+)')

def fix_urls(document, base_url):
	ret = []
	last_end = 0
	for match in find_re.finditer(document):
		url = match.group(1)
		if url[0] in "\"'":
			url = url.strip(url[0])
		parsed = urlparse.urlparse(url)
		if parsed.scheme == parsed.netloc == '': #relative to domain
			url = urlparse.urljoin(base_url, url)
			ret.append(document[last_end:match.start(1)])
			ret.append('"%s"' % (url,))
			last_end = match.end(1)
	ret.append(document[last_end:])
	return ''.join(ret)

def get_feed_matches(text, pattern):
	results = []
	try:
		regex = re.compile(pattern, re.MULTILINE | re.DOTALL | re.IGNORECASE)
	except Exception, e:
		print >>sys.stderr, e
		return results
	# print >>sys.stderr, 'pattern hash: %r' % hashlib.md5(pattern).hexdigest()
	# print >>sys.stderr, 'text hash: %r' % hashlib.md5(text).hexdigest()
	found = regex.search(text)
	# print >>sys.stderr, 'found %r\n' % found
	while(found):
		results.append(found)
		pos = found.end()
		found = regex.search(text, pos)
	return results

class Feed(storable.Storable):
	def __init__(self):
		super(Feed, self).__init__('feed')
	
	def get_origin_page(self):
		result = urllib2.urlopen(self.origin_url)
		text = result.read()
		base_url = os.path.dirname(self.origin_url)
		return fix_urls(text, base_url)
	
	def extract_items(self):
		text = self.get_origin_page()
		return get_feed_matches(text, self.item_match.replace('\r\n', '\n'))
	
	def get_items(self, cached=False):
		return [self.convert_match(x) for x in self.extract_items()]
	
	def convert_match(self, match):
		info = dict(
			title		= match.expand(self.title_pattern),
			link		= match.expand(self.link_pattern),
			description	= match.expand(self.body_pattern),
			guid		= match.expand(self.link_pattern),
			pubDate		= dateutil.parser.parse(match.expand(self.date_pattern)),
		)
		return rss.RSSItem(**info)
	
	def to_xml(self, req):
		text = self.get_origin_page()
		matches = self.get_items()
		return rss.RSS2(
			title = self.title,
			link = req.get_path('feeds', self.url_code),
			description = self.description,
			lastBuildDate = datetime.datetime.now(),
			items = matches,
		).to_xml('UTF-8')

