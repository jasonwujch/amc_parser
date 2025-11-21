# 2016 AMC 10B Problem 17

## Problem

All the numbers $2, 3, 4, 5, 6, 7$ are assigned to the six faces of a cube, one number to each face. For each of the eight vertices of the cube, a product of three numbers is computed, where the three numbers are the numbers assigned to the three faces that include that vertex. What is the greatest possible value of the sum of these eight products?

$\textbf{(A)}\ 312 \qquad \textbf{(B)}\ 343 \qquad \textbf{(C)}\ 625 \qquad \textbf{(D)}\ 729 \qquad \textbf{(E)}\ 1680$

## Solution 1
Let us call the six faces of our cube $a,b,c,d,e,$ and $f$ (where $a$ is opposite $d$ , $c$ is opposite $e$ , and $b$ is opposite $f$ . Thus, for the eight vertices, we have the following products: $abc,abe,bcd,bde,acf,cdf,aef,$ and $def$ . Let us find the sum of these products: \[abc+abe+bcd+bde+acf+cdf+aef+def\] We notice $b$ is a factor of the first four terms, and $f$ is a factor of the last four terms. \[b(ac+ae+cd+de)+f(ac+ae+cd+de)\] Now, we can factor even more:
\begin{align*} & (b+f)(ac+ae+cd+de) \\ = &(b+f)(a(c+e)+d(c+e)) \\ = &(b+f)(a+d)(c+e) \end{align*} We have the product. Notice how the factors are sums of opposite faces. The greatest sum possible is $(7+2)$ , $(6+3)$ , and $(5+4)$ all factors. \begin{align*} & (7+2)(6+3)(5+4) \\ = & 9 \cdot 9 \cdot 9 \\ = & 729. \end{align*} Thus our answer is $\boxed{\textbf{(D) }729}$ .

## Solution 2(cheap parity)
We will use parity. If we attempt to maximize this cube in any given way, for example making sure that the sides with 5,6 and 7 all meet at one single corner, the first two answers clearly are out of bounds. Now notice the fact that any three given sides will always meet at one of the eight points. Also note the fact that there are 3 odd numbers. This means that there must be one side that has an odd area! Any odd number added with even numbers is always odd. Given that e) is even, d) is our only choice. Thus our answer is $\boxed{\textbf{(D) }729}$ .

## Solution 3
We first find the factorization $(b+f)(a+d)(c+e)$ using the method in Solution 1. By using AM-GM, we get, $(b+f)(a+d)(c+e) \le \left( \frac{a+b+c+d+e+f}{3} \right)^3$ . To maximize the factorization, we get the answer is $\left( \frac{27}{3} \right)^3 = \boxed{\textbf{(D)}\ 729}$

## Solution 4 (Cheap Solution)
First, we intuitively notice that multiplying large numbers together and smaller numbers together tends to produce larger sums, while multiplying large numbers with smaller numbers tends to produce smaller sums. From this, we guess that it is optimal to have $7, 6,$ and $5$ to be around one vertex to produce at least one large product of $210$ . We can immediately eliminate a) and b) as answer choices since they are very close to this product, as well as e) since it is exactly $8 \cdot 210$ and we know that every following product will be smaller than this. We also guess that that is is most likely optimal to create a pairing where a number and its complement (the number that's the difference of 9 and this number) are on opposite sides. Using these two guesses, we can construct a net of sides and brute force the solution (or estimate) leaving us with $\boxed{\textbf{(D) }729}$ .

## Video Solution by OmegaLearn
https://youtu.be/mgEZOXgIZXs?t=117
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .