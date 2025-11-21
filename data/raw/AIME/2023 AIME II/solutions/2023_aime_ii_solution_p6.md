# 2023 AIME II Problem 6

## Problem

Consider the L-shaped region formed by three unit squares joined at their sides, as shown below. Two points $A$ and $B$ are chosen independently and uniformly at random from inside the region. The probability that the midpoint of $\overline{AB}$ also lies inside this L-shaped region can be expressed as $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$ [asy] unitsize(2cm); draw((0,0)--(2,0)--(2,1)--(1,1)--(1,2)--(0,2)--cycle); draw((0,1)--(1,1)--(1,0),dashed); [/asy]

## Video Solution by MOP 2024
https://youtube.com/watch?v=0UViBt-LYTo&t=0s

## Solution 1
We proceed by calculating the complement.
Note that the only configuration of the 2 points that makes the midpoint outside of the L shape is one point in the top square, and one in the right square. This occurs with $\frac{2}{3} \cdot \frac{1}{3}$ probability.
Let the topmost coordinate have value of: $(x_1,y_1+1)$ , and rightmost value of: $(x_2+1,y_2)$ .
The midpoint of them is thus: \[\left(\frac{x_1+x_2+1}{2}, \frac{y_1+y_2+1}{2} \right)\]
It is clear that $x_1, x_2, y_1, y_2$ are all between 0 and 1. For the midpoint to be outside the L-shape, both coordinates must be greater than 1, thus: \[\frac{x_1+x_2+1}{2}>1 \implies x_1+x_2>1\]
By symmetry this has probability $\frac{1}{2}$ . Also by symmetry, the probability the y-coordinate works as well is $\frac{1}{2}$ . Thus the probability that the midpoint is outside the L-shape is: \[\frac{2}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{18}\]
We want the probability that the point is inside the L-shape however, which is $1-\frac{1}{18}=\frac{17}{18}$ , yielding the answer of $17+18=\boxed{35}$ ~SAHANWIJETUNGA

## Solution 2（Calculus)
We assume each box has side length 1. We index the upper left box, the bottom left box, the bottom right box as II, III, IV, respectively. We index the missing upper right box as I. We put the graph to a coordinate system by putting the intersecting point of four foxes at the origin, the positive direction of the $x$ axis at the intersecting line of boxes I and IV, and the positive direction of the $y$ -axis at the intersecting line of boxes I and II. We denote by $M$ the midpoint of $AB$ .
Therefore, \begin{align*} \Bbb P \left( M \in II \cup III \cup IV \right) & = 1 - \Bbb P \left( M \in I \right) . \end{align*}
We observe that a necessary for $M \in I$ is either $A \in II$ and $B \in IV$ , or $A \in IV$ and $B \in II$ . In addition, by symmetry, \[ \Bbb P \left( M \in I | A \in II, B \in IV \right) = \Bbb P \left( M \in I | A \in IV, B \in II \right) . \]
Thus, \begin{align*} \Bbb P \left( M \in I \right) & = 2 \Bbb P \left( M \in I | A \in II, B \in IV \right) \Bbb P \left( A \in II, B \in IV \right) \\ & = 2 \Bbb P \left( M \in I | A \in II, B \in IV \right) \Bbb P \left( A \in II \right) \Bbb P \left( B \in IV \right) \\ & = 2 \Bbb P \left( M \in I | A \in II, B \in IV \right) \cdot \frac{1}{3} \cdot \frac{1}{3} \\ & = \frac{2}{9} \Bbb P \left( M \in I | A \in II, B \in IV \right) \\ & = \frac{2}{9} \Bbb P \left( x_M > 0, y_M > 0 | x_A < 0, y_A > 0, x_B > 0, y_B < 0 \right) \\ & = \frac{2}{9} \Bbb P \left( x_M > 0 | x_A < 0, x_B > 0 \right) \cdot \Bbb P \left( y_M > 0 | y_A > 0, y_B < 0 \right) \\ & = \frac{2}{9} \Bbb P \left( x_M > 0 | x_A < 0, x_B > 0 \right)^2 \\ & = \frac{2}{9} \Bbb P \left( x_A + x_B > 0 | x_A < 0, x_B > 0 \right)^2 \\ & = \frac{2}{9} \left( \int_{x_A = -1}^0 \int_{x_B = 0}^1 \mathbf 1 \left\{ x_A + x_B > 0 \right\} dx_B dx_A \right)^2 \\ & = \frac{2}{9} \left( \int_{x_A = -1}^0 \int_{x_B = - x_A}^1 dx_B dx_A \right)^2 \\ & = \frac{2}{9} \left( \int_{x_A = -1}^0 \left( 1 + x_A \right) dx_A \right)^2 \\ & = \frac{2}{9} \left( \frac{1}{2} \right)^2 \\ & = \frac{1}{18} . \end{align*} The second equality follows from the condition that the positions of $A$ and $B$ are independent. The sixth equality follows from the condition that for each point of $A$ and $B$ , the $x$ and $y$ coordinate are independent.
Therefore, \begin{align*} \Bbb P \left( M \in II \cup III \cup IV \right) & = 1 - \frac{1}{18} \\ & = \frac{17}{18} . \end{align*}
Therefore, the answer is $17 + 18 = \boxed{\textbf{(035) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Geometry)
The only configuration of two points that makes the midpoint outside of the $L-$ shape is one point in the top square, and one in the right square with probability $\frac{2}{9}$ (see Solution $1.)$
We use the coordinate system shown in diagram. Let the arbitrary point $A(x, -y), x \in [0,1], y \in [0,1]$ be in right square. It is clear that iff point $B$ lies in yellow rectangle with sides $x$ and $1 – y,$ then the midpoint $AB$ lies outside of the $L.$
Probability of this is $p = x(1 – y).$
Consider the points $A_1(1-y,-x), A_2(1-x,y-1), A_3(y,x-1).$
Similarly we find $p_1 = (1-y)(1-x), p_2= (1-x)y, p_3 = xy.$
The probability that the midpoint of one of the segments $A_1B, A_2B, A_3B$ and $AB$ is outside of the $L-$ shape is \[\frac {p_1+p_2+p_3+p}{4} = \frac {1}{4}.\] If point $A$ is in the right square, point $B$ in the top square, the probability that the midpoint of $\overline{AB}$ lies outside $L-$ shape is $\frac {1}{4} \implies$
If points $A$ and $B$ are chosen independently and uniformly at random in $L-$ shape, then the probability that the midpoint of $\overline{AB}$ lies outside $L-$ shape is $\frac {1}{4} \cdot \frac {2}{9} = \frac {1}{18}.$ Therefore the probability that the point is inside the $L-$ shape is $1-\frac{1}{18}=\frac{17}{18} \implies \boxed{35}.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 4 (Coordinates, similar to Solution 1)
Consider this diagram:
First, the one of points must be in the uppermost box and the other in the rightmost box. This happens with probability 2/3*1/3=2/9.
We need the midpoints of the $x$ coordinates to be greater than $1$ but less than $2.$
We need the midpoints of the $y$ coordinates to be greater than $1$ but less than $2.$
Thus, we set up: \[1<\frac{x_1+x_2}{2}<2\] \[1<\frac{y_1+y_2}{2}<2\]
Using geometric probability, as shown below, we get that the probability of happening is 1/2. This is for both. So we have probability 1/2*1/2=1/4.
Thus, the fraction is 1-(2/9*1/4)= 1-1/18=17/18.
The answer is 17+18=35
mathboy282
Minor edit by whatsoever281

## Solution 5
We casework on the squares the two points are in. Unless the two squares are on opposite corners, which happens with probability $\frac{2}{9}$ . If the points are on opposite corners, the points must be on the upper half of the splitting diagonal for the midpoint to not be in the square. This occurs with probability $\frac{1}{4}$ . We take the complement and get final answer $(\frac{2}{9})(\frac{3}{4}) + (\frac{7}{9}) = \frac{17}{18}$ .
CORRECTION: This solution is wrong. We can have one point above the splitting diagonal and one point below the splitting diagonal and still have the midpoint not be in the square.

## Video Solution by The Power of Logic
https://youtu.be/KngzOXcmM-E
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .