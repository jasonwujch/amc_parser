# 2017 AIME II Problem 11

## Problem

Five towns are connected by a system of roads. There is exactly one road connecting each pair of towns. Find the number of ways there are to make all the roads one-way in such a way that it is still possible to get from any town to any other town using the roads (possibly passing through other towns on the way).

## Solution
It is obvious that any configuration of one-way roads which contains a town whose roads all lead into it or lead out of it cannot satisfy the given. We claim that any configuration which does not have a town whose roads all lead into it or lead out of it does satisfy the given conditions. Now we show that a loop of $3$ or more towns exist. Pick a town, then choose a neighboring town to travel to $5$ times. Of these $6$ towns visited, at least two of them must be the same; therefore there must exist a loop of $3$ or more towns because a loop of $2$ towns cannot exist. We want to show that the loop can be reached from any town, and any town can be reached from the loop.
$\textbf{Case 1}$ . The loop has $5$ towns. Clearly every town can be reached by going around the loop.
$\textbf{Case 2}$ . The loop has $4$ towns. The town not on the loop must have a road leading to it. This road comes from a town on the loop. Therefore this town can be reached from the loop. This town not on the loop must also have a road leading out of it. This road leads to a town on the loop. Therefore the loop can be reached from the town.
$\textbf{Case 3}$ . The loop has $3$ towns. There are two towns not on the loop; call them Town $A$ and Town $B$ . Without loss of generality assume $A$ leads to $B$ . Because a road must lead to $A$ , the town where this road comes from must be on the loop. Therefore $A$ and therefore $B$ can be reached from the loop. Because a road must lead out of $B$ , the town it leads to must be on the loop. Therefore the loop can be reached from $B$ and also $A$ .
The number of good configurations is the total number of configurations minus the number of bad configurations. There are $2^{{5\choose2}}$ total configurations. To find the number of bad configurations in which a town exists such that all roads lead to it, there are $5$ ways to choose this town and $2^6$ ways to assign the six other roads that do not connect to this town. The same logic is used to find the number of bad configurations in which a town exists such that all roads lead out of it. It might be tempting to conclude that there are $5 \cdot 2^6+5 \cdot 2^6$ bad configurations, but the configurations in which there exists a town such that all roads lead to it and a town such that all roads lead out of it are overcounted. There are $5$ ways to choose the town for which all roads lead to it, $4$ ways to choose the town for which all roads lead out of it, and $2^3$ ways to assign the remaining $3$ roads not connected to either of these towns. Therefore, the answer is $2^{{5\choose2}}-(5 \cdot 2^6+5 \cdot 2^6-5\cdot 4 \cdot 2^3)=\boxed{544}$ .
### Diagram
Note that this isn't necessarily a diagram of the actual sequence of roads (I haven't drawn in every pair of cities to be connected), but a simplified diagram that can be used to represent a visualized representation of the loops in the cases mathboy282

