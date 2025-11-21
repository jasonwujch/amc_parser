# 2020 AIME I Problem 10

## Problem

Let $m$ and $n$ be positive integers satisfying the conditions

$\quad\bullet\ \gcd(m+n,210)=1,$

$\quad\bullet\ m^m$ is a multiple of $n^n,$ and

$\quad\bullet\ m$ is not a multiple of $n.$

Find the least possible value of $m+n.$

## Solution 1
Taking inspiration from $4^4 \mid 10^{10}$ we are inspired to take $n$ to be $p^2$ , the lowest prime not dividing $210$ , or $11 \implies n = 121$ . Now, there are $242$ factors of $11$ , so $11^{242} \mid m^m$ , and then $m = 11k$ for $k \geq 22$ . Now, $\gcd(m+n, 210) = \gcd(11+k,210) = 1$ . Noting $k = 26$ is the minimal that satisfies this, we get $(n,m) = (121,286)$ . Thus, it is easy to verify this is minimal and we get $\boxed{407}$ . ~awang11

## Solution 2
We essentially have that $\gcd(m,n) \notin \{1, m, n\},$ or the set of factors of $210.$
This implies that one number must be odd and the other must be even so that they don’t add up to a multiple of $2.$ If $n$ is even and $m$ is odd it would be impossible for $m^m$ to be a multiple of $n^n,$ so $m$ must be even and $n$ must be odd.
Now we need to choose the prime factor for $m$ and $n$ to share. It can't be $2,3,5,$ or $7$ so the next smallest option is $11.$
So far we have $m = 22$ and $n = 11.$ We need to add more factors so that $m$ is not a multiple of $n$ but $m^m$ is a multiple of $n^n.$ Note that no matter how many additional factors we add to $m,$ it will always be a multiple of $11,$ so we have to add another factor to $n$ to make sure it doesn't divide $m.$ Again the smallest option is $11,$ so $n$ becomes $121 \implies n^n = 11^{242},$ and $m^m = 2^{22} \cdot 11^{22}.$ All we need to do now is significantly increase the value of $m$ so that the exponent on $11$ becomes larger than $242.$ If we added another factor of $11$ to $m$ then it would be a multiple of $n$ again, so the next smallest option is $13.$ Then $m = 22\cdot 13 = 286.$ $m^m$ becomes $2^{286} \cdot 11^{286} \cdot 13^{286}$ which satisfies the problem's condition.
Therefore, the least possible value of $m + n$ is $121 + 286 = \boxed{407}.$
~ grogg007

## Solution 3
Assume for the sake of contradiction that $n$ is a multiple of a single digit prime number, then $m$ must also be a multiple of that single digit prime number to accommodate for $n^n | m^m$ . However that means that $m+n$ is divisible by that single digit prime number, which violates $\gcd(m+n,210) = 1$ , so contradiction.
$n$ is also not 1 because then $m$ would be a multiple of it.
Thus, $n$ is a multiple of 11 and/or 13 and/or 17 and/or...
Assume for the sake of contradiction that $n$ has at most 1 power of 11, at most 1 power of 13...and so on... Then, for $n^n | m^m$ to be satisfied, $m$ must contain at least the same prime factors that $n$ has. This tells us that for the primes where $n$ has one power of, $m$ also has at least one power, and since this holds true for all the primes of $n$ , $n|m$ . Contradiction.
Thus $n$ needs more than one power of some prime. The obvious smallest possible value of $n$ now is $11^2 =121$ . Since $121^{121}=11^{242}$ , we need $m$ to be a multiple of 11 at least $242$ that is not divisible by $121$ and most importantly, $\gcd(m+n,210) = 1$ . $242$ is divisible by $121$ , out. $253+121$ is divisible by 2, out. $264+121$ is divisible by 5, out. $275+121$ is divisible by 2, out. $286+121=37\cdot 11$ and satisfies all the conditions in the given problem, and the next case $n=169$ will give us at least $169\cdot 3$ , so we get $\boxed{407}$ .

## Solution 4 (Official MAA)
Let $m$ and $n$ be positive integers where $m^m$ is a multiple of $n^n$ and $m$ is not a multiple of $n$ . If a prime $p$ divides $n$ , then $p$ divides $n^n$ , so it also divides $m^m$ , and thus $p$ divides $m$ . Therefore any prime $p$ dividing $n$ also divides both $m$ and $k = m + n$ . Because $k$ is relatively prime to $210=2\cdot3\cdot5\cdot7$ , the primes $2$ , $3$ , $5$ , and $7$ cannot divide $n$ . Furthermore, because $m$ is divisible by every prime factor of $n$ , but $m$ is not a multiple of $n$ , the integer $n$ must be divisible by the square of some prime, and that prime must be at least $11$ . Thus $n$ must be at least $11^2 = 121$ .
If $n=11^2$ , then $m$ must be a multiple of $11$ but not a multiple of $121$ , and $m^m$ must be divisible by $n^n = 121^{121} = 11^{242}$ . Therefore $m$ must be a multiple of $11$ that is greater than $242$ . Let $m = 11m_0$ , with $m_0 > 22$ . Then $k = m + n = 11(m_0 + 11)$ . The least $m_0 > 22$ for which $m_0 + 11$ is not divisible by any of the primes $2$ , $3$ , $5$ , or $7$ is $m_0 = 26$ , giving the prime $m_0 + 11 = 37$ . Hence the least possible $k$ when $n = 121$ is $k = 11 \cdot 37 = 407$ .
It remains to consider other possible values for $n$ . If $n = 13^2 = 169$ , then $m$ must be divisible by $13$ but not $169$ , and $m^m$ must be a multiple of $n^n = 169^{169} = 13^{338}$ , so $m > 338$ . Then $k = m + n > 169 + 338 = 507$ . All other possible values for $n$ have $n \ge 242$ , and in this case $m > n \ge 242$ , so $k \ge 2 \cdot 242 = 484$ . Hence no greater values of $n$ can produce lesser values for $k$ , and the least possible $k$ is indeed $407$ .

## Video Solution
https://youtu.be/Z47NRwNB-D0

## Video Solution
https://www.youtube.com/watch?v=FQSiQChGjpI&list=PLLCzevlMcsWN9y8YI4KNPZlhdsjPTlRrb&index=7 ~ MathEx
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .