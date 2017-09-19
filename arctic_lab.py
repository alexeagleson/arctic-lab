#!/usr/bin/python
#
# libtcod python tutorial
#

# arctic-lab-testing@hotmail.com
# testing123

# https://alexeagleson.wixsite.com/thething


# V.0003
# Added A Star pathfinding

# V.0004
# Removed all level up and magic spell mechanics

# V.0005
# Changed font and organized the main panel

# V.0006
# Player moves randomly now, no control.

# V.0007
# Removed all code except basic functions.  Roughly 50% size of V0006

# V.0008
# Added food and a tendency to walk toward it

# V.0009
# Player automatically walks to find food anywhere on the map

# V.0010
# Player runs around the map eating food.  Food is consumed and reduces hunger.  Dies when hunger reaches 100 percent

# V.0011
# Added pause button, console window outlines and clickable objects in FOV

# V.0012
# Added more players moving about the dungeon (wangos)

# V.0013
# Added player movement control and the ability to pick items up by clicking

# V.0014
# Units now look for the nearest object -- death works better.

# V.0015
# Improved the functionality of the menu function

# V.0016
# Reverted game to turn based

# V.0017
# Ability to give items and items drop on the floor when object killed

# V.0020
# The Thing can be killed, can be cured with medicine.  Game is now techniclaly playable.

# V.0021
# Added the ability to grab and move objects

# V.0022
# Throwing works!

# V.0023
# Basics of room types created

# V.0024
# Object groups and design work well now -- basic structure is in place for creating prototypes

# V.0025
# Switching object groups to grid -- in progress

# V.0026
# Drawn grids of object groups implemented

# V.0027
# objects groups can be spawned against walls

# V.0028
# added a trakcer for the map to check for objects specificlaly on x,y tile for efficiency

# V.0030
# Redesigned the wal blocking and object collisions happen - much more smooth now.  Size affects everything.

# V.0031
# Added object weights and factored them into grabbing and throwing

# V.0032
# Added information panel for objects on right side
# Added functionality for throwing that randomizes chance of collision_object

# V.0033
# Added door functionality

# V.0034
# Improved how hallways are generated

# V.0036
# map generation works better... i think

# V.0037
# added doors to rooms

# V.0038
# Fixed FOV and added profile pics

# V.0039
# Added guns

# V.0040
# added fire oh my god fire is so cool

# V.0041
# Good, but still need to fix the placement of group objects

# V.0042
# Smplified the object design function

# V.0043
# Added inventory and components being thrown when destroyed, also added object descriptions to side panel

# V.0044
# Finally fixed placement of object groups -- works really well now

# V.0045
# Object projectile velocity has been implemented (with destroyable oil barrels!)

# V.0046
# Improved collision interaction

# V.0050
# Added outdoor snow and also the whole friggin building burns down

# V.0051
# FIRE EVERYWHERE

# V.0051
# Added hotkeys for grabbing, opening doors and picking items up.

# V.0052
# Basic improvements

# V.0054
# MAde game played in real time instead of turn based

# V.0055
# The Thing can now split in two

# V.0056
# The thing can now attack it's way through objects

# V.0058
# Fixed throw/gun accuracy

# V.0059
# Made all walls objects

# V.0060
# Improved the "nearest unit" function -- now moves to the next nearest if the nearest one is unreachable

# V.0061
# Made turn based again

# V.0063
# Added object units have feeligns for one another - scale of 0 - 10.  at 0 will attack and accuse of being the thing

# V.0064
# Added message window frame

# V.0065
# Made messages into a class

# V.0066
# Can click on messages to see objects

# V.0067
# Begnning workings of dealing with object quantities

# V.0068
# Object quantities work better.  Rendering works better.

# V.0069
# Added dialogue prompts with yes/no answers

# V.0070
# Units can now be assigned task to go and fetch an item and bring it to you

# V.0071
# Objects will now tell you what is in their way when they are trying to do a task

# V.0072
# Can now give specific tasks to NPCs with the speak command

# V.0073
# specific requests of NPCs  now work better

# V.0074
# Fixed error in astar pathing

# V.0075
# Fixed fire burning and added more info to object info panel

# V.0076
# Improved the usefulness of the fetch tasks -- more context specific

# V.0077
# Added highlighting menu options and optional ID tags for objects

# V.0080
# Fixed tasks and now prompts for how many objects when giving tasks

# V.0081
# Objects will now wait 20 turns then try a task again

# V.0082
# placing objects now checks for collisions

# V.0083
# Hotkeys are context sensitive - wont prompt with one item nearby

# V.0084
# Improved ID's and added x,y coordinates to object menus

# V.0085
# throwing and collisions work better

# V.0086
# Units now are starting to task themselves with various things

# V.0087
# units now task to move between rooms -- wait a certain amout of time between tasks.  movement looks very natural and organic now

# V.0089
# Added exterior doors and made the rendering better outside

# V.0090
# The thing now absorbs people

# V.0091
# Improved variables for factoring in throwing and lifting

# V.0092
# added head, torso, arms and legs

# V.0093
# major improvement to projectile damage calculations

# V.0094
# Major improvements to collision and destruction

# V.0095
# Really good tweaking of collision messages and damage and accuracy

# V.0096
# Added a total turn limit on tasks

# V.0097
# Added a rocket launcher, and now energy from destruction of object is transferred into its tossing of its contents

# V.0098
# Major update to change how projectiles work - they are now a class that queues movement so they all move simultaneously

# V.0099
# Added some basic timing of functions to track efficiency

# V.0100
# added more timing functions

# V.0101
# Added swapping positions task, but doesnt go back to original one

# V.0102
# Added a queue system for tasks

# V.0103
# fixed big glitch with paths that dont delete and bad pointers

# V.0104
# Units now ask nicely to passand  and SLowed game turn rate and made so you cant move during projetiles

# V.0105
# fixing dialogue loading times nd menus -- work in progress

# V.0106-
# Added big text boxes -- Improved message colour scheme

# V.0107
# Improved dialogue and main game screen has a basic game description

# V.0108
# ask people about tehmselves

# V.0110
# Added HEAR ALL and SHOW ALL and fixed FOV

# V.0111
# Added Ishi's new scientist characters.  Some unique character flavour with 10 different dialogue options and brief character descriptions visible in game.

# V.0112
# Added the ability to scroll the message window up and down.

# V.0113
# Added lock and key functionality -- can create objects that are locked, and keys that specifically work on the objects you create.

# V.0114
# Now shows a message when an object is added to inventory
# Random objects can no longer be placed to block paths (still seems to happen on occasion, but less often.  Need to improve further).

# V.0115
# Can now grab a stack of objects, and throw them one at a time.  Pew pew pew.

# V.0116
# Fixed glitch where game would hang and crash on big explosions

# V.0117
# Quality of life improvements:
# context sensitive hotkeys for grab/add to inventory -- will no longer ask if you want to add an item to inventory you can't lift.  
# Can no longer add units (people and dogs) to your inventory... sorry

# V.0118
# Oh shit everything went wrong -- reverting to 0117

# V.0119
# Huge efficinecy gains -- everything runs faster now.  
# Explosions and projectiles run about 5x faster.  The reason is that NPCs now only look for tasks within their field of vision, rather than sorting and categorizing every single object withing X number of tiles.  
# This also has the bonus effect where NPCs will not suddenly get interested in an object on the other side of the wall.  They only go looking for objects they can actually see.

# V.0120
# Added the 'Examine' function.  When used, it has a % chance of revealing The Thing.  Using it lowers your relationship value with whoever you are creeping on

# V.0121
# NPCs now go around examining one another, building suspicion, lower relationship levels, and changing base dialogue to negative dialogue over time.  They will also reveal The Thing for you.

# V.0122
# The Thing will now act exactly as a normal NPC until it identifies a target who is completely alone, and then will choose to attack them when no one is watching.  
# It will constantly check while chasing a target whether other units are around, and change its plan if so (it will flee to another room if too many units are nearby)

# V.0123
# Big update in progress... backup save.

# V.0124
# Still going -- computer crashed hard and actually corrupted the file... havn't seen that happen in awhile

# V.0125
# Backup save in the middle of this mess...

# V.0126
# Two major updates, as well as a lot of general code cleanup:
# The Thing can now re-assimilate into its original form.  It will do so if it can manage to hide out of view of any NPCs.  Each turn hidden the is a % chance of reassimilation.
# There is now a feature where units can try to "manoeuvre" past objects that would otherwise block them.  Chance of success depends on size, possible to fail miserabley and lsoe turn.  NPCs use it as well.
# This "manoeuvre" movement has replaced the previous "ask permission to pass" NPCs would use.  Now they just squeeze by one another in hallways without making eye contact.  So it's more realistic now.

# V.0127
# Dogs can no longer open doors

# V.0128
# Combined two separate functions that serve the same purpose into one
# Previously the action of making a decision of how to move, and the function that calculates the difficulty of the move for the A* pathfinder were separate functions.
# Even though they performed the same task, they would output different results (one would be an action, the other the difficulty of that action).  I was having to duplicate every new action option that was created.
# They are now combined together and the function calling them specifies if they want to return the difficulty of the move, or perform the move itself.

# V.0129
# Fixed bug where units would stop taking turns if you grabbed and dragged them.

# V.0130
# Improved random placement of object groups so that it doesn't block paths for humanoid sized objects

# V.0131
# Major update to how object groups can be created.
# -- Can spawn random sized stacks of objects
# -- Can spawn objects with randomized inventories of chosen objects
# -- Can spawn objects that can be randomly locked

# V.0132
# Added more simple room designs - Lunch Room, Rec Room & Armoury.  Key to the lockers in the Armoury is in cabinet in MacReady's room.

# V.0133
# Added hotkeys for lock/unlock, and pick up object now context sensitive to take objects from inventory (like out of lockers as example, rather than picking up the locker itself)
# Also added a game end prompt where if The Thing is killed, the game ends and it asks if you would like to continue or not.

# V.0134
# Improved the way object groups are created and placed.  Less overlap and easier to create unique randomized objects, such as lockers with items inside them.

# V.0135
# Dramatically improved projectile rendering speed by not rendering the entire screen every move tick, just the object itself.  
# It's actually TOO fast now.  Will likely need to slow it down intentiaonally to show movement properly.

# V.0136
# Objects units can now only carry around a total weight equal to their own body weight.  This includes objects with other objects inside them, for example a filing cabinet with a computer inside might me too much to 
# pick up, but the cabinet itself would not be.

# V.0137
# Added some free open source music & sound effects.

# V.0138
# Sound effects are now only audible within the player's field of vision.

# V.0139
# Fixed weight calculation when picking up stacks of objects

# V.0140
# Added toggles for "show full map", and "hear all messages" on the title screen.
# Improved the decision making for The Thing -- previously once it decided it would attack, it would not stop even if more scientists entered the room.
# Now, at the last second when going to attack, it can change its mind if more witnesses are present and continue staying in disguise.

# V.0141
# First binary .exe build of the game completed using py2exe!  Testing and works on another machine.

# V.0142
# The 'escape key' now quits the current session and returns to the main menu rather than closing the game
# Can now start a fresh new game without closing the application and rebooting
# Trying to "consume" an object no longer crashes the game
# Trying to speak to an inanimate object no longer crashes the game
# Converted WAV music to OGG to dramatically reduce binary build size

# V.0142
# Added explored territory feature -- places you have been stay visible, but darker outside your FOV
# Objects show their last known locations -- it's posisble for an item to stil appear on your screen after it's been destroyed.  Only returning to the room 
# and putting the object into your field of vision again will update the visual state.
# Unit NPCs will not appear at all once they are outside your FOV -- too confusing to show their last known location since they are always moving.
# Menu's will no longer exit if you click outside of the option text -- to cancel a menu now press right mouse button

# v0.14.3
# Fixed: pressing right click to close menu no longer selects the top option
# Fixed: units could not path through doorways with obstacles in them (would repeatedly open/close the door)
# Decided MacReady's a big fan of BTO.

# v0.14.4
# In-progress major overhaul to the lighting system

# v0.14.5
# Major overhaul to the lighting system -- now allows separate light sources with their own FOV's (lamps for examaple)
# Previously tiles were 'illumnated' if they were within the player's FOV.  Now tiles are flagged as illuminated based on all light sources, and only 'render' as illuminated if in player's FOV.  
# Player now has a 20 tile "vision" radius and an 8 tile natural light source radius.  Player can see a tile 20 tiles away if it's illuminated by an external source, but if there is none, will only be able to see 8 tiles away.
# Biggest challenge was that tiles now had to be overhauled from previously having only an 'illuminated / not illuminated' state, to now keeping track of which of the four cardinal directions are illuminated.
# What was happening when this feature was introduced, was that external light sources outside were illuminating the exterior wall, and the player could see them lit up when inside the room (which doesn't make sense).
# Now the external light, if on the north side of the building, will only illuminate the north side of the wall, and the player inside will not see it as illuminated because he / she is looking at the south side.

# v0.14.6
# Added on/off functionality for objects -- can assign functions to objects like light on/off as example
# Added a flashlight that you can pick up with a higher FOV radius that the player's default

# v0.14.7
# Added a radio with music
# Added 'main power' function with generator that controls all lamps in the facility

# v0.14.8
# Added hotkeys for activate/deactivate objects
# Improved the context sensitive object selection with hotkeys

# v0.14.9
# Main generator now properly controls all lamps, as well as the radio
# Objects that were off before shutting down main power will stay off, objects that were on will turn back on

# v0.15.0
# Added info to object descriptions to show their state (items with locks will show (Locked) or (Unlocked), lamps will show (On) / (Off) etc.

# v0.15.1
# Can now attack by clicking the right mouse button
# Radio functions more like a radio -- music still plays when radio is off, and will resume at a later time in the song when turned back on
# Main power being shut off now dramatically reduces the player's natrual light radius -- encouraging the use of flashlights

# v0.15.2
# Implemented directional lighting - flashlights now shine a directional beam that moves with the direction you move when you are carrying it
# New 'X' hotkey will lock your movement, so that you can shine the flashlight around the room without moving or using up your turn

# v0.15.3
# Directional lighting is now a cone shape rather than a rectangle

# v0.15.4
# 


#TO DO:

# console info tooltip?
# attack should make a different sound if it does damage

# refactor object placement system
# AI improvements - pick up objects for a reason
# feelings / suspicion system
# end goal -- kill the thing -- final score
# objects can stil block on diagonals and against object_groups
# fix the x y coordinates system, particularly for objects in inventory

# arms and legs function -- if broken cannot perform tasks
# stacked_object = try_to_stack(map[x][y].objects_on_this_tile, object_to_place) list indices must be intgers not Nonetype

# Load any object into rocket launcher
# burning thing x / burning thingy . burn value >= 0 list must be int not nontype













# CURRENT FOCUS:

# Game engine
# UI
# Crashes


# 3 characters macready, nauls and wilfred brimley: accuracy, speed, strength
# point system: 1 point per thing kill, 10 points for survive, -2 points per innocent scientist kill, -1 point per dog kill
# more points for special character things


import copy
import math
import sys
import textwrap
import time
import pygame
import pygame.mixer
import sdl2

import libtcodpy as libtcod

# actual size of the window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 67

# size of the map
MAP_WIDTH = 90
MAP_HEIGHT = 45

# sizes and coordinates relevant for the GUI

OBJECT_INFO_BAR_WIDTH = SCREEN_WIDTH - MAP_WIDTH
PANEL_HEIGHT = SCREEN_HEIGHT - MAP_HEIGHT
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MESSAGE_PANEL_WIDTH = SCREEN_WIDTH - OBJECT_INFO_BAR_WIDTH
MSG_WIDTH = MESSAGE_PANEL_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1

INVENTORY_WIDTH = 50

# parameters for dungeon generator
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

FOV_ALGO = 0  # default FOV algorithm
FOV_LIGHT_WALLS = True  # light walls or not
MAX_VISIBILITY_RADIUS = 20

SIZE_TO_BLOCK_SIGHT = 10

LIMIT_FPS = 60  # 30 frames-per-second maximum

# For testing full visibility
SHOW_ALL = False
HEAR_ALL = False
PLAY_MUSIC = False
ID_TAGS_ON = True

MAX_ATTEMPTS_TO_PLACE_OBJECTS = 25
PRINT_COLLISIONS = False
PRINT_OBJECT_PLACEMENT_DETAILS = False

TOTAL_MAX_TURNS_PER_TASK = 50

AVERAGE_TURN_WAIT_BETWEEN_NEW_TASKS = 0

MINIMUM_DAMAGE_TO_REGISTER = 10
MAXIMUM_DAMAGE_ALLOWED = 100
MINIMUM_PROBABILITY_TO_ATTEMPT = 25

STANDARD_ACCURACY_DISTANCE = 5
TARGETED_THROW_ACCURACY_BONUS = 5

DEFAULT_INTERNAL_KINETIC_ENERGY = 10
LOSS_OF_MOMENTUM_ON_IMPACT = 0.75


MORE_ERROR_LOGGING = False
ACTIVATE_FUNCTION_TIMERS = True
DONT_TIME_LOOPS = True
MINIMUM_PROCESS_TIME_TO_ALERT = 0.05

NUMBER_OF_SECONDS_BETWEEN_TURNS = 0.05
NUMBER_OF_TURNS_UNTIL_THE_THING = 20

MAXIMUM_PROJECTILE_DISTANCE = 10

DEFAULT_FEELINGS_FOR = 8.0

CHANCE_OF_EXAMINE_SUCCESS_OUT_OF_100 = 100

EXAMINE_FEELINGS_CHANGE = -1

DISTANCE_TO_INTERACT = 3

EXPLORED_TILE_COLOUR_DESATURATION = 0.25

DISABLE_THE_THING = False

# as a fraction of total size of object
DEFAULT_HEAD_SIZE = 0.1
DEFAULT_TORSO_SIZE = 0.3
DEFAULT_LARM_SIZE = 0.1
DEFAULT_RARM_SIZE = 0.1
DEFAULT_LLEG_SIZE = 0.2
DEFAULT_RLEG_SIZE = 0.2

lab_rooms = ['Dog Cages Room', 'Computer Lab', "MacReady's Room"]
lab_rooms_original = list(lab_rooms)

action_colour = libtcod.red
narrator_colour = libtcod.purple
dialogue_colour = libtcod.green

temporary_obstacles = []

def current_message_colour(message_type):
	global action_colour, narrator_colour, dialogue_colour
	
	if message_type == 'Action':
		if action_colour == libtcod.red:
			action_colour = libtcod.lighter_red
		else:
			action_colour = libtcod.red
		return action_colour
	elif message_type == 'Narrator':
		if narrator_colour == libtcod.purple:
			narrator_colour = libtcod.lighter_purple
		else:
			narrator_colour = libtcod.purple
		return narrator_colour
	elif message_type == 'Dialogue':
		if dialogue_colour == libtcod.green:
			dialogue_colour = libtcod.lighter_green
		else:
			dialogue_colour = libtcod.green
		return dialogue_colour
	elif message_type == 'Debug':
		return libtcod.yellow
		
	return None
	
def generate_4_digit_ID():
		# Assign an ID identifier
		return libtcod.random_get_int(0, 1000, 9999)
	

class Message:
	# a tile of the map and its properties
	def __init__(self, text, type, relevant_objects = None):
		self.text = text
		self.type = type
		self.relevant_objects = relevant_objects
		self.x = OBJECT_INFO_BAR_WIDTH + 1
		self.y = None
		
		self.ID = generate_4_digit_ID()
		
		self.colour = None

		self.add_message()

	def add_message(self):
		global fov_map, message_scroll_state
		
		if not HEAR_ALL:
			if self.relevant_objects:
				if not libtcod.map_is_in_fov(fov_map, self.relevant_objects[0].x, self.relevant_objects[0].y):
					return False
			
		if len(self.text) > (MESSAGE_PANEL_WIDTH - 2):
			all_message_text = textwrap.wrap(self.text, (MESSAGE_PANEL_WIDTH - 2))
			
			for i in range(0, len(all_message_text)):
				message_copy = copy.deepcopy(self)
				message_copy.text = all_message_text[i]
				game_msgs.append(message_copy)
				
		else:
			game_msgs.append(self)
		
		message_scroll_state = 0
		return True


class Tile:
	# a tile of the map and its properties
	def __init__(self, wall):
		self.wall = wall

		self.x = None
		self.y = None

		self.char = '#'
		self.foreground_colour = libtcod.white
		self.background_colour = libtcod.black

		self.room_name = None
		self.objects_on_this_tile = []

		self.on_fire = False
		self.burn_value = 5
		
		self.explored = False
		self.last_known_char = None
		self.last_known_foreground_colour = None
		self.last_known_background_colour = None
		
		self.rendered_on_frame_number = None
		
		self.illuminated = False
		self.illuminated_up = False
		self.illuminated_down = False
		self.illuminated_left = False
		self.illuminated_right = False

		
	def distance_to(self, other):
		# return the distance to another object
		dx = other.x - self.x
		dy = other.y - self.y
		return math.sqrt(dx ** 2 + dy ** 2)
		
	def angle_to(self, other):
		dx = other.x - self.x
		dy = other.y - self.y
		if abs(dx) >= abs(dy):
			if dx >= 0:
				return 'Right'
			elif dx < 0:
				return 'Left'
		elif abs(dx) < abs(dy):
			if dy >= 0:
				return 'Down'
			elif dy < 0:
				return 'Up'
		
	def check_blocks_sight(self):
		if self.wall:
			return True

		for obj in self.objects_on_this_tile:
			if obj.size >= SIZE_TO_BLOCK_SIGHT:
				return True
			if obj.blocks_sightline:
				return True
		return False

	def set_on_fire(self):
		global map

		if self.on_fire:
			return False

		if self.burn_value >= 0:

			# If there is nothing on the tile to burn then dont burn
			if not self.objects_on_this_tile:
				return False

			self.on_fire = True
			self.char = 'F'
			self.foreground_colour = libtcod.light_red
			if not map[self.x][self.y] in tiles_on_fire:
				tiles_on_fire.append(map[self.x][self.y])
			return True
		return False

	def total_tile_size(self):
		total_size = 0
		for obj in self.objects_on_this_tile:
			total_size += obj.size
		return total_size
		
	def render_me(self):
		global fov_map, EXPLORED_TILE_COLOUR_DESATURATION
		
		if not self.illuminated:
			if player.x >= self.x and self.illuminated_right: self.illuminated = True
			if player.y >= self.y and self.illuminated_down: self.illuminated = True
			if player.x <= self.x and self.illuminated_left: self.illuminated = True
			if player.y <= self.y and self.illuminated_up: self.illuminated = True

			
		visible = libtcod.map_is_in_fov(fov_map, self.x, self.y)
		
		if SHOW_ALL or (visible and self.illuminated):
		
			self.explored = True
			self.last_known_char = self.char
			self.last_known_foreground_colour = self.foreground_colour * EXPLORED_TILE_COLOUR_DESATURATION
			self.last_known_background_colour = self.background_colour * EXPLORED_TILE_COLOUR_DESATURATION

			if len(self.objects_on_this_tile) > 0:
				biggest_object = pick_largest(self.objects_on_this_tile)
				use_this_foreground_colour = biggest_object.foreground_colour
				use_this_background_colour = biggest_object.background_colour
				
				if use_this_foreground_colour == self.background_colour: use_this_foreground_colour = use_this_foreground_colour * EXPLORED_TILE_COLOUR_DESATURATION
				if not use_this_background_colour: use_this_background_colour = self.background_colour
				
				if not biggest_object.unit:
					self.last_known_char = biggest_object.char
					self.last_known_foreground_colour = use_this_foreground_colour * EXPLORED_TILE_COLOUR_DESATURATION
					self.last_known_background_colour = use_this_background_colour * EXPLORED_TILE_COLOUR_DESATURATION
				else:
					self.last_known_char = self.char
					self.last_known_foreground_colour = self.foreground_colour * EXPLORED_TILE_COLOUR_DESATURATION
					self.last_known_background_colour = self.background_colour * EXPLORED_TILE_COLOUR_DESATURATION

				libtcod.console_put_char_ex(con, self.x, self.y, biggest_object.char, use_this_foreground_colour, use_this_background_colour)

			else:
				libtcod.console_put_char_ex(con, self.x, self.y, self.char, self.foreground_colour, self.background_colour)
		else:
			if self.explored:
				libtcod.console_put_char_ex(con, self.x, self.y, self.last_known_char, self.last_known_foreground_colour, self.last_known_background_colour)
			else:
				libtcod.console_put_char_ex(con, self.x, self.y, ' ', libtcod.black, libtcod.black)
			
		return True
		
		

class Rect:
	# a rectangle on the map. used to characterize a room.
	def __init__(self, x, y, w, h):
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h

		self.name = None

	def center(self):
		center_x = (self.x1 + self.x2) / 2
		center_y = (self.y1 + self.y2) / 2
		return (center_x, center_y)

	def intersect(self, other):
		# returns true if this rectangle intersects with another one
		return (self.x1 <= other.x2 and self.x2 >= other.x1 and
				self.y1 <= other.y2 and self.y2 >= other.y1)


class Room_Type:
	def __init__(self, name):
		self.name = name
		self.objects_in_room = []


class Object:
	# this is a generic object: the player, a monster, an item, the stairs...
	# it's always represented by a character on screen.
	def __init__(self,
				 x,
				 y,
				 char,
				 name,
				 foreground_colour,
				 background_colour=None,
				 always_visible=False,
				 condition=100,
				 size=0,
				 material='Wood',
				 weight=None,
				 indestructible=False,
				 affixed_to_ground=False,
				 blocks_sightline=False,
				 destroyed=False,
				 functions_as_door=False,
				 components=[],
				 inventory=[],
				 in_inventory_of=None,
				 food_value=0,
				 drink_value=0,
				 rest_value=0,
				 temp_value=0,
				 description=None,
				 unit=None):

		self.x = x
		self.y = y
		self.char = char
		self.name = name
		self.foreground_colour = foreground_colour
		self.background_colour = background_colour

		self.always_visible = always_visible

		self.condition = condition

		self.size = float(size)
		self.material = material

		self.weight = (get_material_stats_by_name(self.material, 'Weight') * self.size * self.size) / 2
		if self.weight <= 0: self.weight = 1

		self.indestructible = indestructible
		self.affixed_to_ground = affixed_to_ground
		self.blocks_sightline = blocks_sightline

		self.destroyed = destroyed
		self.functions_as_door = functions_as_door
		self.functions_as_lock = False
		self.functions_on_off = False
		self.attached_to_main_power = False

		self.components = components
		self.inventory = inventory
		self.in_inventory_of = in_inventory_of
		self.allow_inventory = True

		self.food_value = food_value
		self.drink_value = drink_value
		self.rest_value = rest_value
		self.temp_value = temp_value

		self.description = description
		
		self.direction = 'Left'
		
		self.movement_locked = False

		self.unit = unit
		if self.unit:  # let the unit component know who owns it
			self.unit.owner = self
			self.stackable = False

		self.open_closed_state = 'Closed'
		self.locked_unlocked_state = 'Locked'
		self.on_off_state = 'Off'

		self.equipped = None
		self.equipped_to = None
		self.attack_function = None
		self.ammunition_for = None
		self.key_for = None

		self.on_fire = False

		self.held_by = None

		self.internal_kinetic_energy = DEFAULT_INTERNAL_KINETIC_ENERGY

		self.quantity = 1

		self.task_queue = []

		self.stackable = False
		
		self.how_should_I_proceed = None
		self.what_object_should_I_interact_with = None
		
		self.light_source = False
		self.light_source_direction = None
		self.light_radius = None
		
		self.on_function = None
		self.on_argument = None
		
		self.off_function = None
		self.off_argument = None

		
		self.ID = generate_4_digit_ID()
		
	def toggle_on_off(self, object_to_toggle, force_state = None):

		if not object_to_toggle.functions_on_off:
			Message(object_to_toggle.name + ' does not have an activate function.', 'Narrator', relevant_objects = [self, object_to_toggle])
			return False
			
		if object_to_toggle.destroyed:
			Message(object_to_toggle.name + ' is broken and cannot be activated.', 'Narrator', relevant_objects = [self, object_to_toggle])
			return False
	
		if force_state:
			if force_state == 'On':
				object_to_toggle.on_off_state = 'Off'
			else:
				object_to_toggle.on_off_state = 'On'
				
		if object_to_toggle.on_off_state == 'On':
			object_to_toggle.on_off_state = 'Off'
			object_to_toggle.off_function(object_to_toggle.off_argument)
			
		elif object_to_toggle.on_off_state == 'Off':
			object_to_toggle.on_off_state = 'On'
			if object_to_toggle.attached_to_main_power and not main_power_on:
				Message(object_to_toggle.name + ' has no power.', 'Narrator', relevant_objects = [self, object_to_toggle])
			else:
				object_to_toggle.on_function(object_to_toggle.on_argument)
				activate_sound.play()
				
		return True
		
		
	def adjust_light_radius(self, new_radius):
		self.light_radius = new_radius
		
	def cancel_all_tasks(self):
		for my_task in self.task_queue:
			my_task.queue_task_end = True
		return True
		
	def check_if_unlocked(self):
		if self.functions_as_lock:
			if self.locked_unlocked_state == 'Locked':
				Message(self.name + ' is locked.', 'Narrator', relevant_objects = [self])
				return False
		return True
		
	def my_total_weight(self, inventory_only = False):
		total_weight = self.quantity * self.weight
		if inventory_only:
			total_weight = 0
		for object in self.inventory:
			total_weight += object.my_total_weight()
		return total_weight
		
	def update_weight(self, override_value = None):
		if override_value:
			self.weight = override_value
		else:
			self.weight = (get_material_stats_by_name(self.material, 'Weight') * self.size)
			
		return True
		
	def move_inventory_coords_to_location(self, x, y):
		for inventory_item in self.inventory:
			inventory_item.x = x
			inventory_item.y = y
			if inventory_item.inventory:
				inventory_item.move_inventory_coords_to_location(x, y)
			
	def establish_properties(self):
		
		self.update_weight()
		
		if self.unit:
			if self.unit.unit_name:
				self.name = self.unit.unit_name
				if self.unit.unit_description:
					self.description = self.unit.unit_description
				if not self.unit.backstory_dialogue:
					self.unit.backstory_dialogue = 301
		
		if self.weight <= 0: self.weight = 1
		
		inventory_names = self.inventory
		self.inventory = []
		
		if inventory_names:
			for name_of_inventory_item in inventory_names:
				self.add_to_inventory(get_object_by_name(name_of_inventory_item))


		# Check if object has become a unit
		if self.unit:  # let the unit component know who owns it
			self.unit.owner = self
			self.stackable = False

			self.unit.update_strength(self.unit.strength)
			
			self.unit.generate_appendages()
		
		# Equip yourright arm as a weapon by default
		if self.unit:
			self.equipped = self.unit.rarm
			
		if self.stackable:
			self.allow_inventory = False

		self.previous_char = self.char
		self.previous_size = self.size
		self.previous_blocks_sightline = self.blocks_sightline
		self.previous_foreground_colour = self.foreground_colour
		self.previous_name = self.name
		self.previous_light_radius = self.light_radius

		return True
		

	def intelligent_move(self, dx, dy):
	
		# This will assign the best course of action to the object's "how_should_I_proceed" variable
		difficulty_of_move = astar_obstacle_function(self.x, self.y, self.x + dx, self.y + dy, self)

		if not self.how_should_I_proceed:
			print 'shouldnt get hereeee'
			return False
		
		if self.how_should_I_proceed == 'Open Door':
			self.open_close(self.what_object_should_I_interact_with)
		elif self.how_should_I_proceed == 'Manoeuvre':
			self.unit.try_to_manoeuvre(dx, dy)
		elif self.how_should_I_proceed == 'Attack':
			self.unit.attack(target_object_or_tile = self.what_object_should_I_interact_with)
		elif self.how_should_I_proceed == 'Basic Move' or self.how_should_I_proceed == 'At Destination':
			self.move(dx, dy)
		else:
			print 'shouldnt get herea'
			return False

		self.how_should_I_proceed = None
		self.what_object_should_I_interact_with = None
		return True
		
		
	def can_i_perform_task(self, object, task):
		if not self.unit:
			return False
		
		metric = None
		if task == 'Drag' or task == 'Lift' or task == 'Throw':
			if task == 'Drag':
				metric = self.unit.drag_weight
			elif task == 'Lift':
				metric = self.unit.lift_weight
			elif task == 'Throw':
				metric = self.unit.throw_weight
			
			if object.weight > metric:
				return False
		
		elif task == 'Open / Close':
			if not object.functions_as_door:
				return False
		elif task == 'Lock / Unlock':
			if not object.functions_as_lock:
				return False
		elif task == 'Activate / Deactivate':
			if not object.functions_on_off:
				return False
		else:
			print 'spelling error: ' + task
			return False

			
		return True
			

	def move(self, dx, dy, force_success = False):
		global map
		
		new_angle = map[self.x][self.y].angle_to(map[self.x + dx][self.y + dy])
		self.direction = new_angle
		if self.unit:
			if self.unit.holding:
				self.unit.holding.direction = new_angle
		
		if self.movement_locked:
			Message(self.name + ' movement locked.  Press x to resume.', 'Narrator', relevant_objects = [self])
			return True

		test_x = -1
		test_y = -1

		move_held_object_check_success = False

		if self.unit:
			if self.unit.holding:
				if not self.can_i_perform_task(self.unit.holding, 'Drag'):
					Message(self.name + ' is too weak to move ' + self.unit.holding.name, 'Action', relevant_objects = [self])
					return False
				move_held_object_check_success = self.move_held_object_check(dx, dy)
				map[self.unit.holding.x][self.unit.holding.y].objects_on_this_tile.remove(self.unit.holding)
				if move_held_object_check_success and not is_blocked(self.unit.holding.x, self.unit.holding.y, self):
					test_x = self.unit.holding.x
					test_y = self.unit.holding.y
				map[self.unit.holding.x][self.unit.holding.y].objects_on_this_tile.append(self.unit.holding)

		# move by the given amount, if the destination is not wall
		if not is_blocked(self.x + dx, self.y + dy, self) or (self.x + dx == test_x and self.y + dy == test_y) or force_success:

			new_x = self.x + dx
			new_y = self.y + dy
			
			

			remove_all_connections_to_object(self)
			place_object_at_location(self, new_x, new_y, stack_objects_allowed = False, force_placement_success = True)

			if self.unit:
				self.unit.turn_taken = True

			if move_held_object_check_success:
				self.unit.holding.move(dx, dy)
			else:
				if self.unit:
					self.unit.let_go()

			return True

		return False

	def move_held_object_check(self, dx, dy):
		if not self.unit.holding:
			return False
		if not is_blocked(self.unit.holding.x + dx, self.unit.holding.y + dy, self.unit.holding):
			# Held object movement is completely clear
			return True
		elif self.unit.holding.x + dx == self.x and self.unit.holding.y + dy == self.y:
			# Held object will move to tile where the unit holding it is currently located, so that's ok too
			return True
		return False

	def throw(self, projectile_object, target = None):
		global player
			
		if not target:
			# Choose a target
			target = target_tile(return_object_if_possible = True)
			
		if not target:
			return False
			
		if isinstance(target, Tile):
			potential_target = pick_largest(target.objects_on_this_tile)
			if potential_target:
				target = pick_largest(target.objects_on_this_tile)
				
		if projectile_object.in_inventory_of:
			projectile_object = projectile_object.take_from_stack(quantity = 1)
			place_object_at_location(projectile_object, self.x, self.y, stack_objects_allowed = False, force_placement_success = True)
				
				
		if projectile_object.quantity > 1:
			projectile_object = projectile_object.take_from_stack(quantity = 1)
			place_object_at_location(projectile_object, projectile_object.x, projectile_object.y, stack_objects_allowed = False, force_placement_success = True)
		else:
			if self.unit:
				self.unit.let_go()
			
		throw_success = process_projectile(self.unit.throw_weight, projectile_object, specific_target_object_or_tile = target, accuracy_modifier = TARGETED_THROW_ACCURACY_BONUS, pass_through_object = self)

		if not throw_success:
			Message(self.name + ' fails miserably to throw ' + projectile_object.name, 'Action', relevant_objects = [self])
			return False

		return True

	def move_towards(self, target_x, target_y):
		# vector from this object to the target, and distance
		dx, dy = get_vector_toward(self, target_x, target_y)
		return self.move(dx, dy)

	def distance_to(self, other):
		# return the distance to another object
		dx = other.x - self.x
		dy = other.y - self.y
		return math.sqrt(dx ** 2 + dy ** 2)

	def distance(self, x, y):
		# return the distance to some coordinates
		return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

	def clear(self):
		# erase the character that represents this object
		if libtcod.map_is_in_fov(fov_map, self.x, self.y):
			libtcod.console_put_char_ex(con, self.x, self.y, '.', libtcod.white, libtcod.black)

	def move_astar(self, target):
		# Allocate a A* path
		# The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited

		my_path = libtcod.path_new_using_function(MAP_WIDTH, MAP_HEIGHT, astar_obstacle_function, self, 0.0)

		# Compute the path between self's coordinates and the target's coordinates
		libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)
		
		# Apply the astar path to the current task
		if libtcod.path_is_empty(my_path):
			if self.task_queue:
				self.task_queue[0].queue_task_end = True
			return False

		# Find the next coordinates in the computed full path
		x, y = libtcod.path_walk(my_path, True)

		if (x or y):
			dx = x - self.x
			dy = y - self.y
			self.intelligent_move(dx, dy)

		# Delete the path to free memory
		libtcod.path_delete(my_path)

		return True
		
	def add_to_inventory(self, object_in_question, quantity = None):
		
		if not object_in_question:
			return False
			
		if not self.allow_inventory:
			print 'object does not have inventory space'
			return False
			
		object_in_question = object_in_question.take_from_stack(quantity)
		
		stack_attempt = try_to_stack(self.inventory, object_in_question)
		
		# If the object stacks, return the pointer to the new stacked object
		if stack_attempt:
			return stack_attempt
			
		self.inventory.append(object_in_question)
		object_in_question.in_inventory_of = self
		
		return object_in_question
		
	def remove_from_inventory(self, object_in_question, quantity = None):
		
		if not object_in_question:
			return False
			
		if not self.allow_inventory:
			print 'object does not have inventory space'
			return False
			
		if not object_in_question in self.inventory:
			if not object_in_question in self.inventory:
				print object_in_question.name + ' is not in inventory of ' + self.name
				return False
		
		object_in_question = object_in_question.take_from_stack(quantity)
		
		return object_in_question
		
	def take_object_from_inventory(self, object_to_take_from, object_to_take, quantity = None):			
		
		taken_object = object_to_take_from.remove_from_inventory(object_to_take, quantity)
		
		if taken_object:
			Message(self.name + ' adds ' + object_to_take.name + ' to inventory.', 'Narrator', relevant_objects = [self, object_to_take])
			return self.add_to_inventory(taken_object, quantity)

		return False
		
	def make_copy(self, object):
		global map
		
		self.x = object.x
		self.y = object.y

		self.inventory = []
		self.in_inventory_of = object.in_inventory_of

		self.equipped_to = None
		
		self.ID = generate_4_digit_ID()	
			
		return True
		
		
	def take_from_stack(self, quantity = None):
	
		if not quantity or quantity > self.quantity:
			quantity = self.quantity
	
		if quantity < self.quantity:
			split_quantity_object = copy.deepcopy(self)
			remove_all_connections_to_object(split_quantity_object)
			self.quantity -= quantity
			split_quantity_object.quantity = quantity
			split_quantity_object.make_copy(self)
			return split_quantity_object
		else:
			remove_all_connections_to_object(self)
			return self
		
	
	def destroy(self, impact_force = None):
		global list_of_things, objects_on_fire, objects_in_motion, player, game_state

		if self.destroyed:
			return False
		
		# Destroyed object loses its contents by adding half the force of the attack that destroyed it
		if impact_force:
			self.internal_kinetic_energy += int(float(impact_force) - (float(impact_force) * LOSS_OF_MOMENTUM_ON_IMPACT))
			
		self.functions_as_lock = False
		self.locked_unlocked_state = 'Unlocked'

		if self.in_inventory_of:
			self.in_inventory_of.unit.drop(self)

		self.blocks_sightline = False
		self.size = 0
		self.char = '='
		self.foreground_colour = libtcod.dark_orange
		self.name = 'Broken ' + self.name
		
		if self.functions_on_off:
			self.toggle_on_off(self, force_state = 'Off')
			
		self.destroyed = True
		
		if self.unit:
			if self.unit.the_thing:
				list_of_things.remove(self)

		for inventory_object in self.inventory:
			
			remove_all_connections_to_object(inventory_object)
			place_object_at_location(inventory_object, self.x, self.y, stack_objects_allowed = False, force_placement_success = True)
			process_projectile(self.internal_kinetic_energy, inventory_object)
		
		self.inventory = []

		for component_name in self.components:

			dropped_component_object = get_object_by_name(component_name)

			if dropped_component_object.on_fire:
				objects_on_fire.append(dropped_component_object)
				map[dropped_component_object.x][dropped_component_object.y].set_on_fire()

			place_object_at_location(dropped_component_object, self.x, self.y, stack_objects_allowed = False, force_placement_success = True)
			process_projectile(self.internal_kinetic_energy, dropped_component_object)

		self.components = []
		
		# Arms and legs fall off!
		if self.unit:
		
			death_sound.play()
			
			my_appendages = [self.unit.head, self.unit.torso, self.unit.larm, self.unit.rarm, self.unit.lleg, self.unit.rleg]
			
			for appendage in my_appendages:
				
				place_object_at_location(appendage, self.x, self.y, stack_objects_allowed = False, force_placement_success = True)
				process_projectile(self.internal_kinetic_energy, appendage)
				
			if self == player:
				menu('Player has been killed', None, ['Ok'], clear_window_after_display = False)
				end_game_return_to_main_menu()
				return True

				
			remove_all_connections_to_object(self)
			
			if self.unit.the_thing:
				choice = menu('The Thing has died!  Keep playing?', None, ['Yes', 'No'], clear_window_after_display = False)

				if choice == 0:
					pass
				else:
					end_game_return_to_main_menu()
						
			del self
		
		return True
		

	def check_if_destroyed(self, impact_force = 0):
		if self.condition <= 0:
			self.destroy(impact_force)
			
	def lock_unlock(self, locked_object, test = False):
		if not locked_object:
			return False
			
		if not locked_object.functions_as_lock:
			Message(locked_object.name + ' does not have a lock function.', 'Narrator', relevant_objects = [locked_object])
			return False
		
		key = None
		for key_object in self.inventory:
			if key_object.key_for == locked_object.name:
				key = key_object
				break
			
		if not key:
			if not test:
				Message(self.name + ' does not have the key for ' + locked_object.name, 'Narrator', relevant_objects = [self])
			return False

		if locked_object.locked_unlocked_state == 'Locked':
			locked_object.locked_unlocked_state = 'Unlocked'
			Message(locked_object.name + ' is now unlocked.', 'Narrator', relevant_objects = [locked_object])
		elif locked_object.locked_unlocked_state == 'Unlocked':
			locked_object.locked_unlocked_state = 'Locked'
			Message(locked_object.name + ' is now locked.', 'Narrator', relevant_objects = [locked_object])
		
		key_unlock_sound.play()
		return True


			

	def open_close(self, door_object):
		if not door_object:
			return False
		if door_object.functions_as_door:
			if door_object.open_closed_state == 'Closed':
				door_object.previous_char = door_object.char
				door_object.previous_size = door_object.size
				door_object.previous_blocks_sightline = door_object.blocks_sightline

				door_object.blocks_sightline = False
				door_object.size = 1
				door_object.char = '/'

				door_object.open_closed_state = 'Open'

			elif door_object.open_closed_state == 'Open':
				door_object.blocks_sightline = door_object.previous_blocks_sightline
				door_object.size = door_object.previous_size
				door_object.char = door_object.previous_char

				door_object.previous_char = None
				door_object.previous_size = None
				door_object.previous_blocks_sightline = None

				door_object.open_closed_state = 'Closed'
			
			if libtcod.map_is_in_fov(fov_map, door_object.x, door_object.y):
				door_sound.play()
			return True

		Message(door_object.name + ' does not function as a door.', 'Action', relevant_objects=[door_object])
		return False
		
def normalize_to_map_width(x_value):
	if x_value < 1: x_value = 1
	if x_value > MAP_WIDTH - 1: x_value = MAP_WIDTH - 1
	return x_value
	
def normalize_to_map_height(y_value):
	if y_value < 1: y_value = 1
	if y_value > MAP_HEIGHT - 1: y_value = MAP_HEIGHT - 1
	return y_value


