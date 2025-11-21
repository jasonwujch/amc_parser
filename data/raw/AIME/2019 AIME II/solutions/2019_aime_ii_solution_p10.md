# 2019 AIME II Problem 10

## Problem

There is a unique angle $\theta$ between $0^{\circ}$ and $90^{\circ}$ such that for nonnegative integers $n$ , the value of $\tan{\left(2^{n}\theta\right)}$ is positive when $n$ is a multiple of $3$ , and negative otherwise. The degree measure of $\theta$ is $\tfrac{p}{q}$ , where $p$ and $q$ are relatively prime integers. Find $p+q$ .

## Solution 1
Note that if $\tan \theta$ is positive, then $\theta$ is in the first or third quadrant, so $0^{\circ} < \theta < 90^{\circ} \pmod{180^{\circ}}$ .
Furthermore, the only way $\tan{\left(2^{n}\theta\right)}$ can be positive for all $n$ that are multiples of $3$ is when: \[2^0\theta \equiv 2^3\theta \equiv 2^6\theta \equiv ... \pmod{180^{\circ}}.\] (This is because if it isn't the same value, the terminal angle will gradually shift from the first quadrant into different quadrants, making the condition for positive tan untrue. This must also be true in order for $\theta$ to be unique.)
This is the case if $2^3\theta \equiv 2^0\theta \pmod{180^{\circ}}$ , so $7\theta \equiv 0^{\circ} \pmod{180^{\circ}}$ . Therefore, recalling that $0^{\circ}<\theta<90^{\circ},$ the possible $\theta$ are: \[\frac{180}{7}^{\circ}, \frac{360}{7}^{\circ}, \frac{540}{7}^{\circ}.\]
$\frac{180}{7}^{\circ}$ does not work since $\tan\left(2 \cdot \frac{180}{7}^{\circ}\right)$ is positive.
$\frac{360}{7}^{\circ}$ does not work because $\tan\left(4 \cdot \frac{360}{7}^{\circ}\right)$ is positive.
Thus, $\theta = \frac{540}{7}^{\circ}$ , and a quick check verifies that it does work. Our desired answer is $540 + 7 = \boxed{547}$ .

## Solution 2
As in the previous solution, we note that $\tan \theta$ is positive when $\theta$ is in the first or third quadrant. In order for $\tan\left(2^n\theta\right)$ to be positive for all $n$ divisible by $3$ , we must have $\theta$ , $2^3\theta$ , $2^6\theta$ , etc to lie in the first or third quadrants. We already know that $\theta\in(0,90)$ . We can keep track of the range of $2^n\theta$ for each $n$ by considering the portion in the desired quadrants, which gives \[n=1 \implies (90,180)\] \[n=2\implies (270,360)\] \[n=3 \implies (180,270)\] \[n=4 \implies (90,180)\] \[n=5\implies(270,360)\] \[n=6 \implies (180,270)\] \[\cdots\] at which point we realize a pattern emerging. Specifically, the intervals repeat every $3$ after $n=1$ . We can use these repeating intervals to determine the desired value of $\theta$ since the upper and lower bounds will converge to such a value (since it is unique, as indicated in the problem). Let's keep track of the lower bound.
Initially, the lower bound is $0$ (at $n=0$ ), then increases to $\frac{90}{2}=45$ at $n=1$ . This then becomes $45+\frac{45}{2}$ at $n=2$ , $45+\frac{45}{2}$ at $n=3$ , $45+\frac{45}{2}+\frac{45}{2^3}$ at $n=4$ , $45+\frac{45}{2}+\frac{45}{2^3}+\frac{45}{2^4}$ at $n=5$ , etc. Due to the observed pattern of the intervals, the lower bound follows a partial geometric series. Hence, as $n$ approaches infinity, the lower bound converges to \[\sum_{k=0}^{\infty}\left(45+\frac{45}{2}\right)\cdot \left(\frac{1}{8}\right)^k=\frac{45+\frac{45}{2}}{1-\frac{1}{8}}=\frac{\frac{135}{2}}{\frac{7}{8}}=\frac{540}{7}\implies p+q=540+7=\boxed{547}\] -ktong
Extra note: If you are still unsure, you can check the upper bound to see if the top converges. This value comes out to be:
$90-\frac{90}{2^3}-\frac{90}{2^6}-\cdots=90\left(1-\sum_{k=1}^{\infty}\frac{1}{2^{3k}}\right)=90\left(1-\frac{1}{7}\right)=\frac{540}{7}$ .
Thus, the limit does in fact converge to the same value on both sides. ~eevee9406

## Solution 3
Since $\tan\left(\theta\right) > 0$ , $0 < \theta < 90$ . Since $\tan\left(2\theta\right) < 0$ , $\theta$ has to be in the second half of the interval (0, 90) ie (45, 90). Since $\tan\left(4\theta\right) < 0$ , $\theta$ has to be in the second half of that interval ie (67.5, 90). And since $\tan\left(8\theta\right) > 0$ , $\theta$ has to be in the first half of (67.5, 90). Inductively, the pattern repeats: $\theta$ is in the second half of the second half of the first half of the second half of the second half... of the interval (0, 90). Consider the binary representation of numbers in the interval (0, 1). Numbers in the first half of the interval start with 0.0... and numbers in the second half start with 0.1... . Similarly, numbers in the second half of the second half start with 0.11... etc. So if we want a number in the first half of the second half of the second half... of the interval, we want its binary representation to be $0.11011011011..._2 = \frac{6}{7}_{10}$ . So we want the number which is 6/7 of the way through the interval (0, 90) so $\theta = \frac{6}{7}\cdot 90 = \frac{540}{7}$ and $p+q = 540 + 7 = \boxed{547}$
~minor edit by Mathkiddie

## Solution 4
With some simple arithmetic and guess and check, we can set the lower bound and upper bounds for the "first round of $3$ powers of two", which are $\frac{540}{8} = 67.5$ and $\frac{630}{8} = 78.75$ . Going on to the "second round of $3$ powers of two, we set the new lower and upper bounds as $\frac{360 \times 12.5}{64} = 70.3125$ and $\frac{360 \times 13.75}{64} = 77.34375$ using some guess and check and bashing. Now, it is obvious that the bounds for the "zeroth round of $3$ powers of two" are $0$ and $90$ , and notice that $90 - 78.75 = 11.25$ and $78.75 - 77.34375 = 1.40625$ and $\frac{11.25}{1.40625} = 8$ . This is obviously a geometric series, so setting $11.25$ as $u$ , we obtain $90 - (u + \frac{u}{8} + \frac{u}{64} + ...)$ = $90 - \frac{u}{1-\frac{1}{8}}$ = $\frac{u}{\frac{7}{8}}$ = $\frac{45}{4} \times \frac{8}{7}$ which simplifies to $\frac{90}{7}$ . We can now finally subtract $\frac{90}{7}$ from $\frac{630}{7}$ and then we get $\frac{540}{7}$ as the unique angle, so $\boxed{547}$ is our answer. -fidgetboss_4000

## Solution 5
Since $7$ is the only number n such that f(x) = $2^{\lfloor x\rfloor}$ $\text{(mod 7)}$ has a period of 3, we find that $\theta$ is a multiple of ${\frac{180}{7}}^\circ$ . Note that the tangents of ${\frac{180}{7}}^\circ$ , ${\frac{360}{7}}^\circ$ , ${\frac{540}{7}}^\circ$ are positive while those of ${\frac{720}{7}}^\circ$ , ${\frac{900}{7}}^\circ$ , and ${\frac{1080}{7}}^\circ$ are negative. With a bit of trial and error, we find $\theta$ is ${\frac{540}{7}}^\circ$ and $540+7$ is $\boxed{547}$ .
~ Afly ( talk )
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .