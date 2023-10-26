import heapq


class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        # Modify the comparssion based on your heurestic function
        return self.cost < other.cost

    def best_first_search(problem):
        start_node = Node(problem.inital_state)
        open_list = []
        closed_set = set()
        heapq.heappush(open_list, closed_set)

        while open_list:
            current_node = heapq.heappop(open_list)

        if problem.is_goal(current_node.state):
            return build_path(current_node)

        closed_set.add(current_node.state)

        for action, successor, step_cost in problem.get_successors(current_node.state):
            if successor not in closed_set:
                child = Node(successor, current_node, step_cost)
                heapq.heappush(open_list, child)

        return None

    def build_path(node):
        path = []
        while node:
            path.insert(0, node.state)
            node = node.parent

        return path

    class Problem:
        def __init__(self, initial_state):
            self.initial_state = initial_state

        def is_goal(self, state):
            raise NotImplementedError("SubClasses must implement is_goal")

        def get_successors(self, state):
            raise NotImplementedError("SubClasses must implement is_goal")

    class EightPuzzleProblem(Problem):
        def is_goal(self, state):
            return state == (1, 2, 3, 8, 0, 4, 7, 6, 5)

        def get_successors(self, state):
            # Implement how to generate successors
            pass

    if __name__ == "__main__":
        initial_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)
        problem = EightPuzzleProblem(initial_state)

        solution_path = best_first_search(problem)
        if solution_path:
            print("Solution Found:")
            for state in solution_path:
                print(state)
        else:
            print("Solution doesn't Exist")
