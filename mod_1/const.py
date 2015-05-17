# -*- coding: utf-8 -*-

#######################################################
###	current revison: Revision: 00 --> 00.00.0000	###
#######################################################

#######################################################
### imports											###
#######################################################

from global_defines import data
# from global_defines import *

def init_data():
	
	###################################################
	### Switches                               	 	###
	### Example --> data().mein_toller_switch	 	###
	###################################################
	
	
	###################################################
	### Counter                               	 	###
	### Example --> data().mein_tollr_counter	 	###
	###################################################
	
	
	###################################################
	### Questbook                               	###
	### Example --> data().qb_001 = -1				###
	###################################################
	# TODO: --> Initiate Questbook pointer
	
	
	#######################################################################
	### Timer                               							###
	### Example --> data().timer_mein_toller_timer = 0					###
	#######################################################################
	
	
	#######################################################################
	### Timer                               							###
	### Example --> data().timervalue_mein_toller_timer = 60 * 1000		###
	#######################################################################
	
	
	#######################################################################
	### Region_Example = 0	                          					###
	### Example --> data().region_lucas	= "region_meine_tolle_rgion" 	###
	#######################################################################
	
	
	#######################################################################
	### Minimap Marker 													###
	### Example --> data().player_knows_meinen_tollen_marker = False 	###
	#######################################################################
	
	
	###############################################################################
	### Spawn-Animals / Animals / Pets											###
	### Example --> data().animals	= ["WOLF_S_LEAD","WOLF_S_1","WOLF_S_2"]		###
	###############################################################################
	# TODO: --> Fill list data().SpawnAnimals
	# TODO: --> Fill list data().animals
	# TODO: --> Fill list data().pets
	
	data().SpawnAnimals = []
	data().animals		= []
	data().pets			= []
	
	data().Timer_SpawnTimeChecker			= 666
	data().Timervalue_SpawnTimeChecker 		= 10 * 60 * 1000.0 #* hour_real_to_game
	data().SpawnAnimalsSpawned				= False
	
	
	
###################################################################################
###################################################################################
###################################################################################


#######################################################
### constanten										###
### Example -->	MEINE_TOLLE_VARIABLE				###
#######################################################

### Main Quest NPCs
### Example --> [CHAR_1, CHAR_2]
MAIN_QUEST_NPCS = []

### Immortal NPCs
### Example --> [CHAR_1, CHAR_2]
IMMORTAL_NPCS = []

### Foes NPCs ###
### Example --> [CHAR_1, CHAR_2]
FOES_NPCS 	=	[]

### Inventories ###
### Example -->	"ADRIAN": ["SET_MEAT_RAW_TINY", SET_MEAT_RAW_TINY]
### Example -->	"ADRIAN": [["SET_MEAT_RAW_TINY", 'SPECIAL_OBJECT_ID'], SET_MEAT_RAW_TINY]
INVENTORY	=	{}

### Main Quest Items ###
### Example --> [ITEM_1, ITEM_2]
QUESTITEMS 	=	[]

### Script use Objects ###
### Example --> [OBJECT_1, OBJECT_2]
#All objects that need special scripts or animations need to be marked at initialisation.
SCRIPT_USE_OBJECTS	=	[]

### Chests Safes ###
### Example --> {'normal':		[('SAFE_1', 'lock1')],
###				 'poison-trap':	[('SAFE_2', 'lock1'),
###								 ('SAFE_3', 'lock1')]}
CHESTS_SAFES	=	{'normal'		:	[],
					 'poison-trap'	:	[],
					 'lock-trap'	:	[],
					 'booby-trap'	:	[]}

### Herbs ###
### Example --> "'SET_ALOE_VERA'	: 	[(300, 300), 	# Vaters Grab
###										 (400, 400),	# am Eingang
###										 (200, 200)]"	# am Ausgang
HERBS		=	{'SET_ALOE_VERA'	: 	[],
				 'SET_WOOD_GARLIC'	:	[],
				 'SET_BURNET'		:	[],
				 'SET_ANGELICA'		:	[]
				 }

### Water Sorces
### Example --> (x, y, value) --> 
###				(300, 300, 4),	# am Friedhof
###				(400, 400, 1)	# wo anders
WATER_SORCE	=	[]

### fx Variablen ###
BARREL	 			= []
CAMPFIRE_SMALL		= []
CAMPFIRE_BIG 		= []
PILLAR_1			= []
PILLAR_2			= []
FLAMBEAU			= []
FIREBASING_SMALL	= []
FIREBASING_BIG		= []

### Beehive ###
### Example --> BIENENSTOCK = {'MZZONE_1_BUILDING_861': 2,
###							   'MZZONE_1_BUILDING_860': 6}
BIENENSTOCK = {}

### CAMERA_VIEWS ###
### Example --> CAM_VIEW_EXAMPLE = [ 232.1510, 188.2696, 8.8335, 0.3895, 0.8434, -0.3702 ]





