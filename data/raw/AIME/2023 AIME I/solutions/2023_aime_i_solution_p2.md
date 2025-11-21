# 2023 AIME I Problem 2

## Problem

Positive real numbers $b \not= 1$ and $n$ satisfy the equations \[\sqrt{\log_b n} = \log_b \sqrt{n} \qquad \text{and} \qquad b \cdot \log_b n = \log_b (bn).\] The value of $n$ is $\frac{j}{k},$ where $j$ and $k$ are relatively prime positive integers. Find $j+k.$

## Solution 1
Denote $x = \log_b n$ . Hence, the system of equations given in the problem can be rewritten as \begin{align*} \sqrt{x} & = \frac{1}{2} x , \\ bx & = 1 + x . \end{align*} Solving the system gives $x = 4$ and $b = \frac{5}{4}$ . Therefore, \[n = b^x = \frac{625}{256}.\] Therefore, the answer is $625 + 256 = \boxed{881}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2
We can use the property that $\log(xy) = \log(x) + \log(y)$ on the first equation. We get $\log_b(bn) = 1 + \log_b(n)$ . Then, subtracting $\log_b(n)$ from both sides, we get $(b-1) \log_b(n) = 1$ , therefore $\log_b(n) = \frac{1}{b-1}$ . Substituting that into our first equation, we get $\frac{1}{2b-2} = \sqrt{\frac{1}{b-1}}$ . Squaring, reciprocating, and simplifying both sides, we get the quadratic $4b^2 - 9b + 5 = 0$ . Solving for $b$ , we get $\frac{5}{4}$ and $1$ . Since the problem said that $b \neq 1$ , $b = \frac{5}{4}$ . To solve for $n$ , we can use the property that $\log_b(n) = \frac{1}{b-1}$ . $\log_\frac{5}{4}(n) = 4$ , so $n = \frac{5^4}{4^4} = \frac{625}{256}$ . Adding these together, we get $\boxed{881}$
~idk12345678

## Solution 3 (quick)
We can let $n=b^{4x^2}$ . Then, in the first equation, the LHS becomes $2x$ and the RHS becomes $2x^2$ . Therefore, $x$ must be $1$ ( $x$ can't be $0$ ). So now we know $n=b^4$ . So we can plug this into the second equation to get $n=b^4$ . This gives $b\cdot4=5$ , so $b= \frac{5}{4}$ and $n= b^4=\frac{625}{256}$ . Adding the numerator and denominator gives $\boxed{881}$ .
Honestly, this problem is kinda well placed.
~yrock

## Video Solution by TheBeautyofMath
https://youtu.be/U96XHH23zhA
~IceMatrix

## Video Solution & More by MegaMath
https://www.youtube.com/watch?v=jxY7BBe-4gU
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .