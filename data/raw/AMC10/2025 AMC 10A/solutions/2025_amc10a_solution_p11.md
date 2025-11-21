# 2025 AMC 10A Problem 11

## Problem

The sequence $1,x,y,z$ is arithmetic. The sequence $1,p,q,z$ is geometric. Both sequences are strictly increasing and contain only integers, and $z$ is as small as possible. What is the value of $x+y+z+p+q$ ?

$\textbf{(A) } 66 \qquad\textbf{(B) } 91 \qquad\textbf{(C) } 103 \qquad\textbf{(D) } 132 \qquad\textbf{(E) } 149$

1 Video Solution

- 1 Video Solution

- 2 Solution 1

- 3 Solution 2

- 4 Solution 3 (Satisfying and Simple)

- 5 Solution 4 (Easy to identify)

- 6 Chinese Video Solution

- 7 Video Solution (Fast and Easy)

- 8 Video Solution by SpreadTheMathLove

- 9 Video Solution

- 10 Video Solution by Daily Dose of Math

- 11 See Also

## Video Solution
https://youtu.be/CCYoHk2Af34

## Solution 1
Since the geometric sequence is more restrictive, we can test values for the common ratio until we find one that works. After a few tests, we find that a common ratio of $4$ results in the geometric sequence $1,4,16,64,$ so the arithmetic sequence is $1,22,43,64.$ The answer is $4+16+64+22+43=\boxed{\text{(E) }149}.$
A more generalized solution is as follows. Let the common difference of the arithmetic sequence be $d$ , and the common ratio of the geometric sequence be $r.$ Hence, the two sequences are $1,1+d,1+2d,1+3d$ and $1,r,r^2,r^3.$ Since $z=1+3d=r^3,$ the arithmetic sequence is $1,1+d,1+2d,r^3.$ Since $d=\dfrac{1+3d-1}{3}=\dfrac{r^3-1}{3}$ is a positive integer, we seek the smallest $r\neq1$ such that $r^3-1=(r-1)(r^2+r+1)$ is divisble by $3,$ so the smallest $r$ is $4$ . The rest follows like above.
~Tacos_are_yummy_1
~Minor edit by dodobird150

## Solution 2
Since $1, x, y, z$ is an arithmetic sequence, we have $y = 2x - 1$ and $z = 3x - 2$ . Since $1, p, q, z$ is a geometric sequence, we have $q = p^2$ and $z = p^3$ . Thus $p^3 = 3x - 2.$
Because $p^3 \equiv p \pmod{3}$ , we get $3x - 2 \equiv p \pmod{3}$ , so $p \equiv 1 \pmod{3}$ . The smallest integer $p > 1$ satisfying this is $p = 4$ .
Then $64 = 3x - 2$ → $x = 22$ , $y = 43$ , $z = 64$ , $q = 16$ . Therefore, $x + y + z + p + q = 22 + 43 + 64 + 4 + 16 = \boxed{\text{(E) }149}$ .
~Continuous_Pi
~ $\LaTeX$ by stevens0209

## Solution 3 (Satisfying and Simple)
So we have that the arithmetic sequence is $1, x, 2x-1, 3x-2$ since common difference is $x - 1$ .
Similarly, geometric sequence is $1, p, p^2, p^3$
So $p^3 = 3x-2$ . We test values above 1 (increasing sequence)
We see that $p = 4, x = 22$ so our answer is $22 + 43 + 64 + 4 + 16 = \boxed{149}$
~Aarav22

## Solution 4 (Easy to identify)
Since only integer ratios work for the geometric series, test the ratio of $2$ , $3$ , and $4$ , by having $z$ be $2$ , $3$ , and $4$ cubed, and finding that $\frac{64-1}{3}=21$ (since that is the common ratio of the arithmetic sequence to get $64$ from $1$ in $4$ terms), then $22+43+4+16+64=149$ , which is E.
Note: We divide $z$ by $3$ because to get from $p$ to $z$ you have to add $3d$ which is the difference of the arithmetic sum.
-Amon26(note)

## Chinese Video Solution
https://www.bilibili.com/video/BV1JYkUBVEMw/
~metrixgo

## Video Solution (Fast and Easy)
https://youtu.be/mxA52qodEqk?si=jxyGlehyqeHxic1i ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by Daily Dose of Math
https://youtu.be/5Fjos1vBt0A
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .