# 2011 AIME II Problem 6

## Problem

Define an ordered quadruple of integers $(a, b, c, d)$ as interesting if $1 \le a<b<c<d \le 10$ , and $a+d>b+c$ . How many interesting ordered quadruples are there?

## Solution 1
Rearranging the inequality we get $d-c > b-a$ . Let $e = 11$ , then $(a, b-a, c-b, d-c, e-d)$ is a partition of 11 into 5 positive integers or equivalently: $(a-1, b-a-1, c-b-1, d-c-1, e-d-1)$ is a partition of 6 into 5 non-negative integer parts. Via a standard stars and bars argument, the number of ways to partition 6 into 5 non-negative parts is $\binom{6+4}4 = \binom{10}4 = 210$ . The interesting quadruples correspond to partitions where the second number is less than the fourth. By symmetry, there are as many partitions where the fourth is less than the second. So, if $N$ is the number of partitions where the second element is equal to the fourth, our answer is $(210-N)/2$ .
We find $N$ as a sum of 4 cases:
- two parts equal to zero, $\binom82 = 28$ ways,
- two parts equal to one, $\binom62 = 15$ ways,
- two parts equal to two, $\binom42 = 6$ ways,
- two parts equal to three, $\binom22 = 1$ way.
Therefore, $N = 28 + 15 + 6 + 1 = 50$ and our answer is $(210 - 50)/2 = \fbox{080}$

## Solution 2
Let us consider our quadruple $(a,b,c,d)$ as the following image $xaxbcxxdxx$ . The location of the letter $a$ , $b$ , $c$ , $d$ represents its value and $x$ is a place holder. Clearly the quadruple is interesting if there are more place holders between $c$ and $d$ than there are between $a$ and $b$ .
$0$ holders between $a$ and $b$ means we consider $a$ and $b$ as one unit $ab$ and $c$ as $cx$ yielding $\binom83 = 56$ ways;
$1$ holder between $a$ and $b$ means we consider $a$ and $b$ as one unit $axb$ and $c$ as $cxx$ yielding $\binom 63 = 20$ ways;
$2$ holders between $a$ and $b$ means we consider $a$ and $b$ as one unit $axxb$ and $c$ as $cxxx$ yielding $\binom43 = 4$ ways.
Since there cannot be $3$ holders between $a$ and $b$ so our total is $56+20+4=\fbox{080}$ .

## Solution 3 (Slightly bashy)
We first start out when the value of $a=1$ .
Doing casework, we discover that $d=5,6,7,8,9,10$ . We quickly find a pattern.
Now, doing this for the rest of the values of $a$ and $d$ , we see that the answer is simply:
$(1)+(2)+(1+3)+(2+4)+(1+3+5)+(2+4+6)+(1)+(2)+(1+3)+(2+4)$ $+(1+3+5)+(1)+(2)+(1+3)+(2+4)+(1)+(2)+(1+3)+(1)+(2)+(1)=\boxed{080}$

## Solution 4 (quick)
Notice that if $a+d>b+c$ , then $(11-a)+(11-d)<(11-b)+(11-c)$ , so there is a bijection between the number of ordered quadruples with $a+d>b+c$ and the number of ordered quadruples with $a+d<b+c$ .
Quick counting gives that the number of ordered quadruples with $a+d=b+c$ is 50. To count this, consider our numbers $1, 2, 3, 4, 5, 6, 7, 8, 9, 10$ . Notice that if, for example, $a+d=b+c=8$ , that the average of $a,d$ and $b,c$ must both be $4$ . In this way, there is a symmetry for this case, centered at $4$ . If instead, say, $a+d=b+c=7$ , an odd number, then there is symmetry with $(a,d);(b,c)$ about $3.5$ . Further, the number of cases for each of these centers of symmetry correspond to a triangular number. Eg centered at $2.5,3,8,8.5$ , there is $1$ case for each and so on, until centered at $5.5$ , there are $10$ possible cases. Adding these all, we have $2(1+3+6)+10=50$ .
Thus the answer is $\frac{\binom{10}{4}-50}{2} = \boxed{080}.$

