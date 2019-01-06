import pygame
class Music():
	"""Create the music for the game."""
	def __init__(self):
		pass
	def looping_music(self,mus_ic):
		"""Initialize the looping game music."""
		pygame.mixer.music.load(mus_ic)
		pygame.mixer.music.play(-1)
	
	def shooting_sound(self):
		"""Initialize the shoot_sound."""
		pygame.mixer.music.pause()
		shoot_sound=pygame.mixer.Sound('sound/gun_shot.wav')
		pygame.mixer.Sound.play(shoot_sound)
		pygame.mixer.music.unpause()
	
		
