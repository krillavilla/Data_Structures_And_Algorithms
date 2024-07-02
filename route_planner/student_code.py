import heapq
import math


def shortest_path(M, start, goal):
    # The open list will be a priority queue
    open_list = []
    # The start node has a g value of 0 and an h value equal to the heuristic
    g_values = {start: 0}
    h_values = {start: heuristic(M, start, goal)}
    # The f value of the start node is the sum of g and h
    f_values = {start: h_values[start]}
    # The start node is added to the open list
    heapq.heappush(open_list, (f_values[start], start))
    # The came_from dictionary will be used to reconstruct the path
    came_from = {start: None}

    while open_list:
        # The node with the lowest f value is removed from the open list
        _, current = heapq.heappop(open_list)
        # If the current node is the goal, the path is reconstructed and returned
        if current == goal:
            return reconstruct_path(came_from, current)
        # Each neighbor of the current node is considered
        for neighbor in M.roads[current]:
            # The g value for the neighbor is the g value of the current node plus the distance between them
            g = g_values[current] + distance(M, current, neighbor)
            # If the neighbor is not in the g_values dictionary or the new g value is lower than the previous one
            if neighbor not in g_values or g < g_values[neighbor]:
                # The g, h, and f values for the neighbor are updated
                g_values[neighbor] = g
                h_values[neighbor] = heuristic(M, neighbor, goal)
                f_values[neighbor] = g_values[neighbor] + h_values[neighbor]
                # The neighbor is added to the open list
                heapq.heappush(open_list, (f_values[neighbor], neighbor))
                # The current node is set as the predecessor of the neighbor
                came_from[neighbor] = current

    # If the open list is empty and the goal has not been reached, there is no path from the start to the goal
    return []


def heuristic(M, start, goal):
    # The heuristic is the straight-line distance between the start and the goal
    return distance(M, start, goal)


def distance(M, node1, node2):
    # The distance between two nodes is the Euclidean distance between their coordinates
    x1, y1 = M.intersections[node1]
    x2, y2 = M.intersections[node2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def reconstruct_path(came_from, current):
    # The path is reconstructed from the goal to the start
    path = [current]
    while came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    # The path is reversed to go from the start to the goal
    path.reverse()
    return path