## Solution 2 (complementary counting)
The only way a town does not meet the conditions in the question is if the town has either all roads leading towards it or all roads leading away from it. For example, if all roads lead away from Town $A$ , there is no way to reach the town starting from Towns $B$ , $C$ , $D$ , or $E$ . If all roads lead towards Town $A$ , there is no way to reach any other town starting from Town $A$ . Thus, we will count the ways this occurs. (To show this, first note that there must always be a directed path that visits every town once, say $A \rightarrow C \rightarrow B \rightarrow E \rightarrow D.$ (Redei's Theorem). Taking cases, it can be seen that if $A$ does not have all its roads leading, then $E$ must have its roads leading into it.)
$\textbf{Case 1}$ . WLOG, Town $A$ has all roads leading towards it.
In this case, the four roads leading to Town $A$ have already been determined. There are $6$ roads that have not been given directions. Each of these roads have $2$ options: it can lead towards one town or the other town. Thus, there are $2^6$ arrangements of roads. However, we must consider the $5$ towns in which this scenario can occur: there are $5 \cdot 2^6=320$ arrangements.
$\textbf{Case 2}$ . WLOG, Town $A$ has all roads leading away.
Notice that this case is symmetrical to the first case. Thus, there are $320$ arrangements.
$\textbf{Case 3}$ . WLOG, Town $A$ has all roads leading towards it and Town $B$ has all roads leading away.
We must check for double-counted cases. Drawing a flow diagram, we see that this case determines $7$ roads. For the undetermined $3$ roads, there are $2^3=8$ arrangements. However, we must again consider the different ways that this case can occur. There are $5$ choices for towns with roads leading towards it $4$ choices for roads leading away. Thus, the total double-counted cases are $5 \cdot 4 \cdot 8=160$ arrangements.
We must subtract the cases we counted from the total. There are a total of $10$ roads with $2$ possible arrangements each. Therefore the total number of cases is $2^{10} =1024$ , and the number of cases that meet the conditions is $1024 - (320+320-160) = \boxed{544}$ arrangements.
~ jf

## Solution 3
Assume the five towns are named A, B, C, D, and E. Draw roads that connect each of the five towns. First, figure out how many total roads there are with no restrictions. This would be $2^{10}$ , or $1024$ . Next, add together the number of restrictions (or incorrect cases) there are. One incorrect case happens if we can't get to one of the five towns. When that happens, any roads that connect that town with any of the other four towns must be one way. Four roads are invalidated (because they are one way) as, assuming we can't get to town A, roads AB, AC, AD, and AE would all be one way. Since there are ${{5\choose1}}$ ways of choosing which town to restrict, there are $5\cdot2^{10-4}$ , or $320$ restrictions in this case. The next case is when we can't get to two of the towns. Let's assume we don't want to get to towns A and B. Then, roads AC, AD, AE, BC, BD, and BE are all invalidated. Since there are ${{5\choose2}}$ of choosing which two towns to restrict, there are $10\cdot2^{10-6}$ , or $160$ restrictions in this case. Notice that when we restrict three towns, it is the same thing as restricting two towns. For example, if we restricted entry to towns C, D, and E from towns A and B, it's the same thing as if we restricted entry to towns A and B from towns C, D, and E, as the exact same roads are invalidated in both cases. Thus, our final answer is $1024-(320+160) = \boxed{544}$ arrangements.
Solution by IronicNinja~

## Solution 4
As noted before, you can see that there are 2 ways that the condition cannot be met; it either has all roads leading into one city, or all roads leading out of one city. We then use complementary counting to count these cases, with PIE. Obviously there are $2^5*2^5$ ways to make roads (just draw a pentagon with all of the diagonals and assume that they are roads, and count the sides and then the diagonals). Then, make all roads leading in to another city. There are 4 roads leading into that city, so there are $2^6$ ways to designate that. Given that there are 5 cities, and it can also be the ways to go out of the city, you get $10*2^6$ ways NOT to get into the city. However, this disregards the case that 2 cities are like this, which is the PIE case. Quick inspection shows that there are no cases where 3 are like that, and inspection with le pentagon can also show you that there are $\binom{5}{2}*2$ (because they can all lead in and all lead out) $*2^3$ (because there are 3 roads left to choose). In the end, this comes out to $2^5*2^5-(10*2^6-2*\binom{5}{2}*2^3)=1024-(640-160)=\boxed{544}$
-dragonon

## Solution 5 (Graph Theory)
We use Claim 1 along with complementary counting. Then, the number of valid cases is the total ( $2^{10}$ ) minus the cases in which there are towns with indegree or outdegree 5. Number of cases in which there is a node with indegree 5: $5*2^6$ 5 ways to choose which town has indegree 5 and for the remaining roads, they each have 2 possible statuses. Similarly, the number of cases in which there is a node with outdegree 5 is also $5*2^6$ The number of cases in which there is a node with indegree 5 and there is a node with outdegree 5: $5*4*2^3$
Thus, answer = $2^{10}-(5*2^6+5*2^6-5*4*2^3)$ = $544$
- Note: In this graph there can be at most one town with indegree 5 or outdegree 5.
Solution by ZHANALEX
### Claim 1
Claim: If and only if there is no town in this graph with a indegree or outdegree of 4, it is possible to reach all of the 4 other towns from any town in the graph.
Proof:
Part 1: If there is no town in this graph with a indegree or outdegree of 4, it is possible to reach all of the 4 other towns from any town in the graph
Since every town has an outgoing road, there is definitely a cycle. (Since there are only n town, eventually you must come back to a town that is already visited) Since a cycle of length 2 is not possible in this problem, the cycle can have a length of 3, 4, or 5. If the cycle has length 5, then it is definitely possible to go from one town to any other town. Ex: If the cycle is 1->2->3->4->5->1, then it is clear that you can reach any other town from one town
If the cycle has length 4: WLOG, let 1->2->3->4->1 be the cycle. Since town 5 has at least one incoming road and one outgoing road, there is definitely an road from a town on the cycle to town 5. There must also be an road from town 5 to another town that is in the cycle. Thus, it is definitely possible to reach any other town from one town.
If the cycle has length 3: WLOG, we can assume that the cycle is 1->2->3->1 and that the road between town 4 and town 5 is 4->5. Since 4 has at least one incoming road, there must be a town in the cycle that has an road to town 4. Since town 5 has at least one outgoing road, there must be a road from town 5 to some town in the cycle. Thus, it is possible to reach any other town starting from one town.
Part 2: If it is possible to reach all of the 4 other towns starting from any town, there can be no town with indegree or outdegree of 4. It is clear that you cannot have any town with indegree or outdegree of 4 or else that town would either be unreachable from the other towns or that town would be unable to reach any other town.
The proof is complete. (It is actually much simpler than it looks)
-ZHANALEX

## Solution 6
We claim the following conditions:
-A path is invalid if a vertex $\omega$ has no arcs leading to it. (1)
-A path is invalid if a vertex $\omega$ has all arcs leading to it. (2)
-A path is always valid if it does not satisfy (1) and (2) and has a "cycle" of arcs of $\omega_1 \to \omega_2 \to \omega_3 \to \omega_1$ . (3)
-(1) and (2) are sufficient to cover all invalid paths.
Call the vertices $\omega_1, \omega_2, \omega_3, \omega_4, \omega_5$ . WLOG, let $\omega_1 \to \omega_2$ . Then, WLOG let $\omega_2 \to \omega_3$ . We have two ways to go from here:
If $\omega_3 \to \omega_1$ , we call it a "cycle".
We will prove (3):
Notice that once $\omega_4, \omega_5$ can reach one of the vertices on the "cycle", it can reach any of the other vertices on the same cycle simply by travelling along the arcs of the cycle. Additionally, one of $\omega_4, \omega_5$ must be able to travel to the cycle. Consider that it cannot, then $\omega_3 \to \omega_4$ and $\omega_5 \to \omega_4$ are forced. Now, $\omega_4 \to \omega_1, \omega_2, \omega_3$ which is on the cycle. Now, if $\omega_5 \to \omega_4$ , it will also be able to travel to the cycle. Otherwise, the directed arc will directly travel to the cycle. Also, each of the vertices $\omega_1, \omega_2, \omega_3$ will travel to $\omega_4, \omega_5$ .
If our graph does not satisfy (1) and (2), $\omega_4, \omega_5$ will connect to the cycle on both directions. This can be shown below:
Clearly $\omega_4, \omega_5$ are connected. Assuming the graph does not satisfy (1) and (2), $\omega_4, \omega_5$ are connected to the cycle consisting of $\omega_1, \omega_2, \omega_3$ . WLOG, let $\omega_4 \to \omega_5$ :
Again, to avoid (2), $\omega_5 \to \omega_a$ where $a\in{1,2,3}$ . Now to avoid (1), one of $\omega_a \to \omega_4, a\in{1,2,3}$ .
Now it is clear that each vertex can go to any other vertex. This concludes our proof.
Say we try to avoid (3) so that WLOG $\omega_5 \to \omega_1$ . If we keep trying to avoid a "cycle", $\omega_3 \to \omega_4$ and $\omega_4 \to \omega_5$ which is a cycle.
Therefore, if there is any path $\omega_a \to \omega_b \to \omega_c$ , it will lead to a cycle and ultimately a valid path. The only way to avoid this is to have (1) or (2).
Consider (1):
WLOG, let $\omega_1$ have no arcs leading to it. Then all other vertices will have an arc directed toward them away from $\omega_1$ . Therefore, one path can have only 1 unique vertex that has no arcs leading to it. There are 5 ways to choose the vertex and $2^{\binom{5}{2}-4}=2^6$ ways for the remaining 6 arcs since they can be directed in any way. There are $2^6\cdot5=320$ paths for this condition.
Consider (2):
WLOG, let $\omega_1$ have all arcs leading to it. Similarly, all other vertices will have an arc that is directed away from them and points to $\omega_1$ . Therefore, only one unique vertex can have all arcs leading to it. There are 5 ways to choose the vertex and $2^{\binom{5}{2}-4}=2^6$ ways for the remaining arcs. There are also $2^6\cdot5=320$ paths for this condition.
However, we have overcounted paths that satisfy both (1) and (2). These paths will have one vertex that has all arcs leading to it and another that has all arcs directed away from it. There are $5\cdot4=20$ ways to choose these 2 vertices, and the remaining $\binom{3}{2}=3$ arcs each have 2 ways to be directed toward each other, so there are a total of $2^3\cdot 20=160$ overlapping paths.
By PIE, the number of invalid cases is $320+320-160=480$ .
The total number of cases is $2^{\binom{5}{2}}=2^{10}=1024$ since there are 10 edges and each can go 2 ways. By complementary counting, the number of valid paths is just $1024-480=\boxed{544}$
-Magnetoninja
Another way to state this problem is finding the number of strongly connected labeled tournaments on $5$ nodes. Finding a strongly connected labeled tournament is the same as finding a way to make all the roads one-way such that there is always a way to get from one town to another. This link gives the number of strongly connected labeled tournaments on $n$ nodes for small $n$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .