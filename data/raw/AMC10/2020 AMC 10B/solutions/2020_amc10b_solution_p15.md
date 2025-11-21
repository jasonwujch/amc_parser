# 2020 AMC 10B Problem 15

## Problem

Steve wrote the digits $1$ , $2$ , $3$ , $4$ , and $5$ in order repeatedly from left to right, forming a list of $10,000$ digits, beginning $123451234512\ldots.$ He then erased every third digit from his list (that is, the $3$ rd, $6$ th, $9$ th, $\ldots$ digits from the left), then erased every fourth digit from the resulting list (that is, the $4$ th, $8$ th, $12$ th, $\ldots$ digits from the left in what remained), and then erased every fifth digit from what remained at that point. What is the sum of the three digits that were then in the positions $2019, 2020, 2021$ ?

$\textbf{(A)}\ 7 \qquad\textbf{(B)}\ 9 \qquad\textbf{(C)}\ 10 \qquad\textbf{(D)}\ 11 \qquad\textbf{(E)}\ 12$

## Solution 1 (Simulation)
Note that cycles exist initially and after each round of erasing.
Let the parentheses denote cycles. It follows that:
1. Initially, the list has cycles of length $5:$ \[(12345)=12345123451234512345\cdots.\]
1. To find one cycle after the first round of erasing, we need one cycle of length $\operatorname{lcm}(3,5)=15$ before erasing. So, we first group $\frac{15}{5}=3$ copies of the current cycle into one, then erase: \begin{align*} (12345)&\longrightarrow(123451234512345) \\ &\longrightarrow(12\cancel{3}45\cancel{1}23\cancel{4}51\cancel{2}34\cancel{5}) \\ &\longrightarrow(1245235134). \end{align*} As a quick confirmation, one cycle should have length $15\cdot\left(1-\frac{1}{3}\right)=10$ at this point.
1. To find one cycle after the second round of erasing, we need one cycle of length $\operatorname{lcm}(4,10)=20$ before erasing. So, we first group $\frac{20}{10}=2$ copies of the current cycle into one, then erase: \begin{align*} (1245235134)&\longrightarrow(12452351341245235134) \\ &\longrightarrow(124\cancel{5}235\cancel{1}341\cancel{2}452\cancel{3}513\cancel{4}) \\ &\longrightarrow(124235341452513). \end{align*} As a quick confirmation, one cycle should have length $20\cdot\left(1-\frac{1}{4}\right)=15$ at this point.
1. To find one cycle after the third round of erasing, we need one cycle of length $\operatorname{lcm}(5,15)=15$ before erasing. We already have it here, so we erase: \begin{align*} (124235341452513)&\longrightarrow(1242\cancel{3}5341\cancel{4}5251\cancel{3}) \\ &\longrightarrow(124253415251). \end{align*} As a quick confirmation, one cycle should have length $15\cdot\left(1-\frac{1}{5}\right)=12$ at this point.
Since $2019,2020,2021$ are congruent to $3,4,5$ modulo $12,$ respectively, the three digits in the final positions $2019,2020,2021$ are $4,2,5,$ respectively: \[(12\underline{425}3415251).\] Therefore, the answer is $4+2+5=\boxed{\textbf{(D)}\ 11}.$
~MRENTHUSIASM (inspired by TheBeautyofMath)

## Solution 2 (Simulation)
After erasing every third digit, the list becomes $1245235134\ldots$ repeated. After erasing every fourth digit from this list, the list becomes $124235341452513\ldots$ repeated. Finally, after erasing every fifth digit from this list, the list becomes $124253415251\ldots$ repeated. Since this list repeats every $12$ digits and $2019,2020,2021$ are $3,4,5$ respectively in $\pmod{12},$ we have that the $2019$ th, $2020$ th, and $2021$ st digits are the $3$ rd, $4$ th, and $5$ th digits respectively. It follows that the answer is $4+2+5= \boxed {\textbf{(D)}\ 11}.$

