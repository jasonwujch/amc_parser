# 2010 AIME I Problem 14

## Problem

For each positive integer $n$ , let $f(n) = \sum_{k = 1}^{100} \lfloor \log_{10} (kn) \rfloor$ . Find the largest value of $n$ for which $f(n) \le 300$ .

Note: $\lfloor x \rfloor$ is the greatest integer less than or equal to $x$ .

## Solution 1
Observe that $f$ is strictly increasing in $n$ . We realize that we need $100$ terms to add up to around $300$ , so we need some sequence of $2$ s, $3$ s, and then $4$ s.
It follows that $n \approx 100$ (alternatively, use binary search to get to this, with $n\le 1000$ ). Manually checking shows that $f(109) = 300$ and $f(110) > 300$ . Thus, our answer is $\boxed{109}$ .

## Solution 2
Because we want the value for which $f(n)=300$ , the average value of the 100 terms of the sequence should be around $3$ . For the value of $\lfloor \log_{10} (kn) \rfloor$ to be $3$ , $1000 \le kn < 10000$ . We want kn to be around the middle of that range, and for k to be in the middle of 0 and 100, let $k=50$ , so $50n=\frac{10000+1000}{2}=\frac{11000}{2}=5500$ , and $n = 110$ . $f(110) = 301$ , so we want to lower $n$ . Testing $109$ yields $300$ , so our answer is still $\boxed{109}$ .

## Solution 3
For any $n$ where the sum is close to $300$ , all the terms in the sum must be equal to $2$ , $3$ or $4$ . Let $M$ be the number of terms less than or equal to $3$ and $N$ be the number of terms equal to $2$ (also counted in $M$ ). With this definition of $M$ and $N$ the total will be $400 - M - N \le 300$ , from which $M + N \ge 100$ . Now $M+1$ is the smallest integer $k$ for which $\log_{10}(kn) \ge 4$ or $kn \ge 10000$ , thus \[M = \left\lfloor\frac{9999}{n}\right\rfloor.\] Similarly, \[N = \left\lfloor\frac{999}{n}\right\rfloor = \left\lfloor\frac{M}{10}\right\rfloor.\]
Therefore, \[M + \left\lfloor \frac{M}{10} \right\rfloor \ge 100 \implies M \ge \left\lceil\frac{1000}{11}\right\rceil = 91 \implies n \le \left\lfloor\frac{9999}{91}\right\rfloor = 109.\] Since we want the largest possible $n$ , the answer is $\boxed{109}$ .

## Solution 4 (similar to Solution 1, but with more detail)
Since we're working with base- $10$ logarithms, we can start by testing out $n$ 's that are powers of $10$ . For $n = 1$ , the terms in the sum are $\lfloor \log_{10} (1)\rfloor, \lfloor \log_{10} (2)\rfloor, \lfloor \log_{10} (3) \rfloor , . . . , \lfloor \log_{10} (100) \rfloor$ . For numbers $1$ - $9$ , $\lfloor \log_{10} (kn) \rfloor = 0$ . Then we have $90$ numbers, namely $10$ - $99$ , for which $\lfloor \log_{10} (kn) \rfloor = 1$ . The last number we have is $100$ , which gives us $\lfloor \log_{10} (kn) \rfloor = 2$ . This sum gives us only $90 + 2 = 92$ , which is much too low. However, applying the same counting technique for $n = 10$ , our sum comes out to be $9 + 180 + 3 = 192$ , since there are $9$ terms for which $\lfloor \log_{10} (kn) \rfloor = 1$ , $90$ terms for which $\lfloor \log_{10} (kn) \rfloor = 2$ , and one term for which $\lfloor \log_{10} (kn) \rfloor = 3$ . So we go up one more power of $10$ and get $18 + 270 + 4 = 292$ , which is very close to what we are looking for.
Now we only have to bump up the value of $n$ a bit and check our sum. Each increase in $n$ by $1$ actually increases the value of our sum by $1$ as well (except for $n = 101$ ), because whenever a $4$ is added to the sum, a $3$ is taken away. It doesn't take long to check and see that the value of $n$ we're looking for is $\boxed{109}$ , which corresponds to a sum of exactly $300$ .
~ anellipticcurveoverq

## Video Solution
2010 AIME I #14
MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .