# 2018 AMC 8 Problem 8

## Problem

Mr. Garcia asked the members of his health class how many days last week they exercised for at least 30 minutes. The results are summarized in the following bar graph, where the heights of the bars represent the number of students.

[asy] size(8cm); void drawbar(real x, real h) { fill((x-0.15,0.5)--(x+0.15,0.5)--(x+0.15,h)--(x-0.15,h)--cycle,gray); } draw((0.5,0.5)--(7.5,0.5)--(7.5,5)--(0.5,5)--cycle); for (real i=1; i<5; i=i+0.5) { draw((0.5,i)--(7.5,i),gray); } drawbar(1.0,1.0); drawbar(2.0,2.0); drawbar(3.0,1.5); drawbar(4.0,3.5); drawbar(5.0,4.5); drawbar(6.0,2.0); drawbar(7.0,1.5); for (int i=1; i<8; ++i) { label("$"+string(i)+"$",(i,0.25)); } for (int i=1; i<9; ++i) { label("$"+string(i)+"$",(0.5,0.5*(i+1)),W); } label("Number of Days of Exercise",(4,-0.1)); label(rotate(90)*"Number of Students",(-0.1,2.75)); [/asy] What was the mean number of days of exercise last week, rounded to the nearest hundredth, reported by the students in Mr. Garcia's class?

$\textbf{(A) } 3.50 \qquad \textbf{(B) } 3.57 \qquad \textbf{(C) } 4.36 \qquad \textbf{(D) } 4.50 \qquad \textbf{(E) } 5.00$

## Solution
The mean, or average number of days is the total number of days divided by the total number of students. The total number of days is $1\cdot 1+2\cdot 3+3\cdot 2+4\cdot 6+5\cdot 8+6\cdot 3+7\cdot 2=109$ . The total number of students is $1+3+2+6+8+3+2=25$ . Hence, $\frac{109}{25}=\boxed{\textbf{(C) } 4.36}$ .
This problem is a good example of times when the problem statement may give information that may seem important to solving the problem, but turns out it's just there to mess around with you.
~Nivaar
In my opinion, I think that it's not a good example of that.
~SuperVince1
I don't think it is a good example either.
~Mr_Frog

## Video Solution (CRITICAL THINKING!!!)
https://youtu.be/YUJ29HaLjLo
~Education, the Study of Everything

## Video Solution
https://youtu.be/1bkVulggOEw
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/51K3uCzntWs?t=466
~ pi_is_3.14
### See Also