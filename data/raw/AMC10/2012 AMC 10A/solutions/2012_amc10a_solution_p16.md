# 2012 AMC 10A Problem 16

## Problem

Three runners start running simultaneously from the same point on a 500-meter circular track. They each run clockwise around the course maintaining constant speeds of 4.4, 4.8, and 5.0 meters per second. The runners stop once they are all together again somewhere on the circular course. How many seconds do the runners run?

$\textbf{(A)}\ 1,000\qquad\textbf{(B)}\ 1,250\qquad\textbf{(C)}\ 2,500\qquad\textbf{(D)}\ 5,000\qquad\textbf{(E)}\ 10,000$

## Solution 1
First consider the first two runners. The faster runner will lap the slower runner exactly once, or run 500 meters farther. Let $x$ be the time these runners run in seconds.
\[4.8x-4.4x=500 \Rightarrow x=1250\]
Because $4.4(1250)=5500$ is a multiple of 500, it turns out they just meet back at the start line.
Now we must find a time that is a multiple of $1250$ and results in the 5.0 m/s runner to end up on the start line. Every $1250$ seconds, that fastest runner goes $5.0(1250)=6250$ meters. In $2(1250)=2500$ seconds, he goes $5.0(2500)=12500$ meters. Therefore the runners run $\boxed{\textbf{(C)}\ 2,500}$ seconds.

## Solution 2
Working backwards from the answers starting with the smallest answer, if they had run $1000$ seconds, they would have run $4400, 4800, 5000$ meters, respectively. The first two runners have a difference of $400$ meters, which is not a multiple of $500$ (one lap), so they are not in the same place.
If they had run $1250$ seconds, the runners would have run $5500, 6000, 6250$ meters, respectively. The last two runners have a difference of $250$ meters, which is not a multiple of $500$ .
If they had run $2500$ seconds, the runners would have run $11000, 12000, 12500$ meters, respectively. The distance separating each pair of runners is a multiple of $500$ , so the answer is $\boxed{\textbf{(C)}\ 2,500}$ seconds.

## Solution 3
Let $t$ be the time run in seconds, then the difference in meters run between the three runners is $0.2t, 0.4t, 0.6t$ . For them to be at the same location all of them need to be multiples of 500. It is now easy to see that $0.2t=500, 0.4t=1000, 0.6t=1500$ , so $t=\boxed{\textbf{(C)}\ 2,500}$ .

## Solution 4
After $t$ seconds, respectively the runners would've ran $4.4t, 4.8t,$ and $5t$ meters. Their current positions on the track are these values $\pmod{500}$ . We're trying to find the value of $t$ such that \[4.4t \equiv 4.8t \equiv 5t \pmod{500}\] Subtracting $4.4t$ on all sides, we get \[0 \equiv 0.4t \equiv 0.6t \pmod{500}\] Now, we must find a value for $t$ such that both $0.6t$ and $0.4t$ are simultaneously multiples of $500$ .
Plugging in $500$ for $0.4t$ we get $t=1250$ , but this does not work for $0.6t$ ( $750$ isn't a multiple of $500$ ). Plugging in $0.4t=1000$ , we get $t=2500$ , and this does work for $0.6t$ .
Therefore, $t=2500$ and the answer is $\boxed{\textbf{(C) } 2500}$ .
- Note: Modular Arithmetic works only for integral values, so my usage of decimals is technically incorrect but the intuition leads to the right answer

## Solution 5
Similar to the solution above, but is much quicker and does not involve trial and error. This uses decimal mod arithmetic, which can be justified by intuition... After $t$ seconds, respectively the runners would've ran $4.4t, 4.8t,$ and $5t$ meters. These three values are congruent $\pmod{500}$ , so \[4.4t \equiv 4.8t \equiv 5t \pmod{500}\] . Subtract $4.4t$ from all three sides to get $0, 0.4t,$ and $0.6t$ are congruent. Now all we need to find is a value of $t$ for which $0.4t$ and $0.6t$ are congruent $\pmod{500}$ . Subtract $0.4t$ from both sides to get $0.2t$ and $0$ are congruent mod $500$ , or that $0.2t=\dfrac{t}{5}$ is a multiple of $500$ . Let $t=500k$ , so we want $100k$ to be a multiple of $500$ , or $k$ to be a multiple of $5$ . Therefore, the smallest value of $t$ is when $k=5$ , and when $t=500k=500(5)=2500 \space \boxed{(\text{C})}$

## Solution 6 (guessing)
First, we determine the LCM of 44, 48, and 50, which is 600(44) = 26,400. Estimating this (ie. division by 10) gives 2640, and from this, we estimate that the time is 2500 seconds. $\boxed{(\text{C})}$ ~elpianista227
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .