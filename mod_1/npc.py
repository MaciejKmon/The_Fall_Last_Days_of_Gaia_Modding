# -*- coding: utf-8 -*-

#######################################################
###	current revison: Revision: 00 --> 00.00.0000	###
#######################################################

#######################################################
### imports											###
#######################################################
from global_defines import *
import globaltext

# >>> id			-->  KEY	--> STR
# >>> gender		-->  0		--> STR
# >>> party			-->  1		--> STR
# >>> x				-->  2		--> FLOAT
# >>> y				-->  3		--> FLOAT
# >>> name			-->  4		--> globaltext.NAME_...
# >>> direction		-->  5		--> FLOAT
# >>> resourceui	-->  6		--> STR
# >>> faction		-->  7		--> STR
# >>> level			-->  8		--> INT
# >>> model			-->  9		--> STR
# >>> gender		--> 10		--> STR
# >>> skin			--> 11		--> STR
# >>> clothes		--> 12		--> STR
# >>> face			--> 13		--> STR
# >>> scale			--> 14		--> FLOAT
# >>> active		--> 15		--> choice --> ACTIVE / INACTIVE

# EXAMPLE
# male	-->		npcs = {'MALE':			['male', 'NPCS', 300.00, 300.00, globaltext.M_NAME_MALE, 180.00, '',
#										 'VILLAGE_PEOPLE', 1, 'low', 'male', 'white', 'ss_001', 'evil19', 0.00, ACTIVE]}
# femal			npcs = {'FEMALE':		['female', 'NPCS', 300.00, 300.00, globaltext.M_NAME_FEMALE, 180.00, '',
#										 'VILLAGE_PEOPLE', 1, 'low', 'female', 'white', 'ss_001', 'evil01', 0.00, ACTIVE]}
# child male	npcs = {'CHILD_MALE':	['male', 'NPCS', 300.00, 300.00, globaltext.M_NAME_CHILD_MALE, 180.00, '',
#										 'VILLAGE_PEOPLE', 1, 'child', 'male', 'white', 'll_001', '002', 0.00, ACTIVE]}
# child female	npcs = {'CHILD_FEMALE':	['female', 'NPCS', 300.00, 300.00, globaltext.M_NAME_CHILD_FEMALE, 180.00, '',
#										 'VILLAGE_PEOPLE', 1, 'child', 'female', 'white', 'll_001', '001', 0.00, ACTIVE]}

# TODO: --> Write dictionary for all npcs
npcs = {}
""" Uncommment following lines to create your first NPC """
npcs = {
	'NPC_1':	['female', 'NPCS', 300.00, 305.00, 'Lolitta aPFF', 180.00, '',
	 'VILLAGE_PEOPLE', 1, 'low', 'female', 'white', 'ss_001', 'evil01', 0.00, ACTIVE],

        'NPC_2':	['female', 'NPCS', 300.00, 310.00, 'Olilla', 180.00, '',
	 'VILLAGE_PEOPLE', 1, 'low', 'female', 'black', 'ss_002', 'evil01', 0.00, ACTIVE],
	}
	
def init_npcs():
	for npc in npcs.keys():
		system.create_character(
			id			= npc,
			gender		= npcs[npc][0],
			party		= npcs[npc][1],
			x			= npcs[npc][2],
			y			= npcs[npc][3],
			name		= npcs[npc][4],
			direction	= npcs[npc][5],
			resourceui	= npcs[npc][6])
		objects.set_attributes(npc,
			faction		= npcs[npc][7],
			level		= npcs[npc][8],
			model		= npcs[npc][9],
			gender		= npcs[npc][10],
			skin		= npcs[npc][11],
			clothes		= npcs[npc][12],
			face		= npcs[npc][13])
		character.update_appearance(npc)
		if not npcs[npc][14] == 0.00:
			character.scale(npc, npcs[npc][14])
		objects.set_active_state(npc, npcs[npc][15])

			
			
# >>> id		--> KEY		--> STR
# >>> type		--> 0		--> choice --> ANIMAL_ANTELOPE, ANIMAL_BEAR, ANIMAL_TIGER, ANIMAL_BISON, ANIMAL_DONKEY, ANIMAL_DEER, ANIMAL_COW, ANIMAL_HORSE, ANIMAL_LIZARD, ANIMAL_WARG, ANIMAL_WILDDOG, ANIMAL_WOLF, ANIMAL_PIG
# >>> party		--> 1		--> STR
# >>> x			--> 2		--> FLOAT
# >>> y			--> 3		--> FLOAT
# >>> direction	--> 4		--> FLOAT

        system.create_animal(id = 'ANIMAL_1', type = ANIMAL_WOLF, party = 'ANIMALS', x = 315.00, y = 300.00, direction=180)
	system.create_animal(id = 'ANIMAL_2', type = ANIMAL_WOLF, party = 'ANIMALS', x = 400.00, y = 300.00, direction=180)
	system.create_animal(id = 'ANIMAL_3', type = ANIMAL_TIGER, party = 'ANIMALS', x = 247.88, y = 316.68, direction=180)
	system.create_animal(id = 'ANIMAL_4', type = ANIMAL_TIGER, party = 'ANIMALS', x = 231.00, y = 100.00, direction=180)
	system.create_animal(id = 'ANIMAL_5', type = ANIMAL_WOLF, party = 'ANIMALS', x = 260.27, y = 317.55, direction=180)
	system.create_animal(id = 'ANIMAL_6', type = ANIMAL_TIGER, party = 'ANIMALS', x = 270.39, y = 311.34, direction=180)

	#### Enemies ####

	system.create_character(
		id="RATSKULL_V111",
		gender="female",
		party="RATSKULLS",
		x=341.21,
		y=243.85,
		direction=180,
                #name=globaltext.NAME_RATSKULL,
                name="Sara the puk",
		resourceui="")
	objects.set_attribute('RATSKULL_V111','foes',['UISPIELER'])
	objects.set_attribute("RATSKULL_V111","faction","RAT_SKULLS")
	objects.set_attribute("RATSKULL_V111","level", 3)
	objects.set_attributes("RATSKULL_V111",
		model="low",
		gender="female",
		skin="white",
		clothes="ratskull",
		face="sara")
	character.update_appearance("RATSKULL_V111")
	objects.create_item_in_inventory("RATSKULL_V111", ["SET_REMINGTON_M870","SET_AMMOPACK_2_12_MM","SET_AMMOPACK_2_12_MM"])
        character.equip("RATSKULL_V111","SET_REMINGTON_M870")
        
	system.create_character(
		id="RATSKULL_V122",
		gender="female",
		party="RATSKULLS",
		x=345.95,
		y=248.86,
		direction=260,
		name="Barbara ass",
		resourceui="")
	objects.set_attribute('RATSKULL_V122','foes',['UISPIELER'])
	objects.set_attribute("RATSKULL_V122","faction","RAT_SKULLS")
	objects.set_attribute("RATSKULL_V122","level", 3)
	objects.set_attributes("RATSKULL_V122",
		model="low",
		gender="female",
		skin="white",
		clothes="shadow_doctor",
		face="barbara")
	character.update_appearance("RATSKULL_V122")
	objects.create_item_in_inventory("RATSKULL_V122", ["SET_MICRO_UZI","SET_AMMOPACK_9_MM"])
        character.equip("RATSKULL_V122","SET_MICRO_UZI")

	#### ####
	system.create_character(
		id="RATSKULL_HUMMER_10",
		gender=MALE,
		party="RATSKULLS",
		x=345.65,
		y=238.22,
		name="Johne",
		direction = 90,
		resourceui="")
	objects.set_attribute('RATSKULL_HUMMER_10','foes',['UISPIELER'])
	objects.set_attribute("RATSKULL_HUMMER_10","faction","RAT_SKULLS")
	objects.set_attribute("RATSKULL_HUMMER_10","level", 2)
	objects.set_attributes("RATSKULL_HUMMER_10",
		gender=MALE,
		model="low",
		face="evil07",
		clothes="ratskull",
		skin="white")
	character.update_appearance("RATSKULL_HUMMER_10")
	objects.create_item_in_inventory("RATSKULL_HUMMER_10",["SET_SIMONOV_SKS","SET_AMMOPACK_7_62SOVJET_MM","SET_AMMOPACK_7_62SOVJET_MM"])
	character.equip("RATSKULL_HUMMER_10","SET_SIMONOV_SKS")
	objects.set_active_state("RATSKULL_HUMMER_10",ACTIVE)


# EXAMPLE
# animals = {'ANIMAL': [ANIMAL_WOLF, 'ANIMALS', 300.00, 300.00,  180.00]}

# TODO: --> Write dictionary including all animals and update lists in const (data().animals / data().SpawnAnimals / data().pets)
animals = {}

def init_animals():
	for animal in animals.keys():
		system.create_animal(id 		= animal,
							 type 		= animals[animal][0],
							 party 		= animals[animal][1],
							 x 			= animals[animal][2],
							 y 			= animals[animal][3],)
							 #direction 	= animals[animal][4])
	
	for animal in data().animals:
		objects.set_attribute(animal,"foes", ["UISPIELER"])
	
	for animal in data().SpawnAnimals:
		objects.set_attribute(animal,"foes", ["UISPIELER"])
		objects.set_active_state(animal,INACTIVE)

## Spawns Animals
# Wrapper function: don't modify!

def spawnAnimals(state):
	if (state == ACTIVE):
		if not data().SpawnAnimalsSpawned:
			for animal in data().SpawnAnimals:
				objects.set_active_state(animal,state)
			data().SpawnAnimalsSpawned = True
	else:
		if data().SpawnAnimalsSpawned:
			for animal in data().SpawnAnimals:
				if not objects.is_destroyed(animal):
					objects.set_active_state(animal,state)
		data().SpawnAnimalsSpawned = False
