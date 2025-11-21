# 2004 AIME II Problem 5

## Problem

In order to complete a large job, $1000$ workers were hired, just enough to complete the job on schedule. All the workers stayed on the job while the first quarter of the work was done, so the first quarter of the work was completed on schedule. Then $100$ workers were laid off, so the second quarter of the work was completed behind schedule. Then an additional $100$ workers were laid off, so the third quarter of the work was completed still further behind schedule. Given that all workers work at the same rate, what is the minimum number of additional workers, beyond the $800$ workers still on the job at the end of the third quarter, that must be hired after three-quarters of the work has been completed so that the entire project can be completed on schedule or before?

## Solution 1
A train is traveling at $1000$ miles per hour and has one hour to reach its destination $1000$ miles away. After $15$ minutes and $250$ miles it slows to $900$ mph, and thus takes $\frac{250}{900}(60)=\frac{50}{3}$ minutes to travel the next $250$ miles. Then it slows to $800$ mph, so the next quarter takes $\frac{250}{800}(60)=\frac{150}{8}$ . The train then has $60-15-\frac{50}{3}-\frac{150}{8}=230/24$ minutes left to travel 250 miles, and doing the arithmetic shows that during this last stretch it must travel more than $1565$ mph to make it on time. Therefore the company needs to add $1566-800 = \boxed{766}$ more workers.
Solution by rocketscience

## Solution 2
Let each worker's speed be $w$ , the entire time be $t$ , and the total work be $1$ .
From the initial problem statement, we have $1000w\cdot\frac{1}{4}t=\frac{1}{4}$ .
We need to find the time the next quarter takes to complete the same amount of work, which is $\frac{1000}{900}\cdot\frac{1}{4}\cdot t=\frac{5}{18}t$ .
Similarly, we find that the time the third quarter takes is $\frac{1000}{800}\cdot\frac{1}{4}\cdot t=\frac{5}{16}t$ .
Finally, the time the last quarter takes is $t\left[1-\left(\frac{1}{4}+\frac{5}{18}+\frac{5}{16}\right)\right]=\frac{23}{144}t$ .
We then let the number of workers needed be $x$ , so we have the equation $\left(800+x\right)w\cdot\frac{23}{144}t=\frac{1}{4}$ . Dividing by the first equation, we have
\[\frac{800+x}{1000}\cdot\frac{\frac{23}{144}}{\frac{1}{4}}=1\] \[\frac{800+x}{1000}\cdot\frac{23}{36}=1\] \[800+x=\frac{36000}{23}\] \[x=\frac{17600}{23}.\]
We can't have a part of a worker, so we take the ceiling of $x$ , which we find to be $\boxed{766}$ .
-flyhawkeye

## Solution 3 (Very fast, the one I used on the test)
Suppose $1000$ workers can complete one quarter of the job in one day. After the first day, there were $900$ workers remaining so the second quarter was completed in $\frac{10}{9}$ days. Now there are only $800$ workers remaining so the third quarter can be completed in $\frac{10}{8}$ days. It has been $1+\frac{10}{9}+\frac{10}{8}=\frac{121}{36}$ days since the job started, and we still have $\frac{23}{36}$ days to complete the last quarter of the job, so we need $\frac{36}{23}$ of $1000$ workers, or $1565.2173913$ . Since we can’t hire fractional workers, $1566-800=\boxed{766}$ must be the answer.
These problems are copyrighted © by the Mathematical Association of America.