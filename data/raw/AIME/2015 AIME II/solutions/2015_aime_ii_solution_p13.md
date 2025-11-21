# 2015 AIME II Problem 13

## Problem

Define the sequence $a_1, a_2, a_3, \ldots$ by $a_n = \sum\limits_{k=1}^n \sin{k}$ , where $k$ represents radian measure. Find the index of the 100th term for which $a_n < 0$ .

## Solution 1
If $n = 1$ , $a_n = \sin(1) > 0$ . Then if $n$ satisfies $a_n < 0$ , $n \ge 2$ , and \[a_n = \sum_{k=1}^n \sin(k) = \cfrac{1}{\sin{1}} \sum_{k=1}^n\sin(1)\sin(k) = \cfrac{1}{2\sin{1}} \sum_{k=1}^n\cos(k - 1) - \cos(k + 1) = \cfrac{1}{2\sin(1)} [\cos(0) + \cos(1) - \cos(n) - \cos(n + 1)].\] Since $2\sin 1$ is positive, it does not affect the sign of $a_n$ . Let $b_n = \cos(0) + \cos(1) - \cos(n) - \cos(n + 1)$ . Now since $\cos(0) + \cos(1) = 2\cos\left(\cfrac{1}{2}\right)\cos\left(\cfrac{1}{2}\right)$ and $\cos(n) + \cos(n + 1) = 2\cos\left(n + \cfrac{1}{2}\right)\cos\left(\cfrac{1}{2}\right)$ , $b_n$ is negative if and only if $\cos\left(\cfrac{1}{2}\right) < \cos\left(n + \cfrac{1}{2}\right)$ , or when $n \in [2k\pi - 1, 2k\pi]$ . Since $\pi$ is irrational, there is always only one integer in the range, so there are values of $n$ such that $a_n < 0$ at $2\pi, 4\pi, \cdots$ . Then the hundredth such value will be when $k = 100$ and $n = \lfloor 200\pi \rfloor = \lfloor 628.318 \rfloor = \boxed{628}$ .
### Clearer Explanation for the End
Notice that we want $\cos(n+1/2)>\cos(1/2).$
Notice that the only interval in which this is true, is where $-1/2 < n + 1/2 < 1/2.$
Thus, we need $-1<n<0.$ So we have $-1+2\pi k <n <0+2\pi k.$
But we want the 100th solution. Which means $n$ is in between $200\pi - 1 < n < 200 \pi.$ So n = 628.
~mathboy282

## Solution 2
Notice that $a_n$ is the imaginary part of $\sum_{k=1}^n e^{ik}$ , by Euler's formula. Using the geometric series formula, we find that this sum is equal to \[\frac{e^{i(n+1)}-e^i}{e^i-1} = \frac{\cos (n+1) - \cos 1 + i (\sin (n+1) - \sin 1) }{\cos 1 - 1 + i \sin 1}\] We multiply the fraction by the conjugate of the denominator so that we can separate out the real and imaginary parts of the above expression. Multiplying, we have \[\frac{(\cos 1 - 1)(\cos(n+1)-\cos 1) + (\sin 1)(\sin(n+1)-\sin 1) + i((\sin(n+1) - \sin 1)(\cos 1 - 1) - (\sin 1)(\cos(n+1)-\cos 1))}{\cos^2 1 - 2 \cos 1 + 1 + \sin^2 1}\] We only need to look at the imaginary part, which is \[\frac{(\sin(n+1) \cos 1 - \cos(n+1) \sin 1) - \sin 1 \cos 1 + \sin 1 - \sin (n+1) + \sin 1 \cos 1}{2-2 \cos 1} = \frac{\sin n - \sin(n+1) + \sin 1}{2-2 \cos 1}\] Since $\cos 1 < 1$ , $2-2 \cos 1 > 0$ , so the denominator is positive. Thus, in order for the whole fraction to be negative, we must have $\sin (n+1) - \sin n > \sin 1 \implies 2 \cos \left(n + \frac{1}{2} \right) \sin \frac{1}{2} > \sin 1 \implies \cos \left( n + \frac{1}{2} \right) > \frac{\sin 1}{2 \sin{\frac{1}{2}}} = \cos \left(\frac{1}{2} \right),$ by sum to product. This only holds when $n$ is between $2\pi k - 1$ and $2\pi k$ for integer $k$ [continuity proof here], and since this has exactly one integer solution for every such interval, the $100$ th such $n$ is $\lfloor 200\pi \rfloor = \boxed{628}$ .

