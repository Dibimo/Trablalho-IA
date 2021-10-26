import math
class Astar:

    def __init__(self, matrix):
        self.mat = self.prepare_matrix(matrix)

    class Node:
        def __init__(self, x, y, weight=0):
            self.x = x
            self.y = y
            self.weight = weight
            self.heuristic = 0
            self.parent = None

        def __repr__(self):
            # return f"({self.weight} | {self.heuristic})"
            return f"({self.x} | {self.y})"

    def print(self):
        for y in self.mat:
            print(y)

    def prepare_matrix(self, mat):
        matrix_for_astar = []
        for y, line in enumerate(mat):
            tmp_line = []
            for x, weight in enumerate(line):
                tmp_line.append(self.Node(x, y, weight=weight))
            matrix_for_astar.append(tmp_line)
        return matrix_for_astar

    def equal(self, current, end):
        return current.x == end.x and current.y == end.y

    def heuristic(self, current, other):
        return abs(current.x - other.x) + abs(current.y - other.y)

    def neighbours_in_closed_list(self,closed_list,neighour):
        for node in closed_list:
            if (node.x == neighour.x) and (node.y == neighour.y):
                return True
        return False

    def neighbours(self, matrix, current):
        neighbours_list = []
        # if current.x - 1 >= 0 and current.y - 1 >= 0 and matrix[current.y - 1][current.x - 1].weight is not None:
        #     neighbours_list.append(matrix[current.y - 1][current.x - 1])
        if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x - 1])
        # if current.x - 1 >= 0 and current.y + 1 < len(matrix) and matrix[current.y + 1][
        #     current.x - 1].weight is not None:
        #     neighbours_list.append(matrix[current.y + 1][current.x - 1])
        if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x])
        if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x])
        # if current.x + 1 < len(matrix[0]) and current.y - 1 >= 0 and matrix[current.y - 1][
        #     current.x + 1].weight is not None:
        #     neighbours_list.append(matrix[current.y - 1][current.x + 1])
        if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x + 1])
        # if current.x + 1 < len(matrix[0]) and current.y + 1 < len(matrix) and matrix[current.y + 1][
        #     current.x + 1].weight is not None:
        #     neighbours_list.append(matrix[current.y + 1][current.x + 1])
        return neighbours_list

    def build(self, end):
        node_tmp = end
        path = []
        total_sum = 0
        while (node_tmp):
            path.append([node_tmp.x, node_tmp.y])
            total_sum += node_tmp.weight
            node_tmp = node_tmp.parent
        # return (list(reversed(path)),total_sum)
        return list(reversed(path))

    def find_shortest_path(self, point_start, point_end):
        final_path = []
        matrix = self.mat
        start = self.Node(point_start[0], point_start[1])
        neighbours_point_start = self.neighbours(matrix,start)
        sum_path = math.inf
        for neighbour in neighbours_point_start:
            path,sum_ = self.run([neighbour.x,neighbour.y],point_end)
            if (sum_ < sum_path):
                final_path = path
        
        return final_path


    def run(self, point_start, point_end):
        matrix = self.mat
        start = self.Node(point_start[0], point_start[1])
        end = self.Node(point_end[0], point_end[1])
        closed_list = []
        open_list = [start]

        i = 0
        while open_list:
            i += 1
            current_node = open_list.pop(0)
            print(f'Laço: {i}')
            print(f'Nodo atual: {current_node.x} {current_node.y}')
            print()

            for node in open_list:
                print(f'Nodo: {node.x} {node.y}')
                print(f'Heuristica: {node.heuristic}')
                print()
                if node.heuristic < current_node.heuristic:
                    current_node = node

            print(f'Nodo escolhido no laço: {current_node.x} {current_node.y}')
            print('-----------')

            if self.equal(current_node, end):
                return self.build(current_node)

            for node in open_list:
                if self.equal(current_node, node):
                    open_list.remove(node)
                    break

            closed_list.append(current_node)

            for neighbour in self.neighbours(matrix, current_node):
                # if neighbour in closed_list:
                #     continue
                if self.neighbours_in_closed_list(closed_list,neighbour):
                    continue
                if neighbour.heuristic < current_node.heuristic or neighbour not in open_list:
                    neighbour.heuristic = neighbour.weight + self.heuristic(neighbour, end)
                    neighbour.parent = current_node
                if neighbour not in open_list:
                    open_list.append(neighbour)
            print(closed_list)
        return None

