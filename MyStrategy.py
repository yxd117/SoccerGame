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

class ShootStrategy(Strategy):
    def __init__(self, angle, norm):
        Strategy.__init__(self,"Shoot")
        self.angle = angle
        self.norm = norm
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(angle = self.angle, norm = self.norm)

class StraightStrategy1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Straight")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        pos_goal = mystate.get_posGoal(id_team)
        if myaction.canShoot(pos_player, pos_ball, pos_goal):
            # print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal)

        if not myaction.canKick(pos_player, pos_ball):
            # print "player's velocity is "
            # print mystate.get_vitPlayer(id_team, id_player)
            # print "going to the ball!"
            return myaction.go(pos_player, pos_ball, 2)
        else: 
            # print "kicking to the ball!"
            return myaction.kick(pos_player, pos_goal)
class StraightStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Straight")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        pos_teammate = mystate.get_posPlayer(id_team, id_player + 1)
        pos_goal = mystate.get_posGoal(id_team)
        if myaction.canShoot(pos_player, pos_ball, pos_goal):
            # print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal)

        if not myaction.canKick(pos_player, pos_ball):
            # print "player's velocity is "
            # print mystate.get_vitPlayer(id_team, id_player)
            # print "going to the ball!"
            return myaction.go(pos_player, pos_ball, 2)
        else: 
            # print "kicking to the ball!"
            # return myaction.kick(pos_player, pos_goal)
            return myaction.kick(pos_player, pos_teammate, 5)


class StraightStrategy3(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Straight")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        pos_goal = mystate.get_posGoal(id_team)
        pos_shoot = mystate.get_posShoot(id_team, id_player)
        # print str(id_player) + ' ' + str(pos_player) + ' ' + str(pos_shoot)
        if myaction.canShoot(pos_player, pos_ball, pos_goal):
            # print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal)

        if not myaction.reachPosition(pos_player, pos_shoot):
            # print "player's velocity is "
            # print mystate.get_vitPlayer(id_team, id_player)
            # print "going to the point!"
            # print str(pos_player) + " to " + str(pos_shoot) + '\n'
            return myaction.go(pos_player, pos_shoot, 0.5)
        else :
            return myaction.go(pos_player, pos_ball)

class DefendStrategy(Strategy):
    def __init__(self, type):
        Strategy.__init__(self,"Straight")
        self.type = type
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state)
        myaction = MyAction()
        pos_ball = mystate.get_posBall()
        pos_player = mystate.get_posPlayer(id_team, id_player)
        pos_def = mystate.get_posGoal(id_team % 2  + 1)
        if self.type == 1 :
            pos_def.y += 2
        elif self.type == 2:
            pos_def.y -= 2
        else:
            pass
        pos_goal = mystate.get_posGoal(id_team)
        # print str(id_player) + ' ' + str(pos_player) + ' ' + str(pos_shoot)
        if myaction.near(pos_player, pos_goal, 45) and myaction.canKick(pos_player, pos_ball):
            print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal, 5)

        if myaction.canKick(pos_player, pos_ball):
            # print "shooting the ball"
            return myaction.shoot(pos_player, pos_goal, 2)
        if myaction.near(pos_player, pos_ball) :
            return myaction.go(pos_player, pos_ball)

        if not myaction.reachPosition(pos_player, pos_def):
            # print "player's velocity is "
            # print mystate.get_vitPlayer(id_team, id_player)
            # print "going to the point!"
            # print str(pos_player) + " to " + str(pos_shoot) + '\n'
            return myaction.go(pos_player, pos_def)



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
