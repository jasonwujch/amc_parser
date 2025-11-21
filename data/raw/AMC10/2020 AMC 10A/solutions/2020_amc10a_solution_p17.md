# 2020 AMC 10A Problem 17

## Problem

Define \[P(x) =(x-1^2)(x-2^2)\cdots(x-100^2).\] How many integers $n$ are there such that $P(n)\leq 0$ ?

$\textbf{(A) } 4900 \qquad \textbf{(B) } 4950\qquad \textbf{(C) } 5000\qquad \textbf{(D) } 5050 \qquad \textbf{(E) } 5100$

## Solution 1 (Casework)
We perform casework on $P(n)\leq0:$
1. $P(n)=0$
1. $P(n)<0$
In this case, there are $100$ such integers $n:$ \[1^2,2^2,3^2,\ldots,100^2.\]
There are $100$ factors in $P(x),$ and we need an odd number of them to be negative. We construct the table below: \[\begin{array}{c|c|c} & & \\ [-2.5ex] \textbf{Interval of }\boldsymbol{x} & \boldsymbol{\#}\textbf{ of Negative Factors} & \textbf{Valid?} \\ [0.5ex] \hline & & \\ [-2ex] \left(-\infty,1^2\right) & 100 & \\ [0.5ex] \left(1^2,2^2\right) & 99 & \checkmark \\ [0.5ex] \left(2^2,3^2\right) & 98 & \\ [0.5ex] \left(3^2,4^2\right) & 97 & \checkmark \\ [0.5ex] \left(4^2,5^2\right) & 96 & \\ [0.5ex] \left(5^2,6^2\right) & 95 & \checkmark \\ [0.5ex] \left(6^2,7^2\right) & 94 & \\ \vdots & \vdots & \vdots \\ [0.75ex] \left(99^2,100^2\right) & 1 & \checkmark \\ [0.5ex] \left(100^2,\infty\right) & 0 & \\ [0.5ex] \end{array}\] Note that there are $50$ valid intervals of $x.$ We count the integers in these intervals: \begin{align*} \left(2^2-1^2-1\right)+\left(4^2-3^2-1\right)+\left(6^2-5^2-1\right)+\cdots+\left(100^2-99^2-1\right)&=\underbrace{\left(2^2-1^2\right)}_{(2+1)(2-1)}+\underbrace{\left(4^2-3^2\right)}_{(4+3)(4-3)}+\underbrace{\left(6^2-5^2\right)}_{(6+5)(6-5)}+\cdots+\underbrace{\left(100^2-99^2\right)}_{(100+99)(100-99)}-50 \\ &=\underbrace{(2+1)+(4+3)+(6+5)+\cdots+(100+99)}_{1+2+3+4+5+6+\cdots+99+100}-50 \\ &=\frac{101(100)}{2}-50 \\ &=5000. \end{align*} In this case, there are $5000$ such integers $n.$
Together, the answer is $100+5000=\boxed{\textbf{(E) } 5100}.$
~PCChess (Solution)
~MRENTHUSIASM (Reformatting)

## Solution 2 (Casework)
Notice that $P(x)$ is nonpositive when $x$ is between $100^2$ and $99^2, 98^2$ and $97^2, \cdots$ , $2^2$ and $1^2$ (inclusive), because there are an odd number of negatives, which means that the number of values equals \[((100+99)(100-99) + 1) + ((98+97)(98-97)+1) + \cdots + ((2+1)(2-1)+1).\] This reduces to \[200 + 196 + 192 + \cdots + 4 = 4(1+2+\cdots + 50) = 4 \cdot\frac{50 \cdot 51}{2} = \boxed{\textbf{(E) } 5100}.\] ~Zeric
~jesselan (Minor Edits)

## Solution 3 (End Behavior)
We know that $P(x)$ is a $100$ -degree function with a positive leading coefficient. That is, $P(x)=x^{100}+ax^{99}+bx^{98}+...+\text{(constant)}$ .
Since the degree of $P(x)$ is even, its end behaviors match. And since the leading coefficient is positive, we know that both ends approach $\infty$ as $x$ goes in either direction, from which \[\lim_{x\to-\infty} P(x)=\lim_{x\to\infty} P(x)=\infty.\] So the first time $P(x)$ is going to be negative is when it intersects the $x$ -axis at an $x$ -intercept and it's going to dip below. This happens at $1^2$ , which is the smallest intercept.
However, when it hits the next intercept, it's going to go back up again into positive territory, we know this happens at $2^2$ . And when it hits $3^2$ , it's going to dip back into negative territory. Clearly, this is going to continue to snake around the intercepts until $100^2$ .
To get the amount of integers below and/or on the $x$ -axis, we simply need to count the integers. For example, the amount of integers in between the $[1^2,2^2]$ interval we got earlier, we subtract and add one. $(2^2-1^2+1)=4$ integers, so there are four integers in this interval that produce a negative result.
Doing this with all of the other intervals, we have \[(2^2-1^2+1)+(4^2-3^2+1)+\cdots+(100^2-99^2+1)=\boxed{\textbf{(E) } 5100}\] from Solution 2's result.
~quacker88

## Solution 4 (Fast)
We know $P(x) \leq 0$ when an odd number of its factors are positive and negative. For example, to make the first factor positive, $x \in [1^2, 2^2]$ . then there will be a even number of positive factors. We would do $2^2 - 1^2 + 1 (\text{inclusive})$ to find all integers that work. In short we can generalize too: \begin{align*} x^2 - (x-1)^2 + 1 &= 2x \\ x^2 - (x^2 - 2x + 1) + 1 &= 2x \\ x^2 - x^2 + 2x - 1 + 1 &= 2x. \\ \end{align*} But remember this only works when $x \in \{2, 4, 6, 8 \cdots 98, 100\}$ because only then will there be a odd amount of positive and negative factors. So we can set $x = 2k$ , for $k \in \{1, 2, 3, 4, \cdots 49, 50\}$ Now we only have to solve: \[\sum_{k=1}^{50}2(2k) = 2\sum_{k = 1}^{50}2k = 4\sum_{k = 1}^{50}k = 4 \cdot \dfrac{(50)(51)}{2} = 2 \cdot (50)(51) = \boxed{\textbf{(E) } 5100}.\] ~Wiselion

## Solution 5 (Fast, Rigorous, No Bashing)
When looking at the question, it should immediately jump out that we need an odd number of terms to be odd. this means that we need to find the number of n such that $(2k+1)^2 \leq n \leq (2k+2)^2$ for some $0 \leq k \leq 49$ such that $k\in \mathbb{Z}/\mathbb{Z}^-$ $\newline$ The number of integers $n$ s.t. $n\in [a,b]$ is $b-a+1$ We want $n\in [(2k+1)^2,(2k+2)^2]$ $\newline$ Thus, it is obvious we want to find $\sum_{k=0}^{49}{((2k+2)^2-(2k+1)^2+1)}$ . $\newline$ If we do some investigation on the term inside the summation, we find that: $\newline$ $(2k+2)^2-(2k+1)^2+1 = (4k^2+8k+4)-(4k^2+4k+1)+1 = 4k+4$ $\newline$ thus: $\sum_{k=0}^{49}{((2k+2)^2-(2k+1)^2+1)} = \sum_{k=0}^{49}{4(k+1)} = 4\sum_{k=0}^{49}{(k+1)} = 4\sum_{k=1}^{50}{k}$ $\newline$ The reason the last step works is that adding 1 inside the summation effectively shifts the bounds up by 1, as it turns k=0 into k=1, and so on. $\newline$ $4\sum_{k=1}^{50}{k} = 4\frac{(50)(51)}{2} = 2(50)(51) = 100(51) = \boxed{\textbf{(E) } 5100}$ $\newline$ ~stereotypicalmathnerd $\newline$ Feel free to make changes/LaTeX optimizations

## Solution 6
Since $P(x)$ starts off at infinity before $x=1^2$ and goes back to infinity after $x=100^2$ , we can draw a sign chart, and notice that every interval that starts where $x$ is the square of an odd number and ends where $x$ is the square of an even number, $P(x)$ is nonpositive. We notice a pattern - from $x=1$ to $x=4$ , there are $4$ integers. From $x=9$ to $x=16$ , there are $8$ integers. So, the number of integers in each interval where $P(x)$ is negative is part of an arithmetic sequence that starts at $4$ and has common difference $4$ . Since there are $50$ such intervals (since every other interval has $P(x)$ be nonpositive), the final number is $200$ . So, the sum of this arithmetic series is $\frac{4+200}{2} \cdot 50 = \boxed{\textbf{(E) } 5100}$ .
~vaishnav

## Solution Visual Aid
Visualization that makes it easier to see solutions:
[asy] size(600); // Draw the main number line (x-axis) draw((-5, 0) -- (5, 0), Arrow); // Line from -10 to 10 with an arrow at the end draw((5, 0) -- (-5, 0), Arrow); // Line from -10 to 10 with an arrow at the end // Add ticks and labels at each integer point from -10 to 10 for (int i = -4; i <= 4; ++i) { if (i != 0) draw((i, -0.1) -- (i, 0.1)); // Tick mark // label(string(i), (i, -0.5), S); // Label each tick below the line } label("$1^2$", (-4, -0.5), S); // Label each tick below the line label("$2^2$", (-3, -0.5), S); // Label each tick below the line label("$3^2$", (-2, -0.5), S); // Label each tick below the line label("$4^2$", (-1, -0.5), S); // Label each tick below the line label("\dots", (0, -0.5), S); // Label each tick below the line label("$97^2$", (1, -0.5), S); // Label each tick below the line label("$98^2$", (2, -0.5), S); // Label each tick below the line label("$99^2$", (3, -0.5), S); // Label each tick below the line label("$100^2$", (4, -0.5), S); // Label each tick below the line label("$0$", (-4, 0.1), N); // Label each tick below the line label("$0$", (-3, 0.1), N); // Label each tick below the line label("$0$", (-2, 0.1), N); // Label each tick below the line label("$0$", (-1, 0.1), N); // Label each tick below the line label("$0$", (1, 0.1), N); // Label each tick below the line label("$0$", (2, 0.1), N); // Label each tick below the line label("$0$", (3, 0.1), N); // Label each tick below the line label("$0$", (4, 0.1), N); // Label each tick below the line label("$+$", (-4.5, 0), N); // Label each tick below the line label("$-$", (-3.5, 0), N); // Label each tick below the line label("$+$", (-2.5, 0), N); // Label each tick below the line label("$-$", (-1.5, 0), N); // Label each tick below the line label("$+$", (4.5, 0), N); // Label each tick below the line label("$-$", (3.5, 0), N); // Label each tick below the line label("$+$", (2.5, 0), N); // Label each tick below the line label("$-$", (1.5, 0), N); // Label each tick below the line [/asy]
### Note
Clearly, there are a finite amount of integers that result in $P(x)$ being nonpositive. This is because there are an even number of factors of $P(x).$ From here, you can read other solutions that count the amount of negative numbers of $P(x).$
~jasmineLOVER7254

## Video Solution (Easy To Follow)
https://www.youtube.com/watch?v=1SFRXR6LbUs&t=4s
~Tips From James Wang

## Video Solution by Pi Academy
https://youtu.be/hqdnNqds2mw?si=dHhmbLrh3pWWIG9T
~ Pi Academy

## Video Solutions
https://youtu.be/3dfbWzOfJAI?t=4026
~ pi_is_3.14
https://youtu.be/zl5rtHnk0rY
~Education, The Study of Everything
https://youtu.be/RKlG6oZq9so
~IceMatrix
https://www.youtube.com/watch?v=YDMMhSguq0w&list=PLeFyQ1uCoINM4D5Lgi5Y3KkfvQuYuIbj
-Walt S.
https://youtu.be/chDmeTQBxq8
~savannahsolver
https://youtu.be/R220vbM_my8?t=463
~ amritvignesh0719062.0
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .