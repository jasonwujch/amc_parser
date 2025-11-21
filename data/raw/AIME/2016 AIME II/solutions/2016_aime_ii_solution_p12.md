# 2016 AIME II Problem 12

## Problem

The figure below shows a ring made of six small sections which you are to paint on a wall. You have four paint colors available and you will paint each of the six sections a solid color. Find the number of ways you can choose to paint the sections if no two adjacent sections can be painted with the same color.

[asy] draw(Circle((0,0), 4)); draw(Circle((0,0), 3)); draw((0,4)--(0,3)); draw((0,-4)--(0,-3)); draw((-2.598, 1.5)--(-3.4641, 2)); draw((-2.598, -1.5)--(-3.4641, -2)); draw((2.598, -1.5)--(3.4641, -2)); draw((2.598, 1.5)--(3.4641, 2)); [/asy]

## Video Solution by grogg007 (Under 5 Mins ⏩)
https://www.youtube.com/watch?v=lTP-jNtpwoI

## Solution 1
Choose a section to start coloring. Assume, WLOG, that this section is color $1$ . We proceed coloring clockwise around the ring. Let $f(n,C)$ be the number of ways to color the first $n$ sections (proceeding clockwise) such that the last section has color $C$ . In general (except for when we complete the coloring), we see that \[f(n,C_i)=\sum_{j\ne i} f(n-1,C_j),\] i.e., $f(n,C_i)$ is equal to the number of colorings of $n-1$ sections that end in any color other than $C_i$ . Using this, we can compute the values of $f(n,C)$ in the following table.
$\begin{tabular}{c|c|c|c|c } \multicolumn{1}{c}{}&\multicolumn{4}{c}{\(C\)}\\ \(n\)&1 & 2 & 3& 4 \\ \hline 1& 1 & 0 & 0 & 0\\ 2 & 0 & 1 & 1 & 1 \\ 3& 3 & 2 & 2 & 2 \\ 4 & 6 & 7 & 7 & 7 \\ 5 & 21 & 20 & 20 & 20\\ 6& 0& 61 & 61 & 61\\ \end{tabular}$
Note that $f(6, 1)=0$ because then $2$ adjacent sections are both color $1$ . We multiply this by $4$ to account for the fact that the initial section can be any color. Thus the desired answer is $(61+61+61) \cdot 4 = \boxed{732}$ .
Solution by Shaddoll

## Solution 2
We use complementary counting. There are $4^6$ total colorings of the ring without restriction. To count the complement, we wish to count the number of colorings in which at least one set of adjacent sections are the same color. There are six possible sets of adjacent sections that could be the same color (think of these as borders). Call these $B_1,B_2,\dots,B_6$ . Let $\mathcal{A}_1, \mathcal{A}_2,\dots,\mathcal{A}_6$ be the sets of colorings of the ring where the sections on both sides of $B_1,B_2,\dots,B_6$ are the same color. We wish to determine $|\mathcal{A}_1\cup\mathcal{A}_2\cup\cdots\cup\mathcal{A}_6|$ . Note that all of these cases are symmetric, and in general, $|\mathcal{A}_i|=4^5$ . There are $6$ such sets $\mathcal{A}_i$ . Also, $|\mathcal{A}_i\cup\mathcal{A}_j|=4^4$ , because we can only change colors at borders, so if we have two borders along which we cannot change colors, then there are four borders along which we have a choice of color. There are $\binom{6}{2}$ such pairs $\mathcal{A}_i\cup\mathcal{A}_j$ . Similarly, $|\mathcal{A}_i\cup \mathcal{A}_j\cup \mathcal{A}_k|=4^3$ , with $\binom{6}{3}$ such triples, and we see that the pattern will continue for 4-tuples and 5-tuples. For 6-tuples, however, these cases occur when there are no changes of color along the borders, i.e., each section has the same color. Clearly, there are four such possibilities.
Therefore, by PIE, \[|\mathcal{A}_1\cup\mathcal{A}_2\cup\cdots\cup\mathcal{A}_6|=\binom{6}{1}\cdot 4^5-\binom{6}{2}\cdot 4^4+\binom{6}{3}\cdot 4^3-\binom{6}{4}\cdot 4^2+\binom{6}{5}\cdot 4^1-4.\] We wish to find the complement of this, or \[4^6-\left(\binom{6}{1}\cdot 4^5-\binom{6}{2}\cdot 4^4+\binom{6}{3}\cdot 4^3-\binom{6}{4}\cdot 4^2+\binom{6}{5}\cdot 4^1-4\right).\] By the Binomial Theorem, this is $(4-1)^6+3=\boxed{732}$ .

