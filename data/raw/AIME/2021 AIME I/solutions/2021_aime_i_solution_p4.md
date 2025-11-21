# 2021 AIME I Problem 4

## Problem

Find the number of ways $66$ identical coins can be separated into three nonempty piles so that there are fewer coins in the first pile than in the second pile and fewer coins in the second pile than in the third pile.

## Solution 1
Suppose we have $1$ coin in the first pile. Then $(1, 2, 63), (1, 3, 62), \ldots, (1, 32, 33)$ all work for a total of $31$ piles. Suppose we have $2$ coins in the first pile, then $(2, 3, 61), (2, 4, 60), \ldots, (2, 31, 33)$ all work, for a total of $29$ . Continuing this pattern until $21$ coins in the first pile, we have the sum \begin{align*} 31+29+28+26+25+\cdots+4+2+1 &= (31+28+25+22+\cdots+1)+(29+26+23+\cdots+2) \\ &= 176+155 \\ &= \boxed{331}. \end{align*}

## Solution 2
We make an equation: $a+b+c=66,$ where $a<b<c.$ We don't have a clear solution, so we'll try complementary counting. First, let's find where $a\geq b\geq c.$ By stars and bars, we have $\dbinom{65}{2}=2080$ to assign positive integer solutions to $a + b + c = 66.$ Now we need to subtract off the cases where it doesn't satisfy the condition.
We start with $a = b.$ We can write that as $2b + c = 66.$ We can find there are 32 integer solutions to this equation. There are $32$ solutions for $b=c$ and $a = c$ by symmetry. We also need to add back $2$ because we subtracted $(a,b,c)=(22,22,22)$ $3$ times.
We then have to divide by $6$ because there are $3!=6$ ways to order $a, b,$ and $c.$ Therefore, we have $\dfrac{\dbinom{65}{2}-96+2}{6} = \dfrac{1986}{6} = \boxed{331}.$
~Arcticturn

## Solution 3
Let the piles have $a, b$ and $c$ coins, with $0 < a < b < c$ . Then, let $b = a + k_1$ , and $c = b + k_2$ , such that each $k_i \geq 1$ . The sum is then $a + a+k_1 + a+k_1+k_2 = 66 \implies 3a+2k_1 + k_2 = 66$ . This is simply the number of positive solutions to the equation $3x+2y+z = 66$ . Now, we take cases on $a$ .
If $a = 1$ , then $2k_1 + k_2 = 63 \implies 1 \leq k_1 \leq 31$ . Each value of $k_1$ corresponds to a unique value of $k_2$ , so there are $31$ solutions in this case. Similarly, if $a = 2$ , then $2k_1 + k_2 = 60 \implies 1 \leq k_1 \leq 29$ , for a total of $29$ solutions in this case. If $a = 3$ , then $2k_1 + k_2 = 57 \implies 1 \leq k_1 \leq 28$ , for a total of $28$ solutions. In general, the number of solutions is just all the numbers that aren't a multiple of $3$ , that are less than or equal to $31$ .
We then add our cases to get \begin{align*} 1 + 2 + 4 + 5 + \cdots + 31 &= 1 + 2 + 3 + \cdots + 31 - 3(1 + 2 + 3 + \cdots + 10) \\ &= \frac{31(32)}{2} - 3(55) \\ &= 31 \cdot 16 - 165 \\ &= 496 - 165 \\ &= \boxed{331} \end{align*} as our answer.

## Solution 4
Let the first pile have $a$ coins, the second $a+b$ coins, and the third $a+b+c$ coins, where $a$ , $b$ , and $c$ are strictly positive integers. Thus the total number of coins is $3a+2b+c=66$ . Perform the substitution $x=a-1$ , $y=b-1$ , and $z=c-1$ to yield the equation $3x+2y+z=60$ , where $x$ , $y$ , and $z$ are instead nonnegative integers.
From here we can set up the generating function $(x^0+x^3+\cdots+x^{60})(x^0+x^2+\cdots+x^{60})(x^0+x^1+\cdots+x^{60})$ . We need to find the coefficient of $x^{60}$ . Multiplying the second and third polynomials with clever reasoning returns
$(x^0+x^3+\cdots+x^{60})(x^0+x^1+2x^2+2x^3+\cdots+31x^{60}+\cdots+2x^{117}+2x^{118}+x^{119}+x^{120})$
where in the second polynomial, for every two terms, the coefficient increases or decreases by one (depending on which side of the polynomial the term resides).
One can notice here that for every term in the first polynomial there exists one and only one term in the second polynomial that, when multiplied, yield $x^{60}$ . Furthermore, we need only consider the coefficients of the second polynomial.
The corresponding coefficient for $x^{60}$ is $1$ , for $x^{57}$ is $2$ , and for $x^{54}$ is $4$ . We notice the pattern: increase by one, increase by two, and so on. When does this pattern stop? For $x^0$ , the corresponding coefficient is $31$ , and we notice that $31\equiv1\mod3$ . As a result, we know that the pattern has $21$ terms, and we can take advantage of the first $20$ by symmetry.
The answer is simply $10(1+29)+31=\boxed{331}$ .
~eevee9406
Solution 4

## Video Solution
https://youtu.be/f7KtovZ4GAk
~MathProblemSolvingSkills.com

## Video Solution
https://youtu.be/M3DsERqhiDk?t=1073
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .