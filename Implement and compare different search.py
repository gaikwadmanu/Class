import heapq
from collections import deque

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle, self.parent, self.move = puzzle, parent, move

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def __repr__(self):
        return str(self.puzzle)

    def is_goal(self):
        n = len(self.puzzle)
        return self.puzzle == [[i * n + j for j in range(n)] for i in range(n)]

    def generate_successors(self):
        n = len(self.puzzle)
        zero_pos = next((i, j) for i in range(n) for j in range(n) if self.puzzle[i][j] == 0)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        for move in moves:
            new_pos = (zero_pos[0] + move[0], zero_pos[1] + move[1])
            if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n:
                new_puzzle = [row.copy() for row in self.puzzle]
                new_puzzle[zero_pos[0]][zero_pos[1]], new_puzzle[new_pos[0]][new_pos[1]] = new_puzzle[new_pos[0]][new_pos[1]], new_puzzle[zero_pos[0]][zero_pos[1]]
                yield PuzzleState(new_puzzle, self, move)

    def heuristic(self):
        n = len(self.puzzle)
        return sum(abs(i - self.puzzle[i][j] // n) + abs(j - self.puzzle[i][j] % n) for i in range(n) for j in range(n) if self.puzzle[i][j] != 0)

def generic_search(initial_state, data_structure):
    frontier, explored = data_structure([initial_state]), set()

    while frontier:
        current_state = data_structure.pop(frontier)
        if current_state.is_goal():
            return current_state
        explored.add(current_state)
        successors = [s for s in current_state.generate_successors() if s not in explored and s not in frontier]
        data_structure.extend(frontier, successors)

def solve_and_measure_performance(initial_state, search_algorithm, data_structure):
    import time

    start_time = time.time()
    solution = search_algorithm(initial_state, data_structure)
    end_time = time.time()

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")

    print(f"Time taken: {end_time - start_time:.5f} seconds")
    print(f"Number of states explored: {len(explored)}")

def print_solution(solution_state):
    path = []
    while solution_state:
        path.insert(0, solution_state)
        solution_state = solution_state.parent

    for state in path:
        print(state)
        print()

def get_user_input():
    n = int(input("Enter the size of the puzzle (e.g., 3 for 3*3): "))
    puzzle = []
    print("Enter the puzzle row by row (use 0 to represent the blank space):")
    for _ in range(n):
        row = list(map(int, input().split()))
        puzzle.append(row)
    return PuzzleState(puzzle)

if __name__ == "__main__":
    initial_state = get_user_input()

    print("Breadth-First Search:")
    solve_and_measure_performance(initial_state, generic_search, deque)

    print("\nDepth-First Search:")
    solve_and_measure_performance(initial_state, generic_search, list)

    print("\nA* Search:")
    solve_and_measure_performance(initial_state, generic_search, heapq)