class Projectile_In_Motion:
	def __init__(self, projectile_object, specific_target_object_or_tile, velocity, accuracy_modifier, pass_through_object, destination_tile_x, destination_tile_y):
		self.projectile_object = projectile_object
		self.specific_target_object_or_tile = specific_target_object_or_tile
		self.velocity = velocity
		self.accuracy_modifier = accuracy_modifier
		self.pass_through_object = pass_through_object
		self.destination_tile_x = destination_tile_x
		self.destination_tile_y = destination_tile_y
		
	def run_turn(self):
		global objects_in_motion, map
		
		dx, dy = get_vector_toward(self.projectile_object, self.destination_tile_x, self.destination_tile_y)
		
		next_tile_x = self.projectile_object.x + dx
		next_tile_y = self.projectile_object.y + dy
		
		collision_object = None

		if self.specific_target_object_or_tile:
			if isinstance(self.specific_target_object_or_tile, Object) and self.specific_target_object_or_tile.x == next_tile_x and self.specific_target_object_or_tile.y == next_tile_y:
				if (len(map[next_tile_x][next_tile_y].objects_on_this_tile)) > 0:
					for potential_collision in map[next_tile_x][next_tile_y].objects_on_this_tile:

						if potential_collision == self.specific_target_object_or_tile:
							if self.accuracy_modifier:
								collision_chance = (self.projectile_object.size + potential_collision.size) + self.accuracy_modifier
							else:
								collision_chance = (self.projectile_object.size + potential_collision.size) * 2
								
							if libtcod.random_get_int(0, 0, 20) < collision_chance:
								collision_object = potential_collision
							else:
								Message(self.projectile_object.name + ' missed ' + potential_collision.name, 'Narrator', relevant_objects=[self.projectile_object, potential_collision])
							
							break
		
		if not collision_object:
			collision_object = is_blocked(next_tile_x, next_tile_y, check_against_object = self.projectile_object, random_collision_chance = True)	
		
		if collision_object:
			if collision_object == self.pass_through_object:
				pass
			else:
				process_collision(self.projectile_object, collision_object, self.velocity)
				objects_in_motion.remove(self)
				self.projectile_object.direction = pick_random(['Up', 'Down', 'Left', 'Right'])
				del self
				return True
		
		previous_x = self.projectile_object.x
		previous_y = self.projectile_object.y
		
		remove_all_connections_to_object(self.projectile_object)
		place_object_at_location(self.projectile_object, next_tile_x, next_tile_y, stack_objects_allowed = False, force_placement_success = True)
		
		map[previous_x][previous_y].render_me()
		map[self.projectile_object.x][self.projectile_object.y].render_me()


		self.accuracy_modifier -= 1

		# If the object reaches its destination
		if (self.projectile_object.x == self.destination_tile_x and self.projectile_object.y == self.destination_tile_y):
			objects_in_motion.remove(self)
			self.projectile_object.direction = pick_random(['Up', 'Down', 'Left', 'Right'])
			del self
			return True

		return True

def process_projectile(energy_force, projectile_object, specific_target_object_or_tile = None, accuracy_modifier = 0, pass_through_object = None):
	global player, objects_in_motion
	
	for object in objects_in_motion:
		if object == projectile_object:
			print 'trying to add ' + projectile_object.name + ' to moving objects when its already in the list.'
			return False

	accuracy_modifier += STANDARD_ACCURACY_DISTANCE
	
	velocity = calculate_velocity(energy_force, projectile_object.weight)

	number_of_tiles_covered = int(velocity)
	
	if number_of_tiles_covered > MAXIMUM_PROJECTILE_DISTANCE: number_of_tiles_covered = MAXIMUM_PROJECTILE_DISTANCE

	if number_of_tiles_covered == 0:
		# Not enough energy to move even one tile
		return False
	
	destination_tile_x = None
	destination_tile_y = None
	
	if specific_target_object_or_tile:
		destination_tile_x = specific_target_object_or_tile.x
		destination_tile_y = specific_target_object_or_tile.y
		
	else:
		dx = libtcod.random_get_int(0, 0 - number_of_tiles_covered, number_of_tiles_covered)
		dy = libtcod.random_get_int(0, 0 - number_of_tiles_covered, number_of_tiles_covered)
		
		destination_tile_x = normalize_to_map_width(projectile_object.x + dx)
		destination_tile_y = normalize_to_map_height(projectile_object.y + dy)
		
		specific_target_object_or_tile = map[destination_tile_x][destination_tile_y]
	
	this_moving_object = Projectile_In_Motion(projectile_object, specific_target_object_or_tile, velocity, accuracy_modifier, pass_through_object, destination_tile_x, destination_tile_y)
	
	objects_in_motion.append(this_moving_object)

	return True

	
	
def astar_obstacle_function(xFrom, yFrom, xTo, yTo, object_moving):
	global map
	difficulty_of_move = 1
	
	object_moving.how_should_I_proceed = None
	object_moving.what_object_should_I_interact_with = None

	if object_moving.task_queue:
		for obj in map[xTo][yTo].objects_on_this_tile:
			if obj == object_moving.task_queue[0].object_moving_to:
				object_moving.how_should_I_proceed = 'At Destination'
				return difficulty_of_move

	blocking_object = is_blocked(xTo, yTo, object_moving)

	if blocking_object:
		if map[xTo][yTo].objects_on_this_tile:
			for obj in map[xTo][yTo].objects_on_this_tile:
			
				# handles attacking your way through objects
				if object_moving.unit:
				
					# Only humans and things can open doors
					if object_moving.unit.creature_type == 'Humanoid' or object_moving.unit.the_thing:
						if obj.functions_as_door and obj.open_closed_state == 'Closed':
							object_moving.how_should_I_proceed = 'Open Door'
							object_moving.what_object_should_I_interact_with = blocking_object
							return difficulty_of_move

					# The trick below is remembering that 0 means cannot pass
					test_register_damage = object_moving.unit.attack(target_object_or_tile = blocking_object, test = True)
					
					if test_register_damage < MINIMUM_DAMAGE_TO_REGISTER:
						difficulty_of_attack = 0
					else:
						difficulty_of_attack = normalize_to((100 - test_register_damage), 1, 100)
					
					manoeuvre_chance = object_moving.unit.try_to_manoeuvre(xTo - object_moving.x, yTo - object_moving.y, return_success_chance = True)	
					if manoeuvre_chance < MINIMUM_PROBABILITY_TO_ATTEMPT:
						difficulty_of_manoeuvre = 0
					else:
						difficulty_of_manoeuvre = normalize_to((100 - manoeuvre_chance), 1, 100)
						
					if difficulty_of_manoeuvre == 0:
						difficulty_of_manoeuvre = 100
						
					if difficulty_of_attack == 0:
						difficulty_of_attack = 100
						
					if difficulty_of_manoeuvre < difficulty_of_attack:
						object_moving.how_should_I_proceed = 'Manoeuvre'
						object_moving.what_object_should_I_interact_with = blocking_object
						return difficulty_of_manoeuvre
						
					if difficulty_of_attack < difficulty_of_manoeuvre:
						object_moving.how_should_I_proceed = 'Attack'
						object_moving.what_object_should_I_interact_with = blocking_object
						return difficulty_of_attack
		
		object_moving.how_should_I_proceed = 'Do Not Try'
		difficulty_of_move = 0
	
	object_moving.how_should_I_proceed = 'Basic Move'
	return difficulty_of_move


class Object_Group:
	def __init__(self, name, grid):
		self.name = name
		self.grid = grid
		self.width = 0
		self.height = 0
		self.object_map = []
		self.place_against_wall = False

		j = 0
		for columns in self.grid:
			i = 0
			for rows in columns:
				if columns[i] != '_':
					if i > self.width:
						self.width = i
					if j > self.height:
						self.height = j
				i += 1
			j += 1

		self.width += 1
		self.height += 1

		self.grid = self.grid[:self.height]
		for trim_this in range(0, len(self.grid)):
			self.grid[trim_this] = self.grid[trim_this][:self.width]

	def debug_print(self):
		print ''
		for columns in self.grid:
			print columns
		print ''
		print 'Width: ' + str(self.width)
		print 'Height: ' + str(self.height)
		print 'Against Wall: ' + str(self.place_against_wall)
		print ''

	def rotate(self):
		if self.place_against_wall == 'Left':
			self.place_against_wall = 'Top'
		elif self.place_against_wall == 'Right':
			self.place_against_wall = 'Bottom'
		elif self.place_against_wall == 'Top':
			self.place_against_wall = 'Right'
		elif self.place_against_wall == 'Bottom':
			self.place_against_wall = 'Left'

		self.grid = zip(*self.grid[::-1])

		temp = self.width
		self.width = self.height
		self.height = temp


def normalize_to(value, min, max):
	if value > max:
		value = max
	if value < min:
		value = min
	return value
		
class Unit:
	# combat-related properties and methods (monster, player, NPC).
	def __init__(self):

		self.holding = None

		self.the_thing = False
		self.the_thing_revealed = False

		self.dialogue = []

		self.strength = 1

		self.turn_taken = False
		
		self.lift_weight = None
		self.drag_weight = None
		self.throw_weight = None
		
		self.creature_type = None
		
		self.head = None
		self.torso = None
		self.larm = None
		self.rarm = None
		self.lleg = None
		self.rleg = None
		
		self.unit_name = None
		self.unit_description = None
		self.backstory_dialogue = None
		
		self.feelings_for = []
		
	def try_to_manoeuvre(self, dx, dy, minimum_size_reduction_percent = 25, maximum_size_reduction_percent = 50, return_success_chance = False):
		
		if self.the_thing_revealed:
			minimum_size_reduction_percent = 50
			maximum_size_reduction_percent = 90
		
		total_size = 0
		for object in map[self.owner.x + dx][self.owner.y + dy].objects_on_this_tile:
			total_size += object.size
			
		# It's minus 1 on fail becuase a draw means success (total of size 10 as example)
		min_size = int(self.owner.size - (float(self.owner.size) * float(maximum_size_reduction_percent / 100.0)))
		max_size = int(self.owner.size - (float(self.owner.size) * float(minimum_size_reduction_percent / 100.0)))
		
		success_size = int(normalize_to((10 - total_size), 0, 10))

		if min_size > success_size:
			return False
			
		success_conditions = normalize_to(len(range(min_size, success_size)), 0, 10)
		fail_conditions = normalize_to((len(range(success_size, max_size)) - 1), 1, 10)
		
		chance_of_success = float(float(success_conditions) / float(success_conditions + fail_conditions)) * 100
		
		if return_success_chance:
			return chance_of_success
		
		
		random_obstacle = pick_random(map[self.owner.x + dx][self.owner.y + dy].objects_on_this_tile)

		previous_size = self.owner.size
		actual_size_reduction = float(libtcod.random_get_int(0, minimum_size_reduction_percent, maximum_size_reduction_percent))
		self.owner.size = self.owner.size - float(float(self.owner.size) * (actual_size_reduction / 100.0))
		attempt_is_blocked = is_blocked(self.owner.x + dx, self.owner.y + dy, check_against_object = self.owner)
		self.owner.size = previous_size
		
		if attempt_is_blocked:
			if random_obstacle:
				Message(self.owner.name + " trips trying to get past " + random_obstacle.name + ".", 'Debug', relevant_objects = [self.owner, random_obstacle])
			return True
		else:
			if random_obstacle:
				Message(self.owner.name + " deftly manoeuvres around " + random_obstacle.name + ".", 'Debug', relevant_objects = [self.owner, random_obstacle])
			self.owner.move(dx, dy, force_success = True)
			return True

	def check_my_feelings_for(self, object, adjust_by = 0):
	
		if adjust_by > 0:
			Message(self.owner.name + " has a higher opinion of " + object.name + "!", 'Narrator', relevant_objects = [self.owner, object])
		elif adjust_by < 0:
			Message(self.owner.name + " has a lower opinion of " + object.name + ".", 'Narrator', relevant_objects = [self.owner, object])
	
		for familiar_unit in self.feelings_for:
			if familiar_unit[0] == object:
				familiar_unit[1] += adjust_by
				familiar_unit[1] = normalize_to(familiar_unit[1], 0, 10)
				return familiar_unit[1]
		
		
		starting_feelings = normalize_to((DEFAULT_FEELINGS_FOR + adjust_by), 0, 10)
		self.feelings_for.append([object, starting_feelings])
		return starting_feelings
		
		
	def update_strength(self, new_value):
		self.strength = new_value
				
		self.lift_weight = int(self.owner.weight * self.strength)
		self.drag_weight = int(self.lift_weight)
		self.throw_weight = int(self.lift_weight / 2)
		
		return True
		
		
	def generate_appendages(self):
	
		generic_appendage = get_predesigned_object_by_name('Generic Object')
		generic_appendage.foreground_colour = self.owner.foreground_colour
		generic_appendage.material = 'Flesh'
		
		# Head
		self.head = copy.deepcopy(generic_appendage)
		self.head.char = 'h'
		self.head.size = float(self.owner.size * DEFAULT_HEAD_SIZE)
		self.head.name = self.owner.name + "'s head"
		self.head.establish_properties()
		
		# Torso
		self.torso = copy.deepcopy(generic_appendage)
		self.torso.char = 'T'
		self.torso.size = float(self.owner.size * DEFAULT_TORSO_SIZE)
		self.torso.name = self.owner.name + "'s torso"
		self.torso.establish_properties()
		
		# Left arm
		self.larm = copy.deepcopy(generic_appendage)
		self.larm.char = 'a'
		self.larm.size = float(self.owner.size * DEFAULT_LARM_SIZE)
		self.larm.name = self.owner.name + "'s left arm"
		self.larm.establish_properties()
		
		# Right arm
		self.rarm = copy.deepcopy(generic_appendage)
		self.rarm.char = 'a'
		self.rarm.size = float(self.owner.size * DEFAULT_RARM_SIZE)
		self.rarm.name = self.owner.name + "'s right arm"
		self.rarm.establish_properties()
		
		# Left leg
		self.lleg = copy.deepcopy(generic_appendage)
		self.lleg.char = 'l'
		self.lleg.size = float(self.owner.size * DEFAULT_LLEG_SIZE)
		self.lleg.name = self.owner.name + "'s left leg"
		self.lleg.establish_properties()
		
		# Right leg
		self.rleg = copy.deepcopy(generic_appendage)
		self.rleg.char = 'l'
		self.rleg.size = float(self.owner.size * DEFAULT_RLEG_SIZE)
		self.rleg.name = self.owner.name + "'s right leg"
		self.rleg.establish_properties()



	def become_the_thing(self):
		global list_of_things
		list_of_things.append(self.owner)
		self.the_thing = True
		self.update_strength(2)
		#self.owner.foreground_colour = libtcod.yellow

		
	def reveal_the_thing(self):
		self.the_thing_revealed = True
		self.owner.foreground_colour = libtcod.light_purple
		self.owner.name = 'The Thing'
		self.owner.cancel_all_tasks()
		Message(self.owner.name + ' has been revealed as The Thing!', 'Narrator', relevant_objects = [self.owner])
		
	def reassimilate(self):
			
		self.the_thing_revealed = False
		self.owner.foreground_colour = libtcod.light_purple
		self.owner.name = 'The Thing'
		self.owner.cancel_all_tasks()
		
		self.owner.char = self.owner.previous_char
		self.owner.foreground_colour = self.owner.previous_foreground_colour
		self.owner.name = self.owner.previous_name
		return True

	def check_for_negative_stats(self):
		if self.hunger < 0:
			self.hunger = 0
		if self.thirst < 0:
			self.thirst = 0
		if self.sleep < 0:
			self.sleep = 0
		if self.fight < 0:
			self.fight = 0
		if self.owner.condition < 0:
			self.owner.condition = 0
			
	def take_turn(self):
		global player, fov_map

		# Currently player cannot take a turn automatically
		if self.owner == player:
			return False
		
		if self.owner.destroyed:
			return False

		self.turn_taken = True

		if self.owner.task_queue:	
			if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
			run_task = self.owner.task_queue[0].run_task()
			if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, self.owner.name + ' running their current task')
			return True
		
		else:
			if libtcod.random_get_int(0, 0, AVERAGE_TURN_WAIT_BETWEEN_NEW_TASKS) == 0:
				if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
				determine_task = self.determine_task()
				if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, self.owner.name + ' determining a new task')
				return True
				
	def determine_task(self, test = False):
		global rooms, map, fov_map
	
		# If they already have a task this should not be called
		if self.owner.task_queue and not test:
			return False
		
		chosen_task = None
		chosen_object_or_room = None
		task_message_ID = None
		nearest_objects_or_rooms = []
		potential_tasks = []
		max_turns_allocated = TOTAL_MAX_TURNS_PER_TASK
		
		potential_tasks.append('Move to Object')
		potential_tasks.append('Move to Room')
		potential_tasks.append('Examine Object')
		potential_tasks.append('Deliver Message to Object')
		
		if self.the_thing:
		
			# he sees through walls he has the sense
			nearby_units = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units', see_through_walls = True)
			
			# This is probably time consuming but also really cool (potentially a lot of FOV computations)
			for potential_target in nearby_units:
			
				other_units_nearby = potential_target.unit.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units', maximum_results = 2, sort_by_distance = False)
				
				# Don't count The Thing itself when looking for threats
				if self.owner in other_units_nearby:
					other_units_nearby.remove(self.owner)
					
				if len(other_units_nearby) >= 1:
					continue
				else:
					chosen_task = 'Attack Object'
					chosen_object_or_room = potential_target
					max_turns_allocated = 5
					break
			
			# The Thing will flee if too many units nearby
			if self.the_thing_revealed:
				units_that_see_me = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units', maximum_results = 1, sort_by_distance = False, see_through_walls = False)
				if len(units_that_see_me) == 0:
					self.reassimilate()
					
				if not chosen_task:
					chosen_task = 'Move to Room'

		if not chosen_task:		
			chosen_task = pick_random(potential_tasks)

		if not chosen_object_or_room:
			if chosen_task == 'Move to Object':
				nearest_objects_or_rooms = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Non Affixed Objects')
			elif chosen_task == 'Move to Room':
				for potential_room in rooms:
					(center_x, center_y) = potential_room.center()
					potential_room_center_tile = map[center_x][center_y]
					if potential_room_center_tile.distance_to(self.owner) <= (MAX_VISIBILITY_RADIUS * 2):
						nearest_objects_or_rooms.append(potential_room_center_tile)

			elif chosen_task == 'Deliver Message to Object':
				nearest_objects_or_rooms = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units')
			elif chosen_task == 'Attack Object':
				nearest_objects_or_rooms = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units')
			elif chosen_task == 'Examine Object':
				nearest_objects_or_rooms = self.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units')

			chosen_object_or_room = pick_random(nearest_objects_or_rooms)
				
		if chosen_object_or_room:
			final_task = Task(task_owner = self.owner, task_type = chosen_task, object_source_of_task = self.owner, object_moving_to = chosen_object_or_room, object_to_interact_with = chosen_object_or_room, search_range = MAX_VISIBILITY_RADIUS, max_turns_allocated = max_turns_allocated, task_message_ID = task_message_ID, quantity = None)
			if test:
				return final_task
			self.owner.task_queue.append(final_task)
			self.owner.task_queue[0].run_task()
			return True

		
		return False
		
	def consume(self, onject_being_consumed):
		Message('Feature not yet implemented into game.', 'Narrator', relevant_objects = [self.owner, onject_being_consumed])
		return False
		

	def attack(self, target_object_or_tile = None, test = False):
	
		if ACTIVATE_FUNCTION_TIMERS: attack_timer = start_test()
		
		if isinstance(target_object_or_tile, Tile):
			target_object_or_tile = pick_largest(target_object_or_tile.objects_on_this_tile)
			
		target_object = target_object_or_tile
			
		if not target_object:
			Message('Nothing to attack', 'Narrator', relevant_objects = [self.owner])
			return False
			
		if self.the_thing:
			if target_object_or_tile.unit:
				other_units_nearby = target_object.unit.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type = 'Units', maximum_results = 2, sort_by_distance = False)
				if self.owner in other_units_nearby:
					other_units_nearby.remove(self.owner)	
				if len(other_units_nearby) >= 2:
					self.owner.cancel_all_tasks()
					return False
		
		if test:
			test_damage = 0
			velocity = calculate_velocity(self.throw_weight, self.owner.equipped.weight)
			test_damage = process_collision(self.owner.equipped, target_object, velocity, test=test)
			return test_damage
			
		Message(self.owner.name + ' attacks ' + target_object.name + '.', 'Action', relevant_objects=[self.owner, target_object])

		if self.owner.equipped.attack_function:

			ammunition = None
			for inventory_object in self.owner.inventory:
				if inventory_object.ammunition_for:
					for weapon_type in inventory_object.ammunition_for:
						if weapon_type ==  self.owner.equipped.name:
							ammunition = inventory_object
							break
					
			if not ammunition:
				Message('No ammo', 'Action', relevant_objects=[self.owner])
				no_ammo_sound.play()
				return False
			else:
				dropped_ammunition = self.drop(ammunition, 1)
				process_projectile(self.owner.equipped.internal_kinetic_energy, dropped_ammunition, target_object, accuracy_modifier = 5)
				gun_sound.play()
				return True
		else:

			velocity = calculate_velocity(self.throw_weight, self.owner.equipped.weight)
			previous_state = self.owner.equipped.indestructible
			self.owner.equipped.indestructible = True
			process_collision(self.owner.equipped, target_object, velocity)
			self.owner.equipped.indestructible = previous_state

			
		if self.the_thing:
			if not self.the_thing_revealed:
				self.reveal_the_thing()
		
			if target_object.destroyed:
				if not target_object == player:
					if target_object.unit:
						Message(target_object.name + ' has been absorbed.', 'Narrator', relevant_objects = [self.owner, target_object])
						
						# The thing gets more massive as it absorbs stuff -- strength will increase by default because weight has increased
						self.update_strength(self.strength * 2)
						
		if ACTIVATE_FUNCTION_TIMERS: end_test(attack_timer, self.owner.name + ' attacks')

		return True

	def player_speak_to(self, spoken_to_object):
		global all_dialogue_IDs

		all_dialogue = []

		for i in range(0, (len(all_dialogue_IDs))):
			all_dialogue.append(get_dialogue_by_ID(all_dialogue_IDs[i]).dialogue)
			if i >= 25:
				break

		if not spoken_to_object.unit:
			Message('Cant speak to an inanimate object.', 'Narrator', relevant_objects=[self.owner, spoken_to_object])
			return False

		nearest_objects = spoken_to_object.unit.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type='Non Affixed Objects', maximum_results = 26)
		nearest_units = spoken_to_object.unit.get_nearest_objects(range = MAX_VISIBILITY_RADIUS, type='Units', maximum_results = 26)

		object_moving_to = None
		object_to_interact_with = None
		object_source_of_task = None
		quantity = None

		task_message_ID = None

		task_options = ['Examine Object', 'Move to Object', 'Find and Collect Object', 'Attack Object', 'Fetch Object for Object', 'Take Object to Object', 'Deliver Message to Object', 'Tell me about yourself...']

		chosen_response_index = menu(spoken_to_object.name + ': What do you want me to do?', None, task_options)

		if chosen_response_index >= 0:
			chosen_response = task_options[chosen_response_index]

			if chosen_response == 'Move to Object' or chosen_response == 'Find and Collect Object' or chosen_response == 'Attack Object' or chosen_response == 'Examine Object':
				object_moving_to = prompt_to_choose_object(nearest_objects, chosen_response + "?")
				object_to_interact_with = object_moving_to
				if chosen_response == 'Find and Collect Object':
					quantity = prompt_for_quantity(object_to_interact_with)
				object_source_of_task = object_moving_to

			elif chosen_response == 'Fetch Object for Object':
				object_moving_to = prompt_to_choose_object(nearest_objects, "Which object do you want fetched?")
				object_to_interact_with = object_moving_to
				quantity = prompt_for_quantity(object_to_interact_with)
				object_source_of_task = prompt_to_choose_object(nearest_units, "Who are you delivering to?")

			elif chosen_response == 'Take Object to Object':
				object_to_interact_with = prompt_to_choose_object(self.owner.inventory, "Which object are you delivering?")
				quantity = prompt_for_quantity(object_to_interact_with)
				object_moving_to = prompt_to_choose_object(nearest_units, "Who are you delivering to?")

				if not object_to_interact_with:
					print 'Nothing in inventory.'
					return False
				else:
					spoken_to_object.take_object_from_inventory(self.owner, object_to_interact_with, quantity)
					
				object_source_of_task = object_moving_to

			elif chosen_response == 'Deliver Message to Object':
				object_moving_to = prompt_to_choose_object(nearest_units, "Who are you delivering to?")
				object_to_interact_with = object_moving_to
				object_source_of_task = object_moving_to
				task_message_index = menu("What do you want me to say?", None, all_dialogue)
				if task_message_index >= 0:
					task_message_ID = all_dialogue_IDs[task_message_index]
				else:
					print 'Did not give a message to deliver'
					return False
					
			elif chosen_response == 'Tell me about yourself...':
				spoken_to_object.unit.speak_to(player, given_dialogue = None, given_dialogue_ID = spoken_to_object.unit.backstory_dialogue)
				return True

			spoken_to_object.task_queue.append(Task(task_owner=spoken_to_object, task_type=chosen_response, object_source_of_task=object_source_of_task, object_moving_to=object_moving_to, object_to_interact_with=object_to_interact_with, search_range=MAX_VISIBILITY_RADIUS, task_message_ID=task_message_ID, quantity = quantity))
			return True

		return False
		
	def examine(self, examined_object):
		if libtcod.random_get_int(0, 0, 100) < CHANCE_OF_EXAMINE_SUCCESS_OUT_OF_100:
			if examined_object.unit:
				if examined_object.unit.the_thing:
					examined_object.unit.reveal_the_thing()
					Message(self.owner.name + ' takes a close look at ' + examined_object.name + "... it's THE THING!", 'Narrator', relevant_objects = [self.owner, examined_object])
					return True
		
		Message(self.owner.name + ' takes a close look at ' + examined_object.name + "... nothing unusual.", 'Narrator', relevant_objects = [self.owner, examined_object])

		if examined_object.unit:
			examined_object.unit.check_my_feelings_for(self.owner, adjust_by = EXAMINE_FEELINGS_CHANGE)
			
		return False
			
	

	def speak_to(self, spoken_to_object, given_dialogue = None, given_dialogue_ID = None):
		if ACTIVATE_FUNCTION_TIMERS: speak_timer = start_test()
		
		if given_dialogue:
			Message(self.owner.name + ' to ' + spoken_to_object.name + ': ' + given_dialogue, 'Dialogue', relevant_objects=[self.owner, spoken_to_object])
			if ACTIVATE_FUNCTION_TIMERS: end_test(speak_timer, self.owner.name + ' speaks')
		else:
			this_dialogue_object = None
			if given_dialogue_ID:
				this_dialogue_object = get_dialogue_by_ID(given_dialogue_ID)
			elif self.dialogue:
				my_feelings_for_object = self.check_my_feelings_for(spoken_to_object)
				dialogue_options = []
				for option in self.dialogue:
					option_object = get_dialogue_by_ID(option)
					if option_object.feelings_range:
						if option_object.feelings_range[0] > my_feelings_for_object or option_object.feelings_range[1] < my_feelings_for_object:
							continue
					dialogue_options.append(option_object)
				this_dialogue_object = pick_random(dialogue_options)
			
			if not this_dialogue_object:
				return False

			actual_dialogue = str(this_dialogue_object.dialogue)
			Message(self.owner.name + ' to ' + spoken_to_object.name + ': ' + actual_dialogue, 'Dialogue', relevant_objects = [self.owner, spoken_to_object])

			if spoken_to_object == player:
				response_ID = prompt_to_choose_dialogue(this_dialogue_object, speaker_object = self.owner)
			else:
				response_ID = prompt_to_choose_dialogue(this_dialogue_object, pick_a_random_response = True, speaker_object = self.owner)
				
			if ACTIVATE_FUNCTION_TIMERS: end_test(speak_timer, self.owner.name + ' replies')

			if response_ID:

				response_dialogue_object = get_dialogue_by_ID(response_ID)
				response_dialogue_actual_dialogue = response_dialogue_object.dialogue
				Message(spoken_to_object.name + ' to ' + self.owner.name + ': ' + response_dialogue_actual_dialogue, 'Dialogue', relevant_objects = [self.owner, spoken_to_object])

				if this_dialogue_object.task_based_on_responses:
					if response_ID in this_dialogue_object.task_based_on_responses:
						given_task = this_dialogue_object.task_based_on_responses[response_ID]
						if given_task:
							self.owner.task_queue.append(Task(task_owner = self.owner, task_type = given_task[0], object_source_of_task = spoken_to_object, object_moving_to = given_task[1], object_to_interact_with = given_task[1], search_range = MAX_VISIBILITY_RADIUS))
							if ACTIVATE_FUNCTION_TIMERS: end_test(speak_timer, self.owner.name + ' final nested reply')
														   
							

	def get_nearest_objects(self, range, type = None, maximum_results = None, sort_by_distance = True, see_through_walls = False):
		global units, affixed_objects, non_affixed_objects, fov_map

		if not type:
			print 'need to specify a type for get nearest objects'
			return False

		if type == 'Units':
			chose_type_of_objects = units
		elif type == 'Affixed Objects':
			chose_type_of_objects = affixed_objects
		elif type == 'Non Affixed Objects':
			chose_type_of_objects = non_affixed_objects
		else:
			return False

		nearby_objects_and_distance = []
		
		if not see_through_walls:
			libtcod.map_compute_fov(fov_map, self.owner.x, self.owner.y, range, FOV_LIGHT_WALLS, FOV_ALGO)
				
		
		for visible_object in chose_type_of_objects:
		
			# Won't return dead units when looking for units
			if type == 'Units' and visible_object.destroyed:
				continue
				
			# Won't return itself
			if visible_object == self.owner:
				continue
				
			if see_through_walls:
				# BIG EFFICIENCY PROBLEMS WITH THIS debug
				visible = (visible_object.x >= self.owner.x - range and visible_object.x <= self.owner.x + range and visible_object.y >= self.owner.y - range and visible_object.y <= self.owner.y + range)
			else:
				visible = libtcod.map_is_in_fov(fov_map, visible_object.x, visible_object.y)
			
			if visible:
			
				distance_to_visible_object = self.owner.distance_to(visible_object)
				nearby_objects_and_distance.append([distance_to_visible_object, visible_object])
				
				
			if maximum_results and not sort_by_distance:
				if len(nearby_objects_and_distance) >= maximum_results:
					break

		if sort_by_distance:
			from operator import itemgetter
			nearby_objects_and_distance = sorted(nearby_objects_and_distance, key = itemgetter(0))
			
		final_list_sorted_by_distance = []
		for object in nearby_objects_and_distance:
			final_list_sorted_by_distance.append(object[1])
			if maximum_results:
				if len(final_list_sorted_by_distance) >= maximum_results:
					break

		return final_list_sorted_by_distance


	def pick_up(self, object_to_pick_up, quantity = None):
	
		if not quantity:
			quantity = 1
	
		if not object_to_pick_up:
			return False
			
		if object_to_pick_up.unit:
			Message('Cannot add units to inventory,', 'Narrator', relevant_objects=[self.owner, object_to_pick_up])
			return False
			
		# If currently holding an object, put it down
		self.let_go()
			
		# Units can pick up and put in iventory items that are 50% the weight of what they can drag
		if not self.owner.can_i_perform_task(object_to_pick_up, 'Lift'):
			Message(object_to_pick_up.name + ' is too heavy for ' + self.owner.name + ' to pick up.', 'Action', relevant_objects=[self.owner, object_to_pick_up])
			return False
		
		if self.owner.my_total_weight(inventory_only = True) + (object_to_pick_up.weight * quantity) > self.owner.weight:
			Message(object_to_pick_up.name + ' is already carrying too much to pick up ' + object_to_pick_up.name + '.', 'Action', relevant_objects=[self.owner, object_to_pick_up])
			return False
			
		
			
		picked_up_object = self.owner.add_to_inventory(object_to_pick_up, quantity = quantity)
	
		if picked_up_object:
			Message(self.owner.name + ' adds ' + object_to_pick_up.name + ' to inventory.', 'Narrator', relevant_objects = [self.owner, object_to_pick_up])
			return picked_up_object
			
		return False


	def drop(self, object_to_drop, quantity = None):
	
		if not object_to_drop:
			return False
			
		# If currently holding an object, put it down
		self.let_go()
			
		dropped_object = self.owner.remove_from_inventory(object_to_drop, quantity = quantity)
	
		if dropped_object:
			place_object_at_location(dropped_object, self.owner.x, self.owner.y, stack_objects_allowed = True, force_placement_success = True)
			return dropped_object
			
		return False
	

	def grab(self, object_to_grab, quantity = None):
	
		if not object_to_grab:
			return False
		
		object_to_grab = object_to_grab.take_from_stack(quantity)
		place_object_at_location(object_to_grab, object_to_grab.x, object_to_grab.y, stack_objects_allowed = False, force_placement_success = True)
			
		self.holding = object_to_grab
		object_to_grab.held_by = self.owner
		return True

	def let_go(self):
		if self.holding:
			self.holding.held_by = None
		self.holding = None
		return True

	def equip(self, equipped_object):
	
		# Unequip
		if self.owner.equipped == equipped_object:
			self.owner.equipped.equipped_to = None
			self.owner.equipped = self.owner.unit.rarm
			return True
			
		if equipped_object in self.owner.inventory:
			self.owner.equipped = equipped_object
			equipped_object.equipped_to = self.owner
			return True
		else:
			Message('Cannot equip item unless in inventory.', 'Action', relevant_objects=[self.owner, equipped_object])

		return False


