# 2012 AIME II Problem 14

## Problem

In a group of nine people each person shakes hands with exactly two of the other people from the group. Let $N$ be the number of ways this handshaking can occur. Consider two handshaking arrangements different if and only if at least two people who shake hands under one arrangement do not shake hands under the other arrangement. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Given that each person shakes hands with two people, we can view all of these through graph theory as 'rings'. This will split it into four cases: Three rings of three, one ring of three and one ring of six, one ring of four and one ring of five, and one ring of nine. (All other cases that sum to nine won't work, since they have at least one 'ring' of two or fewer points, which doesn't satisfy the handshaking conditions of the problem.)
Case 1: To create our groups of three, there are $\dfrac{\dbinom{9}{3}\dbinom{6}{3}\dbinom{3}{3}}{3!}$ . In general, the number of ways we can arrange people within the rings to count properly is $\dfrac{(n-1)!}{2}$ , since there are $(n-1)!$ ways to arrange items in the circle, and then we don't want to want to consider reflections as separate entities. Thus, each of the three cases has $\dfrac{(3-1)!}{2}=1$ arrangements. Therefore, for this case, there are $\left(\dfrac{\dbinom{9}{3}\dbinom{6}{3}\dbinom{3}{3}}{3!}\right)(1)^3=280$
Case 2: For three and six, there are $\dbinom{9}{6}=84$ sets for the rings. For organization within the ring, as before, there is only one way (i.e. $(3-1)!/2$ )to arrange the ring of three. For six, there is $\dfrac{(6-1)!}{2}=60$ . This means there are $(84)(1)(60)=5040$ arrangements.
Case 3: For four and five, there are $\dbinom{9}{5}=126$ sets for the rings. Within the five, there are $\dfrac{4!}{2}=12$ , and within the group of four there are $\dfrac{3!}{2}=3$ arrangements. This means the total is $(126)(12)(3)=4536$ .
Case 4: For the nine case, there is $\dbinom{9}{9}=1$ arrangement for the ring. Within it, there are $\dfrac{8!}{2}=20160$ arrangements.
Summing the cases, we have $280+5040+4536+20160=30016 \to \boxed{016}$ .
Note: the reason why we divided by $3!$ in Case 1 and not the other three cases is because for case one and case one only, the groups each have 3 people, implying a symmetric configuration.
For example, for 3 people A, B, C in group 1, they could very well be in group 2 or 3 too, because each group has 3 people.
However, for all the other three cases, the configurations are not symmetric and so dividing by $2!$ or like would be incorrect. It is not possible to configure A, B, C such that they can be both a group of 3 and a group of 6, since {A, B, C} only has 3 elements.
~mathboy282

## Solution 2
Let $f_N$ be the number of ways a group of $N$ people can shake hands with exactly two of the other people from the group, where $N \ge 3$ .
We can easily find that $f_3=1$ .
Continuing on, we will label the people as $A$ , $B$ , $C$ ,... corresponding with $N$ .
$f_4$ : There are $\dbinom{3}{2}=3$ possible ways for person $A$ to shake hands with two others (WLOG assume $A$ shakes hands with $B$ and $C$ ), and there is only one possible outcome thereon ( $B$ and $C$ both shakes hands with $D$ ).
Therefore, we can conclude that $f_4=3$
$f_5$ : There are $\dbinom{4}{2}=6$ possible ways for person $A$ to shake hands with two others (WLOG assume they are $B$ and $C$ ). Then, $B$ and $C$ must also shake hands with the remaining two people ( $2$ ways), and those last $2$ people must shake hands with each other ( $1$ way). Therefore, $f_5=\dbinom{4}{2}\ast(2)\ast(1)=12$
$f_6$ : There are $\dbinom{5}{2}=10$ possible ways for person $A$ to shake hands with two others (WLOG assume they are $B$ and $C$ ). However, $B$ and $C$ shake hands with each other, then there are $f_3$ ways for the rest of the people to shake hands. If $B$ and $C$ shake hands with two others out of the three remaining people (3 $\ast$ 2 ways), those $2$ people must shake hands with the last person ( $1$ way). Therefore, $f_6=\dbinom{5}{2}\ast(f_3)+3\ast(2)\ast(1)=70$
Now we have enough information to find $f_9$
$f_9$ : There are $\dbinom{8}{2}=28$ possible ways for person $A$ to shake hands with two others (WLOG assume they are $B$ and $C$ ).
Case 1: $B$ and $C$ shake hands with each other
There are $f_6$ ways for $D$ , $E$ , $F$ , $G$ , $H$ , and $I$ to shake hands
Case 2: $B$ and $C$ shake hands with one of the others out of the $6$ remaining people ( $6$ ways)
There are $f_5$ ways for $E$ , $F$ , $G$ , $H$ , and $I$ to shake hands
Case 3: If $B$ and $C$ shake hands with two different people (there are 6 $\ast$ 5 ways to choose the people but WLOG assume they are $D$ and $E$ ). Calculations of Case 3 are in its subcases.
Subcase 3.1: $D$ and $E$ shake hands with each other There are $f_4$ ways for $F$ , $G$ , $H$ , and $I$ to shake hands
Subcase 3.2: $D$ and $E$ each shake hands with one other person (there are $4$ ways to choose the person, WLOG let that be $F$ ) There are $f_3$ ways for $G$ , $H$ , and $I$ to shake hands
Subcase 3.3: $D$ and $E$ each shake hands with two different people (there are 4 $\ast$ 3 ways, WLOG let that be $F$ and $G$ ) There are $2\ast1$ ways for $F$ and $G$ to then shake hands with $H$ and $I$ , and $H$ and $I$ will shake hands with each other.
We have
\begin{align*} 28(f_6+6\ast(f_5)+6\ast(5)\ast(f_4)+4\ast(f_3)+4\ast(3)\ast(2)\ast(1) &= 28(70+6\ast(12)+6\ast(5)\ast(3+4\ast(1)+4\ast(3)\ast(2)\ast(1) \\ &= 30016 \end{align*}
which gives us the answer of $\boxed{016}$
~ Danielzh

## Video Solution
Very Neat solution: https://www.youtube.com/watch?v=lG8N9RuI-8o
### Similar Problems
2006 HMMT feb. combo #9.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .