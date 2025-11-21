# 2015 AIME I Problem 12

## Problem

Consider all 1000-element subsets of the set $\{1, 2, 3, ... , 2015\}$ . From each such subset choose the least element. The arithmetic mean of all of these least elements is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p + q$ .

### Hint

Use the Hockey Stick Identity in the form

\[\binom{a}{a} + \binom{a+1}{a} + \binom{a+2}{a} + \dots + \binom{b}{a} = \binom{b+1}{a+1}.\]

(This is best proven by a combinatorial argument that coincidentally pertains to the problem: count two ways the number of subsets of the first $(b + 1)$ numbers with $(a + 1)$ elements whose least element is $i$ , for $1 \le i \le b - a + 1$ .)

## Solution 1
Let $M$ be the desired mean. Then because $\dbinom{2015}{1000}$ subsets have 1000 elements and $\dbinom{2015 - i}{999}$ have $i$ as their least element, \begin{align*} \binom{2015}{1000} M &= 1 \cdot \binom{2014}{999} + 2 \cdot \binom{2013}{999} + \dots + 1016 \cdot \binom{999}{999} \\ &= \binom{2014}{999} + \binom{2013}{999} + \dots + \binom{999}{999} \\ & + \binom{2013}{999} + \binom{2012}{999} + \dots + \binom{999}{999} \\ & \dots \\ & + \binom{999}{999} \\ &= \binom{2015}{1000} + \binom{2014}{1000} + \dots + \binom{1000}{1000} \\ &= \binom{2016}{1001}. \end{align*} Using the definition of binomial coefficient and the identity $n! = n \cdot (n-1)!$ , we deduce that \[M = \frac{2016}{1001} = \frac{288}{143}.\] The answer is $\boxed{431}.$
### Potential Inspiration
For solution 1, the inspiration could be that once we select the set $\{a_1, a_2,...,a_{2015}\}$ , where $a_1<a_2<...<a_{2015}$ , we want to multiply each such set by $a_1$ and sum up through all such sets.
So, how do we scale each such set by $a_1$ ? We realize that if we were to choose one more element, specifically, less than $a_1$ , this could be done in $a_1-1$ ways.
Oh! So, now if we add $1$ to all the numbers in our set, they become $\{a_1+1, a_2+1,...,a_{2015}+1\}$ , so the number of ways to pick another number below the least number in this set is $a_1$ !

## Solution 2
Each 1000-element subset $\left\{ a_1, a_2,a_3,...,a_{1000}\right\}$ of $\left\{1,2,3,...,2015\right\}$ with $a_1<a_2<a_3<...<a_{1000}$ contributes $a_1$ to the sum of the least element of each subset. Now, consider the set $\left\{a_1+1,a_2+1,a_3+1,...,a_{1000}+1\right\}$ . There are $a_1$ ways to choose a positive integer $k$ such that $k<a_1+1<a_2+1,a_3+1<...<a_{1000}+1$ ( $k$ can be anything from $1$ to $a_1$ inclusive). Thus, the number of ways to choose the set $\left\{k,a_1+1,a_2+1,a_3+1,...,a_{1000}+1\right\}$ is equal to the sum. But choosing a set $\left\{k,a_1+1,a_2+1,a_3+1,...,a_{1000}+1\right\}$ is the same as choosing a 1001-element subset from $\left\{1,2,3,...,2016\right\}$ !
Thus, the average is $\frac{\binom{2016}{1001}}{\binom{2015}{1000}}=\frac{2016}{1001}=\frac{288}{143}$ . Our answer is $p+q=288+143=\boxed{431}$ .

