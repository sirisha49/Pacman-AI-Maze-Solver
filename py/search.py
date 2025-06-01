# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = util.Stack()
    initial_state = problem.getStartState()
    stack.push((initial_state, []))

    visited_states = set()

    while not stack.isEmpty():
        current_state, path_actions = stack.pop()
        if current_state in visited_states:
            continue
        visited_states.add(current_state)
        if problem.isGoalState(current_state):
            return path_actions
        successors = problem.getSuccessors(current_state)
        for next_state, move, _ in successors:
            stack.push((next_state, path_actions + [move]))

    return []

def breadthFirstSearch(problem):
    queue = util.Queue()
    initial_state = problem.getStartState()
    queue.push((initial_state, []))

    visited_states = set()

    while not queue.isEmpty():
        current_state, path_actions = queue.pop()
        if current_state in visited_states:
            continue
        visited_states.add(current_state)
        if problem.isGoalState(current_state):
            return path_actions
        successors = problem.getSuccessors(current_state)
        for next_state, move, _ in successors:
            queue.push((next_state, path_actions + [move]))

    return []


def uniformCostSearch(problem):
    priority_queue = []
    initial_state = problem.getStartState()
    heappush(priority_queue, (0, (initial_state, [])))

    visited_costs = {}

    while priority_queue:
        path_cost, (current_state, path_actions) = heappop(priority_queue)
        if problem.isGoalState(current_state):
            return path_actions
        if current_state in visited_costs and visited_costs[current_state] <= path_cost:
            continue
        visited_costs[current_state] = path_cost
        successors = problem.getSuccessors(current_state)
        for next_state, move, step_cost in successors:
            new_path_actions = path_actions + [move]
            total_cost = path_cost + step_cost
            if next_state not in visited_costs or visited_costs[next_state] > total_cost:
                heappush(priority_queue, (total_cost, (next_state, new_path_actions)))

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    priority_queue = util.PriorityQueue()
    initial_state = problem.getStartState()
    initial_priority = heuristic(initial_state, problem)
    priority_queue.push((initial_state, []), initial_priority)

    visited_costs = {}

    while not priority_queue.isEmpty():
        current_state, path_actions = priority_queue.pop()
        if problem.isGoalState(current_state):
            return path_actions
        if current_state in visited_costs and visited_costs[current_state] <= problem.getCostOfActions(path_actions):
            continue
        visited_costs[current_state] = problem.getCostOfActions(path_actions)
        successors = problem.getSuccessors(current_state)
        for next_state, move, _ in successors:
            new_path_actions = path_actions + [move]
            path_cost = problem.getCostOfActions(new_path_actions)
            heuristic_cost = heuristic(next_state, problem)
            total_priority = path_cost + heuristic_cost

            if next_state not in visited_costs or visited_costs[next_state] > path_cost:
                priority_queue.update((next_state, new_path_actions), total_priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
