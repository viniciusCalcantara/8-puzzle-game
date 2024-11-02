from typing import Optional, Tuple

NumberPosition = Tuple[int, int]

State = Tuple[
                Tuple[
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                    NumberPosition,
                ],
                Tuple[int, int, int, int, int, int, int, int, int]
            ]

def find_number_by_position(i: int, j:  int, arr) -> int:
    it = 0
    while (it // 3 == i and it % 3 == j) is False:
        it += 1 
    return arr[it]


class Node: 
    def __init__(self, state: State, goal: State, parent: Optional['Node'] = None, action: str | None = None, path_cost: int = 0):
        self.state = state
        self.goal = goal
        self.parent = parent
        self.childs = []
        self.action = action
        self.path_cost = path_cost

    def manhattan_distance(self) -> int:
        distance = 0
        for number in range(9):
            distance += abs(self.state[0][number][0] - self.goal[0][number][0]) + abs(self.state[0][number][1] - self.goal[0][number][1])
        return distance

    def __lt__(self, other: 'Node') -> bool:
        return self.manhattan_distance() > other.manhattan_distance()

    def __eq__(self, other: 'Node') -> bool:
        return self.state == other.state

    def __str__(self) -> str:
        ans = ''
        cont = 0
        for x in self.state[1]:
            ans += str(x) + ' '
            cont += 1
            if cont % 3 == 0:
                ans += '\n'
        return ans


class Problem:
    def __init__(
            self,
            initial_state: State,
            goal_state: State,
        ):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state: State) -> bool:
        return state == self.goal_state

    def result(self, state: State, action: str) -> State | None:
        position_list = [list(position) for position in state[0]]
        x, y = position_list[0]
        new_x, new_y = x, y
        number_to_move = 0
        arr_list = list(state[1])

        if action == 'up' and x > 0:
            number_to_move = find_number_by_position(x - 1, y, state[1])
            position_list[0] = (x - 1, y)
            position_list[number_to_move] = (x, y)
            new_x = x - 1
        elif action == 'down' and x < 2:
            number_to_move = find_number_by_position(x + 1, y, state[1])
            position_list[0] = (x + 1, y)
            position_list[number_to_move] = (x, y)
            new_x = x + 1
        elif action == 'left' and y > 0:
            number_to_move = find_number_by_position(x, y - 1, state[1])
            position_list[0] = (x, y - 1)
            position_list[number_to_move] = (x, y)
            new_y = y - 1
        elif action == 'right' and y < 2:
            number_to_move = find_number_by_position(x, y + 1, state[1])
            position_list[0] = (x, y + 1)
            position_list[number_to_move] = (x, y)
            new_y = y + 1
        else:
            return None
        
        zero_position_on_list = arr_list.index(0)
        arr_list[arr_list.index(number_to_move)] = 0
        arr_list[zero_position_on_list] = number_to_move
        return tuple([tuple([tuple(position) for position in position_list]), tuple(arr_list)])

    def actions(self, state: State) -> list[str]:
        zero_position = state[0][0]
        if zero_position == (0, 0):
            return ['down', 'right']
        elif zero_position == (0, 1):
            return ['down', 'left', 'right']
        elif zero_position == (0, 2):
            return ['down', 'left']
        elif zero_position == (1, 0):
            return ['up', 'down', 'right']
        elif zero_position == (1, 1):
            return ['up', 'down', 'left', 'right']
        elif zero_position == (1, 2):
            return ['up', 'down', 'left']
        elif zero_position == (2, 0):
            return ['up', 'right']
        elif zero_position == (2, 1):
            return ['up', 'left', 'right']
        elif zero_position == (2, 2):
            return ['up', 'left']

    def action_cost(self, state1, action, state2):
        return 1