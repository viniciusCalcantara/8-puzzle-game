import bisect

from data_structs import Node, Problem

def parity(arr):
    inv_count = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if arr[j] and arr[i] and arr[i] > arr[j]:
                inv_count += 1
    return inv_count % 2

def max_neighbor(problem: Problem, node: Node) -> Node:
    s = node.state
    for action in problem.actions(s):
        new_s = problem.result(s, action)
        cost = problem.action_cost(s, action, new_s) 
        node.childs.append(Node(state=new_s, goal=problem.goal_state, parent=node, action=action, path_cost=cost))
    
    node.childs.sort()
    max_neighbor_node = None
    if len(node.childs) > 0:
        max_neighbor_node = node.childs[-1]
    return max_neighbor_node


def hill_climbing(problem: Problem, start_node) -> Node:
    current = start_node
    while True:
        neighbor = max_neighbor(problem, current)
        if current.manhattan_distance() < neighbor.manhattan_distance():
            return current
        current = neighbor