## Solution 3 (Analysis)
Note that cycles exist initially and after each round of erasing.
We will consider one cycle after all three rounds of erasing. Suppose this cycle has length $L$ before any round of erasing. It follows that:
1. Initially, one cycle has length $5,$ from which $L$ must be divisible by $5.$
1. After the first round of erasing, one cycle has length $L\left(1-\frac13\right)=\frac23L,$ from which $L$ must be divisible by $3.$
1. After the second round of erasing, one cycle has length $L\left(1-\frac13\right)\left(1-\frac14\right)=\frac12L,$ from which $L$ must be divisible by $2.$
1. After the third round of erasing, one cycle has length $L\left(1-\frac13\right)\left(1-\frac14\right)\left(1-\frac15\right)=\frac25L,$ from which $L$ must be divisible by $5.$
The least such positive integer $L$ is $\operatorname{lcm}(5,3,2)=30.$ So, there is a repeating pattern for every $30$ digits on the original list. As shown below, the digits erased in the first, second, and third rounds are colored in red, yellow, and green, respectively: [asy] /* Made by MRENTHUSIASM */ size(20cm); for (real i=2.5; i<30; i+=3) { fill((i-0.5,0)--(i-0.5,4)--(i+0.5,4)--(i+0.5,0)--cycle,red); } for (real i=4.5; i<30; i+=6) { fill((i-0.5,0)--(i-0.5,4)--(i+0.5,4)--(i+0.5,0)--cycle,yellow); } fill((7,0)--(7,4)--(8,4)--(8,0)--cycle,green); fill((18,0)--(18,4)--(19,4)--(19,0)--cycle,green); fill((27,0)--(27,4)--(28,4)--(28,0)--cycle,green); for (real i=1; i<5; ++i) { for (real j=0; j<30; ++j) { label("$"+string(1+j%5)+"$",(j+0.5,i-0.5)); } } for (real i=0; i<30; ++i) { label("$\vdots$",(i+0.5,-1/3)); } add(grid(30,4,linewidth(1.25))); [/asy] As indicated by the white squares, each group of $30$ digits on the original list has $\frac25\cdot30=12$ digits remaining on the final list.
Since $2019,2020,2021$ are congruent to $3,4,5$ modulo $12,$ respectively, the three digits in the final positions $2019,2020,2021$ are $4,2,5,$ respectively: [asy] /* Made by MRENTHUSIASM */ size(20cm); for (real i=2.5; i<30; i+=3) { fill((i-0.5,0)--(i-0.5,1)--(i+0.5,1)--(i+0.5,0)--cycle,red); } for (real i=4.5; i<30; i+=6) { fill((i-0.5,0)--(i-0.5,1)--(i+0.5,1)--(i+0.5,0)--cycle,yellow); } fill((7,0)--(7,1)--(8,1)--(8,0)--cycle,green); fill((18,0)--(18,1)--(19,1)--(19,0)--cycle,green); fill((27,0)--(27,1)--(28,1)--(28,0)--cycle,green); for (real j=0; j<30; ++j) { label("$"+string(1+j%5)+"$",(j+0.5,0.5)); } draw((3.5,-1.25)--(3.5,-0.2),linewidth(1.25),EndArrow); draw((6.5,-1.25)--(6.5,-0.2),linewidth(1.25),EndArrow); draw((9.5,-1.25)--(9.5,-0.2),linewidth(1.25),EndArrow); add(grid(30,1,linewidth(1.25))); [/asy] Therefore, the answer is $4+2+5=\boxed{\textbf{(D)}\ 11}.$
~MRENTHUSIASM

## Solution 4 (Analysis)
As the LCM of $3$ , $4$ , and $5$ is $60$ , let us look at a $60$ -digit block of original numbers (many will be erased by Steve). After he erases every third number $\left(\dfrac{1}{3}\right)$ , then every fourth number of what remains $\left(\dfrac{1}{4}\right)$ , then every fifth number of what remains $\left(\dfrac{1}{5}\right)$ , we are left with $\dfrac{2}{3} \cdot \dfrac{3}{4} \cdot \dfrac{4}{5} \cdot 60=24$ digits from this $60$ -digit block. $2019 \equiv 3 \pmod {24}, 2020 \equiv 4 \pmod {24}, 2021 \equiv 5 \pmod {24}$ . Writing out the first few digits of this sequence, we have $\underbrace{1}_{\#1}, \underbrace{2}_{\#2}, \cancel{3}, \underbrace{4}_{\#3}, \cancel{5}, \cancel{1}, \underbrace{2}_{\#4}, \cancel{3}, \cancel{4}, \underbrace{5}_{\#5}, \dots$ . Therefore, our answer is $4+2+5=\boxed{\textbf{(D)}\ 11}$ .
~BakedPotato66

## Solution 5
Lemma: Given a sequence $a_1, a_2, a_3, \cdots$ , and an positive integer $k>2$ . If we erase every $k$ th item in this sequence, and we name $b_1, b_2, b_3, \cdots$ as the remaining sequence. Then we have \[b_{(k-1)m+1}=a_{km+1}, b_{(k-1)m+2}=a_{km+2}, \cdots, b_{(k-1)m+k-1}=a_{km+k-1}.\]
Proof: For $a_{km+j}$ with some $j, 1\le j\le k-1$ , we will have $m$ items removed before this item, so it becomes $b_{(k-1)m+j}$ in the new sequence. Hence, we have $b_{(k-1)m+j}=a_{km+j}$ .
If we start with $a_1, a_2, a_3, \cdots,$ and let $b_1, b_2, \cdots$ be the sequence after removing all the indexes that are multiples of $3$ . Then, we have $b_{2n+1}=a_{3n+1},b_{2n+2}=a_{3n+2}$ .
Similarly, if we start with $b_1, b_2, b_3, \cdots,$ and remove all multiples of $4$ , and get $c_1, c_2, \cdots$ We have $c_{3n+1}=b_{4n+1},c_{3n+2}=b_{4n+2}, c_{3n+3}=b_{4n+3}$ .
If we start with $c_1, c_2, \cdots$ and $d_1, d_2, \cdots$ are remove all multiples of $5$ , we get \[d_{4n+1}=c_{5n+1}, d_{4n+2}=c_{5n+2}, d_{4n+3}=c_{5n+3}, d_{4n+4}=c_{5n+4}.\] Therefore, \begin{align*} d_{2019}&=d_{4\cdot504+3}=c_{5\cdot 504+3}=c_{2523}=c_{3\cdot 840+3}=b_{4\cdot 840+3}=b_{3363}=b_{2\cdot 1681+1}=a_{3\cdot 1681+1}=a_{5044}=a_4=4, \\ d_{2020}&=d_{4\cdot504+4}=c_{5\cdot 504+4}=c_{2524}=c_{3\cdot841+1}=b_{4\cdot841+1}=b_{3365}=b_{2\cdot1682+1}=a_{3\cdot 1682+1}=a_{5047}=a_2=2, \\ d_{2021}&=d_{4\cdot505+1}=c_{5\cdot505+1}=c_{2526}=c_{3\cdot841+3}=b_{4\cdot841+3}=b_{3367}=b_{2\cdot1683+1}=a_{3\cdot1683+1}=a_{5050}=a_5=5, \end{align*} and the answer is $4+2+5=\boxed{\textbf{(D)}\ 11}$ .
~szhangmath

## Video Solution (HOW TO CRITICALLY THINK!!!)
https://youtu.be/yDX4h6YSY8Q
~Education, the Study of Everything

## Video Solution
https://youtu.be/t6yjfKXpwDs?t=1004
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .