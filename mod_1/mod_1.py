# -*- coding: utf-8 -*-

#######################################################
###	current revison: Revision: 00 --> 00.00.0000	###
#######################################################

#######################################################
### imports											###
#######################################################
from global_defines import *
import const
import music
import skies
import sounds
import dialogs
import npc
import water
import object_events
import system_events
import enemy_script
import schedules
import character

def init_parties():
	system.create_party(id="NPCS",type=PT_COMPUTER)
	system.create_party(id="UISPIELER",type=PT_HUMAN)
	system.create_party(id="ANIMALS",type=PT_COMPUTER)
	system.create_party(id="RATSKULLS",type=PT_COMPUTER)
	# TODO: def init_parties() --> initiate partys

def get_zone_enter_location(enterdirection):
	# TODO: def get_zone_enter_location(enterdirection) --> enter starting location
	start_locations = \
		{	"NORTH":	(300.00, 300.00),
	 		"SOUTH":	(300.00, 300.00),
	 		"WEST":		(300.00, 300.00),
	 		"EAST":		(300.00, 300.00),
	 	}
	if (enterdirection in start_locations.keys()):
		return start_locations[enterdirection]
	else:
		raise ValueError, ("no spawn location for this direction registerd: " + enterdirection + "\n" 
						   "valid data = %s" %start_locations.keys())
						                                    
def on_end_music():
	music.get_next_song()
	return True

def on_init(sky = None, mission_time = None):
	sky = skies.get_sky_presets()
	skies.init_sky_preset(sky)
	#system.set_mission_time("12:00:00")
	# TODO: on_init() --> Set start time only for first map
	
	system_events.on_init()

def on_map_loaded():
	const.init_data()
	init_fx()
	init_object_anim()
	init_parties()
	#### ####
	# place player characters
	location = get_zone_enter_location( system.zone_transfer_get_direction() )
	system.zone_transfer_place_characters( location[0], location[1] )
	import debug; debug.cheat_party(party=False, x=location[0], y=location[1])
	
	npc.init_npcs()
	init_main_quest_npcs()
	#init_immortal_npcs()
	init_foes_npcs()
	npc.init_animals()
	
	print location
	#system.zone_transfer_place_characters( location[0], location[1] )
	#import debug; debug.cheat_party(party=False, x=location[0], y=location[1])
	init_exit_zones()
	init_equipment()
	init_items()
	init_quest_items()
	init_scriptuse_objects()
	init_herbs()
	init_bienen()
	set_water_source()
	init_regions()
	init_questbook()
	schedules.init_schedules()
	init_chests_safes()
	# TODO: def on_map_loaded() --> Add function/commands to execute at zone initialisation

	####I have uncommented it to create animal#####
	# uncomment following line to create the wolf
	
	
def on_map_reentry():
	init_fx()
	location = get_zone_enter_location( system.zone_transfer_get_direction() )
	system.zone_transfer_place_characters( location[0], location[1] )
	schedules.init_schedules()
	# TODO: def on_map_reentry() --> Add functions/commands for entering the zone again

def on_post_load():
	init_fx()
	schedules.init_schedules()
	# TODO: def on_post_load() --> Special commands to be executed on load of a game in this zone
	
	
def init_main_quest_npcs():
	# TODO: def init_main_quest_npcs() --> Update list const.MAIN_QUEST_NPCS
	for char in const.MAIN_QUEST_NPCS:
		character.set_main_quest_npc_state(char, True)

def init_immortal_npcs():
	# TODO: def init_immortal_npcs() --> Update list const.IMMORTAL_NPCS
	for char in const.IMMORTAL_NPCS:
		objects.set_immortal_state(char, True)

def init_foes_npcs():
	# TODO: def init_foes_npcs() --> Update list const.FOES_NPCS
	for foes_npc in const.FOES_NPCS:
		objects.set_attribute(foes_npc, 'foes', ['UISPIELER'])

def init_exit_zones():
	### Example -->	system.add_region( id = "REGION_EXIT_NORTH", x1 = 0.00, y1 = 0.00, x2 = 799.00, y2 = 209.3 )
	###				system.register_exit(regionname = "REGION_EXIT_NORTH" )
	# TODO: def init_exit_zones() --> initiate exit region
	pass

def init_equipment():
	## init all Equipment for NPCs and TA-NPCs
	# TODO: def init_equipment() --> update dictionary const.INVENTORY
	for char in const.INVENTORY.keys():
		for item in const.INVENTORY[char]:
			if isinstance(item, str):
				objects.create_item_in_inventory(object= char, equipment = item)
			elif isinstance(item, list):
				if len(item) == 2:
					objects.create_item_in_inventory(object= char, equipment = item[0], id = item[1])
			else:
				pass
				

def init_items():
        
	### init all Items
	### Example -->	object.create_item_in_inventory(	object="BUILDING_123",equipment=["SET_MEAT_RAW_TINY"])
	### Example -->	system.create_object(equipmenttype="SET_MEAT_RAW_TINY",x=320,y=526,direction=47)
	# TODO: def init_items() --> place items

	#Start Area
	
	system.create_object(equipmenttype="SET_AMMOPACK_50_AE_DUMDUM",x=320,y=301,direction=47)
        system.create_object(equipmenttype="SET_NORMAL_CLOTHES_4",x=320,y=301,direction=47)
	system.create_object(equipmenttype="SET_DESERT_EAGLE",x=320,y=301,direction=47)

	object.create_item_in_inventory(	object="E:.MODDING.MODS.TUTORIAL_MOD.MOD_1_BUILDING_249",equipment=["SET_MEAT_RAW_TINY"])
        object.create_item_in_inventory(	object="E:.MODDING.MODS.TUTORIAL_MOD.MOD_1_BUILDING_249",equipment=["SET_AMMOPACK_2_12_MM_QB_8"])
	object.create_item_in_inventory(	object="E:.MODDING.MODS.TUTORIAL_MOD.MOD_1_BUILDING_249",equipment=["SET_REMINGTON_M870"])

	#Ammo in case near tower
        object.create_item_in_inventory(	object="E:.MODDING.MODS.TUTORIAL_MOD.MOD_1_BUILDING_217",equipment=["SET_DESERT_EAGLE_W_LASERPOINTER", "SET_HK_USP_45"])

        object.create_item_in_inventory(	object="MOD_1_BUILDING_251",equipment=["SET_MP5"])

        #object.create_item_in_inventory(	object="E:.MODDING.MODS.TUTORIAL_MOD.MOD_1_BUILDING_",equipment=[""])
        
	pass

def init_quest_items():
	# TODO: def init_quest_items() --> Update list const.QUESTITEMS
	for item in const.QUESTITEMS:
		objects.set_attribute(item, "generic_item", False)

def init_scriptuse_objects():
	# TODO: def init_scriptuse_objects()' --> Update list const.SCRIPT_USE_OBJECTS
	for script_use_object in const.SCRIPT_USE_OBJECTS:
		system.mark_for_script_use(script_use_object)

def init_chests_safes():
	# TODO: def init_chests_safes()' --> Update dictionary const.CHESTS_SAFES
	for closure_type in const.CHESTS_SAFES.keys():
		for chest_safe in const.CHESTS_SAFES[closure_type]:
			objects.add_closed_lock(const.CHESTS_SAFES[closure_type][chest_safe][0], const.CHESTS_SAFES[closure_type][chest_safe][1], closure_type = closure_type)

def init_fx():
	# TODO: def init_fx() --> Update list const.BARREL
	for barrel in const.BARREL:
		init_fx_burning_barrel(barrel)

	# TODO: def init_fx() --> Update list const.CAMPFIRE_SMALL
	for campfire_small in const.CAMPFIRE_SMALL:
		init_fx_campfire_small(campfire_small)

	# TODO: def init_fx() --> Update list const.CAMPFIRE_BIG
	for campfire_big in const.CAMPFIRE_BIG:
		init_fx_campfire_big(campfire_big)

	# TODO: def init_fx() --> Update list const.PILLAR_1
	for pillar_1 in const.PILLAR_1:
		init_fx_pillar_1(pillar_1)

	# TODO: def init_fx() --> Update list const.PILLAR_2
	for pillar_2 in const.PILLAR_2:
		init_fx_pillar_2(pillar_2)

	# TODO: def init_fx() --> Update list const.FLAMBEAU
	for flambeau in const.FLAMBEAU:
		init_fx_flambeau(flambeau)

	# TODO: def init_fx() --> Update list const.FIREBASING_SMALL
	for firebasing_small in const.FIREBASING_SMALL:
		init_fx_firebasing_small(firebasing_small)

	# TODO: def init_fx() --> Update list const.FIREBASING_BIG
	for firebasing_big in const.FIREBASING_BIG:
		init_fx_firebasing_big(firebasing_big)

def init_fx_burning_barrel(barrel):
	system.start_effect_object(object=barrel, node="sort1", parameter = fx_fire_brennende_tonne)
	sounds.play_3d_sound_object(sfx_id="campfire_small", object=barrel,loop=True)

def init_fx_campfire_small(campfire_small):
	system.start_effect_object(object=campfire_small, node="effekt_feuer", parameter=fx_fire_lagerfeuer)
	sounds.play_3d_sound_object(sfx_id="campfire_big", object=campfire_small, loop=True)
	
def init_fx_campfire_big(campfire_big):
	system.start_effect_object(object=campfire_big, node="effekt_feuer", parameter=fx_fire_lagerfeuer)
	system.start_effect_object(object=campfire_big, node="effekt_feuer01", parameter=fx_fire_lagerfeuer_01)
	system.start_effect_object(object=campfire_big, node="effekt_feuer02", parameter=fx_fire_lagerfeuer_02)
	system.start_effect_object(object=campfire_big, node="effekt_feuer03", parameter=fx_fire_lagerfeuer_03)
	system.start_effect_object(object=campfire_big, node="effekt_feuer04", parameter=fx_fire_lagerfeuer_04)
	sounds.play_3d_sound_object(sfx_id="campfire_big", object=campfire_big, loop=True)

def init_fx_pillar_1(pillar_1):
	system.start_effect_object(object = pillar_1, node="dmyp_fire", parameter=fx_fire_pilar_1)
	sounds.play_3d_sound_object(sfx_id="campfire_small", object=pillar_1, loop=True)
	
def init_fx_pillar_2(pillar_2):
	system.start_effect_object(object = pillar_2, node="dmyp_fire0", parameter=fx_fire_pilar_2)
	system.start_effect_object(object = pillar_2, node="dmyp_fire1", parameter=fx_fire_pilar_2)
	system.start_effect_object(object = pillar_2, node="dmyp_fire2", parameter=fx_fire_pilar_2)
	system.start_effect_object(object = pillar_2, node="dmyp_fire3", parameter=fx_fire_pilar_2)
	sounds.play_3d_sound_object(sfx_id="campfire_small", object=pillar_2, loop=True)
	
def init_fx_flambeau(flambeau):
	system.start_effect_object(object = flambeau , node="dmyp_fire", parameter=fx_fire_pilar_2)
	sounds.play_3d_sound_object(sfx_id="campfire_small", object=flambeau, loop=True)
	
def init_fx_firebasing_small(firebasing_small):
	system.start_effect_object(object=firebasing_small, node="dmyp_fire", parameter=fx_fire_basin_small)
	sounds.play_3d_sound_object(sfx_id="campfire_small", object=firebasing_small, loop=True)

def init_fx_firebasing_big(firebasing_big):
	system.start_effect_object(object=firebasing_big, node="dmyp_fire0", parameter=fx_fire_big)
	sounds.play_3d_sound_object(sfx_id="campfire_big",object=firebasing_big,loop=True)

def init_object_anim():
	# TODO: def init_object_anim() --> initiate object animation
	pass

def init_herbs():
	for herbs in const.HERBS.keys():
		for pos in const.HERBS[herbs]:
			system.create_object(equipmenttype = herbs, x = pos[0], y = pos[1])
	# TODO: def init_herbs() --> Update dictionary const.HERBS
	
def init_bienen():
	for stock in const.BIENENSTOCK.keys():
		objects.create_item_in_inventory(stock, ['SET_BEESWAX']*const.BIENENSTOCK[stock])
	# TODO: def init_bienen() --> Update dictionary const.BIENENSTOCK
	
def set_water_source():
	for water_sorce in const.WATER_SORCE:
		water.set_water_source(water_sorce[1], water_sorce[1], water_sorce[2])
	# TODO: def set_water_source() --> Update list const.WATER_SORCE
	
def init_regions():
	### Example --> system.add_region("MEINE_TOLLE_REGION", 300, 300, 400, 400)
	###				system.notify_region_entered(region="MEINE_TOLLE_REGION", partyid="UISPIELER", permanent=True)
	pass
	
def init_questbook():
	### Example --> data().qb_001 = system.register_qb_entry('ZONE9_AIM_01')
	# TODO: def init_questbook() --> Initiate Questbook
	pass
	
	
def on_enter_region(id, objectid, partyid):
	pass

def can_use( character_id, object_id ):
        #### Modified  ####
	"""Returns True for items the character is able to use."""
	# uncomment following lines to make wolf usuable
	if character_id in system.get_pcs() and object_id == 'ANIMAL_1':
                #system.get_pcs() gives a list of all pcs 
		return True #allows action (on_use is started)
	
	return object_events.can_use( character_id, object_id )


def pre_use( character_id, object_id, item_id, item_type ):
	"""Is called directly before a char uses an item on an object."""
	
	object_events.pre_use( character_id, object_id, item_id, item_type )


def on_use(character_id, object_id, item_id, item_type):
        #### Modified  ####
	"""Is called when the player wants to use an item."""
	# uncommment following lines to get meat from wolf
	if object_id == 'ANIMAL_1':
		objects.create_item_in_inventory('ALTER_EGO','SET_MEAT_RAW')
                dialogs.callback_tests()
		return True #stop here, cause event is handled
		
	# for homework add following line before 'return  #stop here, cause event is handled'
	#	dialogs.callback_tests()
	
	# TODO: def on_use( character_id, object_id ) --> functions for special items/objects:on_use
	return object_events.on_use(character_id, object_id, item_id, item_type)
 

def on_use_failed( character_id, object_id, item_id, item_type ):	
	"""Is called when on_use returned False for this item."""
	
	return object_events.on_use_failed( character_id, object_id, item_id, item_type )


def can_exchange( character_id, target_id, item_id, item_type ):
	"""Return True if the item can be given from character to target."""
	# TODO: def can_exchange( character_id, target_id, item_id, item_type ) --> functions for special items/objects:can_exchange
	return object_events.can_exchange( character_id, target_id, item_id, item_type )


def on_exchange( character_id, target_id, item_id, item_type ):
	"""Is called when the item should be transfered from character to target."""
	# TODO: def on_exchange( character_id, target_id, item_id, item_type ) --> functions for special items/objects:on_exchange
	return object_events.on_exchange( character_id, target_id, item_id, item_type )


def can_examine_object( character_id, object_id ):
	"""Returns True if the object can be examined."""
	# TODO: def can_examine_object( character_id, object_id ) --> functions for special items/objects:can_examine
	return object_events.can_examine_object( character_id, object_id )


def pre_examine_object( character_id, object_id ):
	"""Is called before the char starts to examine a object."""
	object_events.pre_examine_object( character_id, object_id )


def on_examine_object( character_id, object_id ):
	"""Called if an item is examined by a character."""
	# TODO: def on_examine_object( character_id, object_id ) --> functions for special items/objects:on_examine
	object_events.on_examine_object( character_id, object_id )


def can_gut_object( character_id, object_id ):
	"""Returns True if the object can be gutted."""
	
	return object_events.can_gut_object( character_id, object_id )


def pre_gut_object( character_id ):
	"""Called before a object is gutted."""
	
	object_events.pre_gut_object( character_id )


def post_gut_object( character_id, object_id = None ):
	"""Called after a object is gutted."""
	
	object_events.post_gut_object( character_id, object_id = None )


def on_gut_object( character_id, object_id ):
	"""Called if an item is gutted by a character."""
	
	object_events.on_gut_object( character_id, object_id )


def on_approach( target, operator ):
	"""Is called when a player char talks to another char or object."""
	if not object_events.on_approach(target, operator):
		dialogs.on_approach(target, operator)
                        

def can_steal_from( thief, victim ):
	"""Returns True if the thief can steal from the victim."""
	# TODO: def can_steal_from( thief, victim ) --> block stealing for special chars
	return object_events.can_steal_from( thief, victim )


def on_steal(target, operator):
	"""Is called when a player char tries to steal something."""
	object_events.on_steal(target, operator)


def on_object_killed(victim, attacker, weapon_type, weapon_id, victims_party):
	"""Called when an object gets killed/destroyed."""
	# TODO: def on_object_killed(victim, attacker, weapon_type, weapon_id, victims_party) --> Actions on kills
	object_events.on_object_killed(victim, attacker, weapon_type, weapon_id, victims_party)


def on_grid_enter( object_id, grid_id, old_grid_id, force_pc = False ):
	"""Called if an object enters a grid."""
	
	object_events.on_grid_enter( object_id, grid_id, old_grid_id, force_pc = False )


def on_enemy_spotted( object_id ):
	"""Called if the player chars spot an enemy and no enemy has been visible yet."""
	# TODO: def on_enemy_spotted( object_id ) --> Actions on enemy spotted
	object_events.on_enemy_spotted( object_id )


def on_sector_cleared( object_id ):
	"""Called if enemies have been visible and are now gone."""
	
	object_events.on_sector_cleared( object_id )


def on_corpse_spotted( object_id ):
	"""Called if the player chars spot a corpse and no corpse has been visible yet."""
	
	object_events.on_corpse_spotted( object_id )


def on_attack( operator_id, target_id ):
	"""Called when an object is attacked."""
	####  ####
	""" Uncommment following lines to activate selfdefence for the wolf """
	if target_id == 'ANIMAL_1':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return
		# stops function, don't call global for this target_id

	if target_id == 'ANIMAL_1':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return

	if target_id == 'ANIMAL_2':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return
	
	if target_id == 'ANIMAL_3':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return
	
	if target_id == 'ANIMAL_4':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return
	
	if target_id == 'ANIMAL_5':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return

	if target_id == 'ANIMAL_6':
                #  If someone attacks ANIMAL_1 do
		objects.set_attribute('ANIMAL_1','foes',['UISPIELER'])
		return
		
	object_events.on_attack( operator_id, target_id )


def can_pick_up(character_id, item_id):
	"""Returns True if the char can pick up the item."""
	
	return object_events.can_pick_up(character_id, item_id)


def on_pick_up( character_id, item_id, item_type ):
	"""Called when an item is picked up."""
	
	return object_events.on_pick_up( character_id, item_id, item_type )


def pre_pick_up(character_id, item_id):
	"""Called when an item is picked up."""
	
	return object_events.pre_pick_up(character_id, item_id)


def can_put_down( character_id, item_id, item_type, x, y, grid_identifier ):
	"""Tests if the given item can be put down by the char."""
	
	return object_events.can_put_down( character_id, item_id, item_type, x, y, grid_identifier )


def on_put_down( character_id, item_id, item_type ):
	"""Called if an item is put down."""
	
	object_events.on_put_down( character_id, item_id, item_type )


def on_wait_for_commando(id):
	"""Is called whenever a char has "nothing to do" i.e. he would play a wait animation."""
	# TODO: def on_wait_for_commando(id) --> Place for special behavior, but try to do it in schedules
	return schedules.Activity(id)


def can_crack_lock( character_id, object_id, dummy ):
	"""Checks if the char is able to crack a lock."""
	
	return object_events.can_crack_lock( character_id, object_id, dummy )


def on_crack_lock(character_id, object_id, dummy_name, x, y, z ):
	"""Equips the char with the right utilities, moves the char to the lock and starts the crack animations."""
	
	object_events.on_crack_lock(character_id, object_id, dummy_name, x, y, z )


def post_crack_lock( character_id, destroy_picklock_chance, object_id ):
	"""Called after a chars tried to crack a lock."""
	
	object_events.post_crack_lock( character_id, destroy_picklock_chance, object_id )


def can_blast_lock( character_id, object_id, dummy ):
	"""Checks if the char is able to blast a lock."""
	
	return object_events.can_blast_lock( character_id, object_id, dummy )


def on_blast_lock( character_id, object_id, dummy_name, x, y, z ):
	"""Is called when the char blasts a lock open."""
	
	return object_events.on_blast_lock( character_id, object_id, dummy_name, x, y, z )


def can_enter_building( character_id, building_id ):
	"""Called if the user clicks to enter a building."""
	
	return object_events.can_enter_building( character_id, building_id )


def on_map_exit(next_zone):
	"""Is called when the player leaves a zone (usully via travel map)."""
	# TODO: def on_map_exit(next_zone) --> Actions on leaving zone
	system_events.on_map_exit(next_zone)


def can_leave_zone_context_menu():
	"""Returns True if the "leave zone" context menu entry should be active."""
	# TODO: def can_leave_zone_context_menu() --> When is player allowed to leave zone?(context Menu)
	return True


def on_leave_zone_context_menu():
	"""Is called when the "leave zone" context menu entry is used."""
	# TODO: def on_leave_zone_context_menu()--> Actions on leaving zone via contrxt menu
	system_events.on_leave_zone_context_menu()


def can_leave_zone():
	"""Returns True if the player chars can leave the zone."""
	# TODO: def can_leave_zone() --> When is player allowed to leave zone?
	return True


def leave_zone():
	# TODO: def leave_zone() --> Actions on leaving zone
	system_events.leave_zone()


def on_timer(id):
	"""Is called when a global timer fires."""
	pass

def tutorial_animation():
	character.play_animation('ALTER_EGO', 'CM_NPC_STEHEN_LIEGESTUETZE_START') 
	character.play_animation('ALTER_EGO', 'CM_NPC_STEHEN_LIEGESTUETZE_LOOP') 
	haracter.play_animation('ALTER_EGO', 'CM_NPC_STEHEN_LIEGESTUETZE_ENDE')
	print "finished tutorial animation"
	
def play_dialog(character_id = None):
	dialogs.tutorial_dlg_1()
