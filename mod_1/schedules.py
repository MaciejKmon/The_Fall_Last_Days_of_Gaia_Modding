# -*- coding: utf-8 -*-

#######################################################
###	current revison: Revision: 00 --> 00.00.0000	###
#######################################################

#######################################################
### imports											###
#######################################################
from global_defines import *
import npc_activities
import const
import character
# import global_schedules



schedules = {}

def init_schedules():
	global schedules
	
	schedules = {
	#######################################################################
	### EXAMPLE --> "DRILL_INSTRUCTOR" : (								###
	###				{													###
	###				S_CONDITION  : lambda: True,						###
	###				"00:00:00" : { 										###
	###					S_START  : [],									###
	###					S_LOOP   : []									###
	###					},												###
	###				},{													###
	###				"00:00:00" : { 										###
	###					S_START  : [],									###
	###					S_LOOP   : []									###
	###					},												###
	###				})													###
	#######################################################################
	
}
	# update with global schedules
	# schedules.update(global_schedules.update_schedules(schedules))


###########################################################################
### wrapper functions, do not modify!									###
###########################################################################

def Activity(id):
	return npc_activities.npc_activity(id, schedules)
	
def GetCurrentPlan(id):
	return npc_activities.npc_get_current_plan(id, schedules)
	
def Dialog(id, partymemberid):
	return npc_activities.npc_dialog(id, partymemberid, schedules)
