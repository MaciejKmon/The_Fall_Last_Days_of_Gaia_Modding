# -*- coding: utf-8 -*-
from global_defines import *
from const import *
import dialog
import schedules

def on_approach(target, operator):
	if dialog.is_dialog_active():
		return
	
	if schedules.Dialog(target, operator):
		return
		
	if target == 'NPC_1':
		tutorial_dlg_1()
	

def tutorial_dlg_1():
	print "First dialog"
	
	""" Uncommment following lines to create your first dialog """
	dialog.init_dialog(type=DIALOGSMALL)
	dialog.add_text(text='Hi, do you have some meat?', speaker='NPC_1', follower='ENDDIALOG')
	dialog.start(False)
	
	
# 'Homework' 
def callback_tests():
	""" Move AE to Girl and faces her """
	objects.move_to_object('ALTER_EGO','NPC_1')
	# write both into stack
	objects.turn_to_object('ALTER_EGO','NPC_1', callback = callback_tests_dlg_2)
	# calls next function when finished turning
	
def callback_tests_dlg_2(character_id = None):
	""" Initiate dialog and play dance for girl when choice 1 is finished """
	dialog.init_dialog(DIALOGLARGE)
	dialog.add_choice('Hi, here is your meat.', speaker = 'ALTER_EGO', follower = 'ENDDIALOG', 
		callback = Lambda("characters.play_animation('NPC_1','CM_NPC_TANZEN_1')"))
	# Above the full play_animation command as string in Lambda assigned to the callback 
	dialog.add_choice('Bye.', speaker = 'ALTER_EGO', follower = 'ENDDIALOG')
	dialog.start(False)
	

