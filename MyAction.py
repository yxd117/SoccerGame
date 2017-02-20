from soccersimulator.mdpsoccer import SoccerAction
from MyState import MyState
from soccersimulator.utils import Vector2D
from soccersimulator import settings

class MyAction:
	# def __init__(self):
	# 	self.act = act
	#to be developed

	def go(self, pos1, pos2, scale = 1):
		acc = MyState.get_vecDist(pos1, pos2).scale(scale)
		return SoccerAction(acc, None)

	def Pass(self, pos1, pos2, normalize = False, scale = 1):
		dire = MyState.get_vecDist(pos1, pos2)
		if normalize:
			dire = dire.normalize()
		dire = dire.scale(scale)
		return SoccerAction(Vector2D(), dire)

	def shoot(self, pos_player, pos_goal, scale = 1):
		dire = MyState.get_vecDist(pos_player, pos_goal).normalize()
		dist_goal = pos_player.distance(pos_goal)
		if scale == 1:
			if dist_goal <= 20:
				scale = 2
			else :
				scale = 2 + (dist_goal - 20) / 10.0
		dire = dire.scale(scale)
		# f = open('shootdata.txt', 'a')
		# f.write("Player position" + str(dire) +'\n')
		return SoccerAction(Vector2D(), dire)
		
	def kick(self, pos_player, pos_dest, normalize = True, scale = 1):
		return self.Pass(pos_player, pos_dest, normalize, scale)

	def canKick(self, pos_player, pos_ball):
		return pos_player.distance(pos_ball) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS)

	def canShoot(self, pos_player, pos_ball, pos_goal):
		return self.canKick(pos_player, pos_ball) and pos_player.distance(pos_goal) <= 40

	def reachPosition(self, pos_player, pos):
		return pos_player.distance(pos) <= 2
	def near(self, pos1, pos2, threshold = 35):
		return pos1.distance(pos2) <= threshold