# 2009 AIME I Problem 6

## Problem

How many positive integers $N$ less than $1000$ are there such that the equation $x^{\lfloor x\rfloor} = N$ has a solution for $x$ ?

## Solution 1
First, $x$ must be less than $5$ , since otherwise $x^{\lfloor x\rfloor}$ would be at least $3125$ which is greater than $1000$ .
Because ${\lfloor x\rfloor}$ must be an integer, let’s do case work based on ${\lfloor x\rfloor}$ :
For ${\lfloor x\rfloor}=0$ , $N=1$ as long as $x \neq 0$ . This gives us $1$ value of $N$ .
For ${\lfloor x\rfloor}=1$ , $N$ can be anything between $1^1$ to $2^1$ excluding $2^1$
Therefore, $N=1$ . However, we got $N=1$ in case 1 so it got counted twice.
For ${\lfloor x\rfloor}=2$ , $N$ can be anything between $2^2$ to $3^2$ excluding $3^2$
This gives us $3^2-2^2=5$ $N$ 's
For ${\lfloor x\rfloor}=3$ , $N$ can be anything between $3^3$ to $4^3$ excluding $4^3$
This gives us $4^3-3^3=37$ $N$ 's
For ${\lfloor x\rfloor}=4$ , $N$ can be anything between $4^4$ to $5^4$ excluding $5^4$
This gives us $5^4-4^4=369$ $N$ 's
Since $x$ must be less than $5$ , we can stop here and the answer is $1+5+37+369= \boxed {412}$ possible values for $N$ .
Alternatively, one could find that the values which work are $1^1,\ 2^2,\ 3^3,\ 4^4,\ \sqrt{5}^{\lfloor\sqrt{5}\rfloor},\ \sqrt{6}^{\lfloor\sqrt{6}\rfloor},\ \sqrt{7}^{\lfloor\sqrt{7}\rfloor},\ \sqrt{8}^{\lfloor\sqrt{8}\rfloor},\ \sqrt[3]{28}^{\lfloor\sqrt[3]{28}\rfloor},\ \sqrt[3]{29}^{\lfloor\sqrt[3]{29}\rfloor},\ \sqrt[3]{30}^{\lfloor\sqrt[3]{30}\rfloor},\ ...,$ $\ \sqrt[3]{63}^{\lfloor\sqrt[3]{63}\rfloor},\ \sqrt[4]{257}^{\lfloor\sqrt[4]{257}\rfloor},\ \sqrt[4]{258}^{\lfloor\sqrt[4]{258}\rfloor},\ ...,\ \sqrt[4]{624}^{\lfloor\sqrt[4]{624}\rfloor}$ to get the same answer.

## Solution 2
For a positive integer $k$ , we find the number of positive integers $N$ such that $x^{\lfloor x\rfloor}=N$ has a solution with ${\lfloor x\rfloor}=k$ . Then $x=\sqrt[k]{N}$ , and because $k \le x < k+1$ , we have $k^k \le x^k < (k+1)^k$ , and because $(k+1)^k$ is an integer, we get $k^k \le x^k \le (k+1)^k-1$ . The number of possible values of $x^k$ is equal to the number of integers between $k^k$ and $(k+1)^k-1$ inclusive, which is equal to the larger number minus the smaller number plus one or $((k+1)^k-1)-(k^k)+1$ , and this is equal to $(k+1)^k-k^k$ . If $k>4$ , the value of $x^k$ exceeds $1000$ , so we only need to consider $k \le 4$ . The requested number of values of $N$ is the same as the number of values of $x^k$ , which is $\sum^{4}_{k=1} [(k+1)^k-k^k]=2-1+9-4+64-27+625-256=\boxed{412}$ .

## Video Solutions

## Video Solution 1
Mostly the above solution explained on video: https://www.youtube.com/watch?v=2Xzjh6ae0MU&t=11s
~IceMatrix

## Video Solution 2
https://youtu.be/kALrIDMR0dg
~Shreyas S

## Video Solution 3
Projective Solution: https://youtu.be/fUef_tVnM5M
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.