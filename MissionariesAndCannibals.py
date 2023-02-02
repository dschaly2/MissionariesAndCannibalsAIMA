"""
Drew Schaly

@author: fill in the blank

This file implements the missionaries and cannibals problem using
the problem class specfied for the AIMA python search.py file

It then finds solutions to this problem using 2 different search algorithms:
Depth First and Breadth First
"""

from search import *

class MandC(Problem):
    ''' This is the Missionaries and Cannibals Problem
    it's inherited from the Problem class (see search.py).
    '''
    def __init__(self, initial, goal):
        #call ths parent class's constructor
        Problem.__init__(self,initial,goal)

    def isValid(self,state, action):
        state = self.result(state,action)
       
        validAction = False
        
        if(all(i >= 0 for i in state)):
            if(state[0] >= state[1] or state[0] == 0):
                if(state[2] >= state[3] or state[2] == 0):
                    validAction = True

        return validAction

    def actions(self,state):
        possibleActions = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        legalActions = []

        for i in range(5):
            if(self.isValid(state,possibleActions[i])):
                legalActions.append(possibleActions[i])

        return legalActions

                    
        # This method should return a set of legal actions from
        # the current state

    def result(self, state, action):
 
        stateList = list(state)
 
        if (stateList[4] == 0):
            stateList[0] = stateList[0] - action[0]
            stateList[2] = stateList[2] + action[0]
            stateList[1] = stateList[1] - action[1]
            stateList[3] = stateList[3] + action[1]
            stateList[4] = 1
        else:
            stateList[2] = stateList[2] - action[0]
            stateList[0] = stateList[0] + action[0]
            stateList[3] = stateList[3] - action[1]
            stateList[1] = stateList[1] + action[1]
            stateList[4] = 0
 
        state = tuple(stateList)

        return state
        
                # This method returns the new state after applying action
        # to state

    # are there additional methods you'd like to define to help solve this problem?

#Now you should test this:

def main():

    initial_state = (3,3,0,0,0) # 3 missionaries and cannibals on left side
    goal_state = (0,0,3,3,1) 
    mc = MandC(initial_state,goal_state)

    soln = depth_first_graph_search(mc)
    print("Depth First Search")
    print("Solution Length: " + str(len(soln.path())))
    print("Nodes Traversed:")
    print(soln.path())
    print("Actions Taken:")
    print(soln.solution())

    soln = breadth_first_search(mc)
    print("Breadth First Search")
    print("Solution Length: " + str(len(soln.path())))
    print("Nodes Traversed:")
    print(soln.path())
    print("Actions Taken:")
    print(soln.solution())

if __name__ == "__main__":
    main()
