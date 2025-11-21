# 2014 AIME I Problem 5

## Problem

Let the set $S = \{P_1, P_2, \dots, P_{12}\}$ consist of the twelve vertices of a regular $12$ -gon. A subset $Q$ of $S$ is called "communal" if there is a circle such that all points of $Q$ are inside the circle, and all points of $S$ not in $Q$ are outside of the circle. How many communal subsets are there? (Note that the empty set is a communal subset.)

## Solution
By looking at the problem and drawing a few pictures, it quickly becomes obvious that one cannot draw a circle that covers $2$ disjoint areas of the $12$ -gon without including all the vertices in between those areas. In other words, in order for a subset to be communal, all the vertices in the subset must be adjacent to one another. We now count the number of ways to select a row of adjacent vertices. We notice that for any subset size between $1$ and $11$ , there are $12$ possible subsets like this (this is true because we can pick any of the $12$ vertices as a "starting" vertex, include some number of vertices counterclockwise from that vertex, and generate all possible configurations). However, we also have to include the set of all $12$ vertices, as well as the empty set. Thus, the total number is $12\cdot11 + 2 = \boxed{134}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .