class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state

    def apply_action(self, action):
        if action[0] == "move":
            block, destination = action[1], action[2]
            self.state[block] = destination
        elif action[0] == "stack":
            block, on_block = action[1], action[2]
            self.state[block] = on_block
        elif action[0] == "unstack":
            block = action[1]
            self.state[block] = "table"

    def goal_achieved(self, goal_state):
        return self.state == goal_state

def goal_stack_planning(world, goals):
    goal_stack = goals.copy()
    actions = []

    while goal_stack:
        current_goal = goal_stack.pop()
        if isinstance(current_goal, list):  # Complex goal
            subgoals = current_goal
            for subgoal in subgoals:
                goal_stack.append(subgoal)
        else:  # Simple goal
            if not world.goal_achieved(current_goal):
                plan = achieve_simple_goal(world, current_goal)
                if plan is None:
                    print("Goal Stack Planning failed.")
                    return None
                actions.extend(plan)

    return actions

def achieve_simple_goal(world, goal):
    if world.goal_achieved(goal):
        return []

    if goal[0] == "clear":
        return [("unstack", goal[1])]

    if goal[0] == "on":
        return [("unstack", goal[1])]

    if goal[0] == "ontable":
        return [("unstack", goal[1])]

    if goal[0] == "holding":
        return [("unstack", goal[1])]

    return None

# Example Block World
initial_state = {"A": "B", "B": "table", "C": "table"}

# Goal: Place all blocks on the table
goal_state = {"A": "table", "B": "table", "C": "table"}

world = BlockWorld(initial_state)
goals = [("ontable", "A"), ("ontable", "B"), ("ontable", "C")]

plan = goal_stack_planning(world, goals)
if plan:
    print("Initial State:", world.state)
    print("Goal State:", goal_state)
    print("Plan:", plan)

    # Apply the plan to reach the goal state
    for action in plan:
        world.apply_action(action)

    print("Final State:", world.state)
