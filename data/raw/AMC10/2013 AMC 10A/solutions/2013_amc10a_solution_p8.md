# 2013 AMC 10A Problem 8

## Problem

What is the value of \[\frac{2^{2014}+2^{2012}}{2^{2014}-2^{2012}} ?\]

$\textbf{(A)}\ -1 \qquad\textbf{(B)}\ 1 \qquad\textbf{(C)}\ \frac{5}{3} \qquad\textbf{(D)}\ 2013 \qquad\textbf{(E)}\ 2^{4024}$

## Solution
Factoring out, we get: $\frac{2^{2012}(2^2 + 1)}{2^{2012}(2^2-1)}$ .
Cancelling out the $2^{2012}$ from the numerator and denominator, we see that it simplifies to $\boxed{\textbf{(C) }\frac{5}{3}}$ .

## Solution 2
Let $x=2^{2012}$ .
Then the given expression is equal to $\frac{4x+x}{4x-x}=\frac{5x}{3x}=\boxed{\textbf{(C) }\frac{5}{3}}$ .

## Video Solution (CREATIVE THINKING)
https://youtu.be/1ULw0x9XK4o
~Education, the Study of Everything

## Solution 3
We observe that all the answer choices other than $\textbf{(C)}$ are integer.
Claim: $\frac{2^{2014}+2^{2012}}{2^{2014}-2^{2012}}$ is not an integer.
Proof: We know that if $b>a$ and $\operatorname{gcd}(a,b) = a$ , then $a|b$ .
So all we need to prove is that $\operatorname{gcd}(2^{2014}+2^{2012}, 2^{2014}-2^{2012}) \neq 2^{2014}+2^{2012} \text{ or } 2^{2014}-2^{2012}$ . Since the numerator is larger than the denominator, the only possible case is $\gcd(2^{2014}+2^{2012}, 2^{2014}-2^{2012}) = 2^{2014}-2^{2012}$ . We have to prove that this is impossible. Using the Euclidean Algorithm we can simplify to obtain \begin{align*} \gcd(2^{2014}+2^{2012}, 2^{2014}-2^{2012}) &= \gcd(2^{2014}+2^{2012}-2^{2014}+2^{2012}, 2^{2014}-2^{2012})\\ &= \gcd(2 \cdot 2^{2012}, 2^{2014}-2^{2012})\\ &= \gcd(2^{2013}, 2^{2014}-2^{2012}) \end{align*} We notice that $2^{2014}-2^{2012}$ can be factored since $2^{2012}$ is a common factor. Factoring gives us $2^{2014}-2^{2012} = 2^{2012}(2^2-1) = 3 \cdot 2^{2012}$ . From this we know that $3$ is a factor of the original expression. Hence $\gcd(2^{2013}, 2^{2014}-2^{2012}) = \gcd(2^{2013}, 3 \cdot 2^{2012}) = 2^{2013} \neq 2^{2012} \cdot 3$ . So $2^{2014}-2^{2012} \nmid 2^{2014}+2^{2012}$ . So the fraction cannot be simplified into an integer. Hence the answer is the only fraction, $\boxed{\textbf{(C)}}$ .
~JerryZYang

## Video Solution
https://www.youtube.com/watch?v=2vf843cvVzo?t=545
~sugar_rush
https://youtu.be/C3prgokOdHc
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .