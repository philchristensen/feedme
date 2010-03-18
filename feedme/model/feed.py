# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

import urllib2

from modu.persist import storable

class Feed(storable.Storable):
	def __init__(self):
		super(Feed, self).__init__('feed')
	
	def get_origin_page(self):
		result = urllib2.urlopen(self.origin_url)
		return result.read()