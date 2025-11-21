# 2005 AIME II Problem 13

## Problem

Let $P(x)$ be a polynomial with integer coefficients that satisfies $P(17)=10$ and $P(24)=17.$ Given that $P(n)=n+3$ has two distinct integer solutions $n_1$ and $n_2,$ find the product $n_1\cdot n_2.$

## Solution
We define $Q(x)=P(x)-x+7$ , noting that it has roots at $17$ and $24$ . Hence $P(x)-x+7=A(x-17)(x-24)$ . In particular, this means that $P(x)-x-3=A(x-17)(x-24)-10$ . Therefore, $x=n_1,n_2$ satisfy $A(x-17)(x-24)=10$ , where $A$ , $(x-17)$ , and $(x-24)$ are integers. This cannot occur if $x\le 17$ or $x\ge 24$ because the product $(x-17)(x-24)$ will either be too large or not be a divisor of $10$ . We find that $x=19$ and $x=22$ are the only values that allow $(x-17)(x-24)$ to be a factor of $10$ . Hence the answer is $19\cdot 22=\boxed{418}$ .

## Solution 2
We know that $P(n)-(n+3)=0$ so $P(n)$ has two distinct solutions so $P(x)$ is at least quadratic. Let us first try this problem out as if $P(x)$ is a quadratic polynomial. Thus $P(n)-(n+3)= an^2+(b-1)n+(c-3)=0$ because $P(n)=an^2+bn+c$ where $a,b,c$ are all integers. Thus $P(x)=ax^2+bx+c$ where $a,b,c$ are all integers. We know that $P(17)$ or $289a+17b+c=10$ and $P(24)$ or $576a+24b+c=17$ . By doing $P(24)-P(17)$ we obtain that $287a+7b=7$ or $41a+b=1$ or $-41a=b-1$ . Thus $P(n)=an^2- (41a)n+(c-3)=0$ . Now we know that $b=-41a+1$ , we have $289a+17(-41a+1)+c=10$ or $408a=7+c$ which makes $408a-10=c-3$ . Thus $P(n)=an^2-(41a)n+(408a-10)=0$ . By Vieta's formulas, we know that the sum of the roots( $n$ ) is equal to 41 and the product of the roots( $n$ ) is equal to $408-\frac{10}{a}$ . Because the roots are integers $\frac{10}{a}$ has to be an integer, so $a=1,2,5,10,-1,-2,-5,-10$ . Thus the product of the roots is equal to one of the following: $398,403,406,407,409,410,413,418$ . Testing every potential product of the roots, we find out that the only product that can have divisors that sum up to $41$ is $\boxed{418}$ .
-David Camacho

## Solution 3
We have $P(n_1) = n_1+3$ . Using the property that $a - b \mid P(a) - P(b)$ whenever $a$ and $b$ are distinct integers, we get \[n_1 - 17 \mid P(n_1) - P(17) = (n_1+3) - 10 = n_1 - 7,\] and \[n_1 - 24 \mid P(n_1) - P(24) = (n_1+3)-17=n_1-14.\] Since $n_1 - 7 = 10 + (n_1-17)$ and $n_1-14 = 10 + (n_1-24)$ , we must have \[n_1 - 17 \mid 10 \; \text{and} \; n_1-24 \mid 10.\] We look for two divisors of $10$ that differ by $7$ ; we find that $\{2, -5\}$ and $\{5, -2\}$ satisfies these conditions. Therefore, either $n_1 - 24 = -5$ , giving $n_1 = 19$ , or $n_1 - 24 = -2$ , giving $n_1 = 22$ . From this, we conclude that $n_1, n_2 = \boxed{19, 22}$ and that $n_1\cdot n_2=\boxed{418}$ .
~ Alcumus (Solution)
These problems are copyrighted © by the Mathematical Association of America.