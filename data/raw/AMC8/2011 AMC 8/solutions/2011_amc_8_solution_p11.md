# 2011 AMC 8 Problem 11

## Problem

The graph shows the number of minutes studied by both Asha (black bar) and Sasha (grey bar) in one week. On the average, how many more minutes per day did Sasha study than Asha?

[asy] size(300); real i; defaultpen(linewidth(0.8)); draw((0,140)--origin--(220,0)); for(i=1;i<13;i=i+1) { draw((0,10*i)--(220,10*i)); } label("$0$",origin,W); label("$20$",(0,20),W); label("$40$",(0,40),W); label("$60$",(0,60),W); label("$80$",(0,80),W); label("$100$",(0,100),W); label("$120$",(0,120),W); path MonD=(20,0)--(20,60)--(30,60)--(30,0)--cycle,MonL=(30,0)--(30,70)--(40,70)--(40,0)--cycle,TuesD=(60,0)--(60,90)--(70,90)--(70,0)--cycle,TuesL=(70,0)--(70,80)--(80,80)--(80,0)--cycle,WedD=(100,0)--(100,100)--(110,100)--(110,0)--cycle,WedL=(110,0)--(110,120)--(120,120)--(120,0)--cycle,ThurD=(140,0)--(140,80)--(150,80)--(150,0)--cycle,ThurL=(150,0)--(150,110)--(160,110)--(160,0)--cycle,FriD=(180,0)--(180,70)--(190,70)--(190,0)--cycle,FriL=(190,0)--(190,50)--(200,50)--(200,0)--cycle; fill(MonD,grey); fill(MonL,lightgrey); fill(TuesD,grey); fill(TuesL,lightgrey); fill(WedD,grey); fill(WedL,lightgrey); fill(ThurD,grey); fill(ThurL,lightgrey); fill(FriD,grey); fill(FriL,lightgrey); draw(MonD^^MonL^^TuesD^^TuesL^^WedD^^WedL^^ThurD^^ThurL^^FriD^^FriL); label("M",(30,-5),S); label("Tu",(70,-5),S); label("W",(110,-5),S); label("Th",(150,-5),S); label("F",(190,-5),S); label("M",(-25,85),W); label("I",(-27,75),W); label("N",(-25,65),W); label("U",(-25,55),W); label("T",(-25,45),W); label("E",(-25,35),W); label("S",(-26,25),W);[/asy]

$\textbf{(A)}\ 6\qquad\textbf{(B)}\ 8\qquad\textbf{(C)}\ 9\qquad\textbf{(D)}\ 10\qquad\textbf{(E)}\ 12$

## Solution
Average the differences between each day. We get $10, -10,\text{ } 20,\text{ } 30,-20$ . We find the average of this list to get $\boxed{\textbf{(A)}\ 6}$ . ( In case you were wondering, the way to calculate the average is $\frac{(10+(-10)+20+30+(-20))}{5} = \frac{ 30}{5} = 6$ . So the answer is indeed $\boxed{\textbf{(A)}\ 6}$ )

## Solution 2
This solution may take longer to do than the first solution. In total, Asha studied for 400 minutes a week (80 minutes per day) and Sasha studied for 430 minutes a week (86 minutes per day). 86 - 80 = 6. Therefore, the answer is $\boxed{\textbf{(A)}\ 6}$ .
-MiracleMaths

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=mYn6tNxrWBU

## Video Solution by WhyMath
https://youtu.be/UKjKW6JYQ_A
### See Also