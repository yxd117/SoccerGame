from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from MyAction import MyAction
from MyState import MyState
import math

GOLF = 0.001
SLALOM = 10.

#golf
class DirectStrategy_golf(Strategy):
    def __init__(self):
		super(DirectStrategy_golf,self).__init__("Demo")

    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            pos_player = mystate.get_posPlayer(id_team, id_player)
            pos_goal = mystate.get_posGoal(id_team)
            if not (myaction.canKick(pos_player, pos_ball)):
                return myaction.go(pos_player, pos_ball, 2)
            else:
                return myaction.kick(pos_player, pos_goal)
        best_index = 0
        min_dis = 1000000
        for i in range(len(zones)) :
            zone = zones[i]
            centre = zone.position+Vector2D(zone.l/2, zone.l/2)
            if centre.distance(pos_player) < min_dis:
                best_index = i
                min_dis = centre.distance(pos_player)

        zone = zones[best_index]
        if zone.dedans(state.ball.position):
            return SoccerAction()
        if not myaction.canKick(pos_player, pos_ball):
            return myaction.go(pos_player, pos_ball, 5)
        else:
			centre = zone.position+Vector2D(zone.l/2, zone.l/2)
			dis = pos_player.distance(centre)
			if dis < 20:
				scale = 0.2
			else:
				scale = 2
			return myaction.kick(pos_player, centre, True, scale)

        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        """ si la ball est dans une zone a valider """

        """ sinon go to the zones"""
        return SoccerAction()
        
class DirectStrategy_slalom(Strategy):
    def __init__(self):
		super(DirectStrategy_slalom,self).__init__("Demo")

    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            pos_player = mystate.get_posPlayer(id_team, id_player)
            pos_goal = mystate.get_posGoal(id_team)
            if not (myaction.canKick(pos_player, pos_ball)):
                return myaction.go(pos_player, pos_ball, 2)
            else:
                return myaction.kick(pos_player, pos_goal)
        best_index = 0
        min_dis = 1000000
        for i in range(len(zones)) :
            zone = zones[i]
            centre = zone.position+Vector2D(zone.l/2, zone.l/2)
            if centre.distance(pos_player) < min_dis:
                best_index = i
                min_dis = centre.distance(pos_player)
        zone = zones[best_index]
        if zone.dedans(state.ball.position):
            return SoccerAction()
        if not myaction.canKick(pos_player, pos_ball):
            return myaction.go(pos_player, pos_ball, 5)
        else:
			centre = zone.position+Vector2D(zone.l/2, zone.l/2)
			dis = pos_player.distance(centre)
			if dis < 20:
				scale = 0.5
			else:
				scale = 2
			return myaction.kick(pos_player, centre, True, scale)

        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        """ si la ball est dans une zone a valider """

        """ sinon go to the zones"""
        return SoccerAction()

team1 = SoccerTeam()
team2 = SoccerTeam()
#~ team1.add("John",DirectStrategy_golf())
team1.add("Johggn",DirectStrategy_golf())

team2.add("John",DirectStrategy_golf())
#~ simu = Parcours1(team1=team1,vitesse=GOLF)
#~ show_simu(simu)
simu = Parcours4(team1=team1,vitesse=GOLF)
show_simu(simu)
#~ simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
#~ show_simu(simu)