def calculate_velocity(throw_weight, weight):
	velocity = int(throw_weight / weight)
	return velocity
	
def calculate_damage(object_source, object_receive, velocity):
		total_damage = float(object_source.weight * velocity)
		
		damage_resistance_due_to_weight = float(object_receive.weight / 1000.0)
		damage_resistance_due_to_resistance = float(get_material_stats_by_name(object_receive.material, 'Break Resistance') / 100.0)
		
		total_damage -= (total_damage * damage_resistance_due_to_weight)
		total_damage -= (total_damage * damage_resistance_due_to_resistance)
			
		return total_damage
			

def process_collision(moving_object, collided_object, velocity, test = False):
	global impact_sound

	if ACTIVATE_FUNCTION_TIMERS: collision_timer = start_test()

	raw_collided_object_damage = 0
	raw_moving_object_damage = 0
	
	if not collided_object.indestructible:
		raw_collided_object_damage = calculate_damage(object_source = moving_object, object_receive = collided_object, velocity = velocity)
	
	if test:
		return normalize_damage(raw_collided_object_damage)
	
	if not moving_object.indestructible:
		raw_moving_object_damage = calculate_damage(object_source = collided_object, object_receive = moving_object, velocity = velocity)

	if moving_object.quantity > 1:
		original_x = moving_object.x
		original_y = moving_object.y
		moving_object = moving_object.take_from_stack(1)
		place_object_at_location(moving_object, original_x, original_y, stack_objects_allowed = False)

	if collided_object.quantity > 1:
		collided_object = collided_object.take_from_stack(1)
		place_object_at_location(collided_object, moving_object.x, moving_object.y, stack_objects_allowed = False)
	
	collided_object_damage = normalize_damage(raw_collided_object_damage)
	moving_object_damage = normalize_damage(raw_moving_object_damage)

	collided_object.condition -= collided_object_damage
	moving_object.condition -= moving_object_damage

	if libtcod.map_is_in_fov(fov_map, collided_object.x, collided_object.y):
		impact_sound.play()
	Message(moving_object.name + ' collides with ' + collided_object.name + '. ' + moving_object.name + ' takes ' + str(moving_object_damage) + ' damage and ' + collided_object.name + ' takes ' + str(collided_object_damage) + ' damage.', 'Action', relevant_objects = [collided_object, moving_object])
	
	collided_object.check_if_destroyed(impact_force = raw_collided_object_damage)
	moving_object.check_if_destroyed(impact_force = raw_moving_object_damage)
	
	if ACTIVATE_FUNCTION_TIMERS: end_test(collision_timer, moving_object.name + ' process collision')

	return True

def normalize_damage(total_damage):
	if total_damage < MINIMUM_DAMAGE_TO_REGISTER:
		total_damage = 0
	elif total_damage > MAXIMUM_DAMAGE_ALLOWED:
		total_damage = MAXIMUM_DAMAGE_ALLOWED
	else:
		total_damage = int(total_damage)
	return total_damage
	
def get_map_tile(x, y, direction):
	if direction == 'C':
		return map[x][y]
	elif direction == 'R':
		right = map[x + 1][y]
	elif direction == 'L':
		left = map[x - 1][y]
	elif direction == 'U':
		up = map[x][y - 1]
	elif direction == 'D':
		down = map[x][y + 1]
	elif direction == 'UR':
		upright = map[x + 1][y - 1]
	elif direction == 'UL':
		upleft = map[x - 1][y - 1]
	elif direction == 'DR':
		downright = map[x + 1][y + 1]
	elif direction == 'DL':
		downleft = map[x - 1][y + 1]
	return False
	

def search_for_door_locations():
	global map
	for x in range(MAP_WIDTH - 1):
		for y in range(MAP_HEIGHT - 1):

			door_chance = 100

			centre = map[x][y]
			right = map[x + 1][y]
			left = map[x - 1][y]
			up = map[x][y - 1]
			down = map[x][y + 1]
			upright = map[x + 1][y - 1]
			upleft = map[x - 1][y - 1]
			downright = map[x + 1][y + 1]
			downleft = map[x - 1][y + 1]

			# right
			if not centre.wall and not right.wall and not upright.wall and not downright.wall and not left.wall and up.wall and down.wall and downleft.wall and upleft.wall:
				if right.room_name != 'Hallway' and libtcod.random_get_int(0, 0, 100) <= door_chance:
					place_object_at_location(get_object_by_name('Door'), x, y)
			# left
			if not centre.wall and not left.wall and not upleft.wall and not downleft.wall and not right.wall and up.wall and down.wall and downright.wall and upright.wall:
				if left.room_name != 'Hallway' and libtcod.random_get_int(0, 0, 100) <= door_chance:
					place_object_at_location(get_object_by_name('Door'), x, y)
			# up
			if not centre.wall and not up.wall and not upright.wall and not upleft.wall and not down.wall and left.wall and right.wall and downleft.wall and downright.wall:
				if up.room_name != 'Hallway' and libtcod.random_get_int(0, 0, 100) <= door_chance:
					place_object_at_location(get_object_by_name('Door'), x, y)
			# down
			if not centre.wall and not down.wall and not downright.wall and not downleft.wall and not up.wall and left.wall and right.wall and upleft.wall and upright.wall:
				if down.room_name != 'Hallway' and libtcod.random_get_int(0, 0, 100) <= door_chance:
					place_object_at_location(get_object_by_name('Door'), x, y)


def get_adjacent_stuff(x, y, what_im_looking_for, include_diagonals=False, include_centre=False):

	return_array = []

	# Looking outside the map
	if x >= MAP_WIDTH - 1 or x <= 1 or y >= MAP_HEIGHT - 1 or y <= 1:
		return return_array
	
	centre = map[x][y]
	right = map[x + 1][y]
	left = map[x - 1][y]
	up = map[x][y - 1]
	down = map[x][y + 1]
	upright = map[x + 1][y - 1]
	upleft = map[x - 1][y - 1]
	downright = map[x + 1][y + 1]
	downleft = map[x - 1][y + 1]

	if what_im_looking_for == 'Room Names':
		if include_centre:
			return_array.append(centre.room_name)
		return_array.append(right.room_name)
		return_array.append(down.room_name)
		return_array.append(left.room_name)
		return_array.append(up.room_name)
	elif what_im_looking_for == 'Objects':
		if include_centre:
			for object in centre.objects_on_this_tile: return_array.append(object)
		for object in right.objects_on_this_tile: return_array.append(object)
		for object in down.objects_on_this_tile: return_array.append(object)
		for object in left.objects_on_this_tile: return_array.append(object)
		for object in up.objects_on_this_tile: return_array.append(object)

	if include_diagonals:
		if what_im_looking_for == 'Room Names':
			return_array.append(upright.room_name)
			return_array.append(upleft.room_name)
			return_array.append(downright.room_name)
			return_array.append(downleft.room_name)
		elif what_im_looking_for == 'Objects':
			for object in upright.objects_on_this_tile: return_array.append(object)
			for object in upleft.objects_on_this_tile: return_array.append(object)
			for object in downright.objects_on_this_tile: return_array.append(object)
			for object in downleft.objects_on_this_tile: return_array.append(object)

	return return_array


def pick_random(options):
	if len(options) == 0:
		return False
	random_choice = libtcod.random_get_int(0, 0, len(options) - 1)
	return options[random_choice]
	
def pick_largest(list_of_objects, exclude_units = False):
	if len(list_of_objects) == 0:
		return False
	largest_object = None
		
	for object in list_of_objects:
		if not largest_object: largest_object = object
		
		if object.size > largest_object.size:
			largest_object = object

	return largest_object
	



def try_to_stack(list_of_objects, new_object):
	if new_object.stackable:
		for object in list_of_objects:
			if object.name == new_object.name:
				if object.weight == new_object.weight:
					if object.condition == new_object.condition:
						if object.material == new_object.material:
							if object.size == new_object.size:
								object.quantity += new_object.quantity
								remove_all_connections_to_object(new_object)
								del new_object
								return object
	return False


def place_object_at_location(object_to_place, x, y, stack_objects_allowed = True, force_placement_success = False):
	global map, affixed_objects, non_affixed_objects, units, temporary_obstacles, light_sources

	remove_all_connections_to_object(object_to_place)
	
	stacked_object = None
	
	if stack_objects_allowed:
		stacked_object = try_to_stack(map[x][y].objects_on_this_tile, object_to_place)
	
	if stacked_object:
		return stacked_object
	
	if not force_placement_success:
		blocking_object = is_blocked(x, y, check_against_object = object_to_place)
		
		attempts = 5
		while(blocking_object and attempts > 0):
			dx = libtcod.random_get_int(0, -1, 1)
			dy = libtcod.random_get_int(0, -1, 1)
			blocking_object = is_blocked(x + dx, y + dy, check_against_object = object_to_place)
			if not blocking_object:
				x = x + dx
				y = y + dy
			attempts -= 1
			
	object_to_place.x = x
	object_to_place.y = y
	
	
	if object_to_place.name == 'Generic Humanoid Obstacle' or object_to_place.name == 'Generic Wall Obstacle':
		temporary_obstacles.append(object_to_place)
		
	if object_to_place.light_source:
		light_sources.append(object_to_place)
	
	if object_to_place.unit:
		units.append(object_to_place)
	elif object_to_place.affixed_to_ground:
		affixed_objects.append(object_to_place)
	elif not object_to_place.affixed_to_ground:
		non_affixed_objects.append(object_to_place)
	else:
		return False
		
	map[x][y].objects_on_this_tile.append(object_to_place)
	
	object_to_place.move_inventory_coords_to_location(x, y)
	
	return object_to_place


def remove_all_connections_to_object(object_to_remove):
	global map, affixed_objects, non_affixed_objects, units, light_sources
	
	if not object_to_remove.x and not object_to_remove.y:
		return True

	object_to_remove.held_by = None

	if object_to_remove.equipped_to:
		object_to_remove.equipped_to.equipped = None
		object_to_remove.equipped_to = None

	if object_to_remove.in_inventory_of:
		if object_to_remove in object_to_remove.in_inventory_of.inventory:
			object_to_remove.in_inventory_of.inventory.remove(object_to_remove)
		object_to_remove.in_inventory_of = None
	elif object_to_remove in map[object_to_remove.x][object_to_remove.y].objects_on_this_tile:
		
		map[object_to_remove.x][object_to_remove.y].objects_on_this_tile.remove(object_to_remove)
		
		if object_to_remove in light_sources:
			light_sources.remove(object_to_remove)
	
		if object_to_remove.unit:
			units.remove(object_to_remove)
		elif object_to_remove.affixed_to_ground:
			affixed_objects.remove(object_to_remove)
		elif not object_to_remove.affixed_to_ground:
			non_affixed_objects.remove(object_to_remove)
		else:
			return False

	return True


def get_vector_toward(base_object, target_x, target_y):
	dx = target_x - base_object.x
	dy = target_y - base_object.y
	distance = math.sqrt(dx ** 2 + dy ** 2)

	if distance == 0:
		dx = 0
		dy = 0
	else:
		# normalize it to length 1 (preserving direction), then round it and
		# convert to integer so the movement is restricted to the map grid
		dx = int(round(dx / distance))
		dy = int(round(dy / distance))

	return (dx, dy)


def random_place_object(object):
	global map
	object_placed = False
	
	test_wall = get_predesigned_object_by_name('Wall')

	while not object_placed:

		x = libtcod.random_get_int(0, 2, MAP_WIDTH - 2)
		y = libtcod.random_get_int(0, 2, MAP_HEIGHT - 2)
		if not is_blocked(x, y, check_against_object = object):
		
			object_placed = True
		
			# If the object will block people...
			if object.size + test_wall.size >= 10:
			
				adjacent_open_spaces = 8
			
				if is_blocked(normalize_to_map_width(x + 1), normalize_to_map_height(y), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x - 1), normalize_to_map_height(y), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x), normalize_to_map_height(y - 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x), normalize_to_map_height(y + 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x + 1), normalize_to_map_height(y - 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x - 1), normalize_to_map_height(y - 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x + 1), normalize_to_map_height(y + 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				if is_blocked(normalize_to_map_width(x - 1), normalize_to_map_height(y + 1), check_against_object = test_wall): adjacent_open_spaces -= 1
				
				if adjacent_open_spaces < 6:
					print 'cannot place object it blocks the path'
					object_placed = False
					
			if object_placed:
				place_object_at_location(object, x, y)
					
	return True


def process_action(action_being_taken, object_taking_action=None, object_being_actioned=None, object_being_targeted=None):
	if object_being_targeted:
		if action_being_taken == 'Throw':
			pass
		else:
			quantity = prompt_for_quantity(object_being_targeted)
	if action_being_taken == 'Pick Up':
		return object_taking_action.unit.pick_up(object_being_targeted, quantity)
	elif action_being_taken == 'Grab':
		return object_taking_action.unit.grab(object_being_targeted)
	elif action_being_taken == 'Release':
		return object_taking_action.unit.let_go()
	elif action_being_taken == 'Drop':
		return object_taking_action.unit.drop(object_being_targeted, quantity)
	elif action_being_taken == 'Consume':
		return object_taking_action.unit.consume(object_being_targeted)
	elif action_being_taken == 'Attack':
		return object_taking_action.unit.attack(target_object_or_tile = object_being_targeted)
	elif action_being_taken == 'Give Object':
		if object_being_targeted.check_if_unlocked():
			selected_object = prompt_to_choose_object(object_taking_action.inventory)
			if selected_object:
				quantity = prompt_for_quantity(selected_object)
				return object_being_targeted.take_object_from_inventory(object_taking_action, selected_object, quantity)
	elif action_being_taken == 'Take Object':
		if object_being_targeted.check_if_unlocked():
			selected_object = prompt_to_choose_object(object_being_targeted.inventory)
			if selected_object:
				quantity = prompt_for_quantity(selected_object)
				return object_taking_action.take_object_from_inventory(object_being_targeted, selected_object, quantity)
			else:
				Message(object_being_targeted.name + ' has no inventory.', 'Action', relevant_objects=[object_being_targeted])
	elif action_being_taken == 'Throw':
		return object_taking_action.throw(object_being_targeted)
	elif action_being_taken == 'Open / Close':
		return object_taking_action.open_close(object_being_targeted)
	elif action_being_taken == 'Lock / Unlock':
		return object_taking_action.lock_unlock(object_being_targeted)
	elif action_being_taken == 'Equip':
		return object_taking_action.unit.equip(object_being_targeted)
	elif action_being_taken == 'Speak':
		return object_taking_action.unit.player_speak_to(object_being_targeted)
	elif action_being_taken == 'Examine':
		return object_taking_action.unit.examine(object_being_targeted)
	elif action_being_taken == 'Activate / Deactivate':
		return object_taking_action.toggle_on_off(object_being_targeted)
	return False


def is_blocked(x, y, check_against_object = None, random_collision_chance = False):
	if len(map[x][y].objects_on_this_tile) == 0:
		return False

	if check_against_object:
		check_against_object_size = check_against_object.size
	else:
		check_against_object_size = 0
	
	total_size = 0
	collision_options = []

	for object in map[x][y].objects_on_this_tile:
		total_size += object.size
		for i in range(0, int(object.size)):
			collision_options.append(object)
		
	if total_size + check_against_object_size > 10:
		return pick_random(collision_options)
		
	if random_collision_chance:
		empty_space_remaining = int(10 - total_size - check_against_object_size)
		if empty_space_remaining < 0: empty_space_remaining = 0
	
	
		for i in range(0, empty_space_remaining):
			collision_options.append(None)
		
		# Chance of hitting an object, or 'None'
		return pick_random(collision_options)

	return False


def create_room(room):
	global map
	global lab_rooms
	# go through the tiles in the rectangle and make them passable
	for x in range(room.x1, room.x2):
		for y in range(room.y1, room.y2):
			map[x][y].wall = False
			map[x][y].char = '.'
			if lab_rooms:
				map[x][y].room_name = lab_rooms[0]
			else:
				map[x][y].room_name = 'Empty Room'
	if lab_rooms:
		room.name = lab_rooms[0]
		del lab_rooms[0]


def create_h_tunnel(x1, x2, y):
	global map
	# horizontal tunnel. min() and max() are used in case x1>x2
	for x in range(min(x1, x2), max(x1, x2) + 1):
		map[x][y].wall = False
		map[x][y].char = '.'
		if not map[x][y].room_name:
			map[x][y].room_name = 'Hallway'


def create_v_tunnel(y1, y2, x):
	global map
	# vertical tunnel
	for y in range(min(y1, y2), max(y1, y2) + 1):
		map[x][y].wall = False
		map[x][y].char = '.'
		if not map[x][y].room_name:
			map[x][y].room_name = 'Hallway'


def convert_wall_tiles_into_objects():
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			if map[x][y].wall:
				generic_wall = get_object_by_name('Wall')
				map[x][y].wall = False
				map[x][y].char = '.'
				map[x][y].room_name = 'Wall'
				place_object_at_location(generic_wall, x, y)


def make_map():
	global map, affixed_objects, non_affixed_objects, units, lab_rooms, rooms

	# fill map with "wall" tiles
	map = [[Tile(True) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			map[x][y].x = x
			map[x][y].y = y

	# the list of objects and units ready to fill
	affixed_objects = []
	non_affixed_objects = []
	units = []
	

	rooms = []
	num_rooms = 0

	for r in range(MAX_ROOMS):
		# random width and height
		w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		# random position without going out of the boundaries of the map
		x = libtcod.random_get_int(0, 3, MAP_WIDTH - w - 3)
		y = libtcod.random_get_int(0, 3, MAP_HEIGHT - h - 3)

		# "Rect" class makes rectangles easier to work with
		new_room = Rect(x, y, w, h)

		# run through the other rooms and see if they intersect with this one
		failed = False
		for other_room in rooms:
			if new_room.intersect(other_room):
				failed = True
				break

		if not failed:
			# this means there are no intersections, so this room is valid

			# "paint" it to the map's tiles
			create_room(new_room)

			# center coordinates of new room, will be useful later
			(new_x, new_y) = new_room.center()

			# all rooms after the first:
			# connect it to the previous room with a tunnel

			if num_rooms > 0:
				# center coordinates of previous room
				(prev_x, prev_y) = rooms[num_rooms - 1].center()

				# draw a coin (random number that is either 0 or 1)
				if libtcod.random_get_int(0, 0, 1) == 1:
					# first move horizontally, then vertically
					create_h_tunnel(prev_x, new_x, prev_y)
					create_v_tunnel(prev_y, new_y, new_x)
				else:
					# first move vertically, then horizontally
					create_v_tunnel(prev_y, new_y, prev_x)
					create_h_tunnel(prev_x, new_x, new_y)

			# finally, append the new room to the list
			rooms.append(new_room)
			num_rooms += 1


def place_objects(room, room_type):
	room_type_object = get_room_type_by_name(room_type)

	for stuff_to_place in room_type_object.objects_in_room:

		object_or_group = stuff_to_place['object_or_group']
		object_or_group_name = stuff_to_place['name_of_object_or_group']
		object_or_group_quantity = libtcod.random_get_int(0, stuff_to_place['minimum_quantity'], stuff_to_place['maximum_quantity'])

		for i in range(0, object_or_group_quantity):

			if object_or_group == 'Group':

				number_of_attempts = 0

				while (number_of_attempts < MAX_ATTEMPTS_TO_PLACE_OBJECTS):

					placements_to_make_if_success = []

					this_object_group = get_object_group_by_name(object_or_group_name)

					random_rotations = libtcod.random_get_int(0, 0, 3)

					for useless_variable in range(0, random_rotations):
						this_object_group.rotate()

					max_x = room.x2 - this_object_group.width
					max_y = room.y2 - this_object_group.height

					if max_x <= room.x1 or max_y <= room.y1:
						print 'This room is too small to fit ' + object_or_group_name
						break

					x = None
					y = None

					if this_object_group.place_against_wall == 'Left':
						x = room.x1
					elif this_object_group.place_against_wall == 'Right':
						x = max_x
					elif this_object_group.place_against_wall == 'Top':
						y = room.y1
					elif this_object_group.place_against_wall == 'Bottom':
						y = max_y

					if not x: x = libtcod.random_get_int(0, room.x1 + 1, max_x)
					if not y: y = libtcod.random_get_int(0, room.y1 + 1, max_y)

					all_clear = True

					for width_traverse in range(0, this_object_group.width):
						for height_traverse in range(0, this_object_group.height):
							# Doesn't allow object group to be placed next to a hallway
							if 'Hallway' in get_adjacent_stuff(x + width_traverse, y + height_traverse, 'Room Names'):
								reason_for_failure = 'Collision with hallway.'
								all_clear = False
								break

							current_character = this_object_group.grid[height_traverse][width_traverse]
							
							if current_character == '_':
								continue
							
							for object_traverse in this_object_group.object_map:
							
								for j in range(0, len(object_traverse)):
									
									if j == 0 and object_traverse[j] <> current_character:
										break
									elif j == 0:
										continue
										
									potential_object = get_object_specific_instance_by_tag(object_traverse[j])

									collision_check = is_blocked(x + width_traverse, y + height_traverse, potential_object)
									
									if collision_check:
										all_clear = False
										break
									
									placements_to_make_if_success.append([potential_object, x + width_traverse, y + height_traverse])
								
								if not all_clear:
									break
										
							if not all_clear:
								break
								
						if not all_clear:
							break

					if all_clear:
						break
					else:
						number_of_attempts += 1
						placements_to_make_if_success = []

				if number_of_attempts >= MAX_ATTEMPTS_TO_PLACE_OBJECTS:
					if MORE_ERROR_LOGGING:
						print 'Failed to place ' + object_or_group_name
						print 'Reason for failure: ' + reason_for_failure
						print ''
					continue

				else:
					# Create the group of objects
					for placement in placements_to_make_if_success:
						place_object_at_location(placement[0], placement[1], placement[2], stack_objects_allowed = False, force_placement_success = True)

			elif object_or_group == 'Object':

				placed_object = get_object_by_name(object_or_group_name)

				number_of_attempts = 0
				while (number_of_attempts < MAX_ATTEMPTS_TO_PLACE_OBJECTS):
					x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
					y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
					if not is_blocked(x, y, placed_object):
						break

					number_of_attempts += 1

				if number_of_attempts >= MAX_ATTEMPTS_TO_PLACE_OBJECTS:
					print 'Failed to place ' + placed_object.name
					return False

				place_object_at_location(placed_object, x, y)

	return True


def render_bar(x, y, chosen_panel, total_width, name, value, maximum, bar_colour, back_colour):
	# render a bar (HP, experience, etc). first calculate the width of the bar
	bar_width = int(float(value) / maximum * total_width)

	# render the background first
	libtcod.console_set_default_background(chosen_panel, back_colour)
	libtcod.console_rect(chosen_panel, x, y, total_width, 1, False, libtcod.BKGND_SCREEN)

	# now render the bar on top
	libtcod.console_set_default_background(chosen_panel, bar_colour)
	if bar_width > 0:
		libtcod.console_rect(chosen_panel, x, y, bar_width, 1, False, libtcod.BKGND_SCREEN)

	# finally, some centered text with the values
	libtcod.console_set_default_foreground(chosen_panel, libtcod.white)
	libtcod.console_print_ex(chosen_panel, x + total_width / 2, y, libtcod.BKGND_NONE, libtcod.CENTER,
							 name + ': ' + str(value) + '/' + str(maximum))


def get_objects_under_mouse():
	global mouse
	# return a string with the names of all objects under the mouse

	(x, y) = (mouse.cx, mouse.cy)
	if x < MAP_WIDTH and y < MAP_HEIGHT:
		objects_under_mouse = [obj for obj in map[x][y].objects_on_this_tile]
		return objects_under_mouse
	else:
		return False
		
def room_name_under_mouse():
	global mouse
	# return a string with the names of all objects under the mouse

	(x, y) = (mouse.cx, mouse.cy)
	if x < MAP_WIDTH and y < MAP_HEIGHT:
		room_name = str(map[x][y].room_name)
		return room_name
	else:
		return False


def start_test():
	test_starts = time.time()
	return test_starts


def end_test(time_variable, function_name):
	if DONT_TIME_LOOPS and '(loop)' in function_name:
		return False
		
	now = time.time()
	if float(now - time_variable) > MINIMUM_PROCESS_TIME_TO_ALERT:
		print("{0} seconds".format(round(now - time_variable, 2))) + ' to run ' + function_name

def render_all():
	global fov_map
	global fov_recompute
	global clicked_object_name
	global panel
	global map
	global message_scroll_button
	global message_scroll_state
	global light_source_fov_maps
	global light_sources
	global player
	
	if not player: libtcod.console_clear(con)

	if fov_recompute:
		# recompute FOV if needed (the player moved or something)
		initialize_fov()
		fov_recompute = False
		
		if not SHOW_ALL:
			for y in range(MAP_HEIGHT):
				for x in range(MAP_WIDTH):
					map[x][y].illuminated = False
					map[x][y].illuminated_left = False
					map[x][y].illuminated_down = False
					map[x][y].illuminated_right = False
					map[x][y].illuminated_up = False
					

			for light_source in light_sources:
				if light_source.distance_to(player) <= MAX_VISIBILITY_RADIUS + light_source.light_radius:
					libtcod.map_compute_fov(fov_map, light_source.x, light_source.y, light_source.light_radius, FOV_LIGHT_WALLS, FOV_ALGO)
					
					up_offset = 0
					down_offset = 0
					left_offset = 0
					right_offset = 0
					
					if light_source.light_source == 'Directional':

						if light_source.direction == 'Up':
							up_offset = light_source.light_radius - 1
						elif light_source.direction == 'Down':
							down_offset = light_source.light_radius
						elif light_source.direction == 'Left':
							left_offset = light_source.light_radius - 1
						elif light_source.direction == 'Right':
							right_offset = light_source.light_radius
						else:
							print 'Should not get here ' + light_source.name
					
					for y in range(normalize_to_map_height(light_source.y - light_source.light_radius + down_offset), normalize_to_map_height(light_source.y + light_source.light_radius - up_offset + 1)):
						for x in range(normalize_to_map_width(light_source.x - light_source.light_radius + right_offset), normalize_to_map_width(light_source.x + light_source.light_radius - left_offset + 1)):
							
							x_normalized_around_zero = light_source.x - x
							y_normalized_around_zero = light_source.y - y
							
							if light_source.light_source == 'Directional':
								if up_offset or down_offset:
									if abs(x_normalized_around_zero) >= abs(y_normalized_around_zero) and abs(x_normalized_around_zero) > 0:
										continue
								elif left_offset or right_offset:
									if abs(y_normalized_around_zero) >= abs(x_normalized_around_zero) and abs(y_normalized_around_zero) > 0:
										continue
									
							visible = libtcod.map_is_in_fov(fov_map, x, y)
							if visible:

								map[x][y].illuminated = True

								if len(map[x][y].objects_on_this_tile) > 0:
									if map[x][y].check_blocks_sight():
										right_blocked = map[x + 1][y].check_blocks_sight()
										down_blocked = map[x][y + 1].check_blocks_sight()
										left_blocked = map[x - 1][y].check_blocks_sight()
										up_blocked = map[x][y - 1].check_blocks_sight()
										
										map[x][y].illuminated = False
										if light_source.x > x and not right_blocked: map[x][y].illuminated_right = True
										if light_source.y > y and not down_blocked: map[x][y].illuminated_down = True
										if light_source.x < x and not left_blocked: map[x][y].illuminated_left = True
										if light_source.y < y and not up_blocked: map[x][y].illuminated_up = True

						
		libtcod.map_compute_fov(fov_map, player.x, player.y, MAX_VISIBILITY_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)
			
		for y in range(MAP_HEIGHT):
			for x in range(MAP_WIDTH):
				map[x][y].render_me()

	# Prepare the four panels
	libtcod.console_print_frame(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, libtcod.BKGND_NONE, libtcod.CENTER, None)

	libtcod.console_set_default_foreground(panel, libtcod.white)
	libtcod.console_set_default_background(panel, libtcod.black)
	libtcod.console_clear(panel)
	libtcod.console_print_frame(panel, 0, 0, OBJECT_INFO_BAR_WIDTH, PANEL_HEIGHT, libtcod.BKGND_NONE, libtcod.CENTER, None)
	
	libtcod.console_set_default_foreground(object_panel, libtcod.white)
	libtcod.console_set_default_background(object_panel, libtcod.black)
	libtcod.console_clear(object_panel)
	libtcod.console_print_frame(object_panel, 0, 0, OBJECT_INFO_BAR_WIDTH, MAP_HEIGHT, libtcod.BKGND_NONE, libtcod.CENTER, "Object Info")
	
	libtcod.console_set_default_foreground(message_panel, libtcod.white)
	libtcod.console_set_default_background(message_panel, libtcod.black)
	libtcod.console_clear(message_panel)
	libtcod.console_print_frame(message_panel, 0, 0, MESSAGE_PANEL_WIDTH, PANEL_HEIGHT, libtcod.BKGND_NONE, libtcod.CENTER, None)
	
	if player:

		# show the player's stats
		render_bar(1, 1, panel, OBJECT_INFO_BAR_WIDTH - 2, 'Condition', player.condition, 100, libtcod.light_red, libtcod.darker_red)
		if player.equipped:
			libtcod.console_print_ex(panel, 1, 13, libtcod.BKGND_NONE, libtcod.LEFT, 'Equipped: ' + player.equipped.name)

		# display names of objects under the mouse
		libtcod.console_set_default_foreground(panel, libtcod.light_gray)
		objects_under_mouse = get_objects_under_mouse()
		room_name_here = room_name_under_mouse()
		if objects_under_mouse:
			libtcod.console_print_ex(panel, 1, 10, libtcod.BKGND_NONE, libtcod.LEFT, objects_under_mouse[0].name + ':' + str(objects_under_mouse[0].ID))
			libtcod.console_print_ex(panel, 1, 11, libtcod.BKGND_NONE, libtcod.LEFT, room_name_here)
			
		libtcod.console_print_ex(panel, 1, 12, libtcod.BKGND_NONE, libtcod.LEFT, 'my weight: ' + str(player.my_total_weight()))

		# display current room
		libtcod.console_print_ex(panel, 1, 14, libtcod.BKGND_NONE, libtcod.LEFT, 'Room: ' + str(map[player.x][player.y].room_name))

		libtcod.console_print_ex(panel, 1, 15, libtcod.BKGND_NONE, libtcod.LEFT, 'Grab: E')
		libtcod.console_print_ex(panel, 1, 16, libtcod.BKGND_NONE, libtcod.LEFT, 'Open/Close: R')
		libtcod.console_print_ex(panel, 1, 17, libtcod.BKGND_NONE, libtcod.LEFT, 'Pick Up: F')
		libtcod.console_print_ex(panel, 1, 18, libtcod.BKGND_NONE, libtcod.LEFT, 'Lock/Unlock: C')
		libtcod.console_print_ex(panel, 1, 19, libtcod.BKGND_NONE, libtcod.LEFT, 'Activate/Deactivate: V')
		libtcod.console_print_ex(panel, 1, 20, libtcod.BKGND_NONE, libtcod.LEFT, 'Attack: Right Click')
		
		if ACTIVATE_FUNCTION_TIMERS: game_message = start_test()
			
		# print the game messages, one line at a time
		y = MSG_HEIGHT - 1
		previous_ID = None
		previous_colour = None
		
		if message_scroll_button == 'Click Up':
			message_scroll_state += 1
		elif message_scroll_button == 'Click Down':
			message_scroll_state -= 1

		if message_scroll_state > len(game_msgs) - (PANEL_HEIGHT - 2): message_scroll_state = len(game_msgs) - (PANEL_HEIGHT - 2)
		if message_scroll_state < 0: message_scroll_state = 0

		for i in reversed(range(0, len(game_msgs) - message_scroll_state)):
			
			current_message = game_msgs[i]
			
			if current_message.ID <> previous_ID:
				if not current_message.colour:
					current_message.colour = current_message_colour(current_message.type)
			else:
				current_message.colour = previous_colour

			libtcod.console_set_default_foreground(message_panel, current_message.colour)
			libtcod.console_print_ex(message_panel, 1, y, libtcod.BKGND_NONE, libtcod.LEFT, current_message.text)
			current_message.y = MAP_HEIGHT + y

			y -= 1
			
			previous_ID = current_message.ID
			previous_colour = current_message.colour

			if y == 0:
				break
		
		if message_scroll_button == 'Highlight Up':
			libtcod.console_set_default_foreground(message_panel, libtcod.green)
		else: 
			libtcod.console_set_default_foreground(message_panel, libtcod.white)
		libtcod.console_print_ex(message_panel, MESSAGE_PANEL_WIDTH - 2, 1, libtcod.BKGND_NONE, libtcod.LEFT, '^')
		
		if message_scroll_button == 'Highlight Down':
			libtcod.console_set_default_foreground(message_panel, libtcod.green)
		else:
			libtcod.console_set_default_foreground(message_panel, libtcod.white)
		libtcod.console_print_ex(message_panel, MESSAGE_PANEL_WIDTH - 2, PANEL_HEIGHT - 2, libtcod.BKGND_NONE, libtcod.LEFT, 'V')
				
		if ACTIVATE_FUNCTION_TIMERS: end_test(game_message, 'printing game msgs')

		if selected_object:
			libtcod.console_print_ex(object_panel, 1, 3, libtcod.BKGND_NONE, libtcod.LEFT, 'Name: ' + selected_object.name )
			libtcod.console_print_ex(object_panel, 1, 4, libtcod.BKGND_NONE, libtcod.LEFT, 'ID: ' + str(selected_object.ID) )
			
			if selected_object.unit:
				libtcod.console_print_ex(object_panel, 1, 6, libtcod.BKGND_NONE, libtcod.LEFT, 'throw weight: ' + str(selected_object.unit.throw_weight))
				
			libtcod.console_print_ex(object_panel, 1, 7, libtcod.BKGND_NONE, libtcod.LEFT, 'Size: ' + str(selected_object.size) + ' ft')
			libtcod.console_print_ex(object_panel, 1, 9, libtcod.BKGND_NONE, libtcod.LEFT, 'Weight: ' + str(selected_object.weight) + ' lbs')
			libtcod.console_print_ex(object_panel, 1, 11, libtcod.BKGND_NONE, libtcod.LEFT, 'Material: ' + selected_object.material)
			libtcod.console_print_ex(object_panel, 1, 12, libtcod.BKGND_NONE, libtcod.LEFT, 'On Fire: ' + str(selected_object.on_fire))
			libtcod.console_print_ex(object_panel, 1, 13, libtcod.BKGND_NONE, libtcod.LEFT, 'stackable: ' + str(selected_object.stackable))
			libtcod.console_print_ex(object_panel, 1, 14, libtcod.BKGND_NONE, libtcod.LEFT, 'internal_kinetic_energy: ' + str(selected_object.internal_kinetic_energy))
			
			if selected_object.inventory:
				libtcod.console_print_ex(object_panel, 1, 15, libtcod.BKGND_NONE, libtcod.LEFT, 'inv: ' + selected_object.inventory[0].name)
				
			if selected_object.components:
				libtcod.console_print_ex(object_panel, 1, 16, libtcod.BKGND_NONE, libtcod.LEFT, 'comp: ' + selected_object.components[0])
				
			if selected_object.equipped:
				libtcod.console_print_ex(object_panel, 1, 17, libtcod.BKGND_NONE, libtcod.LEFT, 'equipped: ' + str(selected_object.equipped.name))
				
			libtcod.console_print_ex(object_panel, 1, 18, libtcod.BKGND_NONE, libtcod.LEFT, 'affixed: ' + str(selected_object.affixed_to_ground))

			if selected_object.task_queue:
				libtcod.console_print_ex(object_panel, 1, 20, libtcod.BKGND_NONE, libtcod.LEFT, 'task: ' + str(selected_object.task_queue[0].task_type))
				if selected_object.task_queue[0].object_source_of_task:
					libtcod.console_print_ex(object_panel, 1, 21, libtcod.BKGND_NONE, libtcod.LEFT, 'source: ' + str(selected_object.task_queue[0].object_source_of_task.name))
				if selected_object.task_queue[0].object_moving_to:
					libtcod.console_print_ex(object_panel, 1, 22, libtcod.BKGND_NONE, libtcod.LEFT, 'move to: ' + str(selected_object.task_queue[0].name_of_object_moving_to))
				if selected_object.task_queue[0].object_to_interact_with:
					libtcod.console_print_ex(object_panel, 1, 23, libtcod.BKGND_NONE, libtcod.LEFT, 'interact: ' + str(selected_object.task_queue[0].object_to_interact_with.name))
											 
			render_bar(1, 5, object_panel, OBJECT_INFO_BAR_WIDTH - 2, 'Cond', selected_object.condition, 100, libtcod.light_red, libtcod.darker_red)

			description = textwrap.wrap(selected_object.description, (OBJECT_INFO_BAR_WIDTH - 2))
			for i in range(0, len(description)):
				libtcod.console_print_ex(object_panel, 1, 29 + i, libtcod.BKGND_NONE, libtcod.LEFT, description[i])

	libtcod.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)
	libtcod.console_blit(panel, 0, 0, OBJECT_INFO_BAR_WIDTH, PANEL_HEIGHT, 0, 0, PANEL_Y)
	libtcod.console_blit(object_panel, 0, 0, OBJECT_INFO_BAR_WIDTH, MAP_HEIGHT, 0, MAP_WIDTH, 0)
	libtcod.console_blit(message_panel, 0, 0, MESSAGE_PANEL_WIDTH, PANEL_HEIGHT, 0, OBJECT_INFO_BAR_WIDTH,SCREEN_HEIGHT - PANEL_HEIGHT)
		
	libtcod.console_flush()
	

def menu(header, main_dialogue, options, clear_window_after_display=True):
	global key, mouse

	if not options:
		options = ['Empty']

	width = len(max(options, key = len)) + 8
	if len(header) + 8 > width:
		width = len(header) + 8

	if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')
	
	highlight_option = 0
	
	main_text_lines = []
	
	if main_dialogue:
	
		if len(main_dialogue.dialogue) > SCREEN_WIDTH / 2:
			width = int(SCREEN_WIDTH / 2) + 8
			
			lines = main_dialogue.dialogue.splitlines()
			
			for line in lines:
				main_text_lines.append('')
				line = line.strip()
				this_section = textwrap.wrap(line, int(SCREEN_WIDTH / 2), replace_whitespace = False)
				for section in this_section:
					main_text_lines.append(section)
		else:
			if len(main_dialogue.dialogue) > (width - 8):
				width = len(main_dialogue.dialogue) + 8
			main_text_lines.append(main_dialogue.dialogue)
	
	if not main_text_lines:
		main_text_height = 0
	else:
		main_text_height = len(main_text_lines) + 1
	
	# calculate total height for the header (after auto-wrap) and one line per option
	if not header:
		header_height = 0
	else:
		header_height = libtcod.console_get_height_rect(con, 0, 0, width, SCREEN_HEIGHT, header)
			
	height = len(options) + header_height + main_text_height + 2
			
	while True:

		# create an off-screen console that represents the menu's window
		window = libtcod.console_new(width, height)

		# print the header, with auto-wrap
		libtcod.console_set_default_foreground(window, libtcod.white)
		libtcod.console_print_frame(window, 0, 0, width, height, libtcod.BKGND_SET, libtcod.CENTER, header)
		
		y = header_height
		
		if main_text_lines:
			for single_line in main_text_lines:
				libtcod.console_print_ex(window, 2, y + 1, libtcod.BKGND_NONE, libtcod.LEFT, single_line)
				y += 1
			
			y += 1
		
		# print all the options
		letter_index = ord('a')
		for option_text in options:
			if y == highlight_option:
				libtcod.console_set_default_foreground(window, libtcod.light_green)

			text = '(' + chr(letter_index) + ') ' + option_text
			libtcod.console_print_ex(window, 2, y + 1, libtcod.BKGND_NONE, libtcod.LEFT, text)
			y += 1
			letter_index += 1
			libtcod.console_set_default_foreground(window, libtcod.white)

		# blit the contents of "window" to the root console
		x = MAP_WIDTH / 2 - width / 2
		y = MAP_HEIGHT / 2 - height / 2
		libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 1.0)

		# compute x and y offsets to convert console position to menu position
		x_offset = x + 2  # x is the left edge of the menu
		y_offset = y + header_height + main_text_height + 1  # subtract the height of the header from the top edge of the menu

		# present the root console to the player and check for input
		libtcod.console_flush()
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

		(menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)

		if menu_x >= 0 and menu_x < width - 4 and menu_y >= 0 and menu_y < height - 2:
			highlight_option = menu_y + main_text_height + 1

			if (mouse.lbutton_pressed):
				# check if click is within the menu and on a choice
				libtcod.console_delete(window)
				if clear_window_after_display: render_all()
				if menu_y < len(options):
					menu_click_sound.play()
					return menu_y
		else:
			highlight_option = None

		if mouse.rbutton_pressed:
			return None

		libtcod.console_delete(window)


def select_quantity_of_object(object, min, max):
	if not object:
		return False

	list_of_numbers = []
	for i in range(min, max + 1):
		list_of_numbers.append(str(i))

	chosen_number = menu("How many of " + object.name + "?", None, list_of_numbers)

	if chosen_number >= 0:
		return list_of_numbers[chosen_number]

	return 0


def conversation_handler():
	None


def handle_mouse():
	global key, selected_object, message_scroll_button
	
	(x, y) = (mouse.cx, mouse.cy)

	if x == MESSAGE_PANEL_WIDTH + OBJECT_INFO_BAR_WIDTH - 2 and y == MAP_HEIGHT + 1:
		message_scroll_button = 'Highlight Up'
		if (mouse.lbutton_pressed):
			message_scroll_button = 'Click Up'
			return False
	elif x == MESSAGE_PANEL_WIDTH + OBJECT_INFO_BAR_WIDTH - 2 and y == MAP_HEIGHT + PANEL_HEIGHT - 2:
		message_scroll_button = 'Highlight Down'
		if (mouse.lbutton_pressed):
			message_scroll_button = 'Click Down'
			return False
	else:
		message_scroll_button = None

	if (mouse.lbutton_pressed):
		if MORE_ERROR_LOGGING:
			print '---'
			print 'illu ' + str(map[x][y].illuminated)
			print 'up ' + str(map[x][y].illuminated_up)
			print 'down ' + str(map[x][y].illuminated_down)
			print 'right ' + str(map[x][y].illuminated_right)
			print 'left ' + str(map[x][y].illuminated_left)
			print '---'

		if y > MAP_HEIGHT and y < SCREEN_HEIGHT and x > OBJECT_INFO_BAR_WIDTH and x < SCREEN_WIDTH:
			# game_msgs
			for message in game_msgs:
				if message.y == y and x <= OBJECT_INFO_BAR_WIDTH + len(message.text):

					if message.relevant_objects:
						selected_object = prompt_to_choose_object(message.relevant_objects)

						# If you don't click on an object, the menu closes
						if not selected_object:
							return False

		if x < MAP_WIDTH and y < MAP_HEIGHT:

			objects_at_location = []

			for obj in map[x][y].objects_on_this_tile:
				if libtcod.map_is_in_fov(fov_map, obj.x, obj.y):
					objects_at_location.append(obj)

			if objects_at_location:
				selected_object = prompt_to_choose_object(objects_at_location)

				# If you don't click on an object, the menu closes
				if not selected_object:
					return False

				# If you do click an object, another context menu appears to decide what to do with it
				action_options = ['Attack', 'Pick Up', 'Grab', 'Release', 'Open / Close', 'Lock / Unlock', 'Give Object', 'Take Object', 'Throw', 'Equip', 'Speak', 'Examine', 'Activate / Deactivate']
				chosen_action = menu(selected_object.name, None, action_options)

				if player.distance_to(selected_object) > DISTANCE_TO_INTERACT:
					Message(selected_object.name + ' is too far away.', 'Action', relevant_objects=[selected_object])
					return False

				object_to_give = None
				if chosen_action >= 0:
					return process_action(action_options[chosen_action], object_taking_action=player, object_being_actioned=object_to_give, object_being_targeted=selected_object)
					


	elif (mouse.rbutton_pressed):
		if x < MAP_WIDTH and y < MAP_HEIGHT:
			# if you click the right mouse button while holding something you will throw it
			if player.unit.holding:
				return player.throw(player.unit.holding, map[x][y])
			elif player.equipped:
				return player.unit.attack(target_object_or_tile = map[x][y])

	return False


def handle_keyboard():
	global key, selected_object, player

	# test for other keys
	key_char = chr(key.c)
	
	if key_char == 't':
		return True
		
	if key_char == 'x' or key_char == 'X':
		if player.movement_locked:
			player.movement_locked = False
		else:
			player.movement_locked = True

	if key_char == 'w' or key_char == 'W':
		move_success = player.move(0, -1)
		if not move_success:
			return player.unit.try_to_manoeuvre(0, -1)
	elif key_char == 'a' or key_char == 'A':
		move_success = player.move(-1, 0)
		if not move_success:
			return player.unit.try_to_manoeuvre(-1, 0)
	elif key_char == 's' or key_char == 'S':
		move_success = player.move(0, 1)
		if not move_success:
			return player.unit.try_to_manoeuvre(0, 1)
	elif key_char == 'd' or key_char == 'D':
		move_success = player.move(1, 0)
		if not move_success:
			return player.unit.try_to_manoeuvre(1, 0)
	elif key_char == 'f' or key_char == 'F' or key_char == 'r' or key_char == 'R' or key_char == 'e' or key_char == 'E' or key_char == 'c' or key_char == 'C' or key_char == 'v' or key_char == 'V':
		
		if key_char == 'e' or key_char == 'E':
			if player.unit.holding:
				return player.unit.let_go()

		adjacent_objects = get_adjacent_stuff(player.x, player.y, 'Objects', include_diagonals = False, include_centre = True)
		
		if player in adjacent_objects: adjacent_objects.remove(player)
		
		objects_to_remove = []
		
		
		# covers the context sensitive keypresses
		for object in adjacent_objects:
			if key_char == 'e' or key_char == 'E':
				if not player.can_i_perform_task(object, 'Drag'):
					objects_to_remove.append(object)
			elif key_char == 'f' or key_char == 'F':
				if not player.can_i_perform_task(object, 'Lift') and not object.allow_inventory:
					objects_to_remove.append(object)
				elif object.unit:
					objects_to_remove.append(object)
			elif key_char == 'r' or key_char == 'R':
				if not player.can_i_perform_task(object, 'Open / Close'):
					objects_to_remove.append(object)
			elif key_char == 'c' or key_char == 'C':
				if not player.can_i_perform_task(object, 'Lock / Unlock'):
					objects_to_remove.append(object)
			elif key_char == 'v' or key_char == 'V':
				if not player.can_i_perform_task(object, 'Activate / Deactivate'):
					objects_to_remove.append(object)
			else:
				break
				
				
		for object in objects_to_remove:
			adjacent_objects.remove(object)

		if adjacent_objects:
			if len(adjacent_objects) > 1:
				selected_object = prompt_to_choose_object(adjacent_objects)
			else:
				selected_object = adjacent_objects[0]
			
			if selected_object:
				
				if key_char == 'f' or key_char == 'F':
					if selected_object.allow_inventory and len(selected_object.inventory) > 0:
						if selected_object.check_if_unlocked():
							selected_object = prompt_to_choose_object(selected_object.inventory)
					quantity = prompt_for_quantity(selected_object)
					return player.unit.pick_up(selected_object, quantity)
					
				elif key_char == 'r' or key_char == 'R':
					return player.open_close(selected_object)
					
				elif key_char == 'c' or key_char == 'C':
					return player.lock_unlock(selected_object)
					
				elif key_char == 'v' or key_char == 'V':
					return player.toggle_on_off(selected_object)
					
				elif key_char == 'e' or key_char == 'E':
					quantity = prompt_for_quantity(selected_object)
					return player.unit.grab(selected_object, quantity)

	elif key_char == 'q' or key_char == 'Q':
		if player.inventory:
			chosen_inventory_object = prompt_to_choose_object(player.inventory)
			if chosen_inventory_object:
				action_options = ['Drop', 'Consume', 'Equip', 'Throw']
				chosen_action = menu(chosen_inventory_object.name, None, action_options)
				if chosen_action >= 0:
					return process_action(action_options[chosen_action], object_taking_action=player, object_being_actioned=None, object_being_targeted=chosen_inventory_object)

	return False


def prompt_for_quantity(object_to_prompt):
	if not object_to_prompt:
		print 'no object to prompt for quantity'
		return False

	if object_to_prompt.quantity > 1:
		quantity = select_quantity_of_object(object_to_prompt, 1, object_to_prompt.quantity)
		return int(quantity)
	else:
		return 1


def prompt_to_choose_dialogue(dialogue_object, pick_a_random_response = False, speaker_object = None):
	if not dialogue_object.responses:
		if MORE_ERROR_LOGGING:
			print 'dialogue has no response options'
			print ''
		return None

	response_ID = None

	response_IDs = []
	response_dialogue = []

	for response_option_ID in dialogue_object.responses:
		response_option_object = get_dialogue_by_ID(response_option_ID)
		response_IDs.append(response_option_object.ID)
		response_dialogue.append(response_option_object.dialogue)

	if pick_a_random_response:
		chosen_response_index = libtcod.random_get_int(0, 0, (len(response_dialogue) - 1))
	else:
		if speaker_object:
			speaker_name = speaker_object.name
		else:
			speaker_name = 'Dialogue'
		chosen_response_index = menu(speaker_name, dialogue_object, response_dialogue)

	if chosen_response_index >= 0 and chosen_response_index < len(response_IDs):
		response_ID = response_IDs[chosen_response_index]

	return response_ID


def prompt_to_choose_object(list_of_objects, header=None):
	selected_object = None
	list_of_objects_names = []

	if not header:
		header = 'Which object would you like to select?'

	if not list_of_objects:
		return None

	for this_object in list_of_objects:
		
		optional_ID_tag = ''
		
		if ID_TAGS_ON:
			optional_ID_tag = '[' + str(this_object.ID) + '] '

		quantity = ''
		if this_object.quantity > 1:
			quantity = ' (x' + str(this_object.quantity) + ')'

		general_info = ''

		
		if this_object.functions_as_door:
			general_info = general_info + ' (' + str(this_object.open_closed_state) + ')'
		if this_object.functions_as_lock:
			general_info = general_info + ' (' + str(this_object.locked_unlocked_state) + ')'
		if this_object.functions_on_off:
			general_info = general_info + ' (' + str(this_object.on_off_state) + ')'
		
		if not this_object.in_inventory_of:
			general_info = general_info + ' (' + map[player.x][player.y].angle_to(this_object) + ')'
			
			#for distance coords
			#x_offset = this_object.x - player.x
			#y_offset = this_object.y - player.y
			#general_info = '  (x:' + str(x_offset) + ', y:' + str(y_offset) + ')'

		list_of_objects_names.append(optional_ID_tag + this_object.name + quantity + general_info)

	chosen_object_index = menu(header, None, list_of_objects_names)
	
	#if chosen_object_index:
	if chosen_object_index >= 0:
		selected_object = list_of_objects[chosen_object_index]

	return selected_object


def target_tile(return_object_if_possible = False, max_range = None):
	global key, mouse, map
	# return the position of a tile left-clicked in player's FOV (optionally in a range), or (None,None) if right-clicked.
	while True:
		# render the screen. this shows the names of objects under the mouse.
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

		render_all()

		(x, y) = (mouse.cx, mouse.cy)

		if mouse.rbutton_pressed or key.vk == libtcod.KEY_ESCAPE:
			return None  # cancel if the player right-clicked or pressed Escape

		if x < MAP_WIDTH and y < MAP_HEIGHT:

			# accept the target if the player clicked in FOV, and in case a range is specified, if it's in that range
			if (mouse.lbutton_pressed and (max_range is None or player.distance(x, y) <= max_range)):
			
				if return_object_if_possible:
					possible_object = pick_largest(map[x][y].objects_on_this_tile)
					if possible_object:
						return possible_object
				
				return map[x][y]
				
def toggle_main_power(force_state = None):
	global light_sources, main_power_on, affixed_objects, non_affixed_objects, player
	
	if main_power_on == True:
		main_power_on = False
		player.light_radius = 3
	else:
		main_power_on = True
		player.light_radius = 7
		
	all_objects = affixed_objects + non_affixed_objects
	
	for an_object in all_objects:
		if an_object.attached_to_main_power:
			if main_power_on:
				if an_object.on_off_state == 'On':
					an_object.on_off_state = 'Off'
					an_object.toggle_on_off(an_object)
			else:
				if an_object.on_off_state == 'On':
					an_object.toggle_on_off(an_object)
					an_object.on_off_state = 'On'
				
def reset_everything():
	global map
	global affixed_objects
	global non_affixed_objects
	global units
	global player
	global game_msgs
	global game_state
	global rooms
	global selected_object
	global tiles_on_fire
	global objects_on_fire
	global objects_in_motion
	global message_scroll_button
	global message_scroll_state
	global temporary_obstacles
	global lab_rooms
	global lab_rooms_original
	global light_sources
	global light_source_fov_maps
	global main_power_on
	global current_music
	
	map = []
	affixed_objects = []
	non_affixed_objects = []
	units = []
	player = None
	game_msgs = []
	game_state = 'playing'
	rooms = []
	selected_object = None
	tiles_on_fire = []
	objects_on_fire = []
	objects_in_motion = []
	message_scroll_button = None
	message_scroll_state = 0
	temporary_obstacles = []
	lab_rooms = list(lab_rooms_original)
	light_sources = []
	light_source_fov_maps = []
	main_power_on = True
	current_music = None


def new_game():
	global map
	global affixed_objects
	global non_affixed_objects
	global units
	global player
	global game_msgs
	global game_state
	global rooms
	global selected_object
	global tiles_on_fire
	global objects_on_fire
	global objects_in_motion
	global message_scroll_button
	global message_scroll_state
	global temporary_obstacles
	global light_sources
	global main_power_on
	
	reset_everything()

	# create object representing the player
	
	player = get_object_by_name('Player')

	# generate map (at this point it's not drawn to the screen)
	make_map()

	add_doors = []

	for x in range(MAP_WIDTH - 1):
		for y in range(MAP_HEIGHT - 1):
			if map[x][y].wall:
				if not map[x + 1][y].wall and not map[x - 1][y].wall:
					add_doors.append([x, y])
				if not map[x][y + 1].wall and not map[x][y - 1].wall:
					add_doors.append([x, y])

	for door in add_doors:
		map[door[0]][door[1]].wall = False
		map[door[0]][door[1]].char = '.'
		map[door[0]][door[1]].room_name = 'Hallway'

	add_doors = []

	for x in range(MAP_WIDTH - 1):
		for y in range(MAP_HEIGHT - 1):
			if map[x][y].wall:
				if not map[x + 1][y].wall and not map[x - 1][y].wall and not map[x][y + 1].wall and not map[x][y - 1].wall:
					add_doors.append([x, y])
	for door in add_doors:
		map[door[0]][door[1]].wall = False
		map[door[0]][door[1]].char = '.'
		map[door[0]][door[1]].room_name = 'Hallway'

	search_for_door_locations()

	for this_room in rooms:
		if this_room.name:
			place_objects(this_room, this_room.name)

	for x in range(MAP_WIDTH - 1):
		for y in range(MAP_HEIGHT - 1):
			adjacent_rooms = get_adjacent_stuff(x, y, 'Room Names', include_diagonals = True)
			outside = True
			for room in adjacent_rooms:
				if room:
					outside = False
					break
			if outside:
				map[x][y].wall = False
				map[x][y].char = ','
				map[x][y].foreground_colour = libtcod.lightest_grey
				map[x][y].background_colour = libtcod.white

	(new_x, new_y) = rooms[0].center()
	
	place_object_at_location(player, new_x, new_y)

	convert_wall_tiles_into_objects()
	
	for x in range(MAP_WIDTH - 1):
		for y in range(MAP_HEIGHT - 1):
			if not map[x][y].room_name:
				map[x][y].room_name = 'Outside'
				
	list_of_exterior_walls = []
	for object in affixed_objects:
		if 'Outside' in get_adjacent_stuff(object.x, object.y, 'Room Names', include_diagonals = False, include_centre = False):
			list_of_exterior_walls.append(object)
	
	for i in range (0, 5):
		exterior_door_chosen_spot = pick_random(list_of_exterior_walls)
		if exterior_door_chosen_spot:
			door_location_x = exterior_door_chosen_spot.x
			door_location_y = exterior_door_chosen_spot.y
			remove_all_connections_to_object(exterior_door_chosen_spot)
			del exterior_door_chosen_spot
			exterior_door_object = place_object_at_location(get_object_by_name('Door'), door_location_x, door_location_y)
			exterior_door_object.foreground_colour = libtcod.light_cyan
			
			
	for obstacle in temporary_obstacles:
		remove_all_connections_to_object(obstacle)
		del obstacle

	game_state = 'playing'
	
	initialize_fov()

	# create the list of game messages and their foreground_colours, starts empty
	game_msgs = []

	# a warm welcoming message!
	Message('Welcome new scientist.  Do your research.  Im sure nobody will become THE THING.', 'Narrator')


def initialize_fov():
	global fov_map

	# create the FOV map, according to the generated map
	fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			libtcod.map_set_properties(fov_map, x, y, not map[x][y].check_blocks_sight(), not map[x][y].wall)
			
	libtcod.console_clear(con)  # unexplored areas start black (which is the default background foreground_colour)


def play_game():
	global key, mouse, game_paused, clicked_object_name, fov_recompute, list_of_things, game_state, all_dialogue_IDs, player, objects_on_fire, objects_in_motion

	all_dialogue_IDs = []
	for i in range(0, 300):
		if get_dialogue_by_ID(i):
			all_dialogue_IDs.append(i)

	list_of_things = []

	chosen_thing = None

	clicked_object_name = ""

	game_paused = False

	player_action = None

	mouse = libtcod.Mouse()
	key = libtcod.Key()
	
	last_tick = libtcod.sys_elapsed_seconds()
	
	num_turns = 0

	random_place_object(get_object_by_name('Nauls'))
	
		
	for i in range(1, 25):
		blah = get_object_by_name('Locker')
		random_place_object(blah)
		
		
	for i in range(1, 15):
		blah = get_object_by_name('Lamp')
		random_place_object(blah)


	# main loop
	while not libtcod.console_is_window_closed() and game_state == 'playing':
		key = libtcod.Key()
	
		fov_recompute = True

		if ACTIVATE_FUNCTION_TIMERS: main_loop_time = start_test()

		if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
		render_all()
		if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, '(loop) render all')

		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

		if handle_mouse():
			player.unit.turn_taken = True

		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

		if libtcod.console_is_key_pressed(libtcod.KEY_ESCAPE):
			end_game_return_to_main_menu()
			return False
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
			
		
		if ACTIVATE_FUNCTION_TIMERS: moving_projectiles_time_variable = start_test()
		
		last_projectile_tick = libtcod.sys_elapsed_seconds()

		# EVENTUALLY THE PROJECTILE RENDER SHOULD BE BASED ON THROW POWER
		while len(objects_in_motion) > 0:
			if libtcod.sys_elapsed_seconds() >  last_projectile_tick + 0.0001:
		
				for moving_thing in objects_in_motion:
					if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
					moving_thing.run_turn()
					if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, moving_thing.projectile_object.name + ' processing projectile movement')
					
				libtcod.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)
				libtcod.console_flush()
					
				last_projectile_tick = libtcod.sys_elapsed_seconds()
			
			
		if ACTIVATE_FUNCTION_TIMERS: end_test(moving_projectiles_time_variable, '(loop) all moving projectiles combined')
		
		if not player.unit.turn_taken:
			if handle_keyboard():
				player.unit.turn_taken = True
		
		if player.unit.turn_taken == True and libtcod.sys_elapsed_seconds() > last_tick + NUMBER_OF_SECONDS_BETWEEN_TURNS:
			
			last_tick = libtcod.sys_elapsed_seconds()

			if ACTIVATE_FUNCTION_TIMERS: all_units_turn_time = start_test()
			temp_units = [this_unit for this_unit in units]
			for some_guy in temp_units:
				if not some_guy.held_by:
					if not some_guy.unit.turn_taken:
						if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
						some_guy.unit.take_turn()
						if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, some_guy.name + ' taking their turn')
						
						# bonus turn for the thing when it's panicking
						if some_guy.unit.the_thing_revealed:
							some_guy.unit.take_turn()
						
						
				some_guy.unit.turn_taken = False
					
			if ACTIVATE_FUNCTION_TIMERS: end_test(all_units_turn_time, '(loop) all units taking thier turns')
			num_turns += 1
			

			# Burning objects handling
			for burning_thing in objects_on_fire:
				if map[burning_thing.x][burning_thing.y].burn_value >= 0:
					if not map[burning_thing.x][burning_thing.y].on_fire:
						map[burning_thing.x][burning_thing.y].on_fire = True
						map[burning_thing.x][burning_thing.y].char = 'F'
						map[burning_thing.x][burning_thing.y].foreground_colour = libtcod.light_red
						tiles_on_fire.append(map[burning_thing.x][burning_thing.y])

				# Be on fire
				burning_thing.condition -= 5
				if not burning_thing.unit:
					burning_thing.char = 'F'
				burning_thing.foreground_colour = pick_random([libtcod.dark_red, libtcod.yellow, libtcod.orange])

				# Burn to death
				if burning_thing.condition <= 0:
					burning_thing.on_fire = False
					objects_on_fire.remove(burning_thing)
					burning_thing.destroy()
					
			if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
			
			# Burning tiles handling
			for burning_tile in tiles_on_fire:
				for burn_this_object in burning_tile.objects_on_this_tile:
					if not burn_this_object.on_fire:
						burn_this_object.on_fire = True
						objects_on_fire.append(burn_this_object)

				burning_tile.burn_value -= 1

				if burning_tile.burn_value <= 3:
					try:
						right = map[normalize_to_map_width(burning_tile.x + 1)][normalize_to_map_height(burning_tile.y)]
						left = map[normalize_to_map_width(burning_tile.x - 1)][normalize_to_map_height(burning_tile.y)]
						up = map[normalize_to_map_width(burning_tile.x)][normalize_to_map_height(burning_tile.y - 1)]
						down = map[normalize_to_map_width(burning_tile.x)][normalize_to_map_height(burning_tile.y + 1)]
						upright = map[normalize_to_map_width(burning_tile.x + 1)][normalize_to_map_height(burning_tile.y - 1)]
						upleft = map[normalize_to_map_width(burning_tile.x - 1)][normalize_to_map_height(burning_tile.y - 1)]
						downright = map[normalize_to_map_width(burning_tile.x + 1)][normalize_to_map_height(burning_tile.y + 1)]
						downleft = map[normalize_to_map_width(burning_tile.x - 1)][normalize_to_map_height(burning_tile.y + 1)]

						right.set_on_fire()
						left.set_on_fire()
						up.set_on_fire()
						down.set_on_fire()
						upright.set_on_fire()
						upleft.set_on_fire()
						downright.set_on_fire()
						downleft.set_on_fire()

					except IndexError:
						None

				if burning_tile.burn_value <= 0:
					tiles_on_fire.remove(burning_tile)
					burning_tile.foreground_colour = libtcod.grey
					burning_tile.char = '.'
					
			if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, 'handling burning stuff')
		
		if not DISABLE_THE_THING:
			if not chosen_thing and num_turns > NUMBER_OF_TURNS_UNTIL_THE_THING:
				thing_candidates = []
				for obj in units:
					if not obj == player:
						thing_candidates.append(obj)
				chosen_thing = thing_candidates[libtcod.random_get_int(0, 0, (len(thing_candidates) - 1))]
				chosen_thing.unit.become_the_thing()
		
		if ACTIVATE_FUNCTION_TIMERS: end_test(main_loop_time, '(loop) main loop')
		

def initialize_sounds():
	global impact_sound
	global gun_sound
	global explosion_sound
	global death_sound
	global no_ammo_sound
	global move_sound
	global door_sound
	global menu_click_sound
	global key_unlock_sound
	global activate_sound
	global current_music
	
	
	current_music = None
	impact_sound = pygame.mixer.Sound('thing_sounds/impact.wav')
	gun_sound = pygame.mixer.Sound('thing_sounds/gun.wav')
	explosion_sound = pygame.mixer.Sound('thing_sounds/explosion.wav')
	death_sound = pygame.mixer.Sound('thing_sounds/death.wav')
	no_ammo_sound = pygame.mixer.Sound('thing_sounds/no_ammo.wav')
	move_sound = pygame.mixer.Sound('thing_sounds/move.wav')
	door_sound = pygame.mixer.Sound('thing_sounds/door.wav')
	menu_click_sound = pygame.mixer.Sound('thing_sounds/menu_click.wav')
	key_unlock_sound = pygame.mixer.Sound('thing_sounds/key_unlock.wav')
	activate_sound = pygame.mixer.Sound('thing_sounds/activate.wav')
	
def end_game_return_to_main_menu():
	global game_state
	game_state = None
	render_all()
	play_music(None)
	return True
	
	
def play_music(music_file):
	global current_music
	if not music_file:
		pygame.mixer.music.stop()
	elif music_file == 'Pause':
		pygame.mixer.music.set_volume(0)
	elif music_file == current_music:
		pygame.mixer.music.set_volume(1)
	else:
		pygame.mixer.music.load('thing_sounds/' + music_file)
		pygame.mixer.music.play(-1)
		current_music = music_file

def main_menu():
	global SHOW_ALL, HEAR_ALL, PLAY_MUSIC, DISABLE_THE_THING, fov_recompute
	fov_recompute = False
	img = libtcod.image_load('menu_background.png')

	pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 1024)
	pygame.mixer.init()
	
	initialize_sounds()
	
	easter_egg = 0

	while not libtcod.console_is_window_closed():
	
		# show the background image, at twice the regular console resolution
		libtcod.image_blit_2x(img, 0, 0, 0)

		# show the game's title, and some credits!
		libtcod.console_set_default_foreground(0, libtcod.light_yellow)
		libtcod.console_print_ex(0, SCREEN_WIDTH / 2 + 2, SCREEN_HEIGHT / 2 - 4 + 2, libtcod.BKGND_NONE, libtcod.CENTER, 'TENTACLE JAZZHANDS')
	
		# show options and wait for the player's choice
		choice = menu('THE THING', get_dialogue_by_ID(307), ['Play a new game', 'Show Full Map [' + str(SHOW_ALL) + ']', 'Show All Messages [' + str(HEAR_ALL) + ']', 'Play Music [' + str(PLAY_MUSIC) + ']', 'Disable The Thing [' + str(DISABLE_THE_THING) + ']', 'Quit'], clear_window_after_display=False)
	
		if choice == 0:  # new game
			if PLAY_MUSIC:
				if easter_egg < 4:
					play_music('music.ogg')
				else:
					play_music('music_2.ogg')
			new_game()
			play_game()
		elif choice == 1:
			if SHOW_ALL:
				SHOW_ALL = False
			else:
				SHOW_ALL = True
		elif choice == 2:  
			if HEAR_ALL:
				HEAR_ALL = False
			else:
				HEAR_ALL = True
		elif choice == 3: 
			if PLAY_MUSIC:
				PLAY_MUSIC = False
			else:
				PLAY_MUSIC = True
			easter_egg += 1
		elif choice == 4: 
			if DISABLE_THE_THING:
				DISABLE_THE_THING = False
			else:
				DISABLE_THE_THING = True
		elif choice == 5:  # quit
			sys.exit()
				

				

def get_room_type_by_name(room_type_name):
	# Create a name for the room
	if room_type_name == 'Dog Cages Room':

		# Repeat the name of the room here.
		this_room = Room_Type('Dog Cages Room')

		# Add as many objects or object groups as you like.  Copy / paste the next four lines as many times as you see hit.
		# The game will randomly fill the room with them, but keep in mind that size / overlap means they may not appear for sure.
		this_room.objects_in_room.append({
			'object_or_group': 'Group',
		# Write 'Object' if you are randomly placing a single object.  'Group' if you are placing a group you created.
			'name_of_object_or_group': 'Dog Cages',  # The name of the object or group
			'minimum_quantity': 3,
		# Game will try to randomly place a number of these objects between the min and max quantity.
			'maximum_quantity': 5})

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Scientist',
			'minimum_quantity': 1,
			'maximum_quantity': 2})

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Oil Barrel',
			'minimum_quantity': 1,
			'maximum_quantity': 2})

	# That's it!  Another example of a computer lab below with... a bunch of computers on the floor.

	elif room_type_name == 'Computer Lab':
		this_room = Room_Type('Computer Lab')

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Computer',
			'minimum_quantity': 2,
			'maximum_quantity': 6})

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Scientist',
			'minimum_quantity': 1,
			'maximum_quantity': 3})

	elif room_type_name == "MacReady's Room":
		this_room = Room_Type("MacReady's Room")

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'J&B',
			'minimum_quantity': 1,
			'maximum_quantity': 3})

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Comfy Bed',
			'minimum_quantity': 1,
			'maximum_quantity': 1})

		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Sombrero',
			'minimum_quantity': 1,
			'maximum_quantity': 1})
			
		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Filing Cabinet',
			'minimum_quantity': 1,
			'maximum_quantity': 1})
			
		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Radio',
			'minimum_quantity': 1,
			'maximum_quantity': 1})
			
		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Generator',
			'minimum_quantity': 1,
			'maximum_quantity': 1})
			
		this_room.objects_in_room.append({
			'object_or_group': 'Object',
			'name_of_object_or_group': 'Flashlight',
			'minimum_quantity': 1,
			'maximum_quantity': 1})

	return this_room


def percentage_chance(probability):
	if libtcod.random_get_int(0, 0, 100) <= probability:
		return True
	return False

def rand_between(min, max):
	return libtcod.random_get_int(0, min, max)
	
def get_object_group_by_name(object_group_name):
	# Create a name for your group of objects
	if object_group_name == 'Dog Cages':
		# Repeat the name again
		this_object_group = Object_Group(object_group_name, grid=[

			# Draw icons to represent the shape of what you are building.  These are NOT the icons that will appear in the game, they are only used
			# to compare to the legend that you create below this.  Make sure to start every build in the upp left corner.  The game will automatically
			# cut off white space below and to the right.

			# X's are used for blank space that CANNOT overlap with anything else.  Underscores are used for blank space that COULD overlap with other objects.

			['X', '+', 'd', '+', 'X', '_', '_', '_'],
			['X', '+', 'X', '+', 'X', '_', '_', '_'],
			['X', '+', 'E', '+', 'X', '_', '_', '_'],
			['X', 'X', 'X', 'X', 'X', '_', '_', '_'],
			['_', '_', '_', '_', '_', '_', '_', '_'],
			['_', '_', '_', '_', '_', '_', '_', '_'],
			['_', '_', '_', '_', '_', '_', '_', '_'],
			['_', '_', '_', '_', '_', '_', '_', '_']])
			
		this_object_group.object_map = []
		
		this_object_group.object_map.append(['+', 'Fence'])
		this_object_group.object_map.append(['d', 'Dog'])
		this_object_group.object_map.append(['E', 'Cage Door'])
		this_object_group.object_map.append(['X', 'Generic Wall Obstacle'])

		this_object_group.place_against_wall = 'Top'


	return this_object_group

def get_object_specific_instance_by_tag(tag_name):

	this_object_instance = None
	
	if tag_name == 'Dog 1':
		this_object_instance = get_object_by_name('Dog')
		this_object_instance.name = 'Pooooo'
		this_object_instance.unit.update_strength(2)
	else:
		this_object_instance = get_object_by_name(tag_name)
		
	# Debug message
	if not this_object_instance:
		print '********************* NEED TO CREATE ' + object_name
		
	return this_object_instance
	

def get_object_by_name(object_name):
	if object_name == 'Wall':
		this_object = get_predesigned_object_by_name('Wall')
		
	elif object_name == 'Generic Humanoid Obstacle':
		this_object = get_predesigned_object_by_name('Humanoid')
		
	elif object_name == 'Generic Wall Obstacle':
		this_object = get_predesigned_object_by_name('Wall')

	elif object_name == 'Door':
		this_object = get_predesigned_object_by_name('Door')

	elif object_name == 'Cage Door':
		this_object = get_predesigned_object_by_name('Door')
		this_object.blocks_sightline = False
		this_object.foreground_colour = libtcod.light_grey

	elif object_name == 'Table':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'T'
		this_object.size = 5
		this_object.material = 'Wood'
		this_object.foreground_colour = libtcod.light_orange
		this_object.description = "A basic table."

	elif object_name == 'Fence':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = '+'
		this_object.size = 9
		this_object.material = 'Metal'
		this_object.affixed_to_ground = True
		this_object.foreground_colour = libtcod.grey
		this_object.description = "A basic " + object_name

	elif object_name == 'Oil Barrel':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'B'
		this_object.size = 7
		this_object.material = 'Metal'
		this_object.components = ['Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire', 'Fire']
		this_object.foreground_colour = libtcod.grey
		this_object.description = "A basic " + object_name
		this_object.internal_kinetic_energy = 10000
		
	elif object_name == 'Mega Bomb':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'n'
		this_object.size = 3
		this_object.material = 'Glass'
		this_object.components = ['Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel']
		this_object.foreground_colour = libtcod.purple
		this_object.description = "Don't fuck with this big ass bomb"
		this_object.internal_kinetic_energy = 1000000
		this_object.ammunition_for = ['Gun']
		
	elif object_name == 'Filing Cabinet':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'C'
		this_object.size = 3
		this_object.material = 'Metal'
		this_object.inventory = ['Locker Key', 'J&B']
		this_object.foreground_colour = libtcod.light_grey
		this_object.description = "A basic " + object_name
		
	elif object_name == 'Locker Key':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'k'
		this_object.size = 0.1
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.white
		this_object.description = "A basic " + object_name
		this_object.key_for = 'Locker'

	elif object_name == 'Computer':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'c'
		this_object.size = 2
		this_object.material = 'Plastic'
		this_object.foreground_colour = libtcod.light_blue
		this_object.description = "A basic " + object_name

	elif object_name == 'J&B':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'j'
		this_object.size = 0.5
		this_object.material = 'Glass'
		this_object.foreground_colour = libtcod.light_purple
		this_object.description = "A basic " + object_name

	elif object_name == 'Chair':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'c'
		this_object.size = 3
		this_object.material = 'Wood'
		this_object.foreground_colour = libtcod.light_orange
		this_object.description = "A basic " + object_name

	elif object_name == 'Watercolour Paints':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'w'
		this_object.size = 1
		this_object.material = 'Wood'
		this_object.foreground_colour = libtcod.lighter_green
		this_object.description = "A basic " + object_name

	elif object_name == 'Gun':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'g'
		this_object.size = 0.5
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.light_grey
		this_object.description = "A basic " + object_name
		this_object.attack_function = 'Gun'
		this_object.internal_kinetic_energy = 1000

	elif object_name == 'Flamethrower':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'F'
		this_object.size = 2
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.lighter_red
		this_object.description = "A basic " + object_name
		this_object.attack_function = 'Flamethrower'
		this_object.internal_kinetic_energy = 1000
		
	elif object_name == 'Rocket Launcher':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'R'
		this_object.size = 2
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.dark_yellow
		this_object.description = "A basic " + object_name
		this_object.attack_function = 'Rocket Launcher'
		this_object.internal_kinetic_energy = 10000

	elif object_name == 'Bullet':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'o'
		this_object.size = 0.1
		this_object.stackable = True
		this_object.quantity = rand_between(1, 10)
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.light_grey
		this_object.ammunition_for = ['Gun']
		this_object.description = "A basic " + object_name

	elif object_name == 'Flame Tank':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 't'
		this_object.size = 0.25
		this_object.stackable = True
		this_object.quantity = rand_between(1, 10)
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.light_grey
		this_object.components = ['Fire', 'Fire', 'Fire']
		this_object.ammunition_for = ['Flamethrower']
		this_object.description = "A basic " + object_name
		
	elif object_name == 'Rocket':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'r'
		this_object.size = 0.25
		this_object.stackable = True
		this_object.quantity = rand_between(1, 10)
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.dark_green
		this_object.components = ['Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel', 'Shrapnel']
		this_object.ammunition_for = ['Rocket Launcher']
		this_object.description = "A basic " + object_name
		
	elif object_name == 'Shrapnel':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = '*'
		this_object.size = 0.5
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.light_grey
		this_object.components = []
		this_object.description = "A basic " + object_name
		
	elif object_name == 'Brick':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = '~'
		this_object.size = 0.5
		this_object.material = 'Stone'
		this_object.foreground_colour = libtcod.light_grey
		this_object.components = []
		this_object.description = "A basic " + object_name

	elif object_name == 'Fire':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'F'
		this_object.size = 1
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.light_red
		this_object.description = "A basic " + object_name
		this_object.on_fire = True
		this_object.stackable = False

	elif object_name == 'Sombrero':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'S'
		this_object.size = 1
		this_object.material = 'Cloth'
		this_object.foreground_colour = libtcod.yellow
		this_object.description = "A sombrero that fits MacReady perfectly."

	elif object_name == 'Comfy Bed':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'B'
		this_object.size = 7
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.brass
		this_object.background_colour = libtcod.white
		this_object.components = ['Comfy Pillow', 'Bedframe']
		this_object.description = "A real comfy bed that semlls of J&B."

	elif object_name == 'Comfy Pillow':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'p'
		this_object.size = 1
		this_object.material = 'Cloth'
		this_object.foreground_colour = libtcod.white
		this_object.description = "Small and triangular."

	elif object_name == 'Bedframe':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'b'
		this_object.size = 6
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.brass
		this_object.description = "Big and brassy. Bedtacular."
		
	elif object_name == 'Locker':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'L'
		this_object.size = 8
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.brass
		this_object.description = "Locker."
		this_object.functions_as_lock = True
		if percentage_chance(50): this_object.inventory.append('Gun')
		if percentage_chance(25): this_object.inventory.append('Flamethrower')
		if percentage_chance(25): this_object.inventory.append('Rocket Launcher')
		if percentage_chance(15): this_object.inventory.append('Mega Bomb')
		if percentage_chance(50): this_object.inventory.append('Bullet')
		if percentage_chance(25): this_object.inventory.append('Flame Tank')
		if percentage_chance(25): this_object.inventory.append('Rocket')
		
	elif object_name == 'Radio':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'R'
		this_object.size = 0.5
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.brass
		this_object.description = "Macready's radio.  Big BTO fan."
		
		this_object.functions_on_off = True
		this_object.on_off_state = 'Off'
		this_object.attached_to_main_power = True
		
		this_object.on_function = play_music
		this_object.on_argument = ('bto.ogg')
		
		this_object.off_function = play_music
		this_object.off_argument = 'Pause'
		
	elif object_name == 'Generator':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'G'
		this_object.size = 1
		this_object.material = 'Glass'
		this_object.foreground_colour = libtcod.grey
		this_object.description = "Powers the lights in the facility."
		
		this_object.functions_on_off = True
		this_object.on_off_state = 'On'
		
		this_object.on_function = toggle_main_power
		this_object.on_argument = 'On'
		
		this_object.off_function = toggle_main_power
		this_object.off_argument = 'Off'
		
	elif object_name == 'Lamp':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'M'
		this_object.size = 1
		this_object.material = 'Glass'
		this_object.foreground_colour = libtcod.dark_yellow
		this_object.description = "A lamp."
		
		this_object.functions_on_off = True
		this_object.on_off_state = 'On'
		this_object.attached_to_main_power = True
		
		this_object.light_source = 'Omni'
		this_object.light_radius = 8
		
		this_object.on_function = this_object.adjust_light_radius
		this_object.on_argument = 8
		
		this_object.off_function = this_object.adjust_light_radius
		this_object.off_argument = 0
		
	elif object_name == 'Flashlight':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'f'
		this_object.size = 0.5
		this_object.material = 'Plastic'
		this_object.foreground_colour = libtcod.dark_yellow
		this_object.description = "A flashlight."
		
		this_object.functions_on_off = True
		this_object.on_off_state = 'Off'
		
		this_object.light_source = 'Directional'
		this_object.light_radius = 0
		
		this_object.on_function = this_object.adjust_light_radius
		this_object.on_argument = 20
		
		this_object.off_function = this_object.adjust_light_radius
		this_object.off_argument = 0
		
	elif object_name == 'Pool Table':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'P'
		this_object.size = 8
		this_object.material = 'Wood'
		this_object.foreground_colour = libtcod.dark_green
		this_object.description = "Super fun."
		
	elif object_name == 'Pinball Machine':
		this_object = get_predesigned_object_by_name('Generic Object')
		this_object.char = 'P'
		this_object.size = 7
		this_object.material = 'Metal'
		this_object.foreground_colour = libtcod.white
		this_object.description = "Super fun."

	# UNITS BELOW THIS LINE
	

	elif object_name == 'Player':
		this_object = get_predesigned_object_by_name('Humanoid')
		this_object.foreground_colour = libtcod.white
		this_object.description = "Player"
		this_object.inventory = ['Flashlight']
		this_object.unit = get_unit_by_name('Scientist')
		this_object.light_source = 'Omni'
		this_object.light_radius = 7

	elif object_name == 'Scientist':
		this_object = get_predesigned_object_by_name('Humanoid')
		this_object.foreground_colour = libtcod.green
		this_object.components = []
		this_object.description = "One of the scientists working in the lab.  He's extremely busy and does not wish to be disturbed."
		this_object.unit = get_unit_by_name('Scientist')

	elif object_name == 'Nauls':
		this_object = get_predesigned_object_by_name('Humanoid')
		this_object.foreground_colour = libtcod.red
		this_object.inventory = ['Locker Key', 'J&B']
		this_object.description = "Guy zooming around on rollerskates. He is very fast."
		this_object.unit = get_unit_by_name('Nauls')

	elif object_name == 'Dog':
		this_object = get_predesigned_object_by_name('Humanoid')
		this_object.foreground_colour = libtcod.light_blue
		this_object.char = 'd'
		this_object.size = 2
		this_object.description = "A doggy."
		this_object.unit = get_unit_by_name('Dog')
	
	# Debug message
	if not this_object:
		print '********************* NEED TO CREATE ' + object_name
		
	this_object.name = object_name
	this_object.establish_properties()
	return this_object