## Solution 3
We use generating functions. Suppose that the colors are $0,1,2,3$ . Then as we proceed around a valid coloring of the ring in the clockwise direction, we know that between two adjacent sections with colors $s_i$ and $s_{i+1}$ , there exists a number $d_i\in\{1,2,3\}$ such that $s_{i+1}\equiv s_i+d_i\pmod{4}$ . Therefore, we can represent each border between sections by the generating function $(x+x^2+x^3)$ , where $x,x^2,x^3$ correspond to increasing the color number by $1,2,3\pmod4$ , respectively. Thus the generating function that represents going through all six borders is $A(x)=(x+x^2+x^3)^6$ , where the coefficient of $x^n$ represents the total number of colorings where the color numbers are increased by a total of $n$ as we proceed around the ring. But if we go through all six borders, we must return to the original section, which is already colored. Therefore, we wish to find the sum of the coefficients of $x^n$ in $A(x)$ with $n\equiv 0\pmod4$ .
Now we note that if $P(x)=x^n$ , then \[P(x)+P(ix)+P(-x)+P(-ix)=\begin{cases}4x^n&\text{if } n\equiv0\pmod{4}\\0&\text{otherwise}.\end{cases}\] Therefore, the sum of the coefficients of $A(x)$ with powers congruent to $0\pmod 4$ is \[\frac{A(1)+A(i)+A(-1)+A(-i)}{4}=\frac{3^6+(-1)^6+(-1)^6+(-1)^6}{4}=\frac{732}{4}.\] We multiply this by $4$ to account for the initial choice of color, so our answer is $\boxed{732}$ .

## Solution 4
Let $f(n)$ be the number of valid ways to color a ring with $n$ sections (which we call an $n$ -ring), so the answer is given by $f(6)$ . For $n=2$ , we compute $f(n)=4\cdot3=12$ . For $n \ge 3$ , we can count the number of valid colorings as follows: choose one of the sections arbitrarily, which we may color in $4$ ways. Moving clockwise around the ring, there are $3$ ways to color each of the $n-1$ other sections. Therefore, we have $4 \cdot 3^{n-1}$ colorings of an $n$ -ring.
However, note that the first and last sections could be the same color under this method. To count these invalid colorings, we see that by "merging" the first and last sections into one, we get a valid coloring of an $(n-1)$ -ring. That is, there are $f(n-1)$ colorings of an $n$ -ring in which the first and last sections have the same color. Thus, $f(n) = 4 \cdot 3^{n-1} - f(n-1)$ for all $n \ge 3$ .
To compute the requested value $f(6)$ , we repeatedly apply this formula: \begin{align*} f(6)&=4\cdot3^5-f(5)\\&=4\cdot3^5-4\cdot3^4+f(4)\\&=4\cdot3^5-4\cdot3^4+4\cdot3^3-f(3)\\&=4\cdot3^5-4\cdot3^4+4\cdot3^3-4\cdot3^2+f(2)\\&=4(3^5-3^4+3^3-3^2+3)\\&=4\cdot3\cdot\frac{3^5+1}{3+1}\\&=\boxed{732}.\end{align*} (Solution by MSTang.)

## Solution 4b (solution for all values of n)
Do the same as solution 4 to get $f(n) = 4 \cdot 3^{n-1} - f(n-1)$ . Then, multiply both sides by $(-1)^{n}$ to get $(-1)^{n}f(n) = (-1)^{n-1}f(n-1) - 4 \cdot (-3)^{n-1}$ . Let $g(n) = (-1)^{n}f(n)$ , $g(n) = g(n-1) - 4 \cdot (-3)^{n-1}$ . $g(n) = g(2) - 4((-3)^{2}+(-3)^{3}+ \cdots + (-3)^{n-1}) = g(2) - 9(1-(-3)^{n-2})$ . $f(n) = (-1)^{n}g(n) = (-1)^{n}g(2)-9(-1)^{n}+3^{n} = \boxed{3(-1)^{n}+3^{n}}$ .

