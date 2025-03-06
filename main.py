from typing import Dict, Set, Union
import numpy as np

def bfs(G: Dict[Union[int, str], Set[Union[int, str]]]):
    """
    Breadth-first search algorithm
    :param G: a graph G, consisting of nodes and vertices v
    :return: none
    """
    visited = {node: False for node in G} # mark all nodes as not visited
    Q = [] # create an empty queue

    for v in G: # for every vertex in G
        if not visited[v]: # if the vertex is not visited
            bfs_from_vertex(G, v, visited, Q) # do breadth first search from that vertex

def bfs_from_vertex(G, v, visited, Q):
    """
    a helper function
    :param G: the graph
    :param v: the node from which we are starting the search
    :param visited: a list of node states
    :param Q: the queue
    :return: none
    """
    visited[v] = True # set the starting node to visited
    Q.enqueue(v) # add the starting node to the queue

    while not Q.isEmpty(): # until the queue has been emptied
        v = Q.dequeue() # remove the first node from the queue

        for w in G[v]: # for every node w that is connected to node v
            if not visited[w]: # if the node w has not been visited
                visited[w] = True # set the node w to visited
                Q.enqueue(w) # add the node w to the queue


