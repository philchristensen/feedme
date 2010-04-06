# feedme
# Copyright (C) 2010 Phil Christensen <phil@bubblehouse.org>
#
# $Id$
#

from modu import editable
from modu.editable import define, util
from modu.editable.datatypes import string, relational, boolean

from feedme.util import checker

__itemdef__ = define.itemdef(
	__config			= dict(
		name				= 'feed',
		label				= 'feeds',
		category			= 'content',
		acl					= 'access admin',
		weight				= 0,
		prewrite_callback	= util.get_url_code_callback('title', 'url_code'),
	),
	
	id					= string.LabelField(
		label			= 'id:',
		size			= 10,
		weight			= -10,
		listing			= True
	),
	
	title				= string.StringField(
		label			= 'title:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True,
		link			= True,
	),
	
	url_code			= string.StringField(
		label			= 'url code:',
		size			= 60,
		maxlength 		= 255,
		weight			= 3,
		listing			= True,
	),
	
	description			= string.TextAreaField(
		label			= 'description:',
		weight			= 4,
	),
	
	active				= boolean.CheckboxField(
		label			= 'active:',
		default_checked	= True,
		weight			= 5,
	),
	
	origin_url			= string.StringField(
		label			= 'origin url:',
		size			= 60,
		maxlength 		= 255,
		weight			= 6,
	),
	
	item_match			= string.TextAreaField(
		label			= 'item match:',
		weight			= 7,
	),
	
	regex_check			= checker.RegexCheckerField(
		label			= 'check regex:',
		weight			= 7.5,
	),
	
	title_pattern		= string.StringField(
		label			= 'title pattern',
		weight			= 7.55,
	),
	
	date_pattern		= string.StringField(
		label			= 'date pattern in YYYY-MM-DD HH:MM format',
		weight			= 7.6,
	),
	
	link_pattern		= string.StringField(
		label			= 'main URL pattern',
		weight			= 7.7,
	),
	
	img_pattern			= string.StringField(
		label			= 'image URL pattern',
		weight			= 7.8,
	),
	
	body_pattern		= string.StringField(
		label			= 'item body pattern',
		weight			= 7.9,
	),
	
	user_link			= relational.ItemTitleField(
		column			= 'user_id',
		label			= 'user link:',
		flabel			= 'username',
		ftable			= 'user',
		listing			= True,
		weight			= 8,
	),
	
	user_id				= relational.ForeignSelectField(
		label			= 'user:',
		ftable			= 'user',
		flabel			= 'username',
		fvalue			= 'id',
		order_by		= 'username',
		weight			= 9,
	),
)
