# 2012 AMC 10A Problem 17

## Problem

Let $a$ and $b$ be relatively prime positive integers with $a>b>0$ and $\dfrac{a^3-b^3}{(a-b)^3} = \dfrac{73}{3}$ . What is $a-b$ ?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 3\qquad\textbf{(D)}\ 4\qquad \textbf{(E)}\ 5$

## Solution 1 (Quick Insight)
Since $a$ and $b$ are relatively prime, $a^3-b^3$ and $(a-b)^3$ are both integers as well. Then, for the given fraction to simplify to $\frac{73}{3}$ , the denominator $(a-b)^3$ must be a multiple of $3.$ Thus, $a-b$ is a multiple of $3$ . Looking at the answer choices, the only multiple of $3$ is $\boxed{\textbf{(C)}\ 3}$ .

## Solution 2
Using difference of cubes in the numerator and cancelling out one $(a-b)$ in the numerator and denominator gives $\frac{a^2 + ab + b^2}{a^2 - 2ab + b^2} = \frac{73}{3}$ .
Set $x = a^2 + b^2$ , and $y = ab$ . Then $\frac{x + y}{x - 2y} = \frac{73}{3}$ . Cross multiplying gives $3x + 3y = 73x - 146y$ , and simplifying gives $\frac{x}{y} = \frac{149}{70}$ . Since $149$ and $70$ are relatively prime, we let $x = 149$ and $y = 70$ , giving $a^2 + b^2 = 149$ and $ab = 70$ . Since $a>b>0$ , the only solution is $(a,b) = (10, 7)$ , which can be seen upon squaring and summing the various factor pairs of $70$ .
Thus, $a - b = \boxed{\textbf{(C)}\ 3}$ .
Remarks:
An alternate method of solving the system of equations involves solving the second equation for $a$ , by plugging it into the first equation, and solving the resulting quartic equation with a substitution of $u = b^2$ . The four solutions correspond to $(\pm10, \pm7), (\pm7, \pm10).$
Also, we can solve for $a-b$ directly instead of solving for $a$ and $b$ : $a^2-2ab+b^2=149-2(70)=9 \implies a-b=3.$
Note that if you double $x$ and double $y$ , you will get different (but not relatively prime) values for $a$ and $b$ that satisfy the original equation.

## Solution 3
The first step is the same as above which gives $\frac{a^2+ab+b^2}{a^2-2ab+b^2}=\frac{73}{3}$ .
Then we can subtract $3ab$ and then add $3ab$ to get $\frac{a^2-2ab+b^2+3ab}{a^2-2ab+b^2}=\frac{73}{3}$ , which gives $1+\frac{3ab}{(a-b)^2}=\frac{73}{3}$ . $\frac{3ab}{(a-b)^2}=\frac{70}{3}$ . Cross multiply $9ab=70(a-b)^2$ . Since $a>b$ , take the square root. $a-b=3\sqrt{\frac{ab}{70}}$ . Since $a$ and $b$ are integers and relatively prime, $\sqrt{\frac{ab}{70}}$ is an integer. $ab$ is a multiple of $70$ , so $a-b$ is a multiple of $3$ . Therefore $a=10$ and $b=7$ is a solution. So $a-b=\boxed{\textbf{(C)}\ 3}$
Note:
From $9ab=70(a-b)^2$ , the Euclidean Algorithm gives $\gcd(a-b,a)=\gcd(a-b,b)=1$ . Thus $(a-b)^2$ is relatively prime to $ab$ , and clearly $9$ and $70$ are coprime as well. The solution must therefore be $(a-b)^2=9 \rightarrow a-b=\boxed{\textbf{(C)}\ 3}$ and $ab=70$ .

## Solution 4
Slightly expanding, we have that $\frac{(a-b)(a^2+ab+b^2)}{(a-b)(a-b)(a-b)}=\frac{73}{3}$ .
Canceling the $(a-b)$ , cross multiplying, and simplifying, we obtain that
$0=70a^2-149ab+70b^2$ . Dividing everything by $b^2$ , we get that
$0=70\left(\frac{a}{b}\right)^2-149\left(\frac{a}{b} \right)+70$ .
Applying the quadratic formula....and following the restriction that $a>b>0$ ....
$\frac{a}{b}=\frac{10}{7}$ .
Hence, $7a=10b$ .
Since they are relatively prime, $a=10$ , $b=7$ .
$10-7=\boxed{\textbf{(C)}\ 3}$ .

## Solution 5
Note that the denominator, when simplified, gets $3.$ We now have to test the answer choices. If one has a good eye or by simply testing the answer choices the answer will be clearly $\boxed{\textbf{(C)}\ 3}$ ~mathboy282

## Solution 6
Let us rewrite the expression as $\frac{(a-b)^2 + 3ab}{(a-b)^2}$ . Now letting $x = a - b$ , we simplify the expression to $\frac{70x^2 + 3ab}{x^2} = \frac{73}{3}$ . Cross multiplying and doing a bit of simplification, we obtain that $ab = \frac{70x^2}{9}$ . Since $a$ and $b$ are both integers, we know that $\frac{70x^2}{9}$ has to be an integer. Experimenting with values of $x$ , we get that $x = 3$ which means $ab = 70$ . We could prime factor from here to figure out possible values of $a$ and $b$ , but it is quite obvious that $a = 10$ and $b=7$ , so our desired answer is $\boxed{\textbf{(C)}\ 3}$ ~triggod

## Solution 7
We expand difference of cubes and cancel $a-b$ from the numerator and denominator and see that $\dfrac{a^2-ab+b^2}{(a-b)^2}=\dfrac{73}3.$ Obviously, we can not equate the numerator and denominator quite yet since that would imply that $a-b$ is irrational ( $\sqrt3$ ). We try the easiest thing to make $\dfrac{73}3$ 's denominator a square: simply multiply by $\dfrac33,$ giving $\dfrac{219}9.$ Setting the denominators to be equal, we see that $(a-b)^2=9\implies a-b=3.$
~ Technodoggo

## Video Solution by OmegaLearn
https://youtu.be/ZWqHxc0i7ro?t=417
~ pi_is_3.14

## Video Solution
https://youtu.be/8SXVrlH71jk
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .