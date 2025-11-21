# 2009 AIME II Problem 14

## Problem

The sequence $(a_n)$ satisfies $a_0=0$ and $a_{n + 1} = \frac85a_n + \frac65\sqrt {4^n - a_n^2}$ for $n\geq 0$ . Find the greatest integer less than or equal to $a_{10}$ .

## Solution
### The "obvious" substitution
An obvious way how to get the $4^n$ from under the square root is to use the substitution $a_n = 2^n b_n$ . Then the square root simplifies as follows: $\sqrt{4^n - a_n^2} = \sqrt{4^n - (2^n b_n)^2} = \sqrt{4^n - 4^n b_n^2} = 2^n \sqrt{1 - b_n^2}$ .
The new recurrence then becomes $b_0=0$ and $b_{n+1} = \frac45 b_n + \frac 35\sqrt{1 - b_n^2}$ .

## Solution 1
We can now simply start to compute the values $b_i$ by hand:
\begin{align*} b_1 & = \frac 35 \\ b_2 & = \frac 45\cdot \frac 35 + \frac 35 \sqrt{1 - \left(\frac 35\right)^2} = \frac{24}{25} \\ b_3 & = \frac 45\cdot \frac {24}{25} + \frac 35 \sqrt{1 - \left(\frac {24}{25}\right)^2} = \frac{96}{125} + \frac 35\cdot\frac 7{25} = \frac{117}{125} \\ b_4 & = \frac 45\cdot \frac {117}{125} + \frac 35 \sqrt{1 - \left(\frac {117}{125}\right)^2} = \frac{468}{625} + \frac 35\cdot\frac {44}{125} = \frac{600}{625} = \frac{24}{25} \end{align*}
We now discovered that $b_4=b_2$ . And as each $b_{i+1}$ is uniquely determined by $b_i$ , the sequence becomes periodic. In other words, we have $b_3=b_5=b_7=\cdots=\frac{117}{125}$ , and $b_2=b_4=\cdots=b_{10}=\cdots=\frac{24}{25}$ .
Therefore the answer is
\begin{align*} \lfloor a_{10} \rfloor & = \left\lfloor 2^{10} b_{10} \right\rfloor = \left\lfloor \dfrac{1024\cdot 24}{25} \right\rfloor = \left\lfloor \dfrac{1025\cdot 24}{25} - \dfrac{24}{25} \right\rfloor \\ & = \left\lfloor 41\cdot 24 - \dfrac{24}{25} \right\rfloor = 41\cdot 24 - 1 = \boxed{983} \end{align*}

## Solution 2
After we do the substitution, we can notice the fact that $\left( \frac 35 \right)^2 + \left( \frac 45 \right)^2 = 1$ , which may suggest that the formula may have something to do with the unit circle. Also, the expression $\sqrt{1-x^2}$ often appears in trigonometry, for example in the relationship between the sine and the cosine. Both observations suggest that the formula may have a neat geometric interpretation.
Consider the equation: \[y = \frac45 x + \frac 35\sqrt{1 - x^2}\]
Note that for $t=\sin^{-1} \frac 35$ we have $\sin t=\frac 35$ and $\cos t = \frac 45$ . Now suppose that we have $x=\sin s$ for some $s$ . Then our equation becomes:
\[y=\cos t \cdot \sin s + \sin t \cdot |\cos s|\]
Depending on the sign of $\cos s$ , this is either the angle addition, or the angle subtraction formula for sine. In other words, if $\cos s \geq 0$ , then $y=\sin(s+t)$ , otherwise $y=\sin(s-t)$ .
We have $b_0=0=\sin 0$ . Therefore $b_1 = \sin(0+t) = \sin t$ , $b_2 = \sin(t+t) = \sin (2t)$ , and so on. (Remember that $t$ is the constant defined as $t=\sin^{-1} \frac 35$ .)
This process stops at the first $b_k = \sin (kt)$ , where $kt$ exceeds $\frac{\pi}2$ . Then we'll have $b_{k+1} = \sin(kt - t) = \sin ((k-1)t) = b_{k-1}$ and the sequence will start to oscillate.
Note that $\sin \frac{\pi}6 = \frac 12 < \frac 35$ , and $\sin \frac{\pi}4 = \frac{\sqrt 2}2 > \frac 35$ , hence $t$ is strictly between $\frac{\pi}6$ and $\frac{\pi}4$ . Then $2t\in\left(\frac{\pi}3,\frac{\pi}2 \right)$ , and $3t\in\left( \frac{\pi}2, \frac{3\pi}4 \right)$ . Therefore surely $2t < \frac{\pi}2 < 3t$ .
Hence the process stops with $b_3 = \sin (3t)$ , we then have $b_4 = \sin (2t) = b_2$ . As in the previous solution, we conclude that $b_{10}=b_2$ , and that the answer is $\lfloor a_{10} \rfloor = \left\lfloor 2^{10} b_{10} \right\rfloor = \boxed{983}$ .

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=z5uZ2PGmIUg
### See Also
These problems are copyrighted © by the Mathematical Association of America.