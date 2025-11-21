# 2014 AIME I Problem 12

## Problem

Let $A=\{1,2,3,4\}$ , and $f$ and $g$ be randomly chosen (not necessarily distinct) functions from $A$ to $A$ . The probability that the range of $f$ and the range of $g$ are disjoint is $\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m$ .

## Solution 1 (casework)
The natural way to go is casework. And the natural process is to sort $f$ and $g$ based on range size! Via Pigeonhole Principle, we see that the only real possibilities are: $f 1 g 1; f 1 g 2; f 1 g 3; f 2 g 2$ . Note that the $1, 2$ and $1, 3$ cases are symmetrical and we need just a $*2$ . Note also that the total number of cases is $4^4*4^4=4^8$ .
$f 1 g 1$ : clearly, we choose one number as the range for $f$ , one for $g$ , yielding $12$ possibilities.
$f 1 g 2$ with symmetry (WLOG $f$ has 1 element): start by selecting numbers for the ranges. This yields $4$ for the one number in $f$ , and $3$ options for the two numbers for $g$ . Afterwards, note that the function with 2 numbers in the range can have $4+6+4=14$ arrangements of these two numbers (1 of one, 3 of the other *2 and 2 of each). Therefore, we have $2*12*14$ possibilities, the 2 from symmetry.
$f 2 g 2$ : no symmetry, still easy! Just note that we have $6$ choices of which numbers go to $f$ and $g$ , and within each, $14*14=196$ choices for the orientation of each of the two numbers. That's $6*196$ possibilities.
$f 1 g 3$ : again, symmetrical (WLOG $f$ has one element): $4$ ways to select the single element for $f$ , and then find the number of ways to distribute the $3$ distinct numbers in the range for $g$ . The only arrangement for the frequency of each number is ${1, 1, 2}$ in some order. Therefore, we have $3$ ways to choose which number is the one represented twice, and then note that there are $12$ ways to arrange these! The number of possibilities in this situation is $2 * 4 * 3 * 12$ .
Total, divided by $4^8$ , gets $\frac{3 * (1 + 2 * 7^2 + 2^2 * 7 + 2^3 * 3)}{4^7}$ , with numerator $\boxed{453}$ .

## Solution 2 (casework)
We note there are $4^4 = 256$ possibilities for each of $f$ and $g$ from $A$ to $A$ since the input of the four values of each function has four options each for an output value.
We proceed with casework to determine the number of possible $f$ with range 1, 2, etc.
- Range 1:
There are 4 possibilities: all elements output to 1, 2, 3, or 4.
- Range 2:
We have ${{4}\choose {2}} = 6$ ways to choose the two output elements for $f$ . At this point we have two possibilities: either $f$ has 3 of 1 element and 1 of the other, or 2 of each element. In the first case, there are 2 ways to pick the element which there are 3 copies of, and ${{4}\choose {1}} = 4$ ways to rearrange the 4 elements, for a total of $6 * 4 * 2 = 48$ ways for this case. For the second case, there are ${{4}\choose {2}} = 6$ ways to rearrange the 4 elements, for a total of $6 * 6 = 36$ ways for this case. Adding these two, we get a total of $36 + 48 = 84$ total possibilities.
- Range 3:
We have ${{4}\choose {3}} = 4$ ways to choose the three output elements for $f$ . We know we must have 2 of 1 element and 1 of each of the others, so there are 3 ways to pick this element. Finally, there are ${{4}\choose{1}}*{{3}\choose{1}} = 12$ ways to rearrange these elements (since we can pick the locations of the 2 single elements in this many ways), and our total is $4 * 3 * 12 = 144$ ways.
- Range 4:
Since we know the elements present, we have $4!$ ways to arrange them, or 24 ways.
(To check, $4 + 84 + 144 + 24 = 256$ , which is the total number of possibilities).
We now break $f$ down by cases, and count the number of $g$ whose ranges are disjoint from $f$ 's.
- Case 1: $f$ 's range contains 1 element
We know that there are 3 possibilities for $g$ with 1 element. Since half the possibilities for $g$ with two elements will contain the element in $f$ , there are $84/2 = 42$ possibilities for $g$ with 2 elements. Since $3/4$ the possibilities for $g$ with 3 elements will contain the element in $f$ , there are $144/4 = 36$ possibilities for $g$ with 3 elements. Clearly, no 4-element range for $g$ is possible, so the total number of ways for this case to happen is $4(3 + 42 + 36) = 324$ .
- Case 2: $f$ 's range contains 2 elements
We know that there are 2 possibilities for $g$ with 1 element. If $g$ has 2 elements in its range, they are uniquely determined, so the total number of sets with a range of 2 elements that work for $g$ is $84/6 = 14$ . No 3-element or 4-element ranges for $g$ are possible. Thus, the total number of ways for this to happen is $84(2 + 14) = 1344$ .
- Case 3: $f$ 's range contains 3 elements
In this case, there is only 1 possibility for $g$ - all the output values are the element that does not appear in $f$ 's range. Thus, the total number of ways for this to happen is $144$ .
- Summing the cases
We find that the probability of $f$ and $g$ having disjoint ranges is equal to:
$\dfrac{324 + 1344 + 144}{256^2}=\dfrac{1812}{2^{16}}= \dfrac{453}{2^{14}}$
Thus, our final answer is $\boxed{453}$ .

## Solution 3 (simplification of Solution 2)
As before, there are 4 functions with a range of size 1, 84 with a range of size 2, and 144 with a range of size 3. If the range of $f$ has size $k$ , the codomain of $g$ is restricted to a set of size $4 - k$ . Any function from $A$ into this codomain will do, so there are $(4 - k)^4$ possibilities for $g$ given a function $f$ . The probability of $f$ and $g$ having disjoint ranges is then \[\frac{4\cdot 3^4 + 84\cdot 2^4 + 144\cdot 1^4}{(4^4)^2} = \frac{\boxed{453}}{2^{14}}.\]

## Video Solution
https://youtu.be/VFj6JesV93M?si=cDAOday30X0O__4T
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .