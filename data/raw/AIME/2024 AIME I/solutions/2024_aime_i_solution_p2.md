# 2024 AIME I Problem 2

## Problem

There exist real numbers $x$ and $y$ , both greater than 1, such that $\log_x\left(y^x\right)=\log_y\left(x^{4y}\right)=10$ . Find $xy$ .

## Solution 1
By properties of logarithms, we can simplify the given equation to $x\log_xy=4y\log_yx=10$ . Let us break this into two separate equations:
\[x\log_xy=10\] \[4y\log_yx=10.\] We multiply the two equations to get: \[4xy\left(\log_xy\log_yx\right)=100.\]
Also by properties of logarithms, we know that $\log_ab\cdot\log_ba=1$ ; thus, $\log_xy\cdot\log_yx=1$ . Therefore, our equation simplifies to:
\[4xy=100\implies xy=\boxed{025}.\]
~Technodoggo

## Solution 2
Convert the two equations into exponents:
\[x^{10}=y^x~(1)\] \[y^{10}=x^{4y}~(2).\]
Take $(1)$ to the power of $\frac{1}{x}$ :
\[x^{\frac{10}{x}}=y.\]
Plug this into $(2)$ :
\[x^{(\frac{10}{x})(10)}=x^{4(x^{\frac{10}{x}})}\] \[{\frac{100}{x}}={4x^{\frac{10}{x}}}\] \[{\frac{25}{x}}={x^{\frac{10}{x}}}=y,\]
So $xy=\boxed{025}$
~alexanderruan

## Solution 3
Similar to solution 2, we have:
$x^{10}=y^x$ and $y^{10}=x^{4y}$
Take the tenth root of the first equation to get
$x=y^{\frac{x}{10}}$
Substitute into the second equation to get
$y^{10}=y^{\frac{4xy}{10}}$
This means that $10=\frac{4xy}{10}$ , or $100=4xy$ , meaning that $xy=\boxed{025}$ .
~MC413551

## Solution 4
The same with other solutions, we have obtained $x^{10}=y^x$ and $y^{10}=x^{4y}$ . Then, $x^{10}y^{10}=y^xx^{4y}$ . So, an obvious solution is to have $x^{10}=x^{4y}$ and $y^{10}=y^{x}$ . Solving, we get $x=10$ and $y=2.5$ .So $xy = \boxed{025}$ .
Change: This is not a correct solution. Plugging in $x=10$ and $y=2.5$ does not satisfy the equations.

## Solution 5(fakesolve)
Using the first expression, we see that $x^{10} = y^x$ . Now, taking the log of both sides, we get $\log_y(x^{10}) = \log_y(y^x)$ . This simplifies to $10 \log_y(x) = x$ . This is still equal to the second equation in the problem statement, so $10 \log_y(x) = x = 4y \log_y(x)$ . Dividing by $\log_y(x)$ on both sides, we get $x = 4y = 10$ . Therefore, $x = 10$ and $y = 2.5$ , so $xy = \boxed{025}$ .
~idk12345678

## Solution 6
Let \[y=x^a\] .We see: \[ax=10\] and \[4x^a/a=10\] which gives rise to \[xy = \boxed{025}\] .
~Grammaticus

## Video Solution
https://youtu.be/qLUahGcewT4
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution
https://youtu.be/6C0yHp5GUBY
~Veer Mahajan

## Video Solution
https://youtu.be/5wHEa9Qwe3k ~Ajeet Dubey ( https://www.ioqm.in )

## Video Solution & More by MegaMath
https://www.youtube.com/watch?v=jxY7BBe-4gU

## Video Solution By MathTutorZhengFrSG
https://youtu.be/HbGlIki_BsY
~MathTutorZhengFrSG
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .