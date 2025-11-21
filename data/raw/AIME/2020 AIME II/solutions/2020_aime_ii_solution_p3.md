# 2020 AIME II Problem 3

## Problem

The value of $x$ that satisfies $\log_{2^x} 3^{20} = \log_{2^{x+3}} 3^{2020}$ can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
Let $\log _{2^x}3^{20}=\log _{2^{x+3}}3^{2020}=n$ . Based on the equation, we get $(2^x)^n=3^{20}$ and $(2^{x+3})^n=3^{2020}$ . Expanding the second equation, we get $8^n\cdot2^{xn}=3^{2020}$ . Substituting the first equation in, we get $8^n\cdot3^{20}=3^{2020}$ , so $8^n=3^{2000}$ . Taking the 100th root, we get $8^{\frac{n}{100}}=3^{20}$ . Therefore, $(2^{\frac{3}{100}})^n=3^{20}$ , and using the our first equation( $2^{xn}=3^{20}$ ), we get $x=\frac{3}{100}$ and the answer is $\boxed{103}$ . ~rayfish

## Easiest Solution
Recall the identity $\log_{a^n} b^{m} = \frac{m}{n}\log_{a} b$ (which is easily proven using exponents or change of base). Then this problem turns into \[\frac{20}{x}\log_{2} 3 = \frac{2020}{x+3}\log_{2} 3\] Divide $\log_{2} 3$ from both sides. And we are left with $\frac{20}{x}=\frac{2020}{x+3}$ .Solving this simple equation we get \[x = \tfrac{3}{100} \Rightarrow \boxed{103}\] ~mlgjeffdoge21

## Solution 2
Because $\log_a{b^c}=c\log_a{b},$ we have that $20\log_{2^x} 3 = 2020\log_{2^{x+3}} 3,$ or $\log_{2^x} 3 = 101\log_{2^{x+3}} 3.$ Since $\log_a{b}=\dfrac{1}{\log_b{a}},$ $\log_{2^x} 3=\dfrac{1}{\log_{3} 2^x},$ and $101\log_{2^{x+3}} 3=101\dfrac{1}{\log_{3}2^{x+3}},$ thus resulting in $\log_{3}2^{x+3}=101\log_{3} 2^x,$ or $\log_{3}2^{x+3}=\log_{3} 2^{101x}.$ We remove the base 3 logarithm and the power of 2 to yield $x+3=101x,$ or $x=\dfrac{3}{100}.$
Our answer is $\boxed{3+100=103}.$ ~ OreoChocolate

## Solution 3 (Official MAA)
Using the Change of Base Formula to convert the logarithms in the given equation to base $2$ yields \[\frac{\log_2 3^{20}}{\log_2 2^x} = \frac{\log_2 3^{2020}}{\log_2 2^{x+3}}, \text{~ and then ~} \frac{20\log_2 3}{x\cdot\log_2 2} = \frac{2020\log_2 3}{(x+3)\log_2 2}.\] Canceling the logarithm factors then yields \[\frac{20}x = \frac{2020}{x+3},\] which has solution $x = \frac3{100}.$ The requested sum is $3 + 100 = 103$ .

## Solution 4
$\log_{2^x} 3^{20} = 2^{xy} = 3^{20}$
$\log_{2^{x+3}} 3^{2020} = (2^{x+3})^y = 3^{2020}$
$3^{2020} = (3^{20})^{101}$
$(2^{xy})^{101} = (2^{x+3})^y = 3^{2020}$
$(2^{xy})^{101} = (2^{x+3})^y \Rightarrow 2^{101xy} = 2^{xy+3y} \Rightarrow 101xy = xy + 3y \Rightarrow 101xy = y(x+3)$
$101x = x + 3$
$100x = 3$
$x = \frac{3}{100}$
$100 + 3 = \boxed{103}$ ~Airplanes2007

## Video Solution
https://www.youtube.com/watch?v=ZCm0SOjTPVE
~North America Math Contest Go Go Go

## Video Solution
https://youtu.be/lPr4fYEoXi0 ~ CNCM

## Video Solution 2
https://www.youtube.com/watch?v=x0QznvXcwHY?t=528
~IceMatrix

## Video Solution 3
https://youtu.be/-CkEF5nWOaI
~avn

## Video Solution 4
https://www.youtube.com/watch?v=2TSNY2DDUbQ&t=3s ~ MathEx

## Video Solution 5 by OmegaLearn
https://youtu.be/RdIIEhsbZKw?t=1648
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .