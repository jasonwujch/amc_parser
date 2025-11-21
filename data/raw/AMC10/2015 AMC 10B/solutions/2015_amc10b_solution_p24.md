# 2015 AMC 10B Problem 24

## Problem

Aaron the ant walks on the coordinate plane according to the following rules. He starts at the origin $p_0=(0,0)$ facing to the east and walks one unit, arriving at $p_1=(1,0)$ . For $n=1,2,3,\dots$ , right after arriving at the point $p_n$ , if Aaron can turn $90^\circ$ left and walk one unit to an unvisited point $p_{n+1}$ , he does that. Otherwise, he walks one unit straight ahead to reach $p_{n+1}$ . Thus the sequence of points continues $p_2=(1,1), p_3=(0,1), p_4=(-1,1), p_5=(-1,0)$ , and so on in a counterclockwise spiral pattern. What is $p_{2015}$ ?

$\textbf{(A) } (-22,-13)\qquad\textbf{(B) } (-13,-22)\qquad\textbf{(C) } (-13,22)\qquad\textbf{(D) } (13,-22)\qquad\textbf{(E) } (22,-13)$

[asy] draw( (0,0)--(1,0)--(1,1)--(-1,1)--(-1,-1)--(1,-1)--(2,-1)--(2,2)--(-2,2)--(-2,-2)--(3,-2)--(3,3) ); label("$p_1$", (1,0), SE); label("$p_4$", (-1,1), NW); label("$p_9$", (2,-1), SE); label("$p_{16}$", (-2,2), NW); label("$p_{25}$", (3,-2), SE); draw( (0,4)--(0,-4) ); label("$y$", (0,4), NW); draw( (-4,0)--(4,0) ); label("$x$", (-4,0), NW); [/asy]

## Solution 1
The first thing we would do is track Aaron's footsteps:
He starts by taking $1$ step East and $1$ step North, ending at $(1,1)$ after $2$ steps and about to head West.
Then he takes $2$ steps West and $2$ steps South, ending at $(-1,-1$ ) after $2+4$ steps, and about to head East.
Then he takes $3$ steps East and $3$ steps North, ending at $(2,2)$ after $2+4+6$ steps, and about to head West.
Then he takes $4$ steps West and $4$ steps South, ending at $(-2,-2)$ after $2+4+6+8$ steps, and about to head East.
From this pattern, we can notice that for any integer $k \ge 1$ he's at $(-k, -k)$ after $2 + 4 + 6 + ... + 4k$ steps, and about to head East. There are $2k$ terms in the sum, with an average value of $(2 + 4k)/2 = 2k + 1$ , so:
\[2 + 4 + 6 + ... + 4k = 2k(2k + 1)\]
If we substitute $k = 22$ into the equation: $44(45) = 1980 < 2015$ . So he has $35$ moves to go. This makes him end up at $(-22+35,-22) = (13,-22) \implies \boxed{\textbf{(D)} (13, -22)}$ .

## Solution 2
We are given that Aaron starts at $(0, 0)$ , and we note that his net steps follow the pattern of $+1$ in the $x$ -direction, $+1$ in the $y$ -direction, $-2$ in the $x$ -direction, $-2$ in the $y$ -direction, $+3$ in the $x$ -direction, $+3$ in the $y$ -direction, and so on, where we add odd and subtract even.
We want $2 + 4 + 6 + 8 + ... + 2n = 2015$ , but it does not work out cleanly. Instead, we get that $2 + 4 + 6 + ... + 2(44) = 1980$ , which means that there are $35$ extra steps past adding $-44$ in the $x$ -direction (and the final number we add in the $y$ -direction is $-44$ ).
So $p_{2015} = (0+1-2+3-4+5...-44+35, 0+1-2+3-4+5...-44)$ .
We can group $1-2+3-4+5...-44$ as $(1-2)+(3-4)+(5-6)+...+(43-44) = -22$ .
Thus $p_{2015} = \boxed{\textbf{(D)}\; (13, -22)}$ .

## Solution 3
Looking at his steps, we see that he walks in a spiral shape. At the $8$ th step, he is on the bottom right corner of the $3\times 3$ square centered on the origin. On the $24$ th step, he is on the bottom right corner of the $5\times 5$ square centered at the origin. It seems that the $p_{n^2-1}$ is the bottom right corner of the $n\times n$ square. This makes sense since, after $n^2-1$ , he has been on $n^2$ dots, including the point $p_0$ . Also, this is only for odd $n$ , because starting with the $1\times 1$ square, we can only add one extra set of dots to each side, so we cannot get even $n$ . Since $45^2=2025$ , $p_{2024}$ is the bottom right corner of the $45\times 45$ square. This point is $\frac{45-1}{2}=22$ over to the right, and therefore $22$ down, so $p_{2024}=(22, -22)$ . Since $p_{2024}$ is $9$ ahead of $p_{2015}$ , we go back $9$ spaces to $\boxed{\textbf{(D)}\; (13, -22)}$ .

## Solution 4 (similar to 3)
We call $p_0$ the first point, $p_1$ the second, and so on. As in Solution 3, we see that he walks in a counterclockwise spiral. We see that his path is traced out by a series of squares with odd-length sides that contain each other. At step $3^2=9,$ he is at $(1,-1)$ ; at step $5^2=25,$ he is at $(2,-2)$ ; and so on. We see that at step $n^2$ where $n$ is an odd number, he is at $(x,-x)$ where $x=\dfrac{n-1}2.$ The closest $n^2$ to $2016$ (we want $p_{2015},$ which is the $2016$ th step) is $45^2=2025,$ so we let $n=45.$ On the $45^2=2025$ th step, $x=\dfrac{45-1}2=22,$ so he is at $(22,-22).$ We see that he approached $(22,-22)$ from the left, so backtrack $2025-2016=9$ steps to the left (i.e. subtracting $9$ from the x-coordinate). Thus, we have $(22-9,-22)=\boxed{\textbf{(D)}~(13,-22).}$ ~Technodoggo

## Solution 5 (Similar to Solution 1)
The first thing is to see the amount of footsteps at points $(k,k)$
We see that at $(1,1)$ he has taken 2 footsteps.
To get to $(2,2)$ , Aaron takes $2$ steps West, $2$ steps South, $3$ steps East, and $3$ steps North.
We can think about this in the following way. For Aaron to get from $(k,k)$ to $(k+1,k+1)$ , he takes $2k+2k+(2k+1)+(2k+1)$ steps = $8k+2$ steps
We can find the total steps taken to get to a point $(k+1,k+1)$
$2+10+18... +8k+2$ = $(4k+2)(k+1$ ) works as a formula
We find that to get to $(22,22)$ this is 2+10+18...+ (4(21)+2)(21)= 1892. We then simply go $88$ steps to get to $(-22,-22)$
and $35$ more to get to the 2015th step at $(13,-22)$ or answer D

## Solution 6
If we graph $p_n$ for a few values of $n$ , we begin to see a particular pattern for $p_n$ when $n$ is a perfect square. For example, $p_0=(0,0)$ , $p_4=(-1,1)$ , $p_{16}=(-2, 2)$ , and so on. Similarly, $p_1=(1,0)$ , $p_9=(2,-1)$ , $p_{25}=(3,-2)$ , and so on. Using this, we can generate a pattern for even and odd squares: \[p_{(2n)^2}=(-n, n)\] \[p_{(2n+1)^2}=(n+1,-n)\]
We notice that $p_{2015}$ is quite close to $p_{2025}=p_{45^2}$ . By the same pattern for odd squares, $p_{2025}=(23,-22)$ . $p_{2015}$ is just $10$ units to the left of $p_{2025}$ . Therefore, $p_{2015}=\boxed{\textbf{(D) }(13,-22)}$ .
~ sid2012

## Solution 7(Similar to 3,4)
Consider $p_k$ . Notice that for $k$ that are odd squares, $p_k$ is in the fourth quadrant, while $k$ that are even squares are located in the second quadrant. Therefore, $p_{2025}$ is in the fourth quadrant. Furthermore, by observation the value of the $y$ coordinate of $p_{k}$ , for odd perfect square $k$ , is $- \frac{ \sqrt{k} -1}{2}$ ; likewise, the absolute value of $x$ coordinate is $\frac{ \sqrt{k} +1}{2}$ . Thus, the coordinates of $p_{2025}$ are $(23,-22)$ . $p_{2015}$ is $10$ steps backward relative to Aaron the ant's movement, so $p_{2015} = (13,-22)$ , and we choose $\boxed{ (D) }$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .