from data_structs import Problem, Node
from best_first_search import best_first_search, parity

initial_state = tuple([
                    tuple([
                        tuple([2, 2]),
                        tuple([1, 0]),
                        tuple([0, 0]),
                        tuple([0, 2]),
                        tuple([1, 2]),
                        tuple([2, 1]),
                        tuple([1, 1]),
                        tuple([2, 0]),
                        tuple([0, 1]),
                    ]),
                    tuple([2, 8, 3, 1, 6, 4, 7, 5, 0])
                ])

goal_state = tuple([
                    tuple([
                        tuple([1, 1]),
                        tuple([0, 0]),
                        tuple([0, 1]),
                        tuple([0, 2]),
                        tuple([1, 2]),
                        tuple([2, 2]),
                        tuple([2, 1]),
                        tuple([2, 0]),
                        tuple([1, 0]),
                    ]),
                    tuple([1, 2, 3, 8, 0, 4, 7, 6, 5])
                ])

problem = Problem(
    initial_state=initial_state,
    goal_state=goal_state
    )

reached = {}
initial_state_parity = parity(initial_state[1]) 
goal_state_parity = parity(goal_state[1])

if __name__ == '__main__':
    if initial_state_parity == goal_state_parity:
        root = Node(problem.initial_state, goal=problem.goal_state)
        ans_node = best_first_search(problem, reached, root)
        aux_node = ans_node

        print('This is the solution:')
        ans = []
        while aux_node is not None:
            ans.append(aux_node)
            aux_node = aux_node.parent
        ans.reverse()
        for node in ans:
            print(node)
            
    else:
        print('This puzzle is not solvable')
        print('Initial state parity:', initial_state_parity)
        print('Goal state parity:', goal_state_parity)
        print('They have different parities')