def get_predesigned_object_by_name(predesigned_object_name):
	if predesigned_object_name == 'Generic Object':
		this_object = Object(
			x=0,
			y=0,
			char='o',
			name=predesigned_object_name,
			foreground_colour=libtcod.light_cyan,
			background_colour=None,
			always_visible=False,
			condition=100,
			size=5,
			material='Metal',
			weight=None,
			indestructible = False,
			affixed_to_ground = False,
			blocks_sightline = False,
			destroyed = False,
			functions_as_door = False,
			components=[],
			inventory=[],
			in_inventory_of=None,
			food_value= 0,
			drink_value= 0,
			rest_value= 0,
			temp_value= 0,
			description='Generic object.',
			unit = None)

	elif predesigned_object_name == 'Humanoid':
		this_object = Object(
			x=0,
			y=0,
			char='@',
			name=predesigned_object_name,
			foreground_colour=libtcod.light_cyan,
			background_colour=None,
			always_visible=False,
			condition=100,
			size=6,
			material='Flesh',
			weight=None,
			indestructible=False,
			affixed_to_ground=False,
			blocks_sightline=False,
			destroyed=False,
			functions_as_door=False,
			components=[],
			inventory=[],
			in_inventory_of=None,
			food_value=0,
			drink_value=0,
			rest_value=0,
			temp_value=0,
			description='Generic person.',
			unit=get_unit_by_name('Generic Humanoid'))

	elif predesigned_object_name == 'Wall':
		this_object = Object(
			x=0,  # Always make 0.  Game with place the location
			y=0,  # Always make 0.  Game with place the location
			char='#',  # Keyboard character the object is displayed as in the game
			name=predesigned_object_name,
			# Name the object is assigned.  Must be unique, can't have two objects with same name.  Caps matters.
			foreground_colour=libtcod.white,
			# Colour of the object in the game.  Use this page for options: http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/color.html?c=true&cpp=false&cs=false&py=false&lua=false
			background_colour=None,  # Don't use this if you can avoid it, game handles the background.
			always_visible=False,  # Leave this as default value, game handles it
			condition=100,  # Leave this as default value, game handles it
			size=10,
			# Size of object - roughly translates into cubic feet.  People are 6 unless they are very tiny people.
			material='Stone',
			# Material object is made out of.  Affects the weight along with the size.  Options are 'Flesh' 'Wood' 'Metal' 'Stone' 'Glass' 'Plastic' 'Cloth'
			weight=None,  # Leave this as default value, game handles it
			indestructible=False,  # Exactly what it says.  True or False.
			affixed_to_ground=True,  # Exactly what it says.  True or False.
			blocks_sightline=False,
			# Blocks the cone of visibility in player's field of vision.  Leave False unless object is huge or something as True can be annoying.
			destroyed=False,  # Leave this as default value, game handles it
			functions_as_door=False,
			# Flag as true if you are making door.  Game will automatically handle the open/close.  There is already a default 'Door' you can use.
			components=['Brick', 'Brick', 'Brick', 'Brick', 'Brick', 'Brick'],
			# This determines what objects this object will break into when destroyed.  For exmaple if you make an Object called 'Table' and an Object called 'Wood' then
			# when 'Table' gets destroyed it will drop 'Wood' if you enter components like: ['Wood'].  If you make the components ['Wood', 'Wood'] then
			# it will drop two wood.  This feature isn't built into the game yet but it will be eventually.
			inventory=[],
			# Similar to components, but specifically for living units.  Can give a 'Scientist' a 'Notepad' or something if you want.
			in_inventory_of=None,  # Leave this as default value, game handles it
			food_value=0,  # Leave this as default value, game handles it
			drink_value=0,  # Leave this as default value, game handles it
			rest_value=0,  # Leave this as default value, game handles it
			temp_value=0,  # Leave this as default value, game handles it
			description='A basic wall.',
			unit=None
			# If you are making a living Unit, then this is where you attach the unit Object (you have to make the Unit object separately.
		)  # If this were a scientist then instead of unit = None it would be: unit = get_unit_by_name('Scientist')
	elif predesigned_object_name == 'Door':
		this_object = Object(
			x=0,
			y=0,
			char='D',
			name=predesigned_object_name,
			foreground_colour=libtcod.light_orange,
			background_colour=None,
			always_visible=False,
			condition=100,
			size=9,
			material='Wood',
			weight=None,
			indestructible=False,
			affixed_to_ground=True,
			blocks_sightline=True,
			destroyed=False,
			functions_as_door=True,
			components=[],
			inventory=[],
			in_inventory_of=None,
			food_value=0,
			drink_value=0,
			rest_value=0,
			temp_value=0,
			description='A basic door.',
			unit=None)
	return this_object


def get_unit_by_name(unit_name):
	# Name does no necessarily have to match an object.  You can assign the 'Scientist' personality to any unit.

	if unit_name == 'Generic Humanoid':
		this_unit = Unit()
		this_unit.strength = 1
		this_unit.creature_type = 'Humanoid'
	elif unit_name == 'Scientist':
		this_unit = get_unit_by_name('Generic Humanoid')
		this_unit.name = unit_name
		this_unit.dialogue.append(302)
		this_unit.dialogue.append(303)
		
		real_name = pick_random(['Francis Bubblesmith', 'Ali Zoheir', 'Jayden Scarpo', 'Oskaar Dahl', 'Mathias Karlsen', 'Ingrid Holm', 'Shira Balewa', 'Jessica Smyth', 'Yollanda Ruud', 'Sophie Strand'])
		this_unit.unit_name = real_name
		this_unit.unit_description = None
		if real_name == 'Francis Bubblesmith':
			this_unit.dialogue.append(311)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Francis struggles to balance his time between the science he is famous for and the distraction he is infamous for.  Around the lab he is known as someone who can get results, it just might take him a while to get around to it."
		elif real_name == 'Ali Zoheir':
			this_unit.dialogue.append(312)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Ali's attention to detail was legendary at Alexandria University in Egypt and earned him the nickname 'Eagle-eye' among his classmates. Hardly anything escapes his scrutiny when he sets his mind to it so long as it is easily quantifiable.  "
		elif real_name == 'Jayden Scarpo':
			this_unit.dialogue.append(313)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Truth be told, Jayden isn't exactly isolated-mission material and hasn't wasted a minute letting his lab-mates know this with constant itching for the amenities of his home in Seattle.   "
		elif real_name == 'Oskaar Dahl':
			this_unit.dialogue.append(314)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Nothing bothers Oskaar. He once lost a toe in a sledding accident and continued on the trail between site and lab without a single complaint. His lab-mates were horrified when he took off his mangled boot, but he just whistled to the first aid kit."
		elif real_name == 'Mathias Karlsen':
			this_unit.dialogue.append(315)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "In his high school days Mathias was a huge jock that could do anything but duck out on a challenge. When his friends dared him to take a science major in college he gritted his teeth and studied extremophile biology for six years. "
		elif real_name == 'Ingrid Holm':
			this_unit.dialogue.append(316)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Ingrid skirts the line between collector and hoarder and has a reputation as the one to go to if anything has gone missing in the lab. Her bunk is so piled up with magazines, vinyl toys and gadgets that she just sleeps on the floor most of the time."
		elif real_name == 'Shira Balewa':
			this_unit.dialogue.append(317)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Shira has had a hard time adjusting to the climate of the far north but doesn't let it show. She's fought tooth and nail to get where she is and is the most stand-offish of all the lab scientists, but her dedication to her work still inspires admiration in her colleagues. "
		elif real_name == 'Jessica Smyth':
			this_unit.dialogue.append(318)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Jessica studied chemistry at MIT and got by on grit, grants and the skin of her own teeth. She doesn't believe in anything she can't prove with science and will laugh openly at anyone who suggests otherwise, up to and including the zodiac being responsible for our behavior and the full moon making people nuts. Which drives her nuts."
		elif real_name == 'Yollanda Ruud':
			this_unit.dialogue.append(319)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Many of her fellow scientists suspect Yollanda doesn't have a sense of smell. The evidence for this is anecdotal at best since they've never asked her, but judging by the odor of her bunk and her rack in the fridge she either can't smell or doesn't care that everyone else always can. "
		elif real_name == 'Sophie Strand':
			this_unit.dialogue.append(320)
			this_unit.backstory_dialogue = 310
			this_unit.unit_description = "Sophie doesn't resemble the typical scientist with her brightly colored hair and silly attitude, but her dedication to her work is a huge source of inspiration. Three of her current experiments have yielded positive results in double-blind trials and she isn't afraid to brag about it."


	elif unit_name == 'Dog':
		this_unit = get_unit_by_name('Generic Humanoid')
		this_unit.name = unit_name
		this_unit.dialogue.append(305)
		this_unit.creature_type = 'Animal'
	elif unit_name == 'Nauls':
		this_unit = get_unit_by_name('Generic Humanoid')
		this_unit.name = unit_name
		this_unit.dialogue.append(306)
	return this_unit


def get_material_stats_by_name(material_name, stat_requested):
	if material_name == 'Flesh':
		if stat_requested == 'Weight':
			weight = 30
		elif stat_requested == 'Break Resistance':
			break_resistance = 50
	elif material_name == 'Wood':
		if stat_requested == 'Weight':
			weight = 30
		elif stat_requested == 'Break Resistance':
			break_resistance = 60
	elif material_name == 'Metal':
		if stat_requested == 'Weight':
			weight = 50
		elif stat_requested == 'Break Resistance':
			break_resistance = 95
	elif material_name == 'Stone':
		if stat_requested == 'Weight':
			weight = 40
		elif stat_requested == 'Break Resistance':
			break_resistance = 95
	elif material_name == 'Glass':
		if stat_requested == 'Weight':
			weight = 10
		elif stat_requested == 'Break Resistance':
			break_resistance = 10
	elif material_name == 'Plastic':
		if stat_requested == 'Weight':
			weight = 10
		elif stat_requested == 'Break Resistance':
			break_resistance = 70
	elif material_name == 'Cloth':
		if stat_requested == 'Weight':
			weight = 10
		elif stat_requested == 'Break Resistance':
			break_resistance = 95

	if stat_requested == 'Weight':
		return weight
	elif stat_requested == 'Break Resistance':
		return break_resistance

	print 'get_material_stats_by_name failed for ' + material_name
	return False


class Task:
	# a tile of the map and its properties
	def __init__(self, task_owner, task_type, object_source_of_task=None, object_moving_to=None, object_to_interact_with=None, search_range = None, max_turns_allocated = TOTAL_MAX_TURNS_PER_TASK, task_message_ID=None, quantity = None):

		self.owner = task_owner
		
		self.task_type = task_type
		self.task_message_ID = task_message_ID

		self.object_source_of_task = object_source_of_task
		self.object_moving_to = object_moving_to
		self.object_to_interact_with = object_to_interact_with
		self.quantity = quantity

		self.max_turns_allocated = max_turns_allocated
		self.turn_countdown = max_turns_allocated
		self.search_range = search_range

		if isinstance(object_moving_to, Object):
			self.name_of_object_moving_to = object_moving_to.name
		elif isinstance(object_moving_to, Tile):
			self.name_of_object_moving_to = object_moving_to.room_name	
		else:
			self.name_of_object_moving_to = object_moving_to
			self.object_moving_to = None

		if not self.object_moving_to:
			possible_objects = self.owner.unit.get_nearest_objects(range=search_range, type='Non Affixed Objects')
			for object in possible_objects:
				if self.name_of_object_moving_to:
					if self.name_of_object_moving_to in object.name:
						self.object_moving_to = object
						break

		if isinstance(object_to_interact_with, Object):
			self.name_of_object_to_interact_with = object_to_interact_with.name
		elif isinstance(object_to_interact_with, Tile):
			self.name_of_object_to_interact_with = object_to_interact_with.room_name	
			self.object_to_interact_with = None
		else:
			self.name_of_object_to_interact_with = object_to_interact_with
			self.object_to_interact_with = None

		if not self.object_to_interact_with:
			possible_objects = self.owner.unit.get_nearest_objects(range=search_range, type='Non Affixed Objects')
			for object in possible_objects:
				if self.name_of_object_to_interact_with:
					if self.name_of_object_to_interact_with in object.name:
						self.object_to_interact_with = object
						break

		self.queue_task_end = False
			
	def end_task(self):
		self.owner.task_queue.remove(self)
		del self
		return True
	
	def run_task(self):
		global light_radius
		if ACTIVATE_FUNCTION_TIMERS: this_section = start_test()
	
		if self.queue_task_end:
			return self.end_task()
		
		self.turn_countdown -= 1	
		
		if self.turn_countdown < 0:
			Message(self.owner.name + ": Screw this I give up on " + self.task_type + ".", 'Dialogue', relevant_objects = [self.owner])
			return self.end_task()

		target_not_found = False

		if not self.object_moving_to:
			target_not_found = True
		else:
			if not self.object_moving_to.x:
				target_not_found = True

		if target_not_found:
			Message(self.owner.name + ': Sorry I do not know where ' + str(self.name_of_object_moving_to) + ' is.', 'Dialogue', relevant_objects=[self.owner])
			return self.end_task()
			
			if ACTIVATE_FUNCTION_TIMERS: end_test(this_section, self.owner.name + ' this section e')

		if self.owner.distance_to(self.object_moving_to) <= 1.5:

			if self.task_type == 'Find and Collect Object' or self.task_type == 'Fetch Object for Object' or self.task_type == 'Move to Object' or self.task_type == 'Move to Room'  or self.task_type == 'Examine Object':

				if self.task_type == 'Move to Room':
					return self.end_task()
			
				if self.task_type == 'Move to Object':
					return self.end_task()
					
				if self.task_type == 'Examine Object':
					self.owner.unit.examine(self.object_to_interact_with)
					return self.end_task()
					
				picked_up_object = self.owner.unit.pick_up(self.object_to_interact_with, self.quantity)
				
				if self.task_type == 'Find and Collect Object':
					return self.end_task()
					
				if not self.object_source_of_task:
					Message(self.owner.name + ': I do not even know where I am taking this thing.', 'Dialogue', relevant_objects=[self.owner])
					return self.end_task()

				if not picked_up_object:
					
					self.owner.task_queue.insert(0, Task(
						task_owner = self.owner, 
						task_type = 'Deliver Message to Object',
						object_source_of_task = self.object_source_of_task, 
						object_moving_to = self.object_source_of_task, 
						object_to_interact_with = None, 
						search_range = MAX_VISIBILITY_RADIUS, 
						task_message_ID = 101, 
						quantity = None))
					
					return self.end_task()
					
				else:
					
					self.owner.task_queue.insert(0, Task(
						task_owner = self.owner, 
						task_type = 'Take Object to Object',
						object_source_of_task = self.object_source_of_task, 
						object_moving_to = self.object_source_of_task, 
						object_to_interact_with = picked_up_object, 
						search_range = MAX_VISIBILITY_RADIUS, 
						task_message_ID = None, 
						quantity = self.quantity))
					
					return self.end_task()
				
			elif self.task_type == 'Take Object to Object' or self.task_type == 'Deliver Message to Object':

				if self.task_type == 'Take Object to Object':
					if self.object_source_of_task.check_if_unlocked():
						Message(self.owner.name + ' to ' + self.object_source_of_task.name + ': Here is your ' + self.name_of_object_to_interact_with + '.', 'Dialogue', relevant_objects=[self.owner, self.object_source_of_task, self.object_to_interact_with])
						self.object_source_of_task.take_object_from_inventory(self.owner, self.object_to_interact_with, self.quantity)
					
				elif self.task_type == 'Deliver Message to Object':
					self.owner.unit.speak_to(self.object_moving_to, given_dialogue = None, given_dialogue_ID = self.task_message_ID)

				return self.end_task()

			elif self.task_type == 'Attack Object':
				my_attack_damage = self.owner.unit.attack(target_object_or_tile = self.object_to_interact_with, test = True)
				if not my_attack_damage:
					Message(self.owner.name + ": I am failing at doing any damage to " + self.name_of_object_to_interact_with + ".", 'Dialogue', relevant_objects=[self.owner, self.object_to_interact_with])
					return self.end_task()
				else:
					self.owner.unit.attack(target_object_or_tile = self.object_to_interact_with)
					if self.object_to_interact_with.destroyed:
						return self.end_task()
						
				return True
		else:
			if ACTIVATE_FUNCTION_TIMERS: time_variable = start_test()
			move_astar = self.owner.move_astar(self.object_moving_to)
			if ACTIVATE_FUNCTION_TIMERS: end_test(time_variable, self.owner.name + ' moving astar')
			return move_astar
			
		return False

class Dialogue:
	# a tile of the map and its properties
	def __init__(self, ID, dialogue):
		self.ID = ID
		self.dialogue = dialogue

		self.question = False
		self.responses = []
		self.task_based_on_responses = {}

		self.frequency_of_dialogue = None
		self.feelings_range = None
		
def get_dialogue_by_ID(dialogue_ID):
	this_dialogue = None

	if dialogue_ID == 1:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Yes.')

	elif dialogue_ID == 2:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='No.')

	elif dialogue_ID == 3:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Good.')

	elif dialogue_ID == 4:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Not good.')

	elif dialogue_ID == 5:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Ok I will.')

	elif dialogue_ID == 6:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Ok I won't.")
			
	elif dialogue_ID == 7:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Thank you.')

	elif dialogue_ID == 8:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Thanks for nothing.")
			
	elif dialogue_ID == 9:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Go eat my dad's dick..")

	elif dialogue_ID == 100:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Hello!')

	elif dialogue_ID == 101:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Sorry I failed at my task.')

	elif dialogue_ID == 200:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Are you feeling good today?')

		this_dialogue.question = True
		this_dialogue.responses = [1, 2]

		this_dialogue.frequency_of_dialogue = 5

	elif dialogue_ID == 201:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Should I go and get a flame tank?')

		this_dialogue.question = True
		this_dialogue.responses = [1, 2]
		this_dialogue.task_based_on_responses = {1: ['Fetch Object for Object', 'Flame Tank'], 2: None}

		this_dialogue.frequency_of_dialogue = 5
		
	elif dialogue_ID == 202:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue='Tell me about yourself...')

		this_dialogue.question = True
		this_dialogue.responses = [301]
		
	elif dialogue_ID == 301:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="I'm calm, impatient and greedy. But what'd you expect from somebody with my terrible past. \n I was born and grew up in a broken family in a wealthy town, I lived happily until I was about 5 years old, but at that point life changed.  I maimed somebody during a power outage and was neglected by everybody. With the help of a suspicious friend I had to survive in a brutal world. But with my cunning and diligence, I managed to reach full potential and escape hell.\nThis has turned me into the man I is today.  Still affected by the past, I now work on helping people. By doing so, I hopes to live a normal life and finally find friends I has never had.")

		this_dialogue.question = True
		this_dialogue.responses = [8]
			
	elif dialogue_ID == 302:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="It's a nice day for some science.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 303:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="How do I know you're not The Thing?  I don't trust you.")
		this_dialogue.feelings_range = [0, 5]
			
	elif dialogue_ID == 305:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Woof woof.")
			
	elif dialogue_ID == 306:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Yo.")
			
	elif dialogue_ID == 307:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Welcome scientist.  You have ventured a long way to reach this remote research lab in Antarctica.\nIt's been 100 days since you left civilization.  Many of your team here at the station are starting to get very nervous.  There have been reports from another nearby Norweigian research station of very unusual activity.\nOne night you wake up to the sound of an explosion in the distance... you decide to investigate.")

	elif dialogue_ID == 310:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="That's nunyo bidness.")
			
	elif dialogue_ID == 311:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="I'll never get these tests done in time.. The director is going to kill me if I'm late again.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 312:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="These numbers don't look right. I wonder if the ambient temperature in the lab is effecting my results.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 313:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="If I don't get a strong cup of coffee soon I'm going to go insane!")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 314:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="You can't do science without a good sweater, and my sweaters are the best.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 315:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="I studied science on a dare and now I'm freezing in the middle of nowhere. Damn my foolish pride!")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 316:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="Another hundred days until I can go home again. Ugh, I should have brought another book.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 317:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="I couldn't be further away from where I came from. The kids at school said I'd never do anything with my life. Good riddance to them!")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 318:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="If I didn't have the scientific method I'd have nothing at all. A better way to spend your life? Prove it!")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 319:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="It isn't so bad working up here in the ice and snow. As long as I have pickled eggs there isn't anything I can't do.")
		this_dialogue.feelings_range = [5, 10]
			
	elif dialogue_ID == 320:
		this_dialogue = Dialogue(
			ID=dialogue_ID,
			dialogue="S to the C to the I to the E, c'mon egg heads sing it with me! N to the C and then another E, SCIENCE is the life for me! Hm.. maybe I should have stuck with cheerleading.")
		this_dialogue.feelings_range = [5, 10]
			
	return this_dialogue

	
libtcod.console_set_custom_font('ascii_font_2.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
#libtcod.console_set_custom_font('ascii_font_7.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
#libtcod.console_set_custom_font('ascii_font_8.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

con = libtcod.console_new(MAP_WIDTH, MAP_HEIGHT)
panel = libtcod.console_new(OBJECT_INFO_BAR_WIDTH, PANEL_HEIGHT)
message_panel = libtcod.console_new(MESSAGE_PANEL_WIDTH, PANEL_HEIGHT)
object_panel = libtcod.console_new(OBJECT_INFO_BAR_WIDTH, MAP_HEIGHT)

mouse = libtcod.Mouse()
key = libtcod.Key()

libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

main_menu()

"""
Anger: resentment, irritation, frustration;
Fear: apprehension, overwhelmed, threatened, scared;
Pain: sad, lonely, hurt, pity;
Joy: hopeful, elated, happy, excitement
Passion: enthusiasm, desire, zest;
Love: affection, tenderness, compassion, warmth;
Shame: embarrassment, humble, exposed;
Guilt: regretful, contrite, and remorseful
"""



