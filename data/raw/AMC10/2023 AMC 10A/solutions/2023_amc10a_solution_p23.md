# 2023 AMC 10A Problem 23

## Problem

If the positive integer $c$ has positive integer divisors $a$ and $b$ with $c = ab$ , then $a$ and $b$ are said to be $\textit{complementary}$ divisors of $c$ . Suppose that $N$ is a positive integer that has one complementary pair of divisors that differ by $20$ and another pair of complementary divisors that differ by $23$ . What is the sum of the digits of $N$ ?

$\textbf{(A) } 9 \qquad \textbf{(B) } 13\qquad \textbf{(C) } 15 \qquad \textbf{(D) } 17 \qquad \textbf{(E) } 19$

## Solution 1
Consider positive integers $a, b$ with a difference of $20$ . Suppose $b = a-20$ . Then, we have $(a)(a-20) = n$ . If there is another pair of two integers that multiply to $n$ but have a difference of 23, one integer must be greater than $a$ , and the other must be smaller than $a-20$ . We can create two cases and set both equal.
We have $(a)(a-20) = (a+1)(a-22) \text{ or } (a+2)(a-21).$ Note that if we go further to $(a+3)(a-20)$ and beyond, that would violate the condition that one of the two integers must be smaller than $a-20.$
Starting with the first case, we have $a^2-20a = a^2-21a-22$ , or $0=-a-22$ , which gives $a=-22$ , which is not possible. The other case is $a^2-20a = a^2-19a-42$ , so $a=42$ . Thus, our product is $(42)(22) = (44)(21)$ , so $n = 924$ . Adding the digits, we have $9+2+4 = \boxed{\textbf{(C) } 15}$ .
-Sepehr2010, mathboy282, the_eaglercraft_grinder

## Solution 2
We have 4 integers in our problem. Let's call the smallest of them $a$ . $a(a+23) =$ either $(a+1)(a+21)$ or $(a+2)(a+22)$ . So, we have the following:
$a^2 + 23a = a^2 + 22a +21$ or
$a^2+23a = a^2 + 24a +44$ .
The second equation has negative solutions, so we discard it. The first equation has $a = 21$ , and so $a + 23 = 44$ . If we check $(a+1)(a+21)$ we get $22 \cdot 42 = 21 \cdot 44$ . $44$ is $2$ times $22$ , and $42$ is $2$ times $21$ , so our solution checks out. Multiplying $21$ by $44$ , we get $924$ => $9 + 2 + 4 = \boxed{\textbf{(C) 15}}$ .
~Arcticturn

## Solution 3 (less words)
From the problems, it follows that
\begin{align*} x(x+20)&=y(y+23) = N\\ x^2+20x&=y^2+23y\\ 4x^2+4\cdot20x &= 4y^2+4\cdot23y\\ 4x^2+4\cdot20x+20^2-20^2 &= 4y^2+4\cdot23y+23^2-23^2\\ (2x+20)^2-20^2 &= (2y+23)^2-23^2\\ 23^2-20^2 &= (2y+23)^2-(2x+20)^2\\ (23+20)(23-20) &= (2y+23+2x+20)(2y+23-2x-20)\\ 43\cdot 3 &= (2y+2x+43)(2y-2x+3)\\ 129\cdot 1 &= (2y+2x+43)(2y-2x+3)\\ \end{align*} Since both $(2y+2x+43)$ and $(2y-2x+3)$ must be integer, we get two equations. \begin{align} 129 \text{ or } 43 &= (2y+2x+43)\\ 1 \text{ or } 3 &= 2y-2x+3\\ \end{align} 43 & 3 yields (0,0) which is not what we want. 129 & 1 yields (22,21) which is more interesting.
Simplifying the equations, we get: \begin{align*} x+y &= 43\\ x-y &= 1\\ x=22&, y=21\\ N &= (22)(22+20) = 924. \end{align*}
So, the answer is $\boxed{\textbf{(C) 15}}$ .
~Technodoggo

## Solution 4
Say one factorization is $n(n+23).$ The two cases for the other factorization are $(n+1)(n+21)$ and $(n+2)(n+22).$ We know it must be the first because of AM-GM intuition: lesser factors of a number are closer together than larger factors of a number. (We can also try both and see which works.) Thus, $n(n+23)=(n+1)(n+21)$ and we find that $n=21,N=924$ meaning the answer is $\boxed{\textbf{(C) }15}.$
~DouDragon

## Solution 5
Since we are given that some pairs of divisors differ by 20 and 23 and we can let the pair be $(x-10)$ and $(x+10)$ as well as $(y-\frac{23}{2})$ and $(y+\frac{23}{2})$ . We also know the product of both the complementary divisors give the same number so $(x-10)(x+10)=(y-\frac{23}{2})(y+\frac{23}{2})$ . Now we let $y=\frac{a}{2}$ . Then we substitute and get $x^2-100=\frac{(a^2-529)}{4}$ . Finally we multiply by 4 and get $4x^2-a^2=-129, a^2-4x^2=129$ . Then we use differences of squares and get $a$ + $2x$ =129, $a$ - $2x$ =1. We finish by getting $a=$ 65 and $x=32$ . So $(42)(22) = 924$ Adding the digits, we have $9+2+4 = \boxed{\textbf{(C) } 15}$ .
~averagejoe
Nunber sense note: To avoid tedious multiplication of 2-digit numbers, observe that $n = (42)(22) = (6)(7)(2)(11)$ , and $(6)(7)(2) = 84$ , and the sum of the digits of $11$ is $2$ , so the sum of the digits of $n$ is equivalent to $(8+4)(2) \equiv 24 \equiv 15 \pmod 9$ . The only equivalent answer choice is $\boxed{15}$ . ~oinava

