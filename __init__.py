from soccersimulator.mdpsoccer import SoccerTeam
from MyStrategy import StraightStrategy, RandomStrategy 
def get_team(i):
	team = SoccerTeam(name="team",login="etu1")
	if i == 1:
		team.add("Mike",StraightStrategy2())
	elif i == 2:
		team.add("Mike",StraightStrategy2())
		team.add("Paul",StraightStrategy2())
	elif i == 4:
		team.add("Mike",StraightStrategy2())
		team.add("Paul",StraightStrategy2())
		team.add("Thomas",StraightStrategy2())
		team.add("Jim",StraightStrategy2())
	return team