from soccersimulator.utils import Vector2D
from soccersimulator import settings

class MyState:
	def __init__(self, state):
		self.state = state
	def get_ball(self):
		return self.state.ball
	def get_posBall(self):
		return self.get_ball().position
	def get_vitBall(self):
		return self.get_ball().vitesse
	def get_statePlayer(self, id_team, id_player):
		return self.state.player_state(id_team, id_player)
	def get_posPlayer(self, id_team, id_player):
		return self.get_statePlayer(id_team, id_player).position
	def get_vitPlayer(self, id_team, id_player):
		return self.get_statePlayer(id_team, id_player).vitesse	
	@staticmethod
	def get_posGoal(id_team, pos = "middle"):
		game_height = settings.GAME_HEIGHT
		goal_height = settings.GAME_GOAL_HEIGHT
		if id_team == 2:
			width = 0
		else:
			width = settings.GAME_WIDTH
		if pos == "left" : 
			height = game_height / 2 - goal_height / 2
		elif pos == "right" :
			height = game_height / 2 + goal_height / 2;
		else :
			height = game_height / 2 ;
		return Vector2D(width, height)
	#Help Function
	@staticmethod
	def get_vecDist(pos1, pos2):
		return pos2 - pos1




