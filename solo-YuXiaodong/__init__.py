from MyGolf import DirectStrategy_slalom, DirectStrategy_golf
from soccersimulator.mdpsoccer import SoccerTeam
def get_golf_team():
	team = SoccerTeam()
	team.add("John",DirectStrategy_golf())
	return team
	
	
def get_slalom_team1():
	team = SoccerTeam()
	team.add("John",DirectStrategy_slalom())
	return team
def get_slalom_team2():
	team = SoccerTeam()
	team.add("John",DirectStrategy_slalom())
	team.add("Paul",DirectStrategy_slalom())
	return team
