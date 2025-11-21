# 2019 AMC 10A Problem 19

## Problem

What is the least possible value of \[(x+1)(x+2)(x+3)(x+4)+2019\] where $x$ is a real number?

$\textbf{(A) } 2017 \qquad\textbf{(B) } 2018 \qquad\textbf{(C) } 2019 \qquad\textbf{(D) } 2020 \qquad\textbf{(E) } 2021$

## Solution 1
Grouping the first and last terms and two middle terms gives $(x^2+5x+4)(x^2+5x+6)+2019$ , which can be simplified to $(x^2+5x+5)^2-1+2019$ . Noting that squares are nonnegative, and verifying that $x^2+5x+5=0$ for some real $x$ , the answer is $\boxed{\textbf{(B) } 2018}$ .

## Solution 2 (Fakesolve)
The largest number that makes this expression minimal is \( x = -1 \). This gives 2019, so is the answer 2019? Well, before we jump to conclusions, we need to understand that there may exist a number around or between the interval \( [-1, 0] \) such that this number \( n \) can make a smaller number. This interval is 1 unit long, so our answer is \( 2019 - 1 = \) $\boxed{\textbf{(B) } 2018}$ .
~Pinotation

## Solution 3
Let $a=x+\tfrac{5}{2}$ . Then the expression $(x+1)(x+2)(x+3)(x+4)$ becomes $\left(a-\tfrac{3}{2}\right)\left(a-\tfrac{1}{2}\right)\left(a+\tfrac{1}{2}\right)\left(a+\tfrac{3}{2}\right)$ .
We can now use the difference of two squares to get $\left(a^2-\tfrac{9}{4}\right)\left(a^2-\tfrac{1}{4}\right)$ , and expand this to get $a^4-\tfrac{5}{2}a^2+\tfrac{9}{16}$ .
Refactor this by completing the square to get $\left(a^2-\tfrac{5}{4}\right)^2-1$ , which has a minimum value of $-1$ . The answer is thus $2019-1=\boxed{\textbf{(B) }2018}$ .

## Solution 4 (calculus)
Similar to Solution 1, grouping the first and last terms and the middle terms, we get $(x^2+5x+4)(x^2+5x+6)+2019$ .
Letting $y=x^2+5x$ , we get the expression $(y+4)(y+6)+2019$ . Now, we can find the critical points of $(y+4)(y+6)$ to minimize the function:
$\frac{d}{dy}(y^2+10y+24)=0$
$2y+10=0$
$2y=-10$
$y=-5,0$
To minimize the result, we use $y=-5$ . Hence, the minimum is $(-5+4)(-5+6)=-1$ , so $-1+2019 = \boxed{\textbf{(B) }2018}$ .
Note : We could also have used the result that minimum/maximum point of a parabola $y = ax^2 + bx + c$ occurs at $x=-\frac{b}{2a}$ .
Note 2: This solution is somewhat "lucky", since when we define variables to equal a function, and create another function out of these variables, the domain of such function may vary from the initial one. This is important because the maximum and minimum value of a function is dependent on its domain, e.g:
$f(x)=x^2$ has no maximum value in the the integers, but once restricting the domain to $(-5, 5)$ the maximum value of $f(x)$ is $25$ .
Also, observe that if we were to evaluate this by taking the derivative of $(x+1)(x+2)(x+3)(x+4)+2019$ , we would get $-5$ as the $x$ -value to obtain the minimum $y$ -value of this expression. It can be seen that $-5$ is actually an inflection point, instead of a minimum or maximum.
-Note 2 from Benedict T (countmath1)

## Solution 5(guess with answer choices)
The expression is negative when an odd number of the factors are negative. This happens when $-2 < x < -1$ or $-4 < x < -3$ . Plugging in $x = -\frac32$ or $x = -\frac72$ yields $-\frac{15}{16}$ , which is very close to $-1$ . Thus the answer is $-1 + 2019 = \boxed{\textbf{(B) }2018}$ .

## Solution 6 (using the answer choices)
Answer choices $C$ , $D$ , and $E$ are impossible, since $(x+1)(x+2)(x+3)(x+4)$ can be negative (as seen when e.g. $x = -\frac{3}{2}$ ). Plug in $x = -\frac{3}{2}$ to see that it becomes $2019 - \frac{15}{16}$ , so round this to $\boxed{\textbf{(B) }2018}$ .
We can also see that the limit of the function is at least $-1$ since at the minimum, two of the numbers are less than $1$ , but two are between $1$ and $2$ .

## Solution 7 (also calculus but more convoluted)
We can ignore the $2019$ and consider it later, as it is a constant. By difference of squares, we can group this into $\left((x+2.5)^2-0.5^2\right)\left((x+2.5)^2-1.5^2\right)$ . We pull a factor of $4$ into each term to avoid dealing with decimals:
\[\dfrac{\left((2x+5)^2-1\right)\left((2x+5)^2-9\right)}{16}.\]
Now, we let $a=2x+5$ . Our expression becomes:
\[\dfrac{(a-1)(a-9)}{16}=\dfrac{a^2-10a+9}{16}.\]
Taking the derivative, we get $\dfrac{2a-10}{16}=\dfrac{a-5}8.$ This is equal to $0$ when $a=5$ , and plugging in $a=5$ , we get the expression is equal to $-1$ and therefore our answer is $2019-1=\boxed{\text{(B)}~2018}.$
~Technodoggo

## Video Solutions
https://www.youtube.com/watch?v=Vf2LkM7ExhY by SpreadTheMathLove
https://www.youtube.com/watch?v=Lis8yKT9WXc (less than 2 minutes)
- https://youtu.be/NRa3VnjNVbw - Education, the Study of Everything
- https://www.youtube.com/watch?v=Mfa7j2BoNjI
- https://youtu.be/tIzJtgJbHGc - savannahsolver
- https://youtu.be/3dfbWzOfJAI?t=3319 - pi_is_3.14
- https://youtu.be/GmUWIXXf_uk?t=1134 ~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .