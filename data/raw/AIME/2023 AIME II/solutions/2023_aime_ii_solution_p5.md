# 2023 AIME II Problem 5

## Problem

Let $S$ be the set of all positive rational numbers $r$ such that when the two numbers $r$ and $55r$ are written as fractions in lowest terms, the sum of the numerator and denominator of one fraction is the same as the sum of the numerator and denominator of the other fraction. The sum of all the elements of $S$ can be expressed in the form $\frac{p}{q},$ where $p$ and $q$ are relatively prime positive integers. Find $p+q.$

## Solution 1
Denote $r = \frac{a}{b}$ , where $gcf\left( a, b \right) = 1$ . We have $55 r = \frac{55a}{b}$ . Suppose $gcf\left( 55, b \right) = 1$ , then the sum of the numerator and the denominator of $55r$ is $55a + b$ . This cannot be equal to the sum of the numerator and the denominator of $r$ , $a + b$ . Therefore, $gcf\left( 55, b \right) \neq 1$ .
Case 1: $b$ can be written as $5c$ with $gcf\left( c, 11 \right) = 1$ .
Thus, $55r = \frac{11a}{c}$ .
Because the sum of the numerator and the denominator of $r$ and $55r$ are the same, \[ a + 5c = 11a + c . \]
Hence, $2c = 5 a$ .
Because $gcf\left( a, b \right) = 1$ , $gcf\left( a, c \right) = 1$ . Thus, $a = 2$ and $c = 5$ . Therefore, $r = \frac{a}{5c} = \frac{2}{25}$ .
Case 2: $b$ can be written as $11c$ with $gcf\left( c, 5 \right) = 1$ .
Thus, $55r = \frac{5a}{c}$ .
Because the sum of the numerator and the denominator of $r$ and $55r$ are the same, \[ a + 11c = 5a + c . \]
Hence, $2a = 5 c$ .
Because $gcf\left( a, b \right) = 1$ , $gcf\left( a, c \right) = 1$ . Thus, $a = 5$ and $c = 2$ . Therefore, $r = \frac{a}{11c} = \frac{5}{22}$ .
Case 3: $b$ can be written as $55 c$ .
Thus, $55r = \frac{a}{c}$ .
Because the sum of the numerator and the denominator of $r$ and $55r$ are the same, \[ a + 55c = a + c . \]
Hence, $c = 0$ . This is infeasible. Thus, there is no solution in this case.
Putting all cases together, $S = \left\{ \frac{2}{25}, \frac{5}{22} \right\}$ . Therefore, the sum of all numbers in $S$ is \[ \frac{2}{25} + \frac{5}{22} = \frac{169}{550} . \]
Therefore, the answer is $169 + 550 = \boxed{\textbf{(719) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
Minor latex edits by T3CHN0B14D3

## Solution 2 (equation with GCDs)
When we simplify a fraction $\frac{a}{b}$ over the integers, we divide the numerator and denominator by $\gcd(a,b).$ So we can clearly see that the fraction $r$ in lowest terms will be \[\frac{\frac{a}{\gcd(a,b)}}{\frac{b}{\gcd(a,b)}}\] and similarly, the fraction $55r$ in lowest terms will be \[\frac{\frac{55a}{\gcd(55a,b)}}{\frac{b}{\gcd(55a,b)}}\]
Now, from the problem's condition, we obtain the following equation: \[\frac{a + b}{\gcd(a,b)} = \frac{55a + b}{\gcd(55a,b)}.\]
Let $\gcd(a,b) = c,$ where $c$ is some positive integer. Then we can write $a$ as $cx$ and $b$ as $cy$ for positive integers $x$ and $y$ such that $\gcd(x,y) = 1.$ Substituting in $cx$ for $a$ and $cy$ for $b$ we get \[\frac{cx + cy}{c} = \frac{55cx + cy}{\gcd(55cx, cy)}\]
which simplifies to
\[x + y = \frac{55x + y}{\gcd(55x,y)}\]
Now, note that since $x$ and $y$ share no common factors, any common factors shared between $55x$ and $y$ must be factors of $55,$ so we can disregard the $x$ in $\gcd(55x,y):$
\[x + y = \frac{55x + y}{\gcd(55,y)}\]
From here we do casework on the possible values of $\gcd(55,y).$ We know that $\gcd(55,y) \in \{1, 5, 11, 55\},$ so we only have to look at four different cases.
Case 1: $\gcd(55,y) = 1:$ This implies \[x + y = 55x + y\] which would make one of the variables $0.$ This case doesn't work.
Case 2: $\gcd(55,y) = 5:$ \[5x + 5y = 55x + y \implies 50x = 4y \implies x = \frac{2}{25}y.\] Since $a = cx$ and $b = cy,$ the value of $r$ is just $\frac{a}{b} = \frac{x}{y},$ so this case gives $\frac{2}{25}$ as a possible value for $r$ .
Case 3: $\gcd(55,y) = 11:$ \[11x + 11y = 55x + y \implies 44x = 10y \implies 22x = 5y \implies r = \frac{5}{22}.\]
Case 4: $\gcd(55,y) = 55:$ \[55x + 55y = 55x + y\] This also makes one of the variables $0$ which we can't have.
So the answer is $\frac{2}{25} + \frac{5}{22} = \frac{169}{550}.$
$169 + 550 = \boxed{719}.$
~ grogg007
### Note
This problem mainly comes down to noticing that $55r$ has to be simplifiable such that the numerator and denominator both change, so they potentially equal their original sum. Then you proceed with casework just as Solution 1.
~BigBrain_2009

## Video Solution by The Power of Logic
https://youtu.be/qUJtReB_9sU
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .