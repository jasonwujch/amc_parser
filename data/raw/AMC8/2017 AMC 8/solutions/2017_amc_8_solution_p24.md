# 2017 AMC 8 Problem 24

## Problem

Mrs. Sanders has three grandchildren, who call her regularly. One calls her every three days, one calls her every four days, and one calls her every five days. All three called her on December 31, 2016. On how many days during the next year did she not receive a phone call from any of her grandchildren?

$\textbf{(A) }78\qquad\textbf{(B) }80\qquad\textbf{(C) }144\qquad\textbf{(D) }146\qquad\textbf{(E) }152$

## Solution 1 (Principle of Inclusion-Exclusion)
We use Principle of Inclusion-Exclusion. There are $365$ days in the year, and we subtract the days that she gets at least $1$ phone call, which is \[\left \lfloor \frac{365}{3} \right \rfloor + \left \lfloor \frac{365}{4} \right \rfloor + \left \lfloor \frac{365}{5} \right \rfloor.\]
To this result we add the number of days where she gets at least $2$ phone calls in a day because we double subtracted these days, which is \[\left \lfloor \frac{365}{12} \right \rfloor + \left \lfloor \frac{365}{15} \right \rfloor + \left \lfloor \frac{365}{20} \right \rfloor.\]
We now subtract the number of days where she gets three phone calls, which is $\left \lfloor \frac{365}{60} \right \rfloor.$ Therefore, our answer is \[365 - \left( \left \lfloor \frac{365}{3} \right \rfloor + \left \lfloor \frac{365}{4} \right \rfloor + \left \lfloor \frac{365}{5} \right \rfloor \right) + \left( \left \lfloor \frac{365}{12} \right \rfloor + \left \lfloor \frac{365}{15} \right \rfloor + \left \lfloor \frac{365}{20} \right \rfloor \right) - \left \lfloor \frac{365}{60} \right \rfloor = 365 - 285+72 - 6 = \boxed{\textbf{(D) }146}.\]

## Solution 2 (Least Common Multiple)
Note that $\operatorname{lcm}(3,4,5)=60,$ so there is a cycle every $60$ days.
As shown below, all days in a cycle that Mrs. Sanders receives a phone call from any of her grandchildren are colored in red, yellow, or green. [asy] /* Made by MRENTHUSIASM */ size(7cm); fill((2,6)--(3,6)--(3,5)--(2,5)--cycle,red); fill((5,6)--(6,6)--(6,5)--(5,5)--cycle,red); fill((8,6)--(9,6)--(9,5)--(8,5)--cycle,red); fill((1,5)--(2,5)--(2,4.5)--(1,4.5)--cycle,red); fill((4,5)--(5,5)--(5,4.5)--(4,4.5)--cycle,red); fill((7,5)--(8,5)--(8,4)--(7,4)--cycle,red); fill((0,4)--(1,4)--(1,3)--(0,3)--cycle,red); fill((3,4)--(4,4)--(4,3.5)--(3,3.5)--cycle,red); fill((6,4)--(7,4)--(7,3)--(6,3)--cycle,red); fill((9,4)--(10,4)--(10,3.5)--(9,3.5)--cycle,red); fill((2,3)--(3,3)--(3,2)--(2,2)--cycle,red); fill((5,3)--(6,3)--(6,2.5)--(5,2.5)--cycle,red); fill((8,3)--(9,3)--(9,2)--(8,2)--cycle,red); fill((1,2)--(2,2)--(2,1)--(1,1)--cycle,red); fill((4,2)--(5,2)--(5,1.5)--(4,1.5)--cycle,red); fill((7,2)--(8,2)--(8,1.5)--(7,1.5)--cycle,red); fill((0,1)--(1,1)--(1,0)--(0,0)--cycle,red); fill((3,1)--(4,1)--(4,0)--(3,0)--cycle,red); fill((6,1)--(7,1)--(7,0)--(6,0)--cycle,red); fill((9,1)--(10,1)--(10,2/3)--(9,2/3)--cycle,red); fill((3,6)--(4,6)--(4,5)--(3,5)--cycle,yellow); fill((7,6)--(8,6)--(8,5)--(7,5)--cycle,yellow); fill((1,4.5)--(2,4.5)--(2,4)--(1,4)--cycle,yellow); fill((5,5)--(6,5)--(6,4)--(5,4)--cycle,yellow); fill((9,5)--(10,5)--(10,4.5)--(9,4.5)--cycle,yellow); fill((3,3.5)--(4,3.5)--(4,3)--(3,3)--cycle,yellow); fill((7,4)--(8,4)--(8,3)--(7,3)--cycle,yellow); fill((1,3)--(2,3)--(2,2)--(1,2)--cycle,yellow); fill((5,2.5)--(6,2.5)--(6,2)--(5,2)--cycle,yellow); fill((9,3)--(10,3)--(10,2.5)--(9,2.5)--cycle,yellow); fill((3,2)--(4,2)--(4,1)--(3,1)--cycle,yellow); fill((7,1.5)--(8,1.5)--(8,1)--(7,1)--cycle,yellow); fill((1,1)--(2,1)--(2,0)--(1,0)--cycle,yellow); fill((5,1)--(6,1)--(6,0)--(5,0)--cycle,yellow); fill((9,2/3)--(10,2/3)--(10,1/3)--(9,1/3)--cycle,yellow); fill((4,6)--(5,6)--(5,5)--(4,5)--cycle,green); fill((9,6)--(10,6)--(10,5)--(9,5)--cycle,green); fill((4,4.5)--(5,4.5)--(5,4)--(4,4)--cycle,green); fill((9,4.5)--(10,4.5)--(10,4)--(9,4)--cycle,green); fill((4,4)--(5,4)--(5,3)--(4,3)--cycle,green); fill((9,3.5)--(10,3.5)--(10,3)--(9,3)--cycle,green); fill((4,3)--(5,3)--(5,2)--(4,2)--cycle,green); fill((9,2.5)--(10,2.5)--(10,2)--(9,2)--cycle,green); fill((4,1.5)--(5,1.5)--(5,1)--(4,1)--cycle,green); fill((9,2)--(10,2)--(10,1)--(9,1)--cycle,green); fill((4,1)--(5,1)--(5,0)--(4,0)--cycle,green); fill((9,1/3)--(10,1/3)--(10,0)--(9,0)--cycle,green); real cur = 1; for (real i=6; i>0; --i) { for (real j=0; j<10; ++j) { label("$"+string(cur)+"$",(j+0.5,i-0.5)); ++cur; } } add(grid(10,6,linewidth(1.25))); [/asy] The year 2017 has $365$ days, or $6$ cycles and $5$ days.
Together, the answer is $24\cdot6+2=\boxed{\textbf{(D) }146}.$
~MRENTHUSIASM

## Solution 3 (Linearity of Expectation)
For any randomly chosen day, there is a $\frac{2}{3}$ chance the first child does not call her, a $\frac{3}{4}$ chance the second child does not call her and a $\frac{4}{5}$ chance the third child does not call her. So, in a randomly chosen day, there is a $\frac{2}{3} \times \frac{3}{4} \times \frac{4}{5} = \frac{2}{5}$ chance no child calls her.
In particular, this "unrigorous" reasoning becomes rigorous, by linearity of expectation, when we take a sample of $360$ days; over the first $360$ days, $360 \times \frac{2}{5} = 144$ days will go without a phone call. Now, we simply check the remaining days; on day $361$ and $362$ , nobody calls her; on day $363$ , the child that calls every three days will call her; on day $364$ , the child that calls every four days will call her; on day $365$ , the child that calls every five days will call her. Thus, we add two more days to $144$ , to get our answer of $\boxed{\textbf{(D) }146}$ .
~ihatemath123

## Video Solutions
https://youtu.be/9JDGys53Sn8
~savannahsolver
https://www.youtube.com/watch?v=6eJ422kMgs0
~David
### See Also