# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:31:16 2022

@author: aelbadra
"""
from graph_traverser import GraphTraverser
from tile_search_problem import TileState, TileProblem


#create a TileProblem

ts = TileState(
    [ 
     [4,  2, 7], 
     [8, -1, 6], 
     [1,  3, 5]
     ], 
    1,1
    )


tp = TileProblem(ts)

gt = GraphTraverser(None)

gt.a_star_traversal(tp)
