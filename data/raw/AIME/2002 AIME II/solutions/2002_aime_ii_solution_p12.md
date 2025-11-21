# 2002 AIME II Problem 12

## Problem

A basketball player has a constant probability of $.4$ of making any given shot, independent of previous shots. Let $a_n$ be the ratio of shots made to shots attempted after $n$ shots. The probability that $a_{10} = .4$ and $a_n\le.4$ for all $n$ such that $1\le n\le9$ is given to be $p^aq^br/\left(s^c\right)$ where $p$ , $q$ , $r$ , and $s$ are primes, and $a$ , $b$ , and $c$ are positive integers. Find $\left(p+q+r+s\right)\left(a+b+c\right)$ .

## Solutions

## Solution 1
We graph the $10$ shots on a grid. Suppose that a made shot is represented by a step of $(0,1)$ , and a missed shot is represented by $(1,0)$ . Then the basketball player's shots can be represented by the number of paths from $(0,0)$ to $(6,4)$ that always stay below the line $y=\frac{2x}{3}$ . We can find the number of such paths using a Pascal's Triangle type method below, computing the number of paths to each point that only move right and up. [asy] size(150); for (int i=0;i<7;++i) {draw((i,0)--(i,4));} for (int i=0;i<5;++i) {draw((0,i)--(6,i));} draw((0,0)--(6,4),dashed); label("$1$",(0,0),SE,fontsize(8)); label("$1$",(1,0),SE,fontsize(8)); label("$1$",(2,0),SE,fontsize(8)); label("$1$",(2,1),SE,fontsize(8)); label("$1$",(3,0),SE,fontsize(8)); label("$2$",(3,1),SE,fontsize(8)); label("$2$",(3,2),SE,fontsize(8)); label("$1$",(4,0),SE,fontsize(8)); label("$3$",(4,1),SE,fontsize(8)); label("$5$",(4,2),SE,fontsize(8)); label("$1$",(5,0),SE,fontsize(8)); label("$4$",(5,1),SE,fontsize(8)); label("$9$",(5,2),SE,fontsize(8)); label("$9$",(5,3),SE,fontsize(8)); label("$1$",(6,0),SE,fontsize(8)); label("$5$",(6,1),SE,fontsize(8)); label("$14$",(6,2),SE,fontsize(8)); label("$23$",(6,3),SE,fontsize(8)); label("$23$",(6,4),SE,fontsize(8)); [/asy] Therefore, there are $23$ ways to shoot $4$ makes and $6$ misses under the given conditions. The probability of each possible sequence occurring is $(.4)^4(.6)^6$ . Hence the desired probability is \[\frac{23\cdot 2^4\cdot 3^6}{5^{10}},\] and the answer is $(23+2+3+5)(4+6+10)=\boxed{660}$ .

## Solution 2
The first restriction is that $a_{10} = .4$ , meaning that the player gets exactly 4 out of 10 baskets. The second restriction is $a_n\le.4$ . This means that the player may never have a shooting average over 40%. Thus, the first and second shots must fail, since $\frac{1}{1}$ and $\frac{1}{2}$ are both over $.4$ , but the player may make the third basket, since $\frac{1}{3} \le .4$ In other words, the earliest the first basket may be made is attempt 3. Using similar reasoning, the earliest the second basket may be made is attempt 5, the earliest the third basket may be made is attempt 8, and the earliest the fourth basket may be made is attempt 10.
Using X to represent a basket and O to represent a failure, this 'earliest' solution may be represented as:
OOXOXOOXOX
To simplify counting, note that the first, second, and tenth shots are predetermined. The first two shots must fail, and the last shot must succeed. Thus, only slots 3-9 need to be counted, and can be abbreviated as follows:
XOXOOXO
The problem may be separated into five cases, since the first shot may be made on attempt 3, 4, 5, 6, or 7. The easiest way to count the problem is to remember that each X may slide to the right, but NOT to the left.
First shot made on attempt 3:
XOXOOXO
XOXOOOX
XOOXOXO
XOOXOOX
XOOOXXO
XOOOXOX
XOOOOXX
Total - 7
First shot made on attempt 4:
Note that all that needs to be done is change each line in the prior case from starting with "XO....." to "OX.....".
Total - 7
First shot made on attempt 5:
OOXXOXO
OOXXOOX
OOXOXXO
OOXOXOX
OOXOOXX
Total - 5
First shot made on attempt 6:
OOOXXXO
OOOXXOX
OOOXOXX
Total - 3
First shot made on attempt 7:
OOOOXXX
Total - 1
The total number of ways the player may satisfy the requirements is $7+7+5+3+1=23$ .
The chance of hitting any individual combination (say, for example, OOOOOOXXXX) is $\left(\frac{3}{5}\right)^6\left(\frac{2}{5}\right)^4$
Thus, the chance of hitting any of these 23 combinations is $23\left(\frac{3}{5}\right)^6\left(\frac{2}{5}\right)^4 = \frac{23\cdot3^6\cdot2^4}{5^{10}}$
Thus, the final answer is $(23+3+2+5)(6+4+10)=\boxed{660}$

## Solution 3
Note $a_{10}=.4$ . Therefore the player made 4 shots out of 10. He must make the 10th shot, because if he doesn't, then $a_9=\frac{4}{9}>.4$ . Since $a_n\leq .4$ for all $n$ less than 11, we know that $a_1=a_2=0$ . Now we must look at the 3rd through 9th shot.
Now let's take a look at those un-determined shots. Let's put them into groups: the 3rd, 4th, and 5th shots in group A, and the 6th, 7th, 8th, and 9th shots in group B. The total number of shots made in groups A and B must be 3, since the player makes the 10th shot. We cannot have all three shots made in group A, since $a_5\leq .4$ . Therefore we can have two shots made, one shot made, or no shots made in group A.
Case 1: Group A contains no made shots.
The number of ways this can happen in group A is 1. Now we must arrange the shots in group B accordingly. There are four ways to arrange them total, and all of them work. There are $\textbf{4}$ possibilities here.
Case 2: Group A contains one made shot.
The number of ways this could happen in group A is 3. Now we must arrange the shots in group B accordingly. There are six ways to arrange them total, but the arrangement "hit hit miss miss" fails, because that would mean $a_7=\frac{3}{7}>.4$ . All the rest work. Therefore there are $3\cdot5=\textbf{15}$ possibilities here.
Case 3: Group A contains two made shots.
The number of ways this could happen in group A is 2 (hit hit miss doesn't work but the rest do). Now we must arrange the shots in group B accordingly. Note hit miss miss miss and miss hit miss miss fail. Therefore there are only 2 ways to do this, and there are $2\cdot 2=\textbf{4}$ total possibilities for this case.
Taking all these cases into account, we find that there are $4+15+4=23$ ways to have $a_{10} = .4$ and $a_n\leq .4$ . Each of these has a probability of $.4^4\cdot.6^6=\frac{2^4\cdot 3^6}{5^{10}}$ . Therefore the probability that we have $a_{10} = .4$ and $a_n\leq .4$ is $\frac{23\cdot2^4\cdot3^6}{5^{10}}$ . Now we are asked to find the product of the sum of the primes and the sum of the exponents, which is $(23+2+3+5)(4+6+10)=33\cdot20=\boxed{660}$ .
These problems are copyrighted © by the Mathematical Association of America.