# 2017 AIME I Problem 13

## Problem

For every $m \geq 2$ , let $Q(m)$ be the least positive integer with the following property: For every $n \geq Q(m)$ , there is always a perfect cube $k^3$ in the range $n < k^3 \leq m \cdot n$ . Find the remainder when \[\sum_{m = 2}^{2017} Q(m)\] is divided by 1000.

## Solution 1
Lemma 1: The ratio between $k^3$ and $(k+1)^3$ decreases as $k$ increases.
Lemma 2: If the range $(n,mn]$ includes $y$ cubes, $(p,mp]$ will always contain at least $y-1$ cubes for all $p$ in $[n,+\infty)$ .
If $m=14$ , the range $(1,14]$ includes one cube. The range $(2,28]$ includes 2 cubes, which fulfills the Lemma. Since $n=1$ also included a cube, we can assume that $Q(m)=1$ for all $m>14$ . Two groups of 1000 are included in the sum modulo 1000. They do not count since $Q(m)=1$ for all of them, therefore \[\sum_{m = 2}^{2017} Q(m) \equiv \sum_{m = 2}^{17} Q(m) \mod 1000\]
Now that we know this we will find the smallest $n$ that causes $(n,mn]$ to contain two cubes and work backwards (recursion) until there is no cube in $(n,mn]$ .
For $m=2$ there are two cubes in $(n,2n]$ for $n=63$ . There are no cubes in $(31,62]$ but there is one in $(32,64]$ . Therefore $Q(2)=32$ .
For $m=3$ there are two cubes in $(n,3n]$ for $n=22$ . There are no cubes in $(8,24]$ but there is one in $(9,27]$ . Therefore $Q(3)=9$ .
For $m$ in $\{4,5,6,7\}$ there are two cubes in $(n,4n]$ for $n=7$ . There are no cubes in $(1,4]$ but there is one in $(2,8]$ . Therefore $Q(4)=2$ , and the same for $Q(5)$ , $Q(6)$ , and $Q(7)$ for a sum of $8$ .
For all other $m$ there is one cube in $(1,8]$ , $(2,16]$ , $(3,24]$ , and there are two in $(4,32]$ . Therefore, since there are 10 values of $m$ in the sum, this part sums to $10$ .
When the partial sums are added, we get $\boxed{059}\hspace{2 mm}QED\hspace{2 mm} \blacksquare$
This solution is brought to you by a1b2

## Solution 2
We claim that $Q(m) = 1$ when $m \ge 8$ .
When $m \ge 8$ , for every $n \ge Q(m) = 1$ , we need to prove there exists an integer $k$ , such that $n < k^3 \le m \cdot n$ .
That's because $\sqrt[3]{m \cdot n} - \sqrt[3]{n} \ge 2\sqrt[3]{n} - \sqrt[3]{n} = \sqrt[3]{n} \ge 1$ , so k exists between $\sqrt[3]{m \cdot n}$ and $\sqrt[3]{n}$
$\sqrt[3]{n} < k \le \sqrt[3]{m \cdot n}$ .
We can then hand evaluate $Q(m)$ for $m = 2,3,4,5,6,7$ , and get $Q(2) = 32$ , $Q(3) = 9$ , and all the others equal 2.
There are a total of 2010 integers from 8 to 2017.
\[\sum_{m = 2}^{2017} Q(m) \equiv \sum_{m = 2}^{7} Q(m) + 2010 \equiv 32+9+2+2+2+2+10 = \boxed{059} \mod 1000\]
-AlexLikeMath

## Solution 3
Note that the problem is just asking for every $m \geq 2$ , find the least $n$ such that there lies a perfect cube in between of $n$ and $mn$ for every $n$ after that minimum including the minimum. We consider $m = 2$ first. Then, we need to find the least $n$ such that for every $n$ after this minimum $n$ , including the minimum, there lies a perfect cube in between of $n$ and $2n$ . Let's denote the range notation as $(n, 2n)$ . Hence, we start with $n = 1$ to get the range of $(1, 2)$ . Clearly, no perfect cube lies between these numbers. Then we go to $n = 2$ to get $(2, 4)$ and here also nothing works. We can see that the perfect cubes are $1, 8, 27 64, 125, 216, 343, 512, 729, 1000, ...$ . Because $1$ can't lie between two positive integers, we need to find the minimum $n$ such that $8$ is between $n$ and $2n$ . Clearly, $n = 4$ will yield this case. We have the range $(4, 8)$ . This works. We now list every $n$ starting from $4$ and see if all of these ranges host a perfect cube in between them. We have $(5, 10)$ works, $(6, 12)$ works $(7, 14)$ works, but $(8, 16)$ doesn't work. This is because the next perfect cube has to be $27$ . Aha! Now we see the case. If we have a range in the following form $(\frac{a^{3}}{2}, a^{3})$ , this will clearly host a perfect cube between them which is $a^{3}$ . But as we keep going, we need to put the next perfect cube after $a^{3}$ into the range which is $(a + 1)^{3}$ . We know that the next range after $(\frac{a^{3}}{2}, a^{3})$ is just $(a^{3}, 2a^{3})$ because we double everything. Hence, $(a + 1)^{3}$ must be in this range. If the perfect cube in between $a^{3}$ and $2a^{3}$ is of the form $a^{3} + \alpha$ , we know that this added constant $\alpha$ is greater than or equal to $(a + 1)^{3} - a^{3} = 3a^{2} + 3a + 1$ . Hence, we let $\alpha = a$ to solve $a^{3} \geq 3a^{2} + 3a + 1$ and for integer solutions, we claim the answer is $a \geq 4$ . We can prove this by induction.
Claim: $a^{3} \geq 3a^{2} + 3a + 1$ for integer solutions exists when $a \geq 4$ .
Proof: Let's plug in $a = 4$ for our base case. We get: $64 \geq 48 + 12 + 1 = 61$ which holds true. Hence, the inductive hypothesis is that $(a + 1)^{3} \geq 3(a + 1)^{2} + 3(a + 1) + 1$ for all $a \geq 3$ . In fact, we simplify to prove $a^{3} \geq 6a + 6$ for all $a \geq 3$ . Now, from our inductive assumption, we need to prove that $3a^{2} + 3a + 1 \geq 6a + 6$ . Hence, $3a^{2} - 3a \geq 5$ for all $a \geq 3$ . Hence, we need to show $a^{2} - a \geq \frac{5}{3}$ for all $a \geq 3$ . But since we're proving this in the integer world, this is equivalent to proving that $a^{2} -a \geq 2$ for all $a \geq 3$ . Now we need to show that $a^{2} \geq a + 2$ . Dividing by $a$ because $a$ is a positive integer means we have to show $a \geq 1 + \frac{2}{a}$ . Now since $a \geq 3$ , $\frac{2}{a} < 1$ and so the $RHS$ of the inequality can't even exceed $2$ whereas the $LHS$ of the inequality is already exceeding $2$ . Therefore, the inductive hypothesis holds true and we are done.
What we have just shown now is that $a \geq 4$ . Now note that the minimum range we found that worked was $(\frac{a^{3}}{2}, a^{3})$ where $n = \frac{a^{3}}{2}$ . We plug in $a = 4$ to get $n = 32$ and hence $Q(2) = 32$ . We can now apply the same procedure to the other numbers and finish as the above solutions.
~ilikemath247365
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .