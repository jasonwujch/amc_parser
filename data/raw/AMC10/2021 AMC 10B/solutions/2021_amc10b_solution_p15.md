# 2021 AMC 10B Problem 15

## Problem

The real number $x$ satisfies the equation $x+\frac{1}{x} = \sqrt{5}$ . What is the value of $x^{11}-7x^{7}+x^3?$

$\textbf{(A)} ~-1 \qquad\textbf{(B)} ~0 \qquad\textbf{(C)} ~1 \qquad\textbf{(D)} ~2 \qquad\textbf{(E)} ~\sqrt{5}$

## Solution 1
We square $x+\frac{1}{x}=\sqrt5$ to get $x^2+2+\frac{1}{x^2}=5$ . We subtract 2 on both sides for $x^2+\frac{1}{x^2}=3$ and square again, and see that $x^4+2+\frac{1}{x^4}=9$ so $x^4+\frac{1}{x^4}=7$ . We can factor out $x^7$ from our original expression of $x^{11}-7x^7+x^3$ to get that it is equal to $x^7(x^4-7+\frac{1}{x^4})$ . Therefore because $x^4+\frac{1}{x^4}$ is 7, it is equal to $x^7(0)=\boxed{\textbf{(B) } 0}$ .

## Solution 2
Multiplying both sides by $x$ and using the quadratic formula, we get $\frac{\sqrt{5} \pm 1}{2}$ . We can assume that it is $\frac{\sqrt{5}+1}{2}$ , and notice that this is the golden mean $\varphi$ , which is well-known to be a solution the equation $x^2-x-1=0$ , i.e. we have $x^2=x+1$ . Repeatedly using this on the given (you can also just note Fibonacci numbers), \begin{align*} (x^{11})-7x^7+x^3 &= (x^{10}+x^9)-7x^7+x^3 \\ &=(2x^9+x^8)-7x^7+x^3 \\ &=(3x^8+2x^7)-7x^7+x^3 \\ &=(3x^8-5x^7)+x^3 \\ &=(-2x^7+3x^6)+x^3 \\ &=(x^6-2x^5)+x^3 \\ &=(-x^5+x^4+x^3) \\ &=-x^3(x^2-x-1) = \boxed{\textbf{(B) } 0} \end{align*}
~Lcz

## Solution 3
We can immediately note that the exponents of $x^{11}-7x^7+x^3$ are an arithmetic sequence, so they are symmetric around the middle term. So, $x^{11}-7x^7+x^3 = x^7(x^4-7+\frac{1}{x^4})$ . We can see that since $x+\frac{1}{x} = \sqrt{5}$ , $x^2+2+\frac{1}{x^2} = 5$ and therefore $x^2+\frac{1}{x^2} = 3$ . Continuing from here, we get $x^4+2+\frac{1}{x^4} = 9$ , so $x^4-7+\frac{1}{x^4} = 0$ . We don't even need to find what $x^7$ is! This is since $x^7\cdot0$ is evidently $\boxed{\textbf{(B) } 0}$ , which is our answer.
~sosiaops

## Solution 4
We begin by multiplying $x+\frac{1}{x} = \sqrt{5}$ by $x$ , resulting in $x^2+1 = \sqrt{5}x$ . Now we see this equation: $x^{11}-7x^{7}+x^3$ . The terms all have $x^3$ in common, so we can factor that out, and what we're looking for becomes $x^3(x^8-7x^4+1)$ . Looking back to our original equation, we have $x^2+1 = \sqrt{5}x$ , which is equal to $x^2 = \sqrt{5}x-1$ . Using this, we can evaluate $x^4$ to be $5x^2-2\sqrt{5}x+1$ , and we see that there is another $x^2$ , so we put substitute it in again, resulting in $3\sqrt{5}x-4$ . Using the same way, we find that $x^8$ is $21\sqrt{5}x-29$ . We put this into $x^3(x^8-7x^4+1)$ , resulting in $x^3(0)$ , so the answer is $\boxed{(B)~0}$ .
~purplepenguin2

## Solution 5
The equation we are given is $x+\tfrac{1}{x}=\sqrt{5}...$ Yuck. Fractions and radicals! We multiply both sides by $x,$ square, and re-arrange to get \[x^2+1=\sqrt{5}x \implies x^4+2x^2+1=5x^2 \implies x^4-3x^2+1=0.\] Now, let us consider the expression we wish to acquire. Factoring out $x^3,$ we have \[x^3\left(x^8-7x^4+1\right) = x^3\left(x^8+2x^4+1-9x^4\right).\] Then, we notice that $x^8+2x^4+1=\left(x^4+1\right)^2.$ Furthermore, \[x^4+1=3x^2 \implies \left(x^4+1\right)^2=x^8+2x^4+1=9x^4.\] Thus, our answer is \[x^3\left(9x^4-9x^4\right) = x^3 \cdot 0 = \boxed{\textbf{(B)}} ~ 0.\] ~peace09

## Solution 6(Non-rigorous for little time)
Multiplying by x and solving, we get that $x = \frac{\sqrt{5} \pm 1}{2}.$ Note that whether or not we take $x = \frac{\sqrt{5} + 1}{2}$ or we take $\frac{\sqrt{5} - 1}{2},$ our answer has to be the same. Thus, we take $x = \frac{\sqrt{5} - 1}{2} \approx 0.62$ . Since this number is small, taking it to high powers like $11$ , $7$ , and $3$ will make the number very close to $0$ , so the answer is $\boxed{(B)~0}.$ ~AtharvNaphade

## Solution 7
We know that $x+\frac{1}{x}=\sqrt{5}$ . Multiply both sides by $x$ to get $x^2+1=x\sqrt{5}$ Squaring both sides: \[x^4+2x^2+1=5x^2\] Subtract $2x^2$ from both sides: \[x^4+1=3x^2\] Squaring both sides: \[x^8+2x^4+1=9x^4\] Subtract $9x^4$ from both sides: \[x^8-7x^4+1=0\] Multiply $x^3$ on both sides: \[x^{11}-7x^7+x^3=\fbox{(B) 0}\] ~sid2012 [1]

## Solution 8 (very intuitive & efficient)
Squaring $x+\frac{1}{x}=\sqrt{5}$ yields $x^2+2+\frac{1}{x^2}=5$ . We subtract $2$ from both sides, yielding $x^2+\frac{1}{x^2}=3$ , and, squaring again, we end up with $x^4+2+\frac{1}{x^4}=9$ . Subtracting $2$ from both sides again, we end up with $x^4+\frac{1}{x^4}=7$ . Observe that $7$ is the coefficient of the $x^7$ term in our second equation, $x^{11}-7x^{7}+x^3$ . We can now substitute $x^4+\frac{1}{x^4}$ into the second equation to result in $x^{11}-\left(x^4+\frac{1}{x^4}\right)x^{7}+x^3$ . Multiplying the middle term out yields $x^{11}-x^{11}-x^{3}+x^{3}$ , and all of the terms cancel out. Therefore, the answer is $\boxed{(B)~0}.$ ~rxm0203

## Video Solution (Super Fast. 2 min and 9 seconds)
https://youtu.be/CJbtpNhMvIM
~Education, the Study of Everything

## Video Solution (Easiest and Fastest BASIC UNDERSTANDING ONLY Required)
https://www.youtube.com/watch?v=tSTn4K-ZB20

## Video Solution by OmegaLearn
https://youtu.be/M4Ffhp9NLKY?t=81
~ pi_is_3.14

## Video Solution by Interstigation (Simple Silly Bashing)
https://youtu.be/Hdk2SDOcw7c
~ Interstigation

## Video Solution by TheBeautyofMath
Not the most efficient method, but gets the job done.
https://youtu.be/L1iW94Ue3eI?t=1468
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .