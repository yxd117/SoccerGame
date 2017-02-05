from soccersimulator.mdpsoccer import SoccerAction
from MyState import get_vecDist, get_posGoal
from soccersimulator.utils import Vector2D

class MyAction:
	def __init__(self, act):
		self.act = act
	#to be developed
	def go(self, pos1, pos2):
		acc = get_vecDist(pos1, pos2)
		return SoccerAction(acc, None)

	def Pass(self, pos1, pos2):
		dire = get_vecDist(pos1, pos2)
		return SoccerAction(Vector2D(), dire)

	def shoot(self, pos):
		dire = get_vecDist(pos, get_posGoal())
		return SoccerAction(Vector2D(), dire)


	