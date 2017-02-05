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

#Help Function
def get_vecDist(self, pos1, pos2):
	return pos2 - pos1
def get_posGoal(id_team):
	if id_team == "team1":
		return Vector2D(0, 45)
	else:
		return Vector2D(150, 45)

