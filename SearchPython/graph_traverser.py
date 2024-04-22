# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:50:58 2022

@author: aelbadra
"""
from tree import Tree, TreeNode
from graph import Graph
import copy

class GraphTraverser:
    
    def __init__(self, g):
        self.graph = g
        self.tree = Tree()
        
    #creates a tree to traverse the graph breadth-first starting at start_node_name
    def breadth_first_traversal(self, start_node_name, target_node_name):
        #check if start node is part of the graph
        if start_node_name not in self.graph.nodes:
            print(start_node_name, "not found in graph!")
            return
        #check if start node is the target node
        if start_node_name == target_node_name:
            print("Start node is the target node! No search needed.")
            return
        
        #setup data structures to keep track of reached nodes and 
        #nodes that ae yet to be expanded per breadth-first
        reached_nodes = {}
        reached_nodes[start_node_name] = 1
        nodes_to_expand = [start_node_name]
        
        
        #construct the traversal tree, starting at the root.
        self.tree = Tree()
        rootNode = TreeNode(start_node_name, None)
        self.tree.set_root(rootNode)

        while len(nodes_to_expand) > 0:
            #expand the node at the beginning of the espansion list
            node_name = nodes_to_expand.pop(0)
            children = self.graph.expand_node(node_name)
            
            for child in children: #for each new child
                child_name = child[0]
                child_edgewt = child[1]
                #if child is target, return solution!
                if child_name == target_node_name:
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n , node_name, child_edgewt)
                    print('Target Reached!')
                    self.tree.print_path(n)
                    return
                #if child is a newly reached node, add to expansion list, tree
                if child_name not in reached_nodes:
                    reached_nodes[child_name] = 1
                    nodes_to_expand.append(child_name)
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n, node_name, child_edgewt)
                    
        #if all nodes were expanded and solution not found:
        print('Target not found!')
        return
    
    #creates a tree to traverse the graph depth-first starting at start_node_name
    def depth_first_traversal(self, start_node_name, target_node_name):
        #check if start node is part of the graph
        if start_node_name not in self.graph.nodes:
            print(start_node_name, "not found in graph!")
            return
        #check if start node is the target node
        if start_node_name == target_node_name:
            print("Start node is the target node! No search needed.")
            return
        
        #setup data structures to keep track of reached nodes and 
        #nodes that ae yet to be expanded per depth-first
        reached_nodes = {}
        reached_nodes[start_node_name] = 1
        nodes_to_expand = [start_node_name]
        
        
        #construct the traversal tree, starting at the root.
        self.tree = Tree()
        rootNode = TreeNode(start_node_name, None)
        self.tree.set_root(rootNode)

        while len(nodes_to_expand) > 0:
            #expand the node at the end of the espansion list
            node_name = nodes_to_expand.pop()
            children = self.graph.expand_node(node_name)
            
            for child in children: #for each new child
                child_name = child[0]
                child_edgewt = child[1]
                #if child is target, return solution!
                if child_name == target_node_name:
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n , node_name, child_edgewt)
                    print('Target Reached!')
                    self.tree.print_path(n)
                    return
                #if child is a newly reached node, add to expansion list, tree
                if child_name not in reached_nodes:
                    reached_nodes[child_name] = 1
                    nodes_to_expand.append(child_name)
                    n = TreeNode(child_name,node_name)
                    self.tree.add_child_node( n, node_name, child_edgewt)
                    
        #if all nodes were expanded and solution not found:
        print('Target not found!')
        return

    
    def dijkstra_traversal(self, start_node_name, target_node_name):
        if start_node_name not in self.graph.nodes:
            print(start_node_name, "not found in graph!")
            return
        #check if start node is the target node
        if start_node_name == target_node_name:
            print("Start node is the target node! No search needed.")
            return
        #Track which nodes we have expanded and calculated distances for
        reached_nodes = {}
        #Need to deep copy the nodes list so that we don't remove nodes from it
        un_reached_nodes = copy.deepcopy(self.graph.nodes)
        #This dict will contain the shortest distance any city is from the start city
        shortest_distance_from_node_to_start = {}
        #Dict will contain the previous node to another in which the distance was found to be the shortest
        #This is so we can trace the path
        shortest_previous_node = {}
        #Assign a large value for the distance from each node to the start node so we can properly compare
        for node in un_reached_nodes:
            shortest_distance_from_node_to_start[node] = 99999
        #We've already visited the start node and we know its distance form itself is 0
        reached_nodes[start_node_name] = 1
        shortest_distance_from_node_to_start[start_node_name] = 0
        #While there are still nodes we haven't visited and calculated the distance of
        while un_reached_nodes:
            #Set the closest node the first index of un_reached_nodes, to then compare
            #Need to reset this for each loop so we are only expanding nodes we havn't visited yet
            closest_node = next(iter(un_reached_nodes))
            #Check each of the nodes we havn't visited yet and select the one closest to the start to expand, per dijkstra algo
            for city in un_reached_nodes:
                if shortest_distance_from_node_to_start[city] < shortest_distance_from_node_to_start[closest_node]:
                    closest_node = city
            #Expand the node the we found to be closest to the start to expand
            children = self.graph.expand_node(closest_node)
            #Loop through nodes children and if the children distance to the start is less that was previously found s
            #Then set that as its new shortest distance
            for child in children:
                #Calculate the distance from the child to the start by adding distance of parent and child together
                distance = shortest_distance_from_node_to_start[closest_node] + child[1]
                #If that distance is less that what is currently set as the child shortest path, update it
                if distance < shortest_distance_from_node_to_start[child[0]]:
                    shortest_distance_from_node_to_start[child[0]] = distance
                    #Add the previous node to dict so we can keep track of the shortest path
                    shortest_previous_node[child[0]] = closest_node
            #Mark the node as vistied
            un_reached_nodes.pop(closest_node)
        
        #List to store the path
        result = []
        #The city we are trying to find the shortest path to
        target = target_node_name
        #Add previous node to list, we build list in reverse, so I use insert at index 0 to maintain correct order
        is_done = False
        while is_done == False:
            result.insert(0, target)
            target = shortest_previous_node[target]
            if target == start_node_name:
                is_done = True
        #Make sure start node is at the beginning
        result.insert(0, start_node_name)
        #Print result
        print('Target Reached!')
        print("Full path: ", result)
        return
        

       
#==================================================================
#==================================================================
#==================================================================
