from tools import  *
from objects import *
from routines import *


#This file is for strategy

class ExampleBot(GoslingAgent):
    def run(agent):

        #An example of pushing routines to the stack:
        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
            elif agent.me.boost < 40:
                # go get boost
                print('getting boost')
                open_boost = [boost for boost in agent.boosts if boost.large and boost.active]
                # closest = open_boost[0]
                closest = None
                
                # closest_distance = None
                for boost in open_boost:
                    # print(boost.large, boost.index)
                    if (closest is None):
                        closest = boost
                        continue
                    distance = (boost.location - agent.me.location).magnitude()
                    if (distance > 700 and distance < (closest.location - agent.me.location).magnitude()):
                        closest = boost
                agent.push(fill_boost(boost=closest))
            else:
                agent.push(short_shot(agent.foe_goal.location))