## Solution 5
Think about a,b,c,and d as distinct objects, that we must place in 4 of 10 spaces. However, in only 1 of 24 of these combinations, will the placement of these objects satisfy the condition in the problem. So we know the total number of ordered quadruples is $(10*9*8*7/24)=210$
Next, intuitively, the number of quadruples where $a+d>b+c$ is equal to the number of quadruples where $a+d<b+c$ . So we need to find the number of quadruples where the two quantities are equal. To do this, all we have to do is consider the cases when $a-d$ ranges from 3 to 9. It would seem natural that a range of 3 would produce 1 option, and a range of 4 would produce 2 options. However, since b and c cannot be equal, a range of 3 or 4 produces 1 option each, a range of 5 or 6 produces 2 options each, a range of 7 or 8 produces 3 options each, and a range of 9 will produce 4 options. In addition, a range of n has 10-n options for combinations of a and d. Multiplying the number of combinations of a and d by the corresponding number of options for b and c gives us 50 total quadruplets where $a+d=b+c$ .
So the answer will be $\frac{210-50}{2} = \boxed{080}.$

## Solution 6
Let $b = a+x$ and $c = a+x+y$ and $d = a+x+y+z$ for positive integers $x,y,z.$ In order to satisfy the other condition we need $z > x$ so we let $z = x+k.$ Now the only other condition we need to satisfy so $a+2x+y+k \le 10.$ This condition can be transformed into $a+2x+y+k+b = 11$ for positive $a,x,y,k,b.$ Now we use generating functions to finish. We find the generating function of the whole expression is $(x + x^2 + \cdots)^4 \cdot (x^2+x^4 + \cdots)$ and we are looking for the $x^{11}$ coefficient. This simplifies to finding the $x^5$ coefficient of $(1+x+\cdots)^4 \cdot (1+x^2+\cdots) =\frac{1}{(1-x)^4} \cdot\frac{1}{1+x}.$ Now this expression simplifies to \[\left(\binom{4}{4}+\binom{5}{4} + \cdots +\binom{4+k}{4}x^k\right)(1-x+x^2-x^3 \cdots).\] The $x^5$ coefficient ends up to be $\binom{9}{4} -\binom{8}{4} +\binom{7}{4} -\binom{6}{4} +\binom{5}{4} -\binom{4}{4} = 126 - 70 + 35 - 15 + 5 - 1 = \boxed{080}.$

## Solution 7 (Slightly Slower)
First, let $a=1$ and $d=10$ . If $b=2$ , then $c$ can be from $3$ to $8$ . If $b=3$ , then $4$ to $7$ . If $b=4$ , then $c$ is between $5$ and $6$ . We find a pattern that whenever $b$ increases by $1$ , when $a$ and $d$ are stationary, then the possible values of $c$ decrease by 2, unless it gets to zero or negative, in which case that case ends. Counting up, we have $6+4+2=12$ different possibilities when $a=1$ and $d=10$ . For $a=1$ and $d=9$ , $b=2$ , then $c$ can be from $3$ to $7$ . If $b=3$ , then $c$ can be from $4$ to $6$ , and so on. Notice that the possible values for each case of $b$ gets one less than if $d$ were one greater, unless that number is zero, in which it stays zero. We then use this pattern to find all the values: $12+9+6+4+2+1+9+6+4+2+1+6+4+2+1+4+2+1+2+1+1 \Rightarrow \\ 12\cdot1+9\cdot2+6\cdot3+4\cdot4+2\cdot5+1\cdot6= \\ 12+18+18+16+10+6=\boxed{\textbf{080}}.$
~ SweetMango77
### Note
Note that the first value of each of the rows, if we arrange them based on values of $a$ , is deleted after each row.

## Solution 8
Rearranging the equation obtains $b-a<d-c$ . Let $a-0=e_0$ , $b-a=e_3+e_1$ , $c-b=e_2$ , $d-c=e_3$ , $11-d=e_4$ . Add up all of these newly defined equations to obtain $e_0+e_1+e_2+2e_3+e_4=11$ . Note that since all $e_n$ were defined to be $e_n\ge1$ , to form our stars and bars argument we can let $d_n+1=e_n$ for all $n$ . Then we obtain $d_0+d_1+d_2+2d_3+d_4=5$ where $d_n$ is nonnegative. Now, we can move the $2d_3$ term to the other side and perform casework.
If $2d_3=0$ : 5 objects for 4 variables -> $\binom{8}{3}$
If $2d_3=2$ : 3 objects for 4 variables -> $\binom{6}{3}$
If $2d_3=4$ : 1 object for 4 variables -> $\binom{4}{3}$
Adding all of these cases up, we get $56+20+4=\boxed{080}$ as our requested answer.
~sigma
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .