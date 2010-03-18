# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.editable import define
from modu.editable.datatypes import string, relational

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'role',
		label			= 'roles',
		category		= 'accounts',
		acl				= 'access admin',
		weight			= 1
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
	),
	
	permissions			= relational.ForeignMultipleSelectField(
		label			= 'permissions:',
		fvalue			= 'id',
		flabel			= 'name',
		ftable			= 'permission',
		ntof			= 'role_permission',
		ntof_f_id		= 'permission_id',
		ntof_n_id		= 'role_id'
	)
)
