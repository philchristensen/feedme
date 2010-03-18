# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import re, datetime
import PyRSS2Gen as rss

def get_feed_matches(text, pattern):
	return re.finditer(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)

def get_feed_item(info):
	return rss.RSSItem(
		pubDate		= datetime.datetime.now(),
		**info,
	)

def default_filter(match):
	return dict(
		title		= match.group('title'),
		link		= match.group('link'),
		description	= match.group('description'),
		guid		= match.group('link'),
	)

def generate_feed(req, text, feed, filter_func=default_filter):
	matches = get_feed_matches(text, feed.item_match)
	return rss.RSS2(
		title = feed.title,
		link = req.get_path('feeds', feed.url_code),
		description = feed.description,
		lastBuildDate = datetime.datetime.now(),
		items = [filter_func(x) for x in matches]
	)

if(__name__ == '__main__'):
	# rss = generate_feed(...)
	# rss.write_xml(open("pyrss2gen.xml", "w"))
	pass
