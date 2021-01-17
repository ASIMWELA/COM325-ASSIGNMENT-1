# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # using stack in oder to facilitate the search from from the last visited Node
    state_actions = util.Stack()

    # initialise the explored node to empty
    # i.e No node is visited in the initial state
    visited_nodes = []
    # Make an empty list of actions
    action_list = []

    # initialize the first state to the stark
    state_actions.push((problem.getStartState(), action_list))

    # loop through states
    while state_actions:
        node, actions = state_actions.pop()

        # check if node is not already visited  and then add it to the visited after being explored
        if not node in visited_nodes:
            visited_nodes.append(node)

            # return actions if the current node is the goal
            if problem.isGoalState(node):

                # actual return here
                return actions

            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                state_actions.push((coordinate, nextActions))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Use Queue to explore all the nodes onn the same level before going to the next level
    state_actions = util.Queue()

    # Make an empty list of explored nodes
    visited_nodes = []

    # Make an empty list of actions
    action_list = []

    # Place the starting point in the queue
    state_actions.push((problem.getStartState(), action_list))

    # loop through states
    while state_actions:

        # remove the last put node to explore it
        node, actions = state_actions.pop()

        # check if the current node being explored is already visited or not
        if not node in visited_nodes:
            visited_nodes.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                state_actions.push((coordinate, nextActions))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    state_actions = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited_nodes = []

    # Make an empty list of actions
    action_list = []

    # Place the starting state in the priority queue
    state_actions.push((problem.getStartState(), action_list), problem)
    while state_actions:

        # remove the last put node to explore it
        node, actions = state_actions.pop()

        # check if the current node being explored is already visited or not
        if not node in visited_nodes:
            visited_nodes.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                state_actions.push((coordinate, nextActions), nextCost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state_actions = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    action_list = []
    # Place the starting point in the priority queue
    state_actions.push((problem.getStartState(), action_list), heuristic(problem.getStartState(), problem))

    # loop through the states
    while state_actions:

        # get the first state
        node, actions = state_actions.pop()

        # check if the current state is already visited
        if not node in visited:

            # add the node ( state) to the visited if it was not already visited
            visited.append(node)

            # if the current node (state) is the goal return its actions
            if problem.isGoalState(node):
                return actions

           # direct to the next node if the current node is not the goal node
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions) + \
                           heuristic(coordinate, problem)
                state_actions.push((coordinate, nextActions), nextCost)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
