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
from re import search

import util
from game import Directions
from typing import List



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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    # util.raiseNotDefined()

    stack = util.Stack()
    visited = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    stack.push((problem.getStartState(), []))
    while not stack.isEmpty():
        state, actions = stack.pop()
        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))

    return []


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    queue = util.Queue()
    visited = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    queue.push((problem.getStartState(), []))
    while not queue.isEmpty():
        state, actions = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, _ in problem.getSuccessors(state):
                queue.push((successor, actions + [action]))

    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    queue = util.PriorityQueue()
    visited = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    # queue.push((problem.getStartState(), []))
    queue.push((problem.getStartState(), [], 0), 0)
    while not queue.isEmpty():
        state, actions, curCost = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, cost in problem.getSuccessors(state):
                queue.push((successor, actions + [action], curCost + cost), curCost + cost)

    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    queue = util.PriorityQueue()
    visited = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    queue.push((problem.getStartState(), [], 0), 0)

    d = {
        problem.getStartState(): 0
    }

    while not queue.isEmpty():
        state, actions, curCost = queue.pop()

        if problem.isGoalState(state):
            return actions

        for successor, action, cost in problem.getSuccessors(state):
            new_actions = actions + [action]
            cost = problem.getCostOfActions(new_actions)
            heuristic_cost = heuristic(successor, problem)

            if successor not in d or d[successor] > cost:
                d[successor] = cost
                queue.push((successor, new_actions, cost), cost + heuristic_cost)

            # heuristic_cost = heuristic(successor, problem)
            # successor_cost = curCost + cost
            #
            # if successor in d and d[successor] <= successor_cost:
            #     continue
            #
            # queue.push((successor, actions + [action], successor_cost), successor_cost + heuristic_cost)
            # d[successor] = successor_cost + heuristic_cost



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
