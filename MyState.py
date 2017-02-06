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

	def get_posShoot(self, id_team, id_player):
		game_height = settings.GAME_HEIGHT
		game_width = settings.GAME_WIDTH
		quarters = [i * settings.GAME_HEIGHT / 4. for i in range(1, 4)]
		rows = [settings.GAME_WIDTH * 0.1, settings.GAME_WIDTH * 0.35, settings.GAME_WIDTH * (1 - 0.35),settings.GAME_WIDTH * (1 - 0.1)]
		pos_player = self.get_posPlayer(id_team, id_player).copy()
		index = id_player % 2
		if index == 1 :
			index += 1
		if id_team == 1:
			return Vector2D(rows[3], quarters[index])
		else:
			return Vector2D(rows[0], quarters[index])
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




