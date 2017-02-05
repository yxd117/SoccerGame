from soccersimulator.mdpsoccer import SoccerAction
from MyState import MyState
from soccersimulator.utils import Vector2D
from soccersimulator import settings

class MyAction:
	# def __init__(self):
	# 	self.act = act
	#to be developed

	def go(self, pos1, pos2):
		acc = MyState.get_vecDist(pos1, pos2)
		return SoccerAction(acc, None)

	def Pass(self, pos1, pos2):
		dire = MyState.get_vecDist(pos1, pos2).normalize()
		return SoccerAction(Vector2D(), dire)

	def shoot(self, pos_player, pos_goal):
		dire = MyState.get_vecDist(pos_player, pos_goal)
		return SoccerAction(Vector2D(), dire)
		
	def kick(self, pos_player, pos_ball):
		return self.Pass(pos_player, pos_ball)

	def canKick(self, pos_player, pos_ball):
		return pos_player.distance(pos_ball) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS)

	def canShoot(self, pos_player, pos_ball, pos_goal):
		return self.canKick(pos_player, pos_ball) and pos_player.distance(pos_goal) <= 40