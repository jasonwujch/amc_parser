# 2023 AIME I Problem 14

## Problem

The following analog clock has two hands that can move independently of each other. [asy] unitsize(2cm); draw(unitcircle,black+linewidth(2)); for (int i = 0; i < 12; ++i) { draw(0.9*dir(30*i)--dir(30*i)); } for (int i = 0; i < 4; ++i) { draw(0.85*dir(90*i)--dir(90*i),black+linewidth(2)); } for (int i = 1; i < 13; ++i) { label("\small" + (string) i, dir(90 - i * 30) * 0.75); } draw((0,0)--0.6*dir(90),black+linewidth(2),Arrow(TeXHead,2bp)); draw((0,0)--0.4*dir(90),black+linewidth(2),Arrow(TeXHead,2bp)); [/asy] Initially, both hands point to the number $12$ . The clock performs a sequence of hand movements so that on each movement, one of the two hands moves clockwise to the next number on the clock face while the other hand does not move.

Let $N$ be the number of sequences of $144$ hand movements such that during the sequence, every possible positioning of the hands appears exactly once, and at the end of the $144$ movements, the hands have returned to their initial position. Find the remainder when $N$ is divided by $1000$ .

## Solution 1 (Drawing the Grid)
This problem is, in essence, the following: A $12\times12$ coordinate grid is placed on a (flat) torus; how many loops are there that pass through each point while only moving up or right? In other words, Felix the frog starts his journey at $(0,0)$ in the coordinate plane. Every second, he jumps either to the right or up, until he reaches an $x$ - or $y$ -coordinate of $12$ . At this point, if he tries to jump to a coordinate outside the square from $(0,0)$ to $(11,11)$ , he "wraps around" and ends up at an $x$ - or $y$ - coordinate of $0$ . How many ways are there for Felix to jump on every grid point in this square, so that he ends at $(0,0)$ ? This is consistent with the construction of the flat torus as $\mathbb Z^2/12\mathbb Z^2$ (2-dimensional modular arithmetic. $(\mathbb{Z}_{12})^2$ )
Moving on, define a $\textit{path}$ from point $A$ to point $B$ to be a sequence of "up"s and "right"s that takes Felix from $A$ to $B$ . The $\textit{distance}$ from $A$ to $B$ is the length of the shortest path from $A$ to $B$ . At the crux of this problem is the following consideration: The points $A_i=(i,11-i), i\in{0,...,11}$ are pairwise equidistant, each pair having distance of $12$ in both directions.
[asy] size(7cm); for (int x=0; x<12; ++x){ for (int y=0; y<12; ++y){ fill(circle((x,y),0.05));}} for (int i=0; i<12; ++i){ fill(circle((i,11-i),0.1),red);} pen p=green+dashed; path u=(3,8)--(4,8)--(4,9)--(4,10)--(4,11)--(5,11)--(5,11.5); path v=(5,-0.5)--(5,0)--(5,1)--(6,1)--(6,2)--(6,3)--(6,4)--(7,4); draw(u,p); draw(v,p); pen p=blue+dashed; path u=(4,7)--(5,7)--(5,8)--(5,9)--(5,10)--(6,10)--(6,11)--(6,11.5); path v=(6,-0.5)--(6,0)--(7,0)--(7,1)--(7,2)--(7,3)--(8,3); draw(u,p); draw(v,p); [/asy]
A valid complete path then joins two $A_i$ 's, say $A_i$ and $A_j$ . In fact, a link between some $A_i$ and $A_j$ fully determines the rest of the cycle, as the path from $A_{i+1}$ must "hug" the path from $A_i$ , to ensure that there are no gaps. We therefore see that if $A_0$ leads to $A_k$ , then $A_i$ leads to $A_{i+k}$ . Only the values of $k$ relatively prime to $12$ result in solutions, though, because otherwise $A_0$ would only lead to $\{A_i:\exists n\in \mathbb Z:i\equiv kn\quad\text{mod 12}\}$ . The number of paths from $A_0$ to $A_k$ is ${12\choose k}$ , and so the answer is
\[{12\choose1}+{12\choose5}+{12\choose7}+{12\choose11}=1\boxed{608}.\]
Notes:
- One can prove that the path from $A_{i+1}$ must "hug" the path from $A_i$ by using techniques similar to those in Solution 2.
- One can count the paths as follows: To get from $A_0$ to $A_i$ , Felix takes $k$ rights and $12-k$ ups, which can be done in ${12\choose k}$ ways.

## Solution 2 (Simple Cyclic Permutation Analysis)
This is more of a solution sketch and lacks rigorous proof for interim steps, but illustrates some key observations that lead to a simple solution.
Note that one can visualize this problem as walking on a $N \times N$ grid where the edges warp. Your goal is to have a single path across all nodes on the grid leading back to $(0,\ 0)$ . For convenience, any grid position are presumed to be in $\mod N$ .
Note that there are exactly two ways to reach node $(i,\ j)$ , namely $(i - 1,\ j)$ and $(i,\ j - 1)$ .
As a result, if a path includes a step from $(i,\ j)$ to $(i + 1,\ j)$ , there cannot be a step from $(i,\ j)$ to $(i,\ j + 1)$ . However, a valid solution must reach $(i,\ j + 1)$ , and the only valid step is from $(i - 1,\ j + 1)$ .
So a solution that includes a step from $(i,\ j)$ to $(i + 1,\ j)$ dictates a step from $(i - 1,\ j + 1)$ to $(i,\ j + 1)$ and by extension steps from $(i - a,\ j + a)$ to $(i - a + 1,\ j + a)$ . We observe the equivalent result for steps in the orthogonal direction.
This means that in constructing a valid solution, taking one step in fact dictates N steps, thus it's sufficient to count valid solutions with $N = a + b$ moves of going right $a$ times and $b$ times up the grid. The number of distinct solutions can be computed by permuting 2 kinds of indistinguishable objects $\binom{N}{a}$ .
Here we observe, without proof, that if $\gcd(a, b) \neq 1$ , then we will return to the origin prematurely. For $N = 12$ , we only want to count the number of solutions associated with $12 = 1 + 11 = 5 + 7 = 7 + 5 = 11 + 1$ .
(For those attempting a rigorous proof, note that $\gcd(a, b) = \gcd(a + b, b) = \gcd(N, b) = \gcd(N, a)$ ).
The total number of solutions, noting symmetry, is thus
\[2\cdot\left(\binom{12}{1} + \binom{12}{5}\right) = 1608\]
This yields $\boxed{\textbf{608}}$ as our desired answer.
~ cocoa @ https://www.corgillogical.com/

## Solution 3 (Matrix Analysis and Permutation)
Define a $12 \times 12$ matrix $X$ . Each entry $x_{i, j}$ denotes the number of movements the longer hand moves, given that two hands jointly make $12 \left( i - 1 \right) + \left( j - 1 \right)$ movements. Thus, the number of movements the shorter hand moves is $12 \left( i - 1 \right) + \left( j - 1 \right) - x_{i, j}$ .
Denote by $r_{i, j}$ the remainder of $x_{i, j}$ divided by 12. Denote by $R$ this remainder matrix.
If two hands can return to their initial positions after 144 movements, then $r_{12, 12} = 0$ or 11. Denote by $S_0$ (resp. $S_{11}$ ) the collection of feasible sequences of movements, such that $r_{12, 12} = 0$ (resp. $r_{12, 12} = 11$ ).
Define a function $f : S_0 \rightarrow S_{11}$ , such that for any $\left\{ x_{i,j} , \ \forall \ i, j \in \left\{ 1, 2, \cdots , 12 \right\} \right\} \in S_0$ , the functional value of the entry indexed as $\left( i, j \right)$ is $12 \left( i - 1 \right) + \left( j - 1 \right) - x_{i, j}$ . Thus, function $f$ is bijective. This implies $| S_0 | = | S_{11} |$ .
In the rest of analysis, we count $| S_0 |$ .
We make the following observations:
- $x_{1, 1} = 0$ and $12 | x_{12, 12}$ .
- Each column of $R$ is a permutation of $\left\{ 0, 1, \cdots , 11 \right\}$ .
- For any $j \in \left\{ 1, 2 ,\cdots , 11 \right\}$ , $x_{i, j+1} - x_{i, j}$ is equal to either 0 for all $i$ or 1 for all $i$ .
- $x_{i+1, 1} = x_{i, 12}$ for any $i \in \left\{ 1, 2, \cdots , 11 \right\}$ .
All observations jointly imply that $x_{i, 12} = i \cdot x_{1, 12}$ . Thus, $\left\{ r_{1, 12}, r_{2, 12} , \cdots , r_{11, 12} \right\}$ is a permutation of $\left\{ 1, 2, \cdots , 11 \right\}$ . Thus, $x_{1, 12}$ is relatively prime to 12.
Because $x_{1, 1} = 0$ and $x_{1, 12} - x_{1, 1} \leq 11$ , we have $x_{1, 12} = 1$ , 5, 7, or 11.
Recall that when we move from $x_{1, 1}$ to $x_{1, 12}$ , there are 11 steps of movements. Each movement has $x_{1, j+1} - x_{i, j} = 0$ or 1. Thus, for each given $x_{1, 12}$ , the number of feasible movements from $x_{1, 1}$ to $x_{1, 12}$ is $\binom{11}{x_{1, 12}}$ .
Therefore, the total number of feasible movement sequences in this problem is \begin{align*} | S_0 | + | S_{11} | & = 2 | S_0 | \\ & = 2 \cdot \sum_{x_{1, 12} = 1, 5, 7, 11} \binom{11}{x_{1, 12}} \\ & = 2 \left( 11 + 462 + 330 + 1 \right) \\ & = 1608 . \end{align*}
Therefore, the answer is $\boxed{\textbf{(608)}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### Supplementary Contents
This can be interpreted as the 2D-model stated in Solution 1. After certain observations, we found out that the first 12 steps determines the all the rest.
This is similar to the situation of Problem 11 of 2025 AIME II ( https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_11 ). In this case, every possible positioning of the hands appears exactly once, meaning that the length of the repeating cycle is 12. As we can see from the pattern, only 1 and numbers relatively prime to 12 can fit in the conditions, which are 1, 5, 7, 11.
In conclusion, \[{12\choose1}+{12\choose5}+{12\choose7}+{12\choose11}=1\boxed{608}.\]
~cassphe

## Video Solution
https://youtu.be/3DtJB78aua4
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution
https://youtu.be/tsoLZj8Dz2o
~MathProblemSolvingSkills.com

## Animated Video Solution
https://youtu.be/A5BqIUPIbVg
~Star League ( https://starleague.us )
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .