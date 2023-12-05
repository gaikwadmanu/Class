import random

class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __repr__(self):
        return str(self.puzzle)

    def is_goal(self):
        return self.puzzle == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def generate_successors(self):
        successors = []
        zero_pos = next((i, j) for i, row in enumerate(self.puzzle) for j, val in enumerate(row) if val == 0)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        for move in moves:
            new_pos = (zero_pos[0] + move[0], zero_pos[1] + move[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_puzzle = [row.copy() for row in self.puzzle]
                new_puzzle[zero_pos[0]][zero_pos[1]], new_puzzle[new_pos[0]][new_pos[1]] = new_puzzle[new_pos[0]][new_pos[1]], new_puzzle[zero_pos[0]][zero_pos[1]]
                successors.append(PuzzleState(new_puzzle))

        return successors

    def heuristic(self):
        # Simple heuristic: count the number of misplaced tiles
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return sum(self.puzzle[i][j] != goal_state[i][j] for i in range(3) for j in range(3))

def hill_climbing(initial_state):
    current_state = initial_state

    while True:
        neighbors = current_state.generate_successors()
        if not neighbors:
            break  # Local minimum or goal state reached
        best_neighbor = min(neighbors, key=lambda state: state.heuristic())
        if best_neighbor.heuristic() >= current_state.heuristic():
            break  # Local maximum reached
        current_state = best_neighbor

    return current_state

def print_solution(solution_state):
    print("Solution found:")
    print(solution_state)

if __name__ == "__main__":
    # Generate a random initial state
    initial_puzzle = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    random.shuffle(initial_puzzle)
    initial_state = PuzzleState(initial_puzzle)

    print("Initial State:")
    print(initial_state)

    final_state = hill_climbing(initial_state)

    print("\nFinal State:")
    print_solution(final_state)
