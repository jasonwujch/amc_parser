# 2005 AMC 10A Problem 17

## Problem

In the five-sided star shown, the letters $A$ , $B$ , $C$ , $D$ , and $E$ are replaced by the numbers $3$ , $5$ , $6$ , $7$ , and $9$ , although not necessarily in this order. The sums of the numbers at the ends of the line segments $\overline{AB}$ , $\overline{BC}$ , $\overline{CD}$ , $\overline{DE}$ , and $\overline{EA}$ form an arithmetic sequence, although not necessarily in this order. What is the middle term of the arithmetic sequence?

[asy] size(150); defaultpen(linewidth(0.8)); string[] strng = {'A','D','B','E','C'}; pair A=dir(90),B=dir(306),C=dir(162),D=dir(18),E=dir(234); draw(A--B--C--D--E--cycle); for(int i=0;i<=4;i=i+1) { path circ=circle(dir(90-72*i),0.125); unfill(circ); draw(circ); label("$"+strng[i]+"$",dir(90-72*i)); } [/asy]

$\textbf{(A) } 9\qquad \textbf{(B) } 10\qquad \textbf{(C) } 11\qquad \textbf{(D) } 12\qquad \textbf{(E) } 13$

## Solution 1 (assuming a solution exists)
Each of $A$ , $B$ , $C$ , $D$ , and $E$ forms part of exactly $2$ sums along line segments (e.g. $A$ forms part of the sums of $\overline{AB}$ and $\overline{EA}$ ). Thus, the sum of all these line segments - i.e. the sum of the $5$ terms of the arithmetic sequence - is exactly twice the sum of $A$ , $B$ , $C$ , $D$ , and $E$ , and since those numbers are $3$ , $5$ , $6$ , $7$ , and $9$ in some order, this reduces to $2 \cdot (3+5+6+7+9) = 60$ .
Now, since the middle term of an arithmetic sequence with an odd number of terms is the average of all the terms of the sequence, the middle number must be $\frac{60}{5} = \boxed{\textbf{(D) } 12}$ .

## Solution 2 (assuming a solution exists; quick)
We observe that the average of $3$ , $5$ , $6$ , $7$ , and $9$ is $\frac{3+5+6+7+9}{5} = \frac{30}{5} = 6$ . Accordingly, setting all $5$ of $A$ , $B$ , $C$ , $D$ , and $E$ to $6$ will give the same sum of sums along the line segments - i.e. the sum of the $5$ terms of the arithmetic sequence (as in Solution 1) - as if we had constructed an actual solution. In particular, this results in all the terms of the arithmetic sequence being $6+6 = 12$ , and again as in Solution 1, the middle term must be the average of the $5$ terms, so it is necessarily $\boxed{\textbf{(D) } 12}$ .

## Solution 3 (rigorous)
As the numbers $A$ , $B$ , $C$ , $D$ , and $E$ are $3$ , $5$ , $6$ , $7$ , and $9$ in some order, we deduce that the smallest term of the arithmetic sequence must be at least $3 + 5 = 8$ , while the largest term must be at most $7 + 9 = 16$ .
Thus, as this sequence has $5$ terms, its common difference $d$ is at most $\frac{16-8}{5-1} = 2$ .
But as $d$ is positive (taking the arithmetic sequence in increasing order without loss of generality) and an integer (since it is a difference of sums of integers), while exactly $2$ of the sums must be odd (since exactly $4$ of the numbers $A$ , $B$ , $C$ , $D$ , and $E$ are odd, while the $5$ th number is even), it follows that $d$ must be odd. Therefore, the only possibility is $d = 1$ .
Next, again noting that the sequence has exactly $2$ odd terms, and thus $5-2 = 3 > 2$ even terms, we observe that the middle term must have the majority parity, i.e. must be even. This means the $2$ terms adjacent to the middle term must be odd, and therefore must be $(6+a)$ and $(6+b)$ with $a,b \in \{3,5,7,9\}$ . Moreover, $(6+a)-(6-b) = a-b$ is exactly twice the common difference, i.e. $2d = 2 \cdot 1 = 2$ .
The only other observation we need is that $a$ and $b$ can't be the smallest, or largest, $2$ odd numbers, because that would make it impossible to construct the smallest, or (respectively) largest, sum from $1$ of the remaining $2$ even numbers and $1$ of the odd numbers. Together with $a-b = 2$ from above, this implies that $a = 5$ and $b = 7$ , so finally, the middle term of the sequence must be $(6+5) + 1 = (6+7) - 1 = \boxed{\textbf{(D) } 12}$ .
(It is now easy to see that one possible solution is $A = 3$ , $B = 9$ , $C = 5$ , $D = 6$ , and $E = 7$ ; this gives the edge sums as $12$ , $14$ , $11$ , $13$ , and $10$ , which indeed form the arithmetic sequence $10,11,12,13,14$ .)
~oinava

## Video Solution 1
https://youtu.be/tKsYSBdeVuw?t=544 by OmegaLearn
~ pi_is_3.14

## Video Solution 2
https://www.youtube.com/watch?v=RljLmFCF2tU
~By Ajeet Dubey ( https://www.ioqm.in )
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .