# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu.editable import define
from modu.editable.datatypes import string, relational

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'user',
		label			= 'users',
		category		= 'accounts',
		acl				= 'access admin',
		weight			= 0
	),
	
	id					= string.LabelField(
		label			= 'id:',
		size			= 10,
		weight			= -10,
		listing			= True
	),
	
	username			= string.StringField(
		label			= 'username:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True
	),
	
	first				= string.StringField(
		label			= 'first:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True
	),
	
	last				= string.StringField(
		label			= 'last:',
		size			= 60,
		maxlength 		= 255,
		weight			= 3,
		listing			= True
	),
	
	crypt				= string.PasswordField(
		label			= 'password:',
		size			= 60,
		maxlength 		= 255,
		weight			= 4
	),
	
	roles				= relational.ForeignMultipleSelectField(
		label			= 'roles:',
		fvalue			= 'id',
		flabel			= 'name',
		ftable			= 'role',
		ntof			= 'user_role',
		ntof_f_id		= 'role_id',
		ntof_n_id		= 'user_id'
	)
)
