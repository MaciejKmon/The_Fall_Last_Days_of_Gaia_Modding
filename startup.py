# -*- coding: utf-8 -*-

from global_defines import *
import skies
import object_events

# for display in the options menu
mod_name = "tutorial"
print"!!!!mod imported"
# globals for event relinking examples
event_on_equip = None

# mod_init is called at startup of the game and on resets of the python 
# interpreter

def mod_init():
	# print something to console and log file, just to see this works correctly
	print "mod_init tutorial"
	
	# sets this zone as campain start
	import global_defines
	#global_defines.ENTRY_ZONE = "tutorial_mod\\mod_1\\mod_1"
	# the inderect import is needed to change the variable
	
	# activate zone on map
	#set_zone_enabled(zone='mod_1', enabled=True)
	#set_zone_enabled(zone='zone_1', enabled=True)
	# defines a sky
	skies.skies['tutorial_mod.mod_1.mod_1'] = 'yellow'
	
	# adds coordinates for the travel map
	system.zones_list['mod_1'] = ("tutorial_mod\\mod_1\\mod_1", [505.00, 477.00])
	
	# sets texts for travel map
	import text
	text.add_global_text(id='ZONE_NAME_MOD_1',  text="""Tutorial Mod""")
	text.add_global_text(id='ZONE_NAME_MOD_1_EXTENDED',  text="""Tutorial Mod – Under Construction""")
	
	# allow direct text entries in dialog declarations
	import debug
	debug.cheat("disable_textid_exception")
	
	###########################################################################
	### Examples for relinking events                                       ###
	###########################################################################
	# overwrite the pointer
	object_events.pre_use = pre_use
	
	# register a new pointer(and overwrite if exists)
	import sys
	sys.modules["object_events"].on_hit = on_hit
	
	#insert code into function(it's more like: executing code before the old function)
	global event_on_equip
	event_on_equip = object_events.on_equip
	object_events.on_equip = on_equip
	
	
def pre_use( character_id, object_id, item_id, item_type ):
	print "mod.pre_use"
	
def on_hit( object_id ):
	print "mod.on_hit"
	
def on_equip(objectid, itemtype, itemid):
	print "mod.on_equip"
	
	event_on_equip(objectid, itemtype, itemid)
