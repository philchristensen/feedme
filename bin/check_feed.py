#!/usr/bin/env python

# DRAM
# Copyright (C) 2007-2010 Anthology of Recorded Music, Inc.
#
# $Id$
#

"""
This runs a regular expression check, to make sure it won't take too long.
"""

import sys, time, os, os.path, warnings, signal

warnings.simplefilter('ignore', RuntimeWarning)
warnings.simplefilter('ignore', DeprecationWarning)

from twisted.python import usage

from modu.persist import dbapi, Store

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modu.sites import feedme_site

from feedme.model import feed

class Options(usage.Options):
	"""
	Implement usage parsing for the match.py script.
	"""
	
	optParameters = [
		['feed', 'f', '', "The URL code of the feed to fetch."],
		['timeout', 't', 5, "The URL code of the feed to fetch."],
	]
	synopsis = 'Usage: check_feed.py [options]'

if(__name__ == '__main__'):
	config = Options()
	try:
		config.parseOptions()
	except usage.UsageError, e:
		print >>sys.stderr, '%s: %s\nTry --help for usage details.' % (sys.argv[0], e)
		sys.exit(1)
	
	child_pid = os.fork()
	if child_pid:
		time.sleep(config['timeout'])
		for sig in ('TERM', 'INT', 'HUP', 'KILL'):
			if(os.system('kill -%s %d' % (sig, child_pid)) != 0):
				print >>sys.stderr, "warning: kill failed: pid=%d, signal=%s" % (child_pid, sig)
				time.sleep(1)
		pid, retval = os.wait()
		sys.exit(retval)
	else:
		if(config['feed']):
			pool = dbapi.connect(feedme_site.db_url)
			store = Store(pool)
		
			store.ensure_factory('feed', model_class=feed.Feed)
			f = store.load_one('feed', url_code=config['feed'])
		
			try:
				sys.stdout.write(f.to_xml())
			except:
				sys.exit(-2)
		else:
			url = sys.stdin.readline()
			pattern = ''
		
			char = sys.stdin.read()
			while(char):
				pattern += char
				char = sys.stdin.read()
		
			base_url = os.path.dirname(url)
			text = feed.fetch_rebased_url(url, base_url)
			
			try:
				feed.get_feed_matches(text, pattern)
			except:
				sys.exit(-2)
		
		sys.exit(0)
