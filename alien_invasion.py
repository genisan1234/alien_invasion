#This is the initial python script for designing the first surface of the game
#The game has been built using the  pygame module downloaded from bitbucket.org
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from music import Music
def run_game():
    #initialising the background settings so that pygame runs properly
	pygame.init()
	#initialising the settings object
	ai_settings=Settings()
	
	#intialising the pygame screen
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#create an instance to store game statistics
	stats=GameStats(ai_settings)
	#create a scoreboard
	sb=Scoreboard(ai_settings,screen,stats)
	#Make a ship
	ship=Ship(ai_settings,screen)
	#Make a group to store bullets
	bullets=Group()
	#set the background color
	bg_color=ai_settings.bg_color
	#Make the play button
	play_button=Button(ai_settings,screen,"Play")
	#Create a group/fleet of aliens
	aliens=Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#Add music to the game
	musi=Music()
	musi.looping_music("music/game_music_1.mp3")
	#start the main loop for the game.
	while True:
		#watch for keyboard and mouse events
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,musi)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()
