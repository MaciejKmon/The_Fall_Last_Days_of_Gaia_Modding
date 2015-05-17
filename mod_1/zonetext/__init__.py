#----------------------------------------------------------------------------
# Name:         __init__.py
# Purpose:      The presence of this file turns this directory into a
#               Python package.
#----------------------------------------------------------------------------

import system
# select language resources
if system.get_language() == "German":
	from german import *
else:
	from english import *
