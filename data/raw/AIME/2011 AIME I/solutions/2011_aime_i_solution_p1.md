# 2011 AIME I Problem 1

## Problem

Jar A contains four liters of a solution that is 45% acid. Jar B contains five liters of a solution that is 48% acid. Jar C contains one liter of a solution that is $k\%$ acid. From jar C, $\frac{m}{n}$ liters of the solution is added to jar A, and the remainder of the solution in jar C is added to jar B. At the end both jar A and jar B contain solutions that are 50% acid. Given that $m$ and $n$ are relatively prime positive integers, find $k + m + n$ .

## Solution 1
Jar A contains $\frac{11}{5}$ liters of water, and $\frac{9}{5}$ liters of acid; jar B contains $\frac{13}{5}$ liters of water and $\frac{12}{5}$ liters of acid.
The gap between the amount of water and acid in the first jar, $\frac{2}{5}$ , is double that of the gap in the second jar, $\frac{1}{5}$ . Therefore, we must add twice as much of jar C into the jar $A$ over jar $B$ . So, we must add $\frac{2}{3}$ of jar C into jar $A$ , so $m = 2, n=3$ .
Since jar C contains $1$ liter of solution, we are adding $\frac{2}{3}$ of a liter of solution to jar $A$ . In order to close the gap between water and acid, there must be $\frac{2}{5}$ more liters of acid than liters of water in these $\frac{2}{3}$ liters of solution. So, in the $\frac{2}{3}$ liters of solution, there are $\frac{2}{15}$ liters of water, and $\frac{8}{15}$ liters of acid. So, 80% of the $\frac{2}{3}$ sample is acid, so overall, in jar C, 80% of the sample is acid.
Therefore, our answer is $80 + 2 + 3 = \boxed{85}$ .
~ ihatemath123

## Solution 2
There are $\frac{45}{100}(4)=\frac{9}{5}$ L of acid in Jar A. There are $\frac{48}{100}(5)=\frac{12}{5}$ L of acid in Jar B. And there are $\frac{k}{100}$ L of acid in Jar C. After transferring the solutions from jar C, there will be $4+\frac{m}{n}$ L of solution in Jar A and $\frac{9}{5}+\frac{k}{100}\cdot\frac{m}{n}$ L of acid in Jar A. $6-\frac{m}{n}$ L of solution in Jar B and $\frac{12}{5}+\frac{k}{100}\cdot \left(1-\frac{m}{n}\right)=\frac{12}{5}+\frac{k}{100}-\frac{mk}{100n}$ of acid in Jar B. Since the solutions are 50% acid, we can multiply the amount of acid for each jar by 2, then equate them to the amount of solution. \[\frac{18}{5}+\frac{km}{50n}=4+\frac{m}{n}\] \[\frac{24}{5}-\frac{km}{50n}+\frac{k}{50}=6-\frac{m}{n}\] Add the equations to get \[\frac{42}{5}+\frac{k}{50}=10\] Solving gives $k=80$ . If we substitute back in the original equation we get $\frac{m}{n}=\frac{2}{3}$ so $3m=2n$ . Since $m$ and $n$ are relatively prime, $m=2$ and $n=3$ . Thus $k+m+n=80+2+3=\boxed{085}$ .

## Solution 3
One might cleverly change the content of both Jars.
Since the end result of both Jars are $50\%$ acid, we can turn Jar A into a 1 gallon liquid with $50\%-4(5\%) = 30\%$ acid
and Jar B into 1 gallon liquid with $50\%-5(2\%) =40\%$ acid.
Now, since Jar A and Jar B contain the same amount of liquid, twice as much liquid will be pour into Jar A than Jar B, so $\dfrac{2}{3}$ of Jar C will be pour into Jar A.
Thus, $m=2$ and $n=3$ .
$\dfrac{30\% + \frac{2}{3} \cdot k\%}{\frac{5}{3}} = 50\%$
Solving for $k$ yields $k=80$
So the answer is $80+2+3 = \boxed{085}$

## Solution 4
One may first combine all three jars in to a single container. That container will have $10$ liters of liquid, and it should be $50\%$ acidic. Thus there must be $5$ liters of acid.
Jar A contained $45\% \cdot 4L$ , or $1.8L$ of acid, and jar B $48\% \cdot 5L$ or $2.4L$ . Solving for the amount of acid in jar C, $k = (5 - 2.4 - 1.8) = .8$ , or $80\%$ .
Once one knows that the jar C is $80\%$ acid, use solution 1 to figure out m and n for $k+m+n=80+2+3=\boxed{085}$ .

## Video Solution
https://www.youtube.com/watch?v=_znugFEst6E&t=919s
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .