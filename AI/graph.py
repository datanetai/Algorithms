
from collections import deque
import heapq

class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x): 
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        for item in items:
            self.add(item)
         
    def add(self, item):
        """Add item to the queuez."""
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """Pop and return the item with min f(item) value."""
        return heapq.heappop(self.items)[1]
    
    def top(self): return self.items[0][1]

    def __len__(self): return len(self.items)


class Problem:
    """
     An Abstract class for a problem which is to be solved.
    """
    def __init__(self, initial,goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    def __lt__(self, node):
        return self.state < node.state
    def __repr__(self) -> str:
        return str(self.state)
    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state,
                                           action, next_state))
        return next_node
    def solution(self):
        return [node.state for node in self.path()[1:]]
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    def __eq__(self, __o: object) -> bool:
        return self.state == __o.state
    
# algorithms
# depth first search
def depth_first_search(problem):
    frontier = [Node(problem.initial)]
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def depth_first_graph_search(problem):
    frontier = [Node(problem.initial)]
    explored = []
    while frontier:
        node = frontier.pop()
        explored.append(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

# breadth first search
def breadth_first_search(problem):
    frontier = [Node(problem.initial)]
    explored = []
    while frontier:
        node = frontier.pop(0)
        explored.append(node.state)
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def best_first_graph_search(problem, f):
    """
    Search the nodes with the lowest f scores first."""
    frontier = PriorityQueue(f=f)
    frontier.append(Node(problem.initial))
    explored = []
    while frontier:
        node = frontier.pop()
        explored.append(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return None

def uniform_cost_search(problem):
    return best_first_graph_search(problem, lambda node: node.path_cost)

def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n)."""
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))

    
class EightPuzzle(Problem):
    


# credit to: https://github.com/aimacode/aima-python/blob/master/search.py