## Solution 5
Label the sections 1, 2, 3, 4, 5, 6 clockwise. We do casework on the colors of sections 1, 3, 5.
Case 1: the colors of the three sections are the same. In this case, each of sections 2, 4, 6 can be one of 3 colors, so this case yields $4 \times 3^3 = 108$ ways.
Case 2: two of sections 1, 3, 5 are the same color. Note that there are 3 ways for which two of the three sections have the same color, and $4 \times 3 = 12$ ways to determine their colors. After this, the section between the two with the same color can be one of 3 colors and the other two can be one of 2 colors. This case yields $3 \times (4 \times 3) \times (3 \times 2 \times 2) = 432$ ways.
Case 3: all three sections of 1, 3, 5 are of different colors. Clearly, there are $4 \times 3 \times 2 = 24$ choices for which three colors to use, and there are 2 ways to choose the colors of each of sections 2, 4, 6. Thus, this case gives $4 \times 3 \times 2 \times 2^3 = 192$ ways.
In total, there are $108 + 432 + 192 = \boxed{732}$ valid colorings.
Solution by ADMathNoob

## Solution 6
We will take a recursive approach to this problem. We can start by writing out the number of colorings for a circle with $1, 2,$ and $3$ compartments, which are $4, 12,$ and $24.$ Now we will try to find a recursive formula, $C(n)$ , for a circle with an arbitrary number of compartments $n.$ We will do this by focusing on the $n-1$ section in the circle. This section can either be the same color as the first compartment, or it can be a different color as the first compartment. We will focus on each case separately.
Case 1:
If they are the same color, we can say there are $C(n-2)$ to fill the first $n-1$ compartments. The $nth$ compartment must be different from the first and second to last compartments, which are the same color. Hence this case adds $3*C(n-2)$ to our recursive formula.
Case 2:
If they are different colors, we can say that there are $C(n-1)$ to fill the first $n-1$ compartments, and for the the $nth$ compartment, there are $2$ ways to color it because the $n-1$ and $1$ compartments are different colors. Hence this case adds $2*C(n-1).$
So our recursive formula, $C(n)$ , is $3*C(n-2) + 2*C(n-1).$ Using the initial values we calculated, we can evaluate this recursive formula up to $n=6.$ When $n=6,$ we get $\boxed{732}$ valid colorings.
Solution by NeeNeeMath

## Solution 7
WLOG, color the top left section $1$ and the top right section $2$ . Then the left section can be colored $2$ , $3$ , or $4$ , and the right section can be colored $1$ , $3$ , or $4$ . There are $3 \cdot 3 = 9$ ways to color the left and right sections. We split this up into two cases.
Case 1: The left and right sections are of the same color. There are $2$ ways this can happen: either they both are $3$ or they both are $4$ . We have $3$ colors to choose for the bottom left, and $2$ remaining colors to choose for the bottom right, for a total of $2 \cdot 3 \cdot 2$ cases.
Case 2: The left and right sections are of different colors. There are $9 - 2 = 7$ ways this can happen. Assume the left is $3$ and the right is $4$ . Then the bottom left can be $1$ , $2$ , or $4$ , and the bottom right can be $1$ , $2$ , or $3$ . However the bottom sections cannot both be $1$ or both be $2$ , so there are $3 \cdot 3 - 2 = 7$ ways to color the bottom sections, for a total for $7 \cdot 7 = 49$ colorings.
Since there were $4 \cdot 3 = 12$ ways to color the top sections, the answer is $12 \cdot (12 + 49) = \boxed{732}$ .

## Solution 8
Label the four colors $1, 2, 3,$ and $4$ , respectively. Now let's imagine a circle with the four numbers $1, 2, 3,$ and $4$ written clockwise. We'll say that a bug is standing on number $a$ . It is easy to see that for the bug to move to a different number, it must walk $1, 2,$ or $3$ steps clockwise. (This is since adjacent numbers can't be the same, as stated in the problem). Note that the sixth number in the bug's walking sequence must not equal the first number. Thus, our total number of ways, $N$ , given the bug's starting number $k$ , is simply the number of ordered quintuplets of positive integers $(a_1, a_2, a_3, a_4, a_5)$ that satisfy $a_i \in \{1, 2, 3\}$ for all $1 \leq i \leq 5$ and \[\sum_{i=1}^{5} a_i \neq 8, 12,\] since the bug cannot land on $k$ again on his fifth and last step. We know that the number of ordered quintuplets of positive integers $(a_1, a_2, a_3, a_4, a_5)$ that satisfy $a_i \in \{1, 2, 3\}$ without the other restriction is just $3^5$ , so we aim to find the number of quintuplets such that \[a_1 + a_2 + a_3 + a_4 + a_5 = 8, 12.\] Note that the number of ordered quintuplets satisfying $\sum_{i=1}^{5} a_i = 8$ is the same as the number of them satisfying $\sum_{i=1}^{5} a_i = 12$ due to symmetry. By stars and bars, there are $\dbinom{7}{4} = 35$ ways to distribute the three "extra" units to the five variables $a_1, a_2, a_3, a_4, a_5$ (since $a_i \geq 1$ ), but ways of distribution such that one variable is equal to $4$ are illegal, so the actual number of ways is $35 - 5 = 30$ . Since there are four possible values of $k$ (or the starting position for the bug), we obtain \[N = 4 \times (3^5 - 2 \times 30) = \boxed{732}.\] -fidgetboss_4000

## Solution 9
Let's number the regions $1,2,\dots 6$ . Suppose we color regions $1,2,3$ . Then, how many ways are there to color $4,5,6$ ?
Note: the numbers are numbered as shown:
[asy] draw(Circle((0,0), 4)); draw(Circle((0,0), 3)); draw((0,4)--(0,3)); draw((0,-4)--(0,-3)); draw((-2.598, 1.5)--(-3.4641, 2)); draw((-2.598, -1.5)--(-3.4641, -2)); draw((2.598, -1.5)--(3.4641, -2)); draw((2.598, 1.5)--(3.4641, 2)); label("1",(-3.5,0)); label("2",(-1.6,3)); label("3",(1.6,3)); label("4",(3.5,0)); label("5",(1.6,-3)); label("6",(-1.6,-3)); [/asy]
$\textbf{Case 1:}$ The colors of $1,2,3$ are $BAB$ , in that order.
Then the colors of $6,5,4$ can be $AXA$ , $AXC$ , $CXA$ , $CXC$ , or $CXD$ in that order, where $X$ is any color not equal to its surroundings. Then there are $4$ choices for $A$ , $3$ choices for $B$ (it cannot be $A$ ), $2$ choices for $C$ , and $1$ for $D$ , the last color. So, summing up, we have \[4*3(1*3+2*2+2*2+2*3+2*1*2)=12*21=252\] colorings.
$\textbf{Case 2:}$ The colors of $1,2,3$ are $BAC$ , in that order.
Again, we list out the possible arrangements of $6,5,4$ : $AXA$ , $AXB$ , $CXA$ , $AXD$ , $DXA$ , $CXB$ , $CXD$ , $DXB$ , or $DXD$ . (Easily simplified; listed here for clarity.) Then there are $4$ choices for $A$ as usual, $3$ choices for $B$ , and so on. Hence we have \[4*3*2(1*3+1*2+1*2+1*2+1*2+1*2+1*2+1*2+1*3)=24*20=480\] colorings in this case.
Adding up, we have $252+480=\boxed{732}$ as our answer.
This solution was brought to you by LEONARD_MY_DUDE

## Solution 10 (chromatic polynomial-VERY HELPFUL)
We quickly notice that this is just the cycle graph with 6 vertices. The chromatic polynomial for a cycle is $(k-1)^n+(-1)^n (k-1)$ where we use $k$ colors on a cycle of $n$ vertices. Plugging in $k=4$ and $n=6$ we arrive at $\boxed{732}$ . ~chrisdiamond10

## Solution 11 (step-by-step case analysis)
Let's label the regions as $1,2,3,4,5,6$ in that order. We start with region $1$ . There are no restrictions on the color of region $1$ so it can be any of the four colors. We know move on the region $2$ . It can be any color but color used for region $1$ , giving us $3$ choices. Section $3$ is where it gets a bit complicated; we will have to do casework based on whether the color of region $3$ is that of region $1$ or not.
If we have the color of region $3$ being different from that of region $1$ (in which we color do so in $2$ ways), then we have need for another casework at region $4$ . If the color of region $4$ is different from that of region $1$ (which can be achieved in $2$ ways), then we have yet another casework split.
If the color of region $5$ is different from that of region $1$ (which can be done in $2$ ways, then we would have a total of $2$ possible colorings for region $6$ (for it cannot be the color of regions $1$ nor $5$ ). Moving on to the case where the color of section $5$ is the same as that of section $1$ (which can be done in $1$ way), we will have $3$ ways (region $6$ cannot be that color of both region $1$ and $5$ ). Thus, if the color of region $4$ is different of that of region $1$ , then we have $2\cdot 2 + 3 = 7$ ways.
If the color of region $4$ is the same as that of region $1$ (which can be done in one way), then the color of region $5$ have to be different from that of sector $1$ ( $3$ ways). That means there will be $2$ choices for the color of region $6$ . So if the color of region $4$ is the same as region $1$ , then we will have $3\cdot 2 = 6$ . That means if the color of section $3$ is different from that of region $1$ , then there are $2\cdot 7 + 6 = 20$ .
Now, moving on to the case where section $3$ has the same color of region $1$ . That means section $4$ will have to be a different color of that of region $1$ ( $3$ ways). So, that means we have region $5$ to be either the same color or different color as region $1$ . If it is different (which can be done in $2$ ways), then there will be $2$ possibilities on the color of sector $6$ . If it is same (which can be done in $1$ way), then there are $3$ ways to color region $6$ . So, if section $3$ has the same color as section $1$ , then we have $3(2\cdot 2 + 3) = 3(7) = 21$ .
Now, in overall we will have $4\cdot 3 (2(20)+21) = 12(61) = \boxed{732}$ .
The full expansion without the explanation is right here:
\[4\cdot 3(2(2\cdot 7 + 3\cdot 2) + 3(2\cdot 2 + 3)) = 732\]
~sml1809

## Solution 12 (Probability & Expected Value)
Let the top-right segment be segment $1,$ and remaining segments are numbered $2,3,4,5,6$ in clockwise order. We have $4$ choices for segment $1,$ and $3$ choices for segments $2,3,4,5.$ For segment $6,$ we wish to find the expected value of the number of choices for segment $6$ 's color, which depends on whether segment $5$ is red. If we let $P(n)$ denote the probability of segment $P$ being the same color as segment $1$ (for simplicity, denote segment $1$ 's color as red), we get the following recurrence relation: \[P(n)=\dfrac{1-P(n-1)}{3}.\] This is because that you cannot have two reds in a row (hence the $1-P(n-1)$ ) and if segment $n-1$ is not red, there are three possible colors, one of which is red (hence the divide by $3$ ). Using the obvious fact that $P(1)=1$ by the definition of $P(n),$ we find that \[P(5)=\dfrac{7}{27}.\] If segment $5$ is red, then there are three possible colors for segment $6.$ If it is not, there are $2$ possible choices for segment $6.$ This means the expected number of color choices for segment $6$ is \[\dfrac{7}{27}\cdot3+\dfrac{20}{27}\cdot2,\] and the total number of colorings of the ring is \[4\cdot3\cdot3\cdot3\cdot3\cdot\left(\dfrac{7}{27}\cdot3+\dfrac{20}{27}\cdot2\right)=\boxed{732}.\]
~BS2012

## Video Solution
Video Solution: https://www.youtube.com/watch?v=Yndl8HqVkJk
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .