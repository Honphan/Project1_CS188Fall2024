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
from collections import deque

import util
from game import Directions
from typing import List

from util import Queue


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
    #Đầu tiên lấy ra vị trí bắt đầu của đối tượng problem và tạo Stack rỗng để chứa các node đã thăm
    startState = problem.getStartState()
    stack = util.Stack()
    path = []
    #Đẩy trạng thái đầu tiên và đường đi vào stack
    stack.push((startState, path))
    visited = set()

    #Kiểm tra stack, nếu không rỗng thì lấy trạng thái tiếp theo và path hiện tại
    while not stack.isEmpty():
        state, path = stack.pop()
        #Nếu state này đã thăm thì quay lại vòng lặp từ đầu
        if state in visited:
            continue
        #Nếu chưa thăm thì thêm vào visited
        visited.add(state)
        #Nếu this state là trạng thái Goal mong muốn thì return về path
        if problem.isGoalState(state):
            return path
        #Duyệt tiếp các state tiếp theo
        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in visited:
                newPath = path + [action]
                stack.push((nextState, newPath))
    return []

    util.raiseNotDefined() #hàm throw lỗi với thông tin debug chi tiết khi một phương thức chưa được implement

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:

    visited = set()
    startState = problem.getStartState()
    path = []
    queue = Queue()
    queue.push((startState, path))
    visited.add(startState)

    while queue:
        state, path = queue.pop()

        if problem.isGoalState(state):
            return path

        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in visited:
                visited.add(nextState)
                newPath = path + [action]
                queue.push((nextState, newPath))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    visited = set()
    startState = problem.getStartState()
    path = []
    priorityQueue = util.PriorityQueue()
    priorityQueue.push((startState, path, 0), 0)

    while not priorityQueue.isEmpty():
        state, path, currentCost = priorityQueue.pop()

        if state in visited:
            continue

        if problem.isGoalState(state):
            return path
        visited.add(state)
        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in visited:

                newCost = cost + currentCost
                newPath = path + [action]
                priorityQueue.push((nextState, newPath, newCost), newCost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    openSet = util.PriorityQueue()
    #closedSet = set() //Ở trường hợp A* này thì khi mình đã duyệt qua state nào đó thì chưa chắc đã là đường đi tối ưu
    #nên nếu sử dụng closedSet thì các node đã duyệt không bao giờ được duyệt lại để lấy đường đi tối ưu nữa./
    startState = problem.getStartState()
    gScore = {startState: 0} #Dòng này có nghĩa là để chỉ chi phi từ node đầu tiên đến vị trị startState. Hiện tại đang là bằng 0./
    path = []
    openSet.push((startState, path), heuristic(startState, problem))

    while not openSet.isEmpty():
        state, path = openSet.pop()

        if problem.isGoalState(state):
            return path
        if gScore[state] + heuristic(state, problem) < 0:
            continue

        for nextState, action, stepCost in problem.getSuccessors(state):
            newCost = stepCost + gScore[state]
            newPath = path + [action]
            if nextState not in gScore or newCost < gScore[nextState]:
                gScore[nextState] = newCost
                f = gScore[nextState] + heuristic(nextState, problem)
                openSet.push((nextState, newPath), f)
    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
