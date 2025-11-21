# 2015 AIME II Problem 1

## Problem

Let $N$ be the least positive integer that is both $22$ percent less than one integer and $16$ percent greater than another integer. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
If $N$ is $22$ percent less than one integer $k$ , then $N=\frac{78}{100}k=\frac{39}{50}k$ . In addition, $N$ is $16$ percent greater than another integer $m$ , so $N=\frac{116}{100}m=\frac{29}{25}m$ . Therefore, $k$ is divisible by $50$ and $m$ is divisible by $25$ . Setting these two equal, we have $\frac{39}{50}k=\frac{29}{25}m$ . Multiplying by $50$ on both sides, we get $39k=58m$ .
The smallest integers $k$ and $m$ that satisfy this are $k=1450$ and $m=975$ , so $N=1131$ . The answer is $\boxed{131}$ .

## Solution 2
Continuing from Solution 1, we have $N=\frac{39}{50}k$ and $N=\frac{29}{25}m$ . It follows that $k=\frac{50}{39}N$ and $m=\frac{25}{29}N$ . Both $m$ and $k$ have to be integers, so, in order for that to be true, $N$ has to cancel the denominators of both $\frac{50}{39}$ and $\frac{25}{29}$ . In other words, $N$ is a multiple of both $29$ and $39$ . That makes $N=\operatorname{lcm}(29,39)=29\cdot39=1131$ . The answer is $\boxed{131}$ .

## Solution 3
We can express $N$ as $0.78a$ and $1.16b$ , where $a$ and $b$ are some positive integers. $N=0.78a=1.16b\implies100N=78a=116b.$ Let us try to find the smallest possible value of $100N$ , first ignoring the integral constraint.
Obviously, we are just trying to find the LCM of $78$ and $116.$ They have no common factors but $2$ , so we multiply $78$ and $116$ and divide by $2$ to get $4524.$ This is obviously not divisible by $100$ , so this is not possible, as it would imply that $N=\dfrac{4524}{100},$ which is not an integer. This can be simplified to $\dfrac{1131}{25}$ .
We know that any possible value of $N$ will be an integral multiple of this value; the smallest such $N$ is achieved by multiplying this value by $25.$ We arrive at $1131$ , which is $\boxed{131}\mod1000.$
~Technodoggo

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=7s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .