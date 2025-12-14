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
from game import Directions
from typing import List
import csv

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
    # print(problem)
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # dùng để chạy thuật toán DFS theo LIFO
    stack = util.Stack()

    # trạng thái bắt đầu
    start_state = problem.getStartState()

    # trạng thái bắt đầu vào Stack: (trạng thái, [hành động],cost)
    stack.push((start_state, [], 0))

    # lưu trạng thái đã đi
    explored_states = set()

    # khi mà stack còn phần tử
    while not stack.isEmpty():
        # Lấy phần tử trên cùng
        cur_state, cur_actions, cur_cost = stack.pop()

        # Kiểm tra goal nếu là goal kết thúc
        if problem.isGoalState(cur_state):
            return cur_actions

        # thêm trạng thái hiện tại vào tập explored_states
        if cur_state not in explored_states:
            explored_states.add(cur_state)

            # Mở rộng theo chiều NORTH, SOUTH, EAST, WEST đẩy vào stack theo thứ tự:
            for successor_state, action, cost in problem.getSuccessors(cur_state):
                # xử lý các trạng thái chưa được mở rộng
                if successor_state not in explored_states:
                    # thêm action vao list cur_action : cộng 2 list
                    new_actions = cur_actions + [action]
                    new_cost = cur_cost + cost
                    stack.push((successor_state, new_actions, new_cost))

    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # dùng để chạy BFS theo FIFO
    queue = util.Queue()
    # lưu trạng thái đã thăm qua
    explored_states = set()
    # trạng thái bắt đầu ((trạng thái, [hành động],cost))
    queue.push((problem.getStartState(), [],0))

    # Ghi các bước chạy vào file csv
    with open('log_q5.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Đặt tên cột
        writer.writerow(['Step', 'CurrState ', 'Cost', 'Path'])

    # Chỉ số bước chạy
    step_count = 0
    # chạy đến khi queue trống
    while not queue.isEmpty():

        # lấy và xóa phẩn tử dưới cùng của queue
        current_state, cur_actions, cur_cost= queue.pop()

        # Ghi ra file
        step_count += 1
        # Mở file và nối dữ liệu vào
        with open('log_q5.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([step_count, str(current_state), cur_cost, str(cur_actions)])

        # nếu nó là goal thì trả về tất cả các bước đã thực hiện để chương trình chạy game
        if problem.isGoalState(current_state):
            return cur_actions

        # nêu node này chưa đc khám phá
        if current_state not in explored_states:
            # thêm nó vào queue
            explored_states.add(current_state)

            # mở rộng từ node hiện tại xong cập nhật các giá trị như action,cost
            for successor_state, action, cost in problem.getSuccessors(current_state):
                new_actions = cur_actions + [action]
                new_cost = cur_cost + cost
                queue.push((successor_state, new_actions, new_cost))

    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # dùng để chạy priority queue
    priority = util.PriorityQueue()
    # lưu trạng thái đã thăm qua
    explored_states = set()
    # trạng thái bắt đầu ((trạng thái, [hành động],cost))
    priority.push((problem.getStartState(), [], 0),0)

    # chạy đến khi queue trống
    while not priority.isEmpty():

        # xóa phẩn tử có độ ưu tiên cao nhất trong p_queue
        current_state, cur_actions, cur_cost = priority.pop()

        # nếu nó là goal thì trả về tất cả các bước đã thực hiện để chương trình chạy game
        if problem.isGoalState(current_state):
            return cur_actions

        # nêu node này chưa đc khám phá
        if current_state not in explored_states:
            # thêm nó vào p_queue
            explored_states.add(current_state)

            # mở rộng từ node hiện tại xong cập nhật các giá trị như action,cost
            for successor_state, action, cost in problem.getSuccessors(current_state):
                new_actions = cur_actions + [action]
                new_cost = cur_cost + cost
                priority.push((successor_state, new_actions, new_cost), new_cost)

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
    # để lưu hàm fn theo thứ tự ưu tiên: fn = cost + hn
    priority_queue = util.PriorityQueue()

    # dùng để lưu tập trạng thái mà ở đó fn là thấp nhất { current_state: fn) fn: nhỏ nhất
    lowest_cost = {}
    priority_queue.push((problem.getStartState(), [], 0),0)

    while not priority_queue.isEmpty():

        # Lấy ra item có fn thấp nhất
        current_state, cur_actions, cur_cost = priority_queue.pop()

        # check xem nếu đẫ có trạng thái đó rồi mà trạng thái đó có fn >=  fn hiện tại thì cho qua
        if current_state in lowest_cost and lowest_cost[current_state] <= cur_cost:
            continue

        # ngược lại thì cập nhật vào lowest_cost
        lowest_cost[current_state] = cur_cost

        # check xem có là goal không
        if problem.isGoalState(current_state):
            return cur_actions

        # Mở rộng từ node hiện tại và cập nhật giá trị
        for successor_state, action, cost in problem.getSuccessors(current_state):
            new_actions = cur_actions + [action]
            new_cost = cur_cost + cost
            hn = heuristic(successor_state, problem)
            fn = new_cost + hn
            priority_queue.push((successor_state, new_actions, new_cost), fn)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
