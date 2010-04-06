# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu import assets
from modu.editable import define
from modu.util import form, tags

class RegexCheckerField(define.definition):
	"""
	Connects to JSON interface for checking regexes.
	"""
	def get_element(self, req, style, storable):
		"""
		@see: L{modu.editable.define.definition.get_element()}
		"""
		store = storable.get_store()
		
		assets.activate_jquery(req)
		req.content.report('header', tags.script(src=req.get_path('regex.js'))[''])
		
		frm = form.FormNode(self.name)(type='fieldset', style='full')
		frm['source'](
			label	= 'source text',
			type	= 'textarea',
		)
		frm['matches'](
			type	= 'markup',
			value	= tags.div(id="result-breakdown")[''],
		)
		frm['check'](
			type	= 'submit',
			value	= 'check',
			attributes = dict(
				id	= 'regex-check-button',
			)
		)
		frm['script'](
			type	= 'markup',
			value	= tags.script(type='text/javascript')["""
			$(document).ready(function(){
				$('#regex-check-button').click(function(){
					var url = $('#form-item-origin_url input').val();
					var pattern = $('#form-item-item_match textarea').val();
					testRegex(url, pattern);
					return false;
				});
			});
			"""],
		)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		@see: L{modu.editable.define.definition.update_storable()}
		"""

