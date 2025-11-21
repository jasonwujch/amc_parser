# 2022 AMC 8 Problem 20

## Problem

The grid below is to be filled with integers in such a way that the sum of the numbers in each row and the sum of the numbers in each column are the same. Four numbers are missing. The number $x$ in the lower left corner is larger than the other three missing numbers. What is the smallest possible value of $x$ ? [asy] unitsize(0.5cm); draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$x$"); [/asy] $\textbf{(A) } -1 \qquad \textbf{(B) } 5 \qquad \textbf{(C) } 6 \qquad \textbf{(D) } 8 \qquad \textbf{(E) } 9 \qquad$

## Solution 1
The sum of the numbers in each row is $12$ . Consider the second row. In order for the sum of the numbers in this row to equal $12$ , the two shaded numbers must add up to $13$ : [asy] unitsize(0.5cm); fill((-3,1)--(1,1)--(1,-1)--(-3,-1)--cycle,mediumgray); draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$x$"); [/asy] If two numbers add up to $13$ , one of them must be at least $7$ : If both shaded numbers are no more than $6$ , their sum can be at most $12$ . Therefore, for $x$ to be larger than the three missing numbers, $x$ must be at least $8$ . We can construct a working scenario where $x=8$ : [asy] unitsize(0.5cm); draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$8$"); label((0,-2),"$-4$"); label((-2,0),"$6$"); label((0,0),"$7$"); [/asy] So, our answer is $\boxed{\textbf{(D) } 8}$ .
~ihatemath123

## Solution 2
The sum of the numbers in each row is $-2+9+5=12,$ and the sum of the numbers in each column is $5+(-1)+8=12.$
Let $y$ be the number in the lower middle. It follows that $x+y+8=12,$ or $x+y=4.$
We express the other two missing numbers in terms of $x$ and $y,$ as shown below: [asy] unitsize(0.5cm); draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$x$"); label((0,-2),"$y$",red+fontsize(11)); label((-2,0),"$y{+}10$",red+fontsize(11)); label((0,0),"$x{-}1$",red+fontsize(11)); [/asy] We have $x>x-1, x>y+10,$ and $x>y.$ Note that the first inequality is true for all values of $x.$ We only need to solve the second inequality so that the third inequality is true for all values of $x.$ By substitution, we get $x>(4-x)+10,$ from which $x>7.$
Therefore, the smallest possible value of $x$ is $\boxed{\textbf{(D) } 8}.$
~MRENTHUSIASM

## Solution 3
This is based on the Solution 2 above and it is perhaps a little simpler than that.
Let $y$ be the number in the lower middle. Applying summation to first two columns yields the following.
[asy] unitsize(0.5cm); draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$x$"); label((0,-2),"$y$",red+fontsize(11)); label((-2,0),"$14{-}x$",red+fontsize(11)); label((0,0),"$3{-}y$",red+fontsize(11)); [/asy]
Since $x$ is greater than the other three, we have $x>14-x,$ or $x>7.$
Therefore, the smallest possible value of $x$ is $\boxed{\textbf{(D) } 8}.$
~vetaltekdi6

## Solution 4 (Answer Choices)
Note that the sum of the rows and columns must be $8+5-1=12$ . We proceed to test the answer choices.
Testing $\textbf{(A)}$ , when $x = -1$ , the number above $x$ must be $15$ , which contradicts the precondition that the numbers surrounding $x$ is less than $x$ .
Testing $\textbf{(B)}$ , the number above $x$ is $9$ , which does not work.
Testing $\textbf{(C)}$ , the number above $x$ is $8$ , which does not work.
Testing $\textbf{(D)}$ , the number above $x$ is $6$ , which does work. Hence, the answer is $\boxed{\textbf{(D) }8}$ .
We do not need to test $\textbf{(E)}$ , because the problem asks for the smallest value of $x$ .
~MrThinker

## Solution 5 (Super fast! No algebra and no testing any of the answer choices!)
The sum of the numbers in each column and row should be $5+(-1)+8=12$ . If we look at the $1^{\text{st}}$ column, the gray squares (shown below) sum to $12-(-2)=14$ .
[asy] draw((3,3)--(-3,3)); draw((3,1)--(-3,1)); draw((3,-3)--(-3,-3)); draw((3,-1)--(-3,-1)); draw((3,3)--(3,-3)); draw((1,3)--(1,-3)); draw((-3,3)--(-3,-3)); draw((-1,3)--(-1,-3)); label((-2,2),"$-2$"); label((0,2),"$9$"); label((2,2),"$5$"); label((2,0),"$-1$"); label((2,-2),"$8$"); label((-2,-2),"$x$"); filldraw((-3,-3)--(-1,-3)--(-1,-1)--(-3,-1)--cycle, lightgray, black+linewidth(1)); filldraw((-1,-1)--(-3,-1)--(-3,1)--(-1,1)--cycle, lightgray, black+linewidth(1)); label(scale(1)*"All credits for original unedited asymptote for the problem go to whoever made the asymptote in the 'Problem' section.", (-0,-5), S); [/asy]
If square $x$ has to be greater than or equal to the three blank squares, then the least $x$ can be is half the sum of the value of the gray squares, which is $14\div2=7$ . But square $x$ has to be greater than and not greater than or equal to the three blank squares, so the least $x$ can be is $7+1=8$ . Testing for the other rows and columns (it might be smaller than the other two squares!), we find that the smallest $x$ can be is indeed $8$ ; the other two squares are less than $8$ . Therefore, the answer is $\boxed{\text{(D) }8}$ .
~ JoyfulSapling

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=2489 ~hsnacademy

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=Bbea8RWE2sMWN6xl&t=3643
~Math-X

## Video Solution (🚀Super Fast. Just 1 min!🚀)
https://youtu.be/7J4EGPaB29Y
~Education, the Study of Everything

## Video Solution
https://youtu.be/0hHlpIVeFjg

## Video Solution
https://www.youtube.com/watch?v=xnGQffaxYAA
~Mathematical Dexterity

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=1857
~Interstigation

## Video Solution
https://youtu.be/hs6y4PWnoWg?t=369
~STEMbreezy

## Video Solution
https://youtu.be/DXFwzrOF4b4
~savannahsolver

## Video Solution
https://www.youtube.com/watch?v=FINk9LgSJpU
~David

## Video Solution by Dr. David
https://youtu.be/c2nArwXxqVI
### See Also