## Solution 3
Similar to solution 2, we set a complex number $z=\cos 1+i\sin 1$ . We start from $z$ instead of $1$ because $k$ starts from $1$ : be careful.
The sum of $z+z^2+z^3+z^4+z^5\dots=\frac{z-z^{n+1}}{1-z}=\frac{z}{z-1}\left(z^n-1\right)$ .
We are trying to make $n$ so that the imaginary part of this expression is negative.
The argument of $z$ is $1$ . The argument of $z-1$ , however, is a little more tricky. $z-1$ is on a circle centered on $(-1,0)$ with radius $1$ . The change in angle due to $z$ is $1$ with respect to the center, but the angle that $z-1$ makes with the $y$ -axis is $half$ the change, due to Circle Theorems (this intercepted arc is the argument of $z$ ), because the $y$ - axis is tangent to the circle at the origin. So $\text{arg}(z-1)=\frac{\pi+1}{2}$ . Dividing $z$ by $z-1$ subtracts the latter argument from the former, so the angle of the quotient with the $x$ -axis is $\frac{1-\pi}{2}$ .
We want the argument of the whole expression $-\pi<\theta<0$ . This translates into $\frac{-\pi-1}{2}<\text{arg}\left(z^n-1\right)<\frac{\pi-1}{2}$ . $z^n-1$ also consists of points on the circle centered at $(-1,0)$ , so we deal with this argument similarly: the argument of $z^n$ is twice the angle $z^n-1$ makes with the $y$ -axis. Since $z^n-1$ is always negative, $\frac{-3\pi}{2}<\text{arg}\left(z^n-1\right)<\frac{-\pi}{2}$ , and the left bound is the only one that is important. Either way, the line (the line consists of both bounds) makes a $\frac{\pi}{2}-\frac{\pi-1}{2}=\frac{-1}{2}$ angle with the $y$ -axis both ways.
So the argument of $z^n$ must be in the bound $-1<\theta<0$ by doubling, namely the last $z^n$ negative before another rotation. Since there is always one $z^n$ in this category per rotation because $\pi$ is irrational, $n_{100}\equiv z^{628}$ and the answer is $\boxed{628}$ .

## Solution 4
By the product-to-sum formula, \[\sin \frac{1}{2} \sin k = \frac{1}{2} \left[ \cos \left( k - \frac{1}{2} \right) - \cos \left( k + \frac{1}{2} \right) \right].\] Thus, we can make the sum in the problem telescope: \begin{align*} a_n &= \sum_{k = 1}^n \sin k \\ &= \sum_{k = 1}^n \frac{\sin \frac{1}{2} \sin k}{\sin \frac{1}{2}} \\ &= \sum_{k = 1}^n \frac{\cos (k - \frac{1}{2}) - \cos (k + \frac{1}{2})}{2 \sin \frac{1}{2}} \\ &= \frac{(\cos \frac{1}{2} - \cos \frac{3}{2}) + (\cos \frac{3}{2} - \cos \frac{5}{2}) + \dots + (\cos \frac{2n - 1}{2} - \cos \frac{2n + 1}{2})}{2 \sin \frac{1}{2}} \\ &= \frac{\cos \frac{1}{2} - \cos \frac{2n + 1}{2}}{2 \sin \frac{1}{2}}. \end{align*}Then $a_n < 0$ when $\cos \frac{1}{2} < \cos \frac{2n + 1}{2}.$ This occurs if and only if \[2 \pi k - \frac{1}{2} < \frac{2n + 1}{2} < 2 \pi k + \frac{1}{2}\] for some integer $k.$ Equivalently, \[2 \pi k - 1 < n < 2 \pi k.\] In other words, $n = \lfloor 2 \pi k \rfloor.$ The 100th index of this form is then $\lfloor 2 \pi \cdot 100 \rfloor = \boxed{628}.$

## Video Solution
https://youtu.be/b1-cUUPjYNk
~MathProblemSolvingSkills
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .