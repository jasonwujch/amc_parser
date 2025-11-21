# 2015 AIME I Problem 9

## Problem

Let $S$ be the set of all ordered triple of integers $(a_1,a_2,a_3)$ with $1 \le a_1,a_2,a_3 \le 10$ . Each ordered triple in $S$ generates a sequence according to the rule $a_n=a_{n-1}\cdot | a_{n-2}-a_{n-3} |$ for all $n\ge 4$ . Find the number of such sequences for which $a_n=0$ for some $n$ .

## Solution 1
Let $a_1=x, a_2=y, a_3=z$ . First note that if any absolute value equals 0, then $a_n=0$ . Also note that if at any position, $a_n=a_{n-1}$ , then $a_{n+2}=0$ . Then, if any absolute value equals 1, then $a_n=0$ . Therefore, if either $|y-x|$ or $|z-y|$ is less than or equal to 1, then that ordered triple meets the criteria. Assume that to be the only way the criteria is met. To prove, let $|y-x|>1$ , and $|z-y|>1$ . Then, $a_4 \ge 2z$ , $a_5 \ge 4z$ , and $a_6 \ge 4z^2$ . However, since the minimum values of $a_5$ and $a_6$ are equal, there must be a scenario where the criteria was met that does not meet our earlier scenarios. Calculation shows that to be $z=1$ , $|y-x|=2$ . Again assume that any other scenario will not meet criteria. To prove, divide the other scenarios into two cases: $z>1$ , $|y-x|>1$ , and $|z-y|>1$ ; and $z=1$ , $|y-x|>2$ , and $|z-y|>1$ . For the first one, $a_4 \ge 2z$ , $a_5 \ge 4z$ , $a_6 \ge 8z$ , and $a_7 \ge 16z$ , by which point we see that this function diverges. For the second one, $a_4 \ge 3$ , $a_5 \ge 6$ , $a_6 \ge 18$ , and $a_7 \ge 54$ , by which point we see that this function diverges.
Therefore, the only scenarios where $a_n=0$ is when any of the following are met: $|y-x|<2$ (280 options) $|z-y|<2$ (280 options, 80 of which coincide with option 1) $z=1$ , $|y-x|=2$ . (16 options, 2 of which coincide with either option 1 or option 2) Adding the total number of such ordered triples yields $280+280-80+16-2=\boxed{494}$ .
- Note to author:
Because $a_4 \ge 2z$ , $a_5 \ge 4z$ , $a_6 \ge 8z$ , and $a_7 \ge 16z$ doesn't mean the function diverges. What if $z = 7$ , $a_4 = 60$ , and $a_5 = 30$ too?
- Note to the Note to author:
This isn't possible because the difference between is either 0, 1, or some number greater than 1. If $a_4 = 63\text{, then }a_5$ is either 0, 63, or some number greater than 63 (since it must be a multiple of $z$ ).

## Solution 2
Note that the only way for a $0$ to be produced at $a_n$ is if either $a_{n-1} = 0$ or $a_{n-2} = a_{n-3}$ . Since the first one will eventually get to the first three assuming that there is no $a_{n-2} = a_{n-3}$ for any $n$ , that is not possible because $a_1 , a_2 , a_3 >= 1$ . Therefore, we need $a_{n - 2} = a_{n - 3}$ .
If $2$ consecutive numbers out of $a_1 , a_2 , a_3$ are equal, then those cases work( $a_1$ and $a_2$ or $a_2$ and $a_3$ $\textbf{NOT}$ $a_1$ and $a_3$ ). This is simply $10 \cdot 10 + 10 \cdot 10 - 10 = 190$ by PIE.
Now, note that if any of the first three numbers have difference of $1$ , we have another working case. First, we calculate how many there are given exactly one of $a_1,a_2$ or $a_2,a_3$ have difference $1$ . Given $3$ numbers such that the first $2$ have difference $1$ , exactly $4$ permutations work(assuming the numbers are $x,y,$ and $z$ such that $|x-y| = 1$ ): $x,y,z$ ; $y,x,z$ ; $z,x,y$ ; and $z,y,x$ . If the two consecutive numbers are $1$ and $2$ , then the last number has $7$ possiblities: $4,5,6,\cdots , 10$ . This is symmetric for $9$ and $10$ . If the consecutive numbers are $(2,3),\cdots , (8,9)$ , there are $6$ possibilities( $10$ minus the numbers themselves and the numbers directly above and below). Note that we are not counting any cases already counted in the first case. Therefore, this case gives you $4(7 + 6 * 7 + 7) = 224$ . Now we consider the case that there both adjacent $a$ s have increments of $1$ . \[+1 , +1 \rightarrow 8\] \[-1 , -1 \rightarrow 8\] \[+1 , -1 \rightarrow 9\] \[-1 , +1 \rightarrow 9\] Therefore this gives $224 + 8 + 8 + 9 + 9 = 258$ . However, note that we have to add the case where you have $3$ consecutive numbers in arrangement such that only $2$ consecutive numbers have difference $1$ . For example, $1,3,2$ is one such triple. There are $8$ triples of consecutive numbers and $4$ ways to arrange each one(e.x: $(1,3,2);(3,1,2);(2,1,3);(2,3,1)$ ). This adds on 32 working cases, so this case gives $258 + 32 = 290$ .
Note that there is an ultraspecial(Yes, I know that's not a word) case where we generate a pair of $a_i$ that have difference one. This can only happen if $a_3 = 1$ and $a_1$ and $a_2$ have difference $2$ . This contributes $14$ cases( $2 * 8$ and then subtract $2$ because of the cases $3,1,1$ and $4,2,1$ ).
Therefore, our answer is $190 + 290 + 14 = \boxed{494}$ . Solution by hyxue

## Video Solution
https://youtu.be/nxieVbkk0jY
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .