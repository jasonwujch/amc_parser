# 2025 AMC 10B Problem 11

## Problem

On Monday, $6$ students went to the tutoring center at the same time, and each one was randomly assigned to one of the $6$ tutors on duty. On Tuesday, the same $6$ students showed up, the same $6$ tutors were on duty, and the students were again randomly assigned to the tutors. What is the probability that exactly $2$ students met with the same tutor both Monday and Tuesday?

$\textbf{(A)}\ \frac{1}{16} \qquad \textbf{(B)}\ \frac{3}{16} \qquad \textbf{(C)}\ \frac{1}{4} \qquad \textbf{(D)}\ \frac{3}{8} \qquad \textbf{(E)}\ \frac{1}{2}$

## Solution 1
On Monday, the first tutor has 6 choices for kids to be assigned to, the second has 5, and so on. Hence, there are $6!$ possible ways to assign the tutors to the kids. On Tuesday, there are $\binom{6}{2}$ ways to choose the kid-tutor pairs that remain the same from Monday. For the other 4 kids, they need to be assigned to the other tutors in such a way that none of those kids are assigned to the same tutor that they were assigned to on Monday. There are $9$ ways to do this. Thus, our final answer is $\frac{\binom{6}{2} \cdot 9}{6!}$ or $\boxed{\textbf{(B)}\hspace{3pt}\frac{3}{16}}$ .
~Milkdrinker
Remark: We can get $9$ either by listing all the possible configurations or by rounding $\frac{4!}{e}$ . This is called a derangement and is notated as $!n$ . It can be calculated with the explicit formula $!n = n!\sum _{i=0}^{n}\frac{(-1)^{i}}{i!}$
More commonly, one could also use PIE, 24 - 24 + 12 - 4 + 1 = 9 ways

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=G_5eGJNCK1Y
~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .