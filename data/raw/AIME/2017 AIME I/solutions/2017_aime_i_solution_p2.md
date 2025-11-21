# 2017 AIME I Problem 2

## Problem

When each of $702$ , $787$ , and $855$ is divided by the positive integer $m$ , the remainder is always the positive integer $r$ . When each of $412$ , $722$ , and $815$ is divided by the positive integer $n$ , the remainder is always the positive integer $s \neq r$ . Find $m+n+r+s$ .

## Solution
Let's work on both parts of the problem separately. First, \[855 \equiv 787 \equiv 702 \equiv r \pmod{m}.\] We take the difference of $855$ and $787$ , and also of $787$ and $702$ . We find that they are $85$ and $68$ , respectively. Since the greatest common divisor of the two differences is $17$ , $m=1,17$ but if $m=1$ , then $r=0$ which violates $r$ being positive,so it's safe to assume that $m = 17$ .
Then, we divide $855$ by $17$ , and it's easy to see that $r = 5$ . Dividing $787$ and $702$ by $17$ also yields remainders of $5$ , which means our work up to here is correct.
Doing the same thing with $815$ , $722$ , and $412$ , the differences between $815$ and $722$ and $412$ are $310$ and $93$ , respectively. Since the only common divisor (besides $1$ , of course) is $31$ , $n = 31$ . Dividing all $3$ numbers by $31$ yields a remainder of $9$ for each, so $s = 9$ . Thus, $m + n + r + s = 17 + 5 + 31 + 9 = \boxed{062}$ .

## Solution 2
We know that $702 = am + r, 787 = bm + r,$ and $855 = cm+r$ where $a-c$ are integers.
Subtracting the first two, the first and third, and the last two, we get $85 = (b-a)m, 153=(c-a)m,$ and $68=(c-b)m.$
We know that $b-a, c-a$ and $c-b$ must be integers, so all the numbers are divisible by $m.$
Factorizing the numbers, we get $85 = 5 \cdot 17, 153 = 3^2 \cdot 17,$ and $68 = 2^2 \cdot 17.$ We see that all these have a factor of 17, so $m=17.$
Finding the remainder when $702$ is divided by $17,$ we get $n=5.$
Doing the same thing for the next three numbers, we get $17 + 5 + 31 + 9 = \boxed{062}$
~solasky

## Solution 3 (Sol. 1 but possibly more clear)
As in Solution 1, we are given $855\equiv787\equiv702\equiv r\pmod{m}$ and $815\equiv722\equiv412\equiv s\pmod{n}.$ Tackling the first equation, we can simply look at $855\equiv787\equiv702\pmod{m}$ . We subtract $702$ from each component of the congruency to get $153\equiv85\equiv0\pmod{m}$ . Thus, we know that $153$ and $85$ must both be divisible by $m$ . The only possible $m$ , in this case, become $17$ and $1$ ; obviously, $m\neq1$ , so we know $m=17$ . We go back to the original equation, plug in $m$ , and we find that $r=5$ .
Similarly, we can subtract out the smallest value in the second congruency, $412$ . We end up with $403\equiv310\equiv0\pmod{n}$ . Again, we find that $n=31$ or $1$ , so $n=31$ . We also find that $s=9$ .
Thus, our answer is $\boxed{062}$ .
~Technodoggo

## Video Solution
https://youtu.be/BiiKzctXDJg ~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .