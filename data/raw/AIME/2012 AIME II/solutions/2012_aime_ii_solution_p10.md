# 2012 AIME II Problem 10

## Problem

Find the number of positive integers $n$ less than $1000$ for which there exists a positive real number $x$ such that $n=x\lfloor x \rfloor$ .

Note: $\lfloor x \rfloor$ is the greatest integer less than or equal to $x$ .

## Solution

## Solution 1
We know that $x$ cannot be irrational because the product of a rational number and an irrational number is irrational (but $n$ is an integer). Therefore $x$ is rational.
Let $x = a + \frac{b}{c}$ where $a,b,c$ are nonnegative integers and $0 \le b < c$ (essentially, $x$ is a mixed number). Then, \[n = \left(a + \frac{b}{c}\right) \left\lfloor a +\frac{b}{c} \right\rfloor \Rightarrow n = \left(a + \frac{b}{c}\right)a = a^2 + \frac{ab}{c}\]
Here it is sufficient for $\frac{ab}{c}$ to be an integer. We can use casework to find values of $n$ based on the value of $a$ :
$a = 0 \implies$ nothing because n is positive
$a = 1 \implies \frac{b}{c} = \frac{0}{1}$
$a = 2 \implies \frac{b}{c} = \frac{0}{2},\frac{1}{2}$
$a = 3 \implies\frac{b}{c} =\frac{0}{3},\frac{1}{3},\frac{2}{3}$
The pattern continues up to $a = 31$ . Note that if $a = 32$ , then $n > 1000$ . However if $a = 31$ , the largest possible $x$ is $31 + \frac{30}{31}$ , in which $n$ is still less than $1000$ . Therefore the number of positive integers for $n$ is equal to $1+2+3+...+31 = \frac{31 \cdot 32}{2} = \boxed{496}.$

## Solution 2
Notice that $x\lfloor x\rfloor$ is continuous over the region $x \in [k, k+1)$ for any integer $k$ . Therefore, it takes all values in the range $[k\lfloor k\rfloor, (k+1)\lfloor k+1\rfloor) = [k^2, (k+1)k)$ over that interval. Note that if $k>32$ then $k^2 > 1000$ and if $k=31$ , the maximum value attained is $31*32 < 1000$ . It follows that the answer is $\sum_{k=1}^{31} (k+1)k-k^2 = \sum_{k=1}^{31} k = \frac{31\cdot 32}{2} = \boxed{496}.$

## Solution 3
Bounding gives $x^2\le n<x^2+x$ . Thus there are a total of $x$ possible values for $n$ , for each value of $x^2$ . Checking, we see $31^2+31=992<1000$ , so there are \[1+2+3+...+31= \boxed{496}\] such values for $n$ .
Here writer's x and question's x are different. Here writer means [x] everywhere he writes x so you can let [x] = k and then use the inequality $k^2\le n<k^2+k$ . this inequality comes from [x] = k $k\le x<k+1$ $k[x]\le x[x]<(k+1)[x]$ $k^2\le n<(k+1)k$ further you can proceed.

## Solution 4
After a bit of experimenting, we let $n=l^2+s, s < 2n+1$ . We claim that I (the integer part of $x$ ) = $l$ . (Prove it yourself using contradiction !) so now we get that $x=l+\frac{s}{l}$ . This implies that solutions exist iff $s<l$ , or for all natural numbers of the form $l^2+s$ where $s<l$ . Hence, 1 solution exists for $l=1$ ! 2 for $l=2$ and so on. Therefore our final answer is $31+30+\dots+1= \boxed{496}$

## Solution 5
Notice we can write $\lfloor x \rfloor$ as $x - \{x\}$ . Since $n$ is a positive integer less than $1000$ ,
\[1 \leq x(x - \{x\}) \leq 999.\]
We now have
\[1 \leq x^{2} - x\{x\} \leq 999.\]
Since $x\{x\}$ ranges from $0$ to $x$ , we can rewrite as
\[1 \leq x^{2} \leq 999 + x.\]
Notice all $x$ that satisfy this inequality range from $1$ to $32$ .
Now every range from $y$ to $y+1$ for $x$ results in exactly $y$ solutions that give a positive integer solution for $n$ . The first range is $1$ to $2$ and the last range is $31$ to $32$ .
Thus, by using our above lemma, we can find the total number of solutions:
\[1+2+\cdots+31 = \frac{31 \cdot 32}{2} = \boxed{496}.\]
~ilikemath247365

## Video Solution
2012 AIME II #10
~MathProblemSolvingSkills.com
### See Also
2009 AIME I Problems/Problem 6
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .