# 2020 AMC 8 Problem 20

## Problem

A scientist walking through a forest recorded as integers the heights of $5$ trees standing in a row. She observed that each tree was either twice as tall or half as tall as the one to its right. Unfortunately some of her data was lost when rain fell on her notebook. Her notes are shown below, with blanks indicating the missing numbers. Based on her observations, the scientist was able to reconstruct the lost data. What was the average height of the trees, in meters?

\[\begingroup \setlength{\tabcolsep}{10pt} \renewcommand{\arraystretch}{1.5} \begin{tabular}{|c|c|} \hline Tree 1 & \rule{0.4cm}{0.15mm} meters \\ Tree 2 & 11 meters \\ Tree 3 & \rule{0.5cm}{0.15mm} meters \\ Tree 4 & \rule{0.5cm}{0.15mm} meters \\ Tree 5 & \rule{0.5cm}{0.15mm} meters \\ \hline Average height & \rule{0.5cm}{0.15mm}\text{ .}2 meters \\ \hline \end{tabular} \endgroup\] $\textbf{(A) }22.2 \qquad \textbf{(B) }24.2 \qquad \textbf{(C) }33.2 \qquad \textbf{(D) }35.2 \qquad \textbf{(E) }37.2$

## Solution 1
We will show that $22$ , $11$ , $22$ , $44$ , and $22$ meters are the heights of the trees from left to right. We are given that all tree heights are integers, so since Tree 2 has height $11$ meters, we can deduce that Trees 1 and 3 both have a height of $22$ meters. There are now three possible cases for the heights of Trees 4 and 5 (in order for them to be integers), namely heights of $11$ and $22$ , $44$ and $88$ , or $44$ and $22$ . Checking each of these, in the first case, the average is $17.6$ meters, which doesn't end in $.2$ as the problem requires. Therefore, we consider the other cases. With $44$ and $88$ , the average is $37.4$ meters, which again does not end in $.2$ , but with $44$ and $22$ , the average is $24.2$ meters, which does. Consequently, the answer is $\boxed{\textbf{(B) }24.2}$ .

## Solution 2
Notice the average height of the trees ends with $0.2$ ; therefore, the sum of all five heights of the trees must end with $1$ or $6$ . ( $0.2$ $\cdot$ $5$ = $1$ ) We already know Tree $2$ is $11$ meters tall. Both Tree $1$ and Tree $3$ must $22$ meters tall - since neither can be $5.5$ . Once again, apply our observation for solving for the Tree $4$ 's height. Tree $4$ can't be $11$ meters for the sum of the five tree heights to still end with $1$ . Therefore, the Tree $4$ is $44$ meters tall. Now, Tree $5$ can either be $22$ or $88$ . Find the average height for both cases of Tree $5$ . Doing this, we realize the Tree $5$ must be $22$ for the average height to end with $0.2$ and that the average height is $\boxed{\textbf{(B)}\ 24.2}$ .

## Solution 3
As in Solution 1, we shall show that the heights of the trees are $22$ , $11$ , $22$ , $44$ , and $22$ meters. Let $S$ be the sum of the heights, so that the average height will be $\frac{S}{5}$ meters. We note that $0.2 = \frac{1}{5}$ , so in order for $\frac{S}{5}$ to end in $.2$ , $S$ must be one more than a multiple of $5$ . Moreover, as all the heights are integers, the heights of Tree 1 and Tree 3 are both $22$ meters. At this point, our table looks as follows: \[\begingroup \setlength{\tabcolsep}{10pt} \renewcommand{\arraystretch}{1.5} \begin{tabular}{|c|c|} \hline Tree 1 & 22 meters \\ Tree 2 & 11 meters \\ Tree 3 & 22 meters \\ Tree 4 & \rule{0.5cm}{0.15mm} meters \\ Tree 5 & \rule{0.5cm}{0.15mm} meters \\ \hline Average height & \rule{0.5cm}{0.15mm}\text{ .}2 meters \\ \hline \end{tabular} \endgroup\]
If Tree 4 now has a height of $11$ , then Tree 5 would need to have height $22$ , but in that case $S$ would equal $88$ , which is not $1$ more than a multiple of $5$ . So we instead take Tree 4 to have height $44$ . Then the sum of the heights of the first 4 trees is $22+11+22+44 = 99$ , so using a height of $22$ for Tree 5 gives $S=121$ , which is $1$ more than a multiple of $5$ (whereas $88$ gives $S = 187$ , which is not). Thus the average height of the trees is $\frac{121}{5} = \boxed{\textbf{(B) }24.2}$ meters.

## Solution 4
Since we know that the tree heights have to be integers, then it is immediate that Tree 1 and 3 have a height of $22$ . Now using the information given by the last column (that the average of the heights of the trees ends in $.2$ ), we can tell that the sum of all the heights of the trees ends in either $1$ or $6$ , because those are the only numbers from $0$ to $9$ that are congruent to $1$ after taking modulo $5$ . The two multiples of eleven (eleven because all of the tree heights have to be a multiple of eleven if they are integers) that come to mind are $66$ and $121$ . Since the sum of the heights of Tree 1, 2, and 3 is already $55$ , we know that $66$ is impossible to obtain. Then, we can decide with relative confidence that the answer should be $\frac{121}{5} = \boxed{\textbf{(B) }24.2}$ .
P.S. : We can check our solution by trying to obtain $121$ . Surely enough, we have Tree 1 = $22$ , Tree 2 = $11$ , Tree 3 = $22$ , Tree 4 = $44$ , and Tree 5 = $22$ . These all add up to get $121$ .

## Solution 5 (basic modular arithmetic)
Since her average ends with 0.2, the sum of her tree heights must be $\equiv 1 \pmod {5}$ . If Tree 1's height is $a$ , Tree 3's is $b$ , Tree 4's is $c$ , and Tree 5's is $d$ , then we $a$ and $b$ are both 22, since all of the tree heights are integers. Now we have $22+11+22+c+d \equiv 1 \pmod {5}$ . Simplifying, we get $c+d \equiv 1 \pmod {5}$ . The only possible combination of $c$ and $d$ that abides the condition are 44 and 22, respectively. Adding these up, we get 121, and $\frac{121}{5}$ is $\boxed{\textbf{(B) }24.2}$ .
-kn07

## Video Solution by Pi Academy (🚀 Very fast, Easy to Understand 🚀)
https://youtu.be/86TYu-cr0WI?si=E29GMDnSKEY0K9gx

## Video Solutions
https://www.youtube.com/watch?v=bHNrBwwUCMI ~NiuniuMaths
https://youtu.be/UnVo6jZ3Wnk?si=1OAhRlAjzYP_EzBa&t=3750 ~Math-X
https://youtu.be/swfsLlZVGbM
~Education, the Study of Everything
https://youtu.be/PCb5vOIioJA
Please like and subscribe!
https://youtu.be/uCV9-WpaIjw
~savannahsolver
https://youtu.be/VnOecUiP-SA
https://youtu.be/YnwkBZTv5Fw?t=1045 ~Interstigation