# 2025 AMC 10B Problem 15

## Problem

The sum \[\sum_{k=1}^{\infty} \frac{1}{k^3 + 6k^2 + 8k}\] can be expressed as $\frac{a}{b}$ , where \( a \) and \( b \) are relatively prime positive integers. What is \( a+b \)?

$\textbf{(A)}~89 \qquad \textbf{(B)}~97 \qquad \textbf{(C)}~102 \qquad \textbf{(D)}~107 \qquad \textbf{(E)}~129$

## Solution 1
Through partial sum decomposition we obtain \[\frac{1}{k^3 + 6k^2 + 8k} = \frac{1}{8} \left( \frac{1}{k} - \frac{2}{k+2} + \frac{1}{k+4} \right),\]
so one can write the expression as
\begin{align*} \frac{1}{8} \sum_{k=1}^\infty \left( \frac{1}{k} - \frac{2}{k+2} + \frac{1}{k+4} \right) &= \frac{1}{8} \sum_{k=1}^\infty \left( \frac{1}{k} - \frac{1}{k+2}-\frac{1}{k+2} + \frac{1}{k+4} \right) \\ &= \frac{1}{8} \sum_{k=1}^\infty \left( \frac{1}{k} - \frac{1}{k+2} \right)+ \frac{1}{8} \sum_{k=1}^\infty \left( \frac{1}{k+4} - \frac{1}{k+2} \right) \\ &= \frac{1}{8} \sum_{k=1}^{\infty} \left( \frac{1}{k} - \frac{1}{k+2} \right) - \frac{1}{8} \sum_{k=1}^{\infty} \left( \frac{1}{k+2} - \frac{1}{k+4} \right) \\ &= \frac{1}{8} \sum_{k=1}^{\infty} \left( \frac{1}{k} - \frac{1}{k+2} \right) - \frac{1}{8} \sum_{k=3}^{\infty} \left( \frac{1}{k} - \frac{1}{k+2} \right) \\ &= \frac{1}{8} \sum_{k=1}^{2} \left( \frac{1}{k} - \frac{1}{k+2} \right) \end{align*} Simplifying the sum and multiplying results in $\frac{11}{96}$ , in which we finally have $11 + 96 =$ $\boxed{\textbf{(D)}~107}$
~Pinotation

## Solution 2
We decompose $\frac{1}{k^3 + 6k^2 + 8k}$ into the sum of 3 partial fractions. We can factor $\frac{1}{k^3 + 6k^2 + 8k}$ as $\frac{1}{k(k + 2)(k + 4)}$ . We can write this as $\frac{1}{k(k + 2)(k + 4)} = \frac{A}{k} + \frac{B}{k + 2} + \frac{C}{k + 4}$ . Multiplying this by $k(k + 2)(k + 4)$ gives $1 = A(k + 2)(k + 4) + Bk(k + 4) + Ck(k + 2)$ . If $k = 0$ , then $8A = 1$ , meaning $A = \frac{1}{8}$ , if $k = -2$ , then $B(-2)(2) = -4B = 1$ , meaning $B = -\frac{1}{4}$ , and if $k = -4$ , $8C = 1$ , $C = \frac{1}{8}$ . We have \[\sum_{k=1}^{\infty} \frac{1}{k^3 + 6k^2 + 8k} = \sum_{k = 1}^{\infty} \frac{1/8}{k} - \frac{1/4}{k + 2} + \frac{1/8}{k + 4}.\]
Subtracting the first 2 fractions is
\[\frac{1}{8} (1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots) - \frac{1}{4} (\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \cdots)\] Since $\frac{1}{8}$ is half of $\frac{1}{4}$ , this is equal to $\frac{3}{16} - \frac{1}{8} (\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \cdots)$ . We subtract the third fraction from this.
\[\frac{3}{16} - \frac{1}{8} (\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \cdots) + \frac{1}{8} (\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \cdots) = \frac{3}{16} - \frac{1}{8} (\frac{7}{12}) = \frac{3}{16} - \frac{7}{96} = \frac{11}{96},\]
meaning the answer is $\boxed{\textbf{(D) } 107}$ .
~Toferlamopher