## Solution 3(NOT RIGOROUS)
Let $p$ be the size of the large set and $q$ be the size of the subset (i.e. in this problem, $p = 2015$ and $q = 1000$ ). We can easily find the answers for smaller values of $p$ and $q$ :
For $p = 2$ and $q = 2$ , the answer is $1$ .
For $p = 3$ and $q = 2$ , the answer is $\frac43$ .
For $p = 4$ and $q = 2$ , the answer is $\frac53$ .
For $p = 3$ and $q = 3$ , the answer is $1$ .
For $p = 4$ and $q = 3$ , the answer is $\frac54$ .
For $p = 5$ and $q = 3$ , the answer is $\frac32$ .
At this point, we can see a pattern: our desired answer is always $\frac{p+1}{q+1}$ . Plugging in $p = 2015$ and $q = 1000$ , the answer is $\frac{2016}{1001}=\frac{288}{143}$ , so $288 + 143 = \boxed{431}$ .

## Solution 4 (short)
In the "average case", the numbers evenly partition the interval [0,2016] into 1001 parts. Then because it asks for the expected value of the least element the answer is $\frac{2016}{1001}$ .
-tigershark22
VIEWER NOTE: This solution doesn't always work, for example, take $n^2$ on $[0,1]$ . The "average case" is $n=\frac{1}{2}\implies n^2=\frac{1}{4}$ but integrating $n^2$ from $0$ to $1$ we see that definitely is not the case. This works only in certain situations, so maybe this solution would be better off with proof that this is one of those situations.

## Solution 5
When it says average, it really just means expected value. Let's do casework.
Our first case is when the smallest number in the subset is $1$ . There are $2014$ numbers to choose from, and $999$ numbers left to choose. So, this contributes $\dbinom{2014}{999}$ to our expected value.
Then, for the smallest number being $2$ , we have $2013$ numbers to choose from and $999$ numbers left to choose. So, this contributes $2\dbinom{2013}{999}$ .
Similarly, the smallest number being $3$ contributes $3\dbinom{2012}{999}$ to our expected value. We keep this up all the way to $1016\dbinom{999}{999}$ .
This makes our sum \[\dbinom{2014}{999} + 2\dbinom{2013}{999} + 3\dbinom{2012}{999} + \cdots + 1016\dbinom{999}{999}.\]
To evaluate this, we can split each binomial into groups of $1$ , like this: $$ (Error compiling LaTeX. Unknown error_msg) \binom{2014}{999} + \binom{2013}{999} + \binom{2013}{999} + \binom{2012}{999} + \binom{2012}{999} + \binom{2012}{999} + \cdots + \underbrace{\binom{999}{999} + \binom{999}{999} + \cdots + \binom{999}{999}}_{\text{1016 $\binom{999}{999}$ 's}}. \[Now, we can turn this into:\] \left( \binom{2014}{999} + \binom{2013}{999} + \cdots + \binom{999}{999} \right) + \left( \binom{2013}{999} + \binom{2012}{999} + \cdots + \binom{999}{999} \right) + \cdots + \left( \binom{1000}{999} + \binom{999}{999} \right) + \binom{999}{999}. \[Now, by the Hockey Stick Identity, we can further simplify this into\] \dbinom{2015}{1000} + \dbinom{2014}{1000} + \cdots + \dbinom{1001}{1000} + \dbinom{1000}{1000}. \[Further simplifying this, we get\] \dbinom{2016}{1001}. $$ (Error compiling LaTeX. Unknown error_msg)
If this is our sum and there are $\dbinom{2015}{1000}$ possible subsets, our average is simply \[\dfrac{\dbinom{2016}{1001}}{\dbinom{2015}{1000}} = \dfrac{2016!}{1001!\,1015!} \times \dfrac{1000!\,1015!}{2015!} = \dfrac{2016}{1001} = \dfrac{288}{143} \Longrightarrow \boxed{431}.\]
-jb2015007

## Video Solution
https://www.youtube.com/watch?v=t-yHTkGkMK4 ~anellipticcurveoverq
### Generalization
https://artofproblemsolving.com/wiki/index.php/1981_IMO_Problems/Problem_2
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .