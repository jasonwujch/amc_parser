# 2002 AMC 12P Problem 10

## Problem

Let $f_n (x) = \text{sin}^n x + \text{cos}^n x.$ For how many $x$ in $[0,\pi]$ is it true that

\[6f_{4}(x)-4f_{6}(x)=2f_{2}(x)?\]

$\text{(A) }2 \qquad \text{(B) }4 \qquad \text{(C) }6 \qquad \text{(D) }8 \qquad \text{(E) more than }8$

## Solution 1
Divide by 2 on both sides to get \[3f_{4}(x)-2f_{6}(x)=f_{2}(x)\] Substituting the definitions of $f_{2}(x)$ , $f_{4}(x)$ , and $f_{6}(x)$ , we may rewrite the expression as \[3(\text{sin}^4{x} + \text{cos}^4{x}) - 2(\text{sin}^6{x} + \text{cos}^6{x}) = 1\] We now simplify each term separately using some algebraic manipulation and the Pythagorean identity.
We can rewrite $3(\text{sin}^4 x + \text{cos}^4 x)$ as $3(\text{sin}^2 x + \text{cos}^2 x)^2 - 6\text{sin}^2 x \text{cos}^2 x$ , which is equivalent to $3 - 6\text{sin}^2 x \text{cos}^2 x$ .
As for $2(\text{sin}^6 x + \text{cos}^6 x)$ , we may factor it as $2(\text{sin}^2 x + \text{cos}^2 x)(\text{sin}^4 x + \text{cos}^4 x - \text{sin}^2 x \text{cos}^2 x)$ which can be rewritten as $2(\text{sin}^4 x + \text{cos}^4 x - \text{sin}^2 x \text{cos}^2 x)$ , and then as $2(\text{sin}^2 x + \text{cos}^2 x)^2 - 6\text{sin}^2 x \text{cos}^2 x$ , which is equivalent to $2 - 6\text{sin}^2 x \text{cos}^2 x$ .
Putting everything together, we have $(3 - 6\text{sin}^2 {x} \text{cos}^2 {x}) - (2 - 6\text{sin}^2 {x} \text{cos}^2 {x}) = 1$ or $1 = 1$ . Therefore, the given equation $3f_{4}(x)-2f_{6}(x)=f_{2}(x)$ is true for all real $x$ , meaning that there are certainly more than $8$ values of $x$ in the interval $[0,\pi]$ that satisfy the given equation, and so the answer is $\boxed{\text{(E) more than }8}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .