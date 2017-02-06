from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator import settings
from MyState import MyState
from MyAction import MyAction


## Random Strategy
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())

class StraightStrategy1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Straight")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        if not myaction.canKick(pos_player, pos_ball):
            print "going to the ball!"
            # print pos_player.distance(pos_ball)
            # print (settings.PLAYER_RADIUS + settings.BALL_RADIUS) + 0.5
            return myaction.go(pos_player, pos_ball)
        else:
            print "kicking the ball!" 
            return myaction.kick(pos_player, pos_ball)

class StraightStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Straight")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        pos_goal = mystate.get_posGoal(id_team)
        if myaction.canShoot(pos_player, pos_ball, pos_goal):
            print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal)

        if not myaction.canKick(pos_player, pos_ball):
            # print "player's velocity is "
            # print mystate.get_vitPlayer(id_team, id_player)
            print "going to the ball!"
            return myaction.go(pos_player, pos_ball)
        else: 
            print "kicking to the ball!"
            return myaction.kick(pos_player, pos_goal)

if __name__ == '__main__':
    ## Creation d'une equipe
    team1 = SoccerTeam(name="team1",login="etu1")
    team2 = SoccerTeam(name="team2",login="etu2")
    team1.add("John",StraightStrategy1()) 
    team2.add("Paul",RandomStrategy())  
    team2.add("Thomas",RandomStrategy())  

    #Creation d'une partie
    simu = Simulation(team1,team2)
    #Jouer et afficher la partie
    show_simu(simu)
    #Jouer sans afficher
    simu.start()
