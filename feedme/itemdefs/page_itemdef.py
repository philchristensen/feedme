# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'page',
		label			= 'pages',
		acl				= 'access admin',
		category		= 'site content',
		weight			= 1
	),
	
	id					= string.LabelField(
		label			= 'id:',
		weight			= -10,
		listing			= True
	),
	
	title				= string.StringField(
		label			= 'title:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True
	),
	
	url_code			= string.StringField(
		label			= 'url code:',
		size			= 40,
		maxlength 		= 255,
		help			= "the url code for this page's permalink",
		weight			= 3,
		listing			= True
	),
	
	data				= fck.FCKEditorField(
		label			= 'page body:',
		weight			= 4
	),
	
	active				= boolean.CheckboxField(
		label			= 'active:',
		weight			= 4
	)
)
