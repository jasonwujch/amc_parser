# 2010 AIME I Problem 5

## Problem

Positive integers $a$ , $b$ , $c$ , and $d$ satisfy $a > b > c > d$ , $a + b + c + d = 2010$ , and $a^2 - b^2 + c^2 - d^2 = 2010$ . Find the number of possible values of $a$ .

## Solution 1
Using the difference of squares , $2010 = (a^2 - b^2) + (c^2 - d^2) = (a + b)(a - b) + (c + d)(c - d) \ge a + b + c + d = 2010$ , where equality must hold so $b = a - 1$ and $d = c - 1$ . Then we see $a = 1004$ is maximal and $a = 504$ is minimal, so the answer is $\boxed{501}$ .
Note: We can also find that $b=a-1$ in another way. We know \[a^{2} - b^{2} + c^{2} - d^{2}=(a+b)+(c+d) \implies (a+b)(a-b)-(a+b)+(c+d)(c-d)-(c+d)=0 \implies (a+b)(a-b-1)+(c+d)(c-d-1)=0\]
Therefore, one of $(a+b)(a-b-1)$ and $(c+d)(c-d-1)$ must be $0.$ Clearly, $a+b \neq 0$ since then one would be positive and negative, or both would be zero. Therefore, $a-b-1=0$ so $a=b+1$ . Similarly, we can deduce that $c=d+1.$

## Solution 2
Since $a+b$ must be greater than $1005$ , it follows that the only possible value for $a-b$ is $1$ (otherwise the quantity $a^2 - b^2$ would be greater than $2010$ ). Therefore the only possible ordered pairs for $(a,b)$ are $(504, 503)$ , $(505, 504)$ , ... , $(1004, 1003)$ , so $a$ has $\boxed{501}$ possible values. Hence the answer is 500+1=501
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .