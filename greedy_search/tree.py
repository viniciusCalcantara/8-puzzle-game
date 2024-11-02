from data_structs import Node
from solve02 import problem, reached, best_first_search
import graphviz

root = Node(problem.initial_state, goal=problem.goal_state)
ans_node = best_first_search(problem, reached, root)


def get_solution_nodes(node):
    solution_nodes = []
    aux_node = node
    while aux_node is not None:
        solution_nodes.append(aux_node)
        aux_node = aux_node.parent
    solution_nodes.reverse()
    return solution_nodes


def visualize_tree(root, solution_nodes):
    dot = graphviz.Digraph(comment='Árvore de Busca')

    def add_nodes_edges(node):
        description = node.__str__()
        description += 'h = ' + str(node.manhattan_distance())
        if node.parent is None:
            dot.node(
                str(id(node)), 
                description, 
                color='red', 
                style='filled', 
                fillcolor='lightgrey'
            )
            solution_nodes.remove(node)
        else:
            if node in solution_nodes:
                dot.node(
                    str(id(node)), 
                    description, 
                    color='red', 
                    style='filled', 
                    fillcolor='lightgrey'
                )
                dot.edge(str(id(node.parent)), str(id(node)), color='red')
                solution_nodes.remove(node)
            else:
                dot.node(str(id(node)), description)
                dot.edge(str(id(node.parent)), str(id(node)))

        for child in node.childs:
            add_nodes_edges(child)

    add_nodes_edges(root)
    dot.render('./search_tree/tree_by_greedy_approach', view=True)

solution_nodes = get_solution_nodes(ans_node)
visualize_tree(root, solution_nodes)