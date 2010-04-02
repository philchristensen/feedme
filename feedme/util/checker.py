# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.editable import define
from modu.util import form

class RegexCheckerField(define.definition):
	"""
	Connects to JSON interface for checking regexes.
	"""
	def get_element(self, req, style, storable):
		"""
		@see: L{modu.editable.define.definition.get_element()}
		"""
		store = storable.get_store()
		
		frm = form.FormNode(self.name)
		frm['source'](
			label	= 'source text',
			type	= 'textarea',
		)
		frm['matches'](
			type	= 'markup',
			value	= '',
		)
		frm['check'](
			type	= 'submit',
			value	= 'check',
		)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		@see: L{modu.editable.define.definition.update_storable()}
		"""

