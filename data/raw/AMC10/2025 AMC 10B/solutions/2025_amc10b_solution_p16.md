# 2025 AMC 10B Problem 16

## Problem

A circle has been divided into 6 sectors of different sizes. Then 2 of the sectors are painted red, 2 painted green, and 2 painted blue so that no two neighboring sectors are painted the same color. One such coloring is shown below.

[asy] unitsize(1.7cm); pair O = (0, 0); real R = 2; pair A = (R, 0); pair B = (0.5*R, 0.866*R); pair C = (0, R); pair D = (-R, 0); pair E = (-0.954*R, -0.3*R); pair F = (-0.22*R, -0.975*R); path sector1 = O -- A .. arc(O,A,B) -- cycle; path sector2 = O -- B .. arc(O,B,C) -- cycle; path sector3 = O -- C .. arc(O,C,D) -- cycle; path sector4 = O -- D .. arc(O,D,E) -- cycle; path sector5 = O -- E .. arc(O,E,F) -- cycle; path sector6 = O -- F .. arc(O,F,A) -- cycle; pen r = rgb(255, 120, 120); pen g = rgb(120, 255, 120); pen b = rgb(120, 120, 255); filldraw(sector1, g); filldraw(sector2, r); filldraw(sector3, b); filldraw(sector4, r); filldraw(sector5, g); filldraw(sector6, b); draw(circle(O, R)); defaultpen(fontsize(12pt)); label("green", (0.57*R, 0.32*R)); label("red", (0.16*R, 0.63*R)); label("blue", (-0.45*R, 0.45*R)); label("red", (-0.69*R, -0.1*R)); label("green", (-0.45*R, -0.5*R)); label("blue", (0.39*R, -0.49*R)); [/asy]

How many different colorings are possible?

$\textbf{(A)}~12\qquad\textbf{(B)}~16\qquad\textbf{(C)}~18\qquad\textbf{(D)}~24\qquad\textbf{(E)}~28$

## Solution 1
Create an arbitrary six slice circular diagram. The first slice has 3 options, and the second has 2, third has 2, fourth has 2, fifth has 2, and the sixth has only 1 color to be chosen.
Understand that if \( \mathbb{X} \) is the set containing all possible cases of the circle, then \( \mathbb{X} \) has a correlation to another set, call it \( \mathbb{K} \), which contains all the colors. This can be quite easily sought as a rotation of one element in \( \mathbb{X} \) that accurately maps to another element in \( \mathbb{X} \) is considered the same.
In simpler terms, to account for overlapping cases in \( \mathbb{X} \), one must divide by 2 (as two colorings that are rotated are considered different, and we don't want that as it defeats the purpose of "unique").
Then, multiplying out we have \( 3 \times 2^4 = 48 \). Dividing by 2 to account for overlap in \( \mathbb{X} \), we get \( 48/2 \) or $\boxed{\textbf{(D) } 24}$
~Pinotation

## Solution 2
Model the circle as the $6$ -cycle \(C_6\) with labeled positions \(1,2,3,4,5,6\) in circular order. We count proper colorings using \(R,G,B\), each appearing exactly twice.
There are two structural possibilities for how the two copies of each color are placed:
{Case 1: All three colors occupy opposite positions.}
Opposite positions in \(C_6\) are the three pairs \((1,4), (2,5), (3,6)\). If each color occupies one opposite pair, then the colors must alternate around the circle, yielding a pattern of the form { $A,B,C,A,B,C$ }
for some ordering \((A,B,C)\) of \((R,G,B)\). The number of such colorings is $3!$ = $6$
{Case 2: Exactly one color occupies opposite positions.}
Choose the color that is opposite: \(3\) choices. Choose which opposite pair it occupies: \(3\) choices one of \((1,4), (2,5), (3,6)\)), for a total of \(3\cdot 3 = 9\) placements.
Removing those two opposite positions leaves two disjoint adjacent pairs among the remaining four positions. For example, if the opposite color is at \((1,4)\), the remaining positions \(\{2,3,5,6\}\) form the two adjacent pairs \((2,3)\) and \((5,6)\). The other two colors must each appear twice, and no adjacent positions may match; therefore each pair must be colored with different colors, and to achieve two copies of each color overall, the two pairs must be complementary:
$(2,3)$ is $(G,B)$ or $(B,G)$ , and then $(5,6)$ in the opposite ordering.
This gives \(2\) valid assignments for the four positions per fixed opposite placement.
Hence, this case contributes \(9\cdot 2 = 18\)
Summing the $2$ cases
$6$ + $18$ = $24$
$\boxed{\textbf{(D) } 24}$ .
~NumberNinja1234
~Extremely minor edit by Boywithnuke

## Solution 3
We can also case differently.
Let us call the sectors $1$ , $2$ , $3$ , $4$ , $5$ , and $6$ going clockwise around the circle. We, without loss of generality, assume $1$ to be colored $R$ . Additionally, without loss of generality, assume $2$ to be colored $B$ . We will nullify these assumptions by multiplying by a factor of $6$ at the end.
We case on the color of sector $6$ .
### Case 1: Sector is colored
Each color is used two times, so we have one $R$ and two $G$ s left to distribute between $3$ , $4$ , and $5$ . Obviously, the $G$ s cannot be adjacent and thus the only possible coloring is $(3, 4, 5) = (G, R, G)$ .
There is $1$ solution for this case.
### Case 2: Sector is colored
In this case, we have we have one $R$ , one $B$ , and one $G$ left to distribute between $3$ , $4$ , and $5$ . Since $3$ , $4$ , and $5$ , are all distinct colors, the only restrictions on this case are that $3$ cannot be colored $B$ and $5$ cannot be colored $G$ .
Quick casework shows that if $3$ is colored $R$ , there are one solution $(3, 4, 5) = (R, G, B)$ and if $3$ is colored $G$ then there are two solutions $(3, 4, 5) = (G, R, B)$ and $(3, 4, 5) = (G, B, R)$ .
There are $3$ solutions for this case.
Thus, the total number of solutions is: \[6 \cdot (1 + 3) = \boxed{\textbf{(D) } 24}\]
~megaboy6679

## Solution 4
We can also have the following two cases:
### Case 1: The three colors on the top semicircle are all different
Then, three are 6 different ways to rearrange the top. For the bottom, the leftmost one has one restriction and the rightmost one has one restriction. Let's say the leftmost cannot be red and the rightmost cannot be green WLOG. Then, we can have the cases (from left to right): {green, blue, red}, {green, red, blue}, and {blue, green, red}. So, there are 3 different ways to rearrange the bottom. So, ,for case one, there are $6\times3=18$ different ways to rearrange.
### Case 2: The three colors on the top has one pair of the same colors
Then, there are 3 ways to choose the same color and then 2 ways to choose the color that is only put in once. After choosing all of that, the bottom then will be fixed (try it yourself if you think it is not). So, case 2 has $3\times2=6$ ways to rearrange.
After combining the 2 cases, we get $18+6=24$ cases, so our answer is $\boxed{\textbf{(D) } 24}$ .
~Yuhao2012

## Solution 5 (simplest and easiest)
Let's assume that the colors do not matter, so let's just start with Red in the very top sector. The fact that the sectors are distinct in size does not matter at all, so just ignore that. If Red is in the top sector, then we have 3 cases:
Case 1: Red is also in the 3rd sector (going clockwise from the top one) Thus, this is only one case because there are already 2 that are together, so the colors of those 2 must be distinct.
Case 2: Red is also in the sector directly opposite. There are 2 cases for this; we can have all the colors being opposite, or we can have a case where everything is symmetric.
Case 3: Red is also in the 5th sector This is basically congruent (symmetric) to the first case, so we also only have 1 case.
Adding all these up, we have $1+2+1=4$ cases in total.
However, we did not consider color yet. Because there are 3 colors, they can be permuted $3!=6$ ways.
Therefore, $6\times4=24$ , so our answer is $\boxed{\textbf{(D) } 24}$ .
~notvalid

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs
### See Also