## Solution 3
We can factor the expression as $\sum_{k = 1}^{\infty} \dfrac{1}{k(k+2)(k+4)}$ . Notice we can express this as a telescoping fractions, $\dfrac{1}{k(k+2)(k+4)} = \dfrac{1}{4}\left(\dfrac{1}{k(k+2)}-\dfrac{1}{(k+2)(k+4)}\right)$ , thus the expression becomes, $\dfrac{1}{4}\left(\sum_{k = 1}^{\infty} \left(\dfrac{1}{k(k+2)}-\dfrac{1}{(k+2)(k+4)}\right)\right)$ . Writing out the first few terms where $n$ is a positive integer, we see that the middle cancels, $\dfrac{1}{4}\left(\dfrac{1}{1\cdot3}+\dfrac{1}{2\cdot4}+\dfrac{1}{3\cdot5}+\dots+\dfrac{1}{n(n+2)}-\dfrac{1}{3\cdot5}-\dfrac{1}{4\cdot6}-\dots-\dfrac{1}{(n+1)(n+3)}-\dfrac{1}{(n+2)(n+4)}\right)$ , leaving behind $\dfrac{1}{4}\left(\dfrac{1}{1\cdot3}+\dfrac{1}{2\cdot4}-\dfrac{1}{(n+1)(n+3)}-\dfrac{1}{(n+2)(n+4)}\right)$ . As $n$ goes to infinity, the last two fractions approach zero, thus the sum is $\dfrac{1}{4}\left(\dfrac{1}{3}+\dfrac{1}{8}\right) = \dfrac{1}{4}\left(\dfrac{11}{24}\right) = \dfrac{11}{96}$ , $a = 11$ , $b = 96$ ,
$11+96 = \boxed{\text{(D) }107}.$
~pigwash

## Solution 4 (fast partial fractions)
First, factoring the denominator gives \[\frac{1}{k^3 + 6k^2 + 8k} = \frac{1}{k(k+2)(k+4)}.\]
We now proceed with partial fraction decomposition. There are numerous methods to do this quickly, but one of the fastest is known as the Heaviside cover-up method. We "cover" one of the factors in the denominator and set $k$ equal to whatever value makes that factor zero. By covering up that factor, we ignore the factor that results in division by zero. What results is the numerator of the corresponding partial fraction.
First, we set $k=0$ to find the numerator of $\frac1k.$ We have $\frac{1}{(0+2)(0+4)}=\frac18,$ so this is the numerator for $\frac1k.$ Next, we set $k=-2$ to find the numerator of $\frac{1}{k+2}:$ we see that $\frac{1}{(-2)(-2+4)}=-\frac14$ is thus the numerator for $\frac{1}{k+2}.$ Finally, we set $k=-4,$ giving $\frac{1}{(-4)(-2)}=\frac18.$
Thus, our partial fraction decomposition is \begin{align*}\frac{1}{k^3 + 6k^2 + 8k} &= \frac{1}{k(k+2)(k+4)} \\ &= \frac{1/8}{k} - \frac{1/4}{k+2} + \frac{1/8}{k+4}. \end{align*}
We see that this telescopes. Writing out a few terms, we see:
\begin{align*} \sum_{k=1}^\infty \left( \frac{1}{8}\cdot\frac{1}{k} - \frac{1}{4}\cdot\frac{1}{k+2} + \frac{1}{8}\cdot\frac{1}{k+4} \right) &= \left(\frac{1}{8}\cdot\frac{1}{1} + \frac{1}{8}\cdot\frac{1}{2} + \frac{1}{8}\cdot\frac{1}{3} + \frac{1}{8}\cdot\frac{1}{4} + \frac{1}{8}\cdot\frac{1}{5} + \frac{1}{8}\cdot\frac{1}{6} + \dots\right) \\ &+ \left(\phantom{\frac{1}{8}\cdot\frac{1}{1} + \frac{1}{8}\cdot\frac{1}{2}\;}- \frac{2}{8}\cdot\frac{1}{3} - \frac{2}{8}\cdot\frac{1}{4} - \frac{2}{8}\cdot\frac{1}{5} - \frac{2}{8}\cdot\frac{1}{6} - \dots\right) \\ &+ \left(\phantom{\frac{1}{8}\cdot\frac{1}{1} + \frac{1}{8}\cdot\frac{1}{2} + \frac{1}{8}\cdot\frac{1}{3} + \frac{1}{8}\cdot\frac{1}{4}\;}+ \frac{1}{8}\cdot\frac{1}{5} + \frac{1}{8}\cdot\frac{1}{6} + \dots\right). \end{align*}
We see that the terms telescope, leaving us with a final sum of \[\frac{1}{8}\cdot\frac{1}{1} + \frac{1}{8}\cdot\frac{1}{2} + \frac{1}{8}\cdot\frac{1}{3} + \frac{1}{8}\cdot\frac{1}{4} - \frac{2}{8}\cdot\frac{1}{3} - \frac{2}{8}\cdot\frac{1}{4}=\frac18+\frac1{16}-\frac1{24}-\frac1{32}=\frac{11}{96}.\]
Hence, the answer is $\boxed{\textbf{(D) }107.}$

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=4OuZ6P06J1c ~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .