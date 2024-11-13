#Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy
import math

class TSPSolver:
    def _init_(self, graph):
        self.n = len(graph)
        self.graph = graph
        self.final_path = [None] * (self.n + 1)
        self.visited = [False] * self.n
        self.final_res = math.inf

    def first_min(self, i):
        return min([self.graph[i][k] for k in range(self.n) if i != k])

    def second_min(self, i):
        return sorted([self.graph[i][k] for k in range(self.n) if i != k])[:2]

    def tsp_recursive(self, curr_bound, curr_weight, level, curr_path):
        if level == self.n:
            if self.graph[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.graph[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_res:
                    self.final_res = curr_res
                    self.final_path[:] = curr_path[:] + [curr_path[0]]
            return

        for i in range(self.n):
            if self.graph[curr_path[level - 1]][i] and not self.visited[i]:
                temp_bound = curr_bound
                curr_weight += self.graph[curr_path[level - 1]][i]
                if level == 1:
                    curr_bound -= (self.first_min(curr_path[level - 1]) + self.first_min(i)) / 2
                else:
                    curr_bound -= (self.second_min(curr_path[level - 1])[1] + self.first_min(i)) / 2
                if curr_bound + curr_weight < self.final_res:
                    curr_path[level] = i
                    self.visited[i] = True
                    self.tsp_recursive(curr_bound, curr_weight, level + 1, curr_path)
                curr_weight -= self.graph[curr_path[level - 1]][i]
                curr_bound = temp_bound
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    self.visited[curr_path[j]] = True

    def solve(self):
        curr_bound = math.ceil(sum(self.first_min(i) + self.second_min(i)[1] for i in range(self.n)) / 2)
        curr_path = [-1] * (self.n + 1)
        self.visited[0] = True
        curr_path[0] = 0
        self.tsp_recursive(curr_bound, 0, 1, curr_path)

    def print_solution(self):
        print("Minimum cost:", self.final_res)
        print("Path:", ' -> '.join(map(str, self.final_path)))

# Example usage
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
solver = TSPSolver(graph)
solver.solve()
solver.print_solution()