# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import re, datetime, simplejson

import PyRSS2Gen as rss

def get_feed_matches(text, pattern):
	results = []
	try:
		regex = re.compile(pattern, re.MULTILINE | re.DOTALL | re.IGNORECASE)
	except:
		return results
	
	found = regex.search(text)
	while(found):
		results.append(found)
		pos = found.end()
		found = regex.search(text, pos)
	return results

def get_feed_item(info):
	return rss.RSSItem(pubDate=datetime.datetime.now(), **info)

def default_filter(match):
	return dict(
		title		= match.group(1),
		link		= match.group(2),
		description	= match.group(3),
		guid		= match.group(4),
	)

def generate_xml_feed(req, feed, filter_func=default_filter):
	text = feed.get_origin_page()
	matches = get_feed_matches(text, feed.item_match)
	return rss.RSS2(
		title = feed.title,
		link = req.get_path('feeds', feed.url_code),
		description = feed.description,
		lastBuildDate = datetime.datetime.now(),
		items = [get_feed_item(filter_func(x)) for x in matches]
	).to_xml('UTF-8')

def generate_json_test(pattern, text):
	matches = get_feed_matches(text, pattern)
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
