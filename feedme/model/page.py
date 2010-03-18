# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.persist import storable

class Page(storable.Storable):
	def __init__(self):
		super(Page, self).__init__('page')
	
	def load_data(self, data):
		# Automatically convert binary data to string.
		if(hasattr(data['data'], 'tostring')):
			data['data'] = data['data'].tostring()
		super(Page, self).load_data(data)
