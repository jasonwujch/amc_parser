# 2003 AMC 10A Problem 21

## Problem

Pat is to select six cookies from a tray containing only chocolate chip, oatmeal, and peanut butter cookies. There are at least six of each of these three kinds of cookies on the tray. How many different assortments of six cookies can be selected?

$\mathrm{(A) \ } 22\qquad \mathrm{(B) \ } 25\qquad \mathrm{(C) \ } 27\qquad \mathrm{(D) \ } 28\qquad \mathrm{(E) \ } 729$

## Video Solution
https://youtu.be/3MiGotKnC_U?t=2554

## Solution 1 (Casework)
Let the ordered triplet $(x,y,z)$ represent the assortment of $x$ chocolate chip cookies, $y$ oatmeal cookies, and $z$ peanut butter cookies.
Using casework :
Pat selects $0$ chocolate chip cookies:
Pat needs to select $6-0=6$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(0,6,0); (0,5,1); (0,4,2); (0,3,3); (0,2,4); (0,1,5); (0,0,6)\} \rightarrow 7$ assortments.
Pat selects $1$ chocolate chip cookie:
Pat needs to select $6-1=5$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(1,5,0); (1,4,1); (1,3,2); (1,2,3); (1,1,4); (1,0,5) \} \rightarrow 6$ assortments.
Pat selects $2$ chocolate chip cookies:
Pat needs to select $6-2=4$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(2,4,0); (2,3,1); (2,2,2); (2,1,3); (2,0,4)\} \rightarrow 5$ assortments.
Pat selects $3$ chocolate chip cookies:
Pat needs to select $6-3=3$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(3,3,0); (3,2,1); (3,1,2); (3,0,3)\} \rightarrow 4$ assortments.
Pat selects $4$ chocolate chip cookies:
Pat needs to select $6-4=2$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(4,2,0); (4,1,1); (4,0,2)\} \rightarrow 3$ assortments.
Pat selects $5$ chocolate chip cookies:
Pat needs to select $6-5=1$ more cookies that are either oatmeal or peanut butter.
The assortments are: $\{(5,1,0); (5,0,1)\} \rightarrow 2$ assortments.
Pat selects $6$ chocolate chip cookies:
Pat needs to select $6-6=0$ more cookies that are either oatmeal or peanut butter.
The only assortment is: $\{(6,0,0)\} \rightarrow 1$ assortment.
The total number of assortments of cookies that can be collected is $7+6+5+4+3+2+1=28 \Rightarrow\boxed{\mathrm{(D)}\ 28}$
There is a much faster way to do casework.
Case 1: 1 type of cookie - 3 ways
Case 2: 2 types of cookies - 3 ways to choose the 2 types of cookies, and 5 ways to choose how of each there are 1 and 5 2 and 4 3 and 3 4 and 2 5 and 1
$3*5=15$ cases for case 2
Case 3: 3 types of cookies - quick examination shows us that the only ways to use all three cookies are the following: 4, 1, 1: this gives us 3!/2!*1! = 3 ways 3, 2, 1: this gives us 3! = 6 ways 2, 2, 2: this gives us 1 way total of 10 cases for this case 10+15+3= $28$ total

## Solution 2
It is given that it is possible to select at least 6 of each. Therefore, we can make a bijection to the number of ways to divide the six choices into three categories, since it is assumed that their order is unimportant. Using the ball and urns/sticks and stones/stars and bars formula, the number of ways to do this is $\binom{6+3-1}{3-1}=\binom{8}{2} = 28 \Rightarrow\boxed{\mathrm{(D)}\ 28}$

## Solution 3
Suppose the six cookies to be chosen are the stars, as we attempt to implement stars and bars. We take two dividers, and place them between the cookies, such that the six cookies are split into 3 groups, where the groups are the number of chocolate chip, oatmeal, and peanut butter cookies, and each group can have 0. First, assume that the two dividers cannot go in between the same two cookies. By stars and bars, there are $\dbinom{7}{2}$ ways to make the groups.
Finally, since the two dividers can be together, we must add those cases where the two dividers are in the same space between cookies. There are 7 spaces, and hence 7 cases.
Our final answer is $21+7=\boxed{\mathrm{(D)}\ 28}$

## Solution 4(Alcumus Solution 1)
The numbers of the three types of cookies must have a sum of six. Possible sets of whole numbers whose sum is six are \[0,0,6;\ 0,1,5;\ 0,2,4;\ 0,3,3;\ 1,1,4;\ 1,2,3;\ \ \text{and}\ 2,2,2.\] Every ordering of each of these sets determines a different assortment of cookies. There are 3 orders for each of the sets \[0,0,6;\ 0,3,3;\ \text{and}\ 1,1,4.\] There are 6 orders for each of the sets \[0,1,5;\ 0,2,4;\ \text{and}\ 1,2,3.\] There is only one order for $2,2,2$ . Therefore the total number of assortments of six cookies is $3\cdot 3 + 3\cdot 6 + 1 = 28$ .

## Solution 5(Alcumus Solution 2)
Also known as the ball-and-urn technique. Construct eight slots, six to place the cookies in and two to divide the cookies by type. Let the number of chocolate chip cookies be the number of slots to the left of the first divider, the number of oatmeal cookies be the number of slots between the two dividers, and the number of peanut butter cookies be the number of slots to the right of the second divider. For example, $111\ | \ 11\ | \ 1$ represents three chocolate chip cookies, two oatmeal cookies, and one peanut butter cookie. There are $\binom{8}{2} = \boxed{28}$ ways to place the two dividers, so there are 28 ways to select the six cookies.

## Cheap Solution 6
Notice that the answer will be able to be represented by a choose binomial $\binom{n}{k}$ , where $n$ is a bit greater than six. Looking at the answer choices, we see $\boxed{28}$ .
~yofro

## Solution 7
(NOTE: Variation of other solutions)
Let $a, b,c$ be the number of cookies that we have for each type respectively. Hence:
$a + b + c = 6.$
Via stars and bars, the number of solutions is simply $\tbinom{8}{2} = 28.$
~yk2007

## Solution 8
This is simply a stars and bars situation, where we distribute 6 items among 3 people.
A quick formula for stars and bars problems is $\tbinom{n+k-1}{k-1}$ where we use combinatrics to evaluate after. Using this, we get $\tbinom{8}{2} = 28.$ .
So, the answer is (D) 28.
~MathKatana

## Video Solution by OmegaLearn
https://youtu.be/0W3VmFp55cM?t=4397
~ pi_is_3.14
### Note
This problem is extremely similar to 2001 AMC 10 Problems/Problem 19 .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .