# 2016 AIME I Problem 13

## Problem

Freddy the frog is jumping around the coordinate plane searching for a river, which lies on the horizontal line $y = 24$ . A fence is located at the horizontal line $y = 0$ . On each jump Freddy randomly chooses a direction parallel to one of the coordinate axes and moves one unit in that direction. When he is at a point where $y=0$ , with equal likelihoods he chooses one of three directions where he either jumps parallel to the fence or jumps away from the fence, but he never chooses the direction that would have him cross over the fence to where $y < 0$ . Freddy starts his search at the point $(0, 21)$ and will stop once he reaches a point on the river. Find the expected number of jumps it will take Freddy to reach the river.

## Video solution by grogg007
https://www.youtube.com/watch?v=lDqHL-onoiw

## Solution
Clearly Freddy's $x$ -coordinate is irrelevant, so we let $E(y)$ be the expected value of the number of jumps it will take him to reach the river from a given $y$ -coordinate. Observe that $E(24)=0$ , and \[E(y)=1+\frac{E(y+1)+E(y-1)+2E(y)}{4}\] for all $y$ such that $1\le y\le 23$ . Also note that $E(0)=1+\frac{2E(0)+E(1)}{3}$ . This gives $E(0)=E(1)+3$ . Plugging this into the equation for $E(1)$ gives that \[E(1)=1+\frac{E(2)+3E(1)+3}{4},\] or $E(1)=E(2)+7$ . Iteratively plugging this in gives that $E(n)=E(n+1)+4n+3$ . Thus $E(23)=E(24)+95$ , $E(22)=E(23)+91=E(24)+186$ , and $E(21)=E(22)+87=E(24)+273=\boxed{273}$ .

## Video Solution
https://youtu.be/T5F4e8NxfG0

## Video Solution
For those who want more explanation, here is a video explaining the solution: https://www.youtube.com/watch?v=jQCGkOGMlFQ
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .