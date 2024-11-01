import bisect

from data_structs import Node, Problem

def parity(arr):
    inv_count = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if arr[j] and arr[i] and arr[i] > arr[j]:
                inv_count += 1
    return inv_count % 2

def expand(problem: Problem, node: Node):
    s = node.state   
    for action in problem.actions(s):
        new_s = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, new_s)
        yield Node(state=new_s, goal=problem.goal_state, parent=node, action=action, path_cost=cost)


def best_first_search(problem: Problem, reached) -> Node | None:
    node = Node(problem.initial_state, goal=problem.goal_state)
    frontier = [node]
    reached[node.state] = node
    while not frontier == []:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                bisect.insort(frontier, child)
    return None