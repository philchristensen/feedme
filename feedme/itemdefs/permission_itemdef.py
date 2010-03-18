# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.editable import define
from modu.editable.datatypes import string, relational

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'permission',
		label			= 'permissions',
		category		= 'accounts',
		acl				= 'access admin',
		weight			= 2
	),
	
	id					= string.LabelField(
		label			= 'id:',
		size			= 10,
		weight			= -10,
		listing			= True
	),
	
	name			= string.StringField(
		label			= 'name:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True
	)
)