## Solution 6
$N$ can be written $N = \left( a - 10 \right) \left( a + 10 \right)$ with a positive integer $a > 10$ and $N = \left( \frac{2b + 1}{2} - \frac{23}{2} \right) \left( \frac{2b + 1}{2} + \frac{23}{2} \right)$ with a positive integer $b > 11$ .
The above equations can be reorganized as \[ \left( 2b + 1 + 2 a \right) \left( 2 b + 1 - 2 a \right) = 43 \cdot 3 . \]
The only solution is $2b + 1 + 2a = 129$ and $2b + 1 - 2a = 1$ . Thus, $a = b = 32$ . Therefore, $N = 924$ . So the sum of the digits of $N$ is $9 + 2 + 4 = \boxed{\textbf{(C)}~15}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 7
We can write $N$ as $a(a+20)$ or $b(b+23)$ where $a$ and $b$ are divisors of $N.$ Since $a(a+20) = b(b+23),$ we know that $a^2 + 20a - b^2 - 23b = 0$ , and we can view this as a quadratic in $a.$
Since the solution for $a$ must be an integer, the discriminant for this quadratic must be a perfect square and therefore $20^2 - 4(-b^2 - 23b) = (2c)^2 = 400 + 4b^2 + 92b$ so $b^2 + 23b -c^2 + 100 = 0.$
Since the discriminant of this quadratic in $b$ must also be a perfect square we know that $23^2 - 4(-c^2+100) = d^2$ which we can simplify as $d^2 - 4c^2 = (d-2c)(d+2c) = 129.$ Since they are both positive integers $d - 2c$ and $d + 2c$ are factors of $129 = 3 \cdot 43$ so $d - 2c = 1$ and $d + 2c = 129$ or $d - 2c = 3$ and $d - 2c = 43.$
These systems of equations give us $(c,d) = (32,65)$ and $(c,d) = (10,23)$ respectively, if we plug our values for $c$ into the equation for $b$ we get $b^2 + 23b - 924 = 0$ and $b^2 + 23b = 0$ respectively. The first equation gives us $b = 21$ or $b = -44$ and the second gives us $b = 0$ or $b = -23$ , since $b$ is positive we know that $b = 21$ and $N = (21)(21 + 23) = 924$ , therefore the sum of the digits of $N$ is $9 + 2 + 4 = \boxed{\textbf{(C) 15}}.$
~SailS

## Solution 8 (Trial and Error)
Consider the numbers of the form $a(a+20)$ . Since $b(b+23)$ is always even, $a$ is even. Thus, for $a \ge 2$ , we calculate $a(a+20)$ for even values of $a$ . Then, we check if it can also be represented as a product of numbers that differ by $23$ . Checking, we see that $22 \cdot 42 = 21 \cdot 44 = 924$ works. Thus, the answer is $9 + 2 + 4 = \boxed{\textbf{(C) 15}}$
~andliu766

## Solution 9
$n(n+20)=m(m+23) \Longrightarrow n^2+20n=m^2+23m \Longrightarrow n^2-m^2+20n-20m=3m$ . Factoring, $(n+m)(n-m)+20(n-m)=3m \Longrightarrow (n-m)(n+m+20)=3m$ . Let $n-m=a>0$ because clearly $n>m$ . Then. $a(2m+20+a)=3m$ . Note that since $20+a>0$ , if $a\geq2$ , then the equation is $4m+a(20+a)>3m$ , so $a=1$ . Plugging this back, we get $2m+21=3m \Longrightarrow m=21$ and $n=22$ . Now we find $N$ as $22*42=924$ so the answer is $15$ .
-Magnetoninja

## Solution 10 (Elementary Algebra)
We are given $a(a+20) = b(b+23) = N$ , and we are trying to find $N$ . Simplifying the equation yields
\[a^2+20a=b^2+23b.\]
Completing the square for $a$ , we get
\[(a+10)^2=b^2+23b+100.\]
Now, we will use the squeezing method to find $b$ . We can set a bound on $b^2+23b+100$ :
\[b^2+20b+100<b^2+23b+100<b^2+24b+144.\]
because the expression is bigger than the lower bound by $3b$ and less than the upper bound by $b+44$ . Simplifying gets:
\[(b+10)^2<b^2+23b+100<(b+12)^2.\]
Since we know that the expression is a perfect square, it must be equal to the only square in between $b+10$ and $b+12$ , i.e. $b+11$ :
\[(b+11)^2=b^2+23b+100.\] \[b^2+22b+121=b^2+23b+100\] \[b=21\] Therefore $N=21(21+23)=21(44)=924.$ The sum of the digits is $9+2+4=\boxed{\textbf{(C) 15}}$
~mathwizard123123

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=qPO3xUAoaBPvvkd2&t=5118 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=gxvKNnXX1gjgdkvP&t=8645
~Math-X

## Video Solution ⚡️ 3 min solution ⚡️
https://youtu.be/fuH_b6AieCQ
~Education, the Study of Everything

## Video Solution 1 by OmegaLearn
https://youtu.be/D_T24PrVk18

## Video Solution by epicbird08
https://youtu.be/HrZ3fia7g2A
~EpicBird08

## Video Solution
https://youtu.be/J9VAVT22L40
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .