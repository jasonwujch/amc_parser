# 2013 AIME II Problem 7

## Problem

A group of clerks is assigned the task of sorting $1775$ files. Each clerk sorts at a constant rate of $30$ files per hour. At the end of the first hour, some of the clerks are reassigned to another task; at the end of the second hour, the same number of the remaining clerks are also reassigned to another task, and a similar assignment occurs at the end of the third hour. The group finishes the sorting in $3$ hours and $10$ minutes. Find the number of files sorted during the first one and a half hours of sorting.

## Solution
There are $x$ clerks at the beginning, and $t$ clerks are reassigned to another task at the end of each hour. So, $30x+30(x-t)+30(x-2t)+30\cdot\frac{10}{60} \cdot (x-3t)=1775$ , and simplify that we get $19x-21t=355$ . Now the problem is to find a reasonable integer solution. Now we know $x= \frac{355+21t}{19}$ , so $19$ divides $355+21t$ , AND as long as $t$ is a integer, $19$ must divide $2t+355$ . Now, we suppose that $19m=2t+355$ , similarly we get $t=\frac{19m-355}{2}$ , and so in order to get a minimum integer solution for $t$ , it is obvious that $m=19$ works. So we get $t=3$ and $x=22$ . One and a half hour's work should be $30x+15(x-t)$ , so the answer is $\boxed{945}$ .

## Solution 2
We start with the same approach as solution 1 to get $19x-21t=355$ . Then notice that $21t + 355 \equiv 0 \pmod{19}$ , or $2t-6 \equiv 0 \pmod{19}$ , giving the smallest solution at $t=3$ . We find that $x=22$ . Then the number of files they sorted will be $30x+15(x-t)=660+285=\boxed{945}.$

## Solution 3 (More rigorous explanation)
From solution one, we can obtain $19x-21t=355$ where $x$ is the number of clerks at the beginning and $t$ is the amount of clerks removed at the end of each hour. Since the number of clerks removed must be less than the amount of clerks at the beginning, we can form the inequality $x > 3t$ . From here, we can replace $21t$ with $7x$ and form the inequality $19x-7x<355$ . This means that $x < \frac{355}{12}$ or $x \le 29$ . We can rewrite our equation at the beginning to become $19x = 355+21t$ . Because $355 \equiv 13 \pmod {19}$ and $21 \equiv 2 \pmod {19}$ , we can figure out that the minimum value of $t$ will be 3 as $13 + 2*3 = 19$ . From here, we can find $x = 22$ and solve that the number of files the clerks sorted in the first 1 hour and 30 minutes is $30(22) + 15(22 - 3) = 660 + 285 = \boxed{945}$ . If we increase $t$ by $19$ , we will have to increase $x$ by $21$ which results in $x$ being $43$ , thus breaking our inequality of $x \le 29$ . Therefore, the only solutions for x and t where both are integers are 22 and 3, respectively.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .