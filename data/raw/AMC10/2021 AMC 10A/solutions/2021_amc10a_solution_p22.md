# 2021 AMC 10A Problem 22

## Problem

Hiram's algebra notes are $50$ pages long and are printed on $25$ sheets of paper; the first sheet contains pages $1$ and $2$ , the second sheet contains pages $3$ and $4$ , and so on. One day he leaves his notes on the table before leaving for lunch, and his roommate decides to borrow some pages from the middle of the notes. When Hiram comes back, he discovers that his roommate has taken a consecutive set of sheets from the notes and that the average (mean) of the page numbers on all remaining sheets is exactly $19$ . How many sheets were borrowed?

$\textbf{(A)} ~10\qquad\textbf{(B)} ~13\qquad\textbf{(C)} ~15\qquad\textbf{(D)} ~17\qquad\textbf{(E)} ~20$

## Solution 1
Suppose the roommate took sheets $a$ through $b$ , or equivalently, page numbers $2a-1$ through $2b$ . Because there are $(2b-2a+2)$ numbers taken, \[\frac{(2a-1+2b)(2b-2a+2)}{2}+19(50-(2b-2a+2))=\frac{50\cdot51}{2} \implies (2a+2b-39)(b-a+1)=\frac{50\cdot13}{2}=25\cdot13.\] The first possible solution that comes to mind is if $2a+2b-39=25, b-a+1=13 \implies a+b=32, b-a=12$ , which indeed works, giving $b=22$ and $a=10$ . The answer is $22-10+1=\boxed{\textbf{(B)} ~13}$ .
~Lcz

## Solution 2
Suppose the smallest page number borrowed is $k,$ and $n$ pages are borrowed. It follows that the largest page number borrowed is $k+n-1.$
We have the following preconditions:
1. $n$ pages are borrowed means that $\frac{n}{2}$ sheets are borrowed, from which $n$ must be even and $n<50.$
1. $k$ must be odd, as the smallest page number borrowed is on the right side (odd-numbered).
1. $1+2+3+\cdots+50=\frac{51(50)}{2}=1275.$
1. The sum of the page numbers borrowed is $\frac{(2k+n-1)n}{2}.$
Together, we have \begin{align*} \frac{1275-\frac{(2k+n-1)n}{2}}{50-n}&=19 \\ 1275-\frac{(2k+n-1)n}{2}&=19(50-n) \\ 2550-(2k+n-1)n&=38(50-n) \\ 2550-(2k+n-1)n&=1900-38n \\ 650&=(2k+n-39)n. \end{align*} The factors of $650$ are \[1,2,5,10,13,25,26,50,65,130,325,650.\] Since $n$ is even and $n<50,$ we only have a few cases to consider: \[\begin{array}{c|c|c} & & \\ [-2.25ex] \boldsymbol{n} & \boldsymbol{2k+n-39} & \boldsymbol{k} \\ [0.5ex] \hline & & \\ [-2ex] 2 & 325 & 181 \\ 10 & 65 & 47 \\ 26 & 25 & 19 \end{array}\] Since $1\leq k \leq 49,$ only $k=47$ or $k=19$ is possible. If $k=47,$ then there will not be enough pages when we take $10$ pages out starting from page $47.$ Therefore, the only possibility is $k=19.$ We conclude that $n=26$ pages, or $\frac n2=\boxed{\textbf{(B)} ~13}$ sheets, are borrowed.
~MRENTHUSIASM

## Solution 2a (Basically the same thing as Solution 2)
Suppose the smallest page number borrowed is $k,$ and the number of sheets is $n$ . It follows that the largest page number borrowed is $k+2n-1.$
Then the total sum of pages he took is $(2k + 2n - 1)2n/2 = (2k + 2n - 1)n$ .
The total sum of all the pages is $\frac{50\cdot51}{2} = 1275$ .
With the mean being 19, we can write $\frac{1275 - (2k + 2n - 1)n}{50 - 2n} = 19$ .
Simplifying, $1275 - (2k + 2n - 1)n = 950 - 38n$ and $325 = (2k + 2n - 39)n$ .
Since $n$ (the number of sheets) is a positive integer, it must be a factor of $325 = 25\cdot13$ . From the answer choices, $\boxed{\textbf{(B)} ~13}$ is the only divisor of $325$ .
-unhappyfarmer

## Solution 3
Let $n$ be the number of sheets borrowed, with an average page number $k+25.5$ . The remaining $25-n$ sheets have an average page number of $19$ which is less than $25.5$ , the average page number of all $50$ pages, therefore $k>0$ . Since the borrowed sheets start with an odd page number and end with an even page number we have $k \in \mathbb N$ . We notice that $n < 25$ and $k \le (49+50)/2-25.5=24<25$ .
The weighted increase of average page number from $25.5$ to $k+25.5$ should be equal to the weighted decrease of average page number from $25.5$ to $19$ , where the weights are the page number in each group (borrowed vs. remained), therefore
\[2nk=2(25-n)(25.5-19)=13(25-n) \implies 13 | n \text{ or } 13 | k\]
Since $n, k < 25$ we have either $n=13$ or $k=13$ . If $n=13$ then $k=6$ . If $k=13$ then $2n=25-n$ which is impossible. Therefore the answer should be $n=\boxed{\textbf{(B)} ~13}$ .
~asops

## Solution 4
Let $(2k-1)-2n$ be pages be borrowed, the sum of the page numbers on those pages is $(2n+2k+1)(n-k)$ while the sum of the rest pages is $1275-(2n+2k+1)(n-k)$ and we know the average of the rest is $\frac{1275-(2n+2k+1)}{50-2n+2k}$ which equals to $19$ ; multiply this out we got $950-38(n-k)=1275-(2n+2k+1)(n-k)$ and we got $(2n+2k-37)(n-k)=325$ . As $325=25\cdot13$ , we can see $n-k=13$ and that is desired $\boxed{\textbf{(B)} ~13}$ .
~bluesoul

## Solution 5
Let $c$ be the number of consecutive sheets Hiram’s roommate borrows, and let $b$ be the number of sheets preceding the $c$ borrowed sheets (i.e. if the friend borrows sheets $3$ , $4$ , and $5$ , then $c=3$ and $b=2$ ).
The sum of the page numbers up till $b$ sheets is $1+2+3+\cdots + 2b=\frac{2b\cdot(2b+1)}{2} = b(2b+1)$ . The last page number of the borrowed sheets would be $2(b+c)$ . Therefore, the sum of the remaining page numbers of the sheets after the $c$ borrowed sheets would be $2(b+c)+1 + 2(b+c)+2+\cdots+50$ .
The total number of page numbers after the borrow would be $50-2c$ .
Thus the average of the page numbers after the borrow would be: \[\frac{b(2b+1)+ 2(b+c)+1 + 2(b+c)+2+\cdots+50}{50-2c} =19.\] By the arithmetic series formula, this turns out to be: \[\frac{b(2b+1)+ \frac{(2(b+c)+1+50)\cdot(50-2c-2b)}{2}}{50-2c} =19\] because in the changed sum, there are $50$ numbers minus $2c$ borrowed numbers and $2b$ numbers from the first $b$ sheets.
This simplifies to \[\frac{b(2b+1)+ (2(b+c)+51)\cdot(25-c-b)}{50-2c} =19 \implies 19(50-2c)= b(2b+1)+ (2b+2c+51)\cdot(25-c-b).\] Noticing that some terms will cancel, we expand, leading to: \[950-38c=2b^2+b+50b-2bc-2b^2+50c-2c^2-2bc+1275-51c-51b\] \[\implies 950-38c=1275-4bc-c-2c^2 \implies 2c^2+4b-37c=325.\] Factoring, we get \[c(2c+4b-37)=325.\] The prime factorization of 325 is $5^2\cdot13$ . Recall that $0\leq c \leq 25$ , so $c$ could be $1$ , $5$ , $13$ , or $25$ .
We can rule out $c=25$ since Hiram would have no paper left over, so the average of the page numbers he has would be $0$ . We can now plug in the other answers for $c$ and we if we get a valid answer for $b$ .
- $c=1 \implies 4b-35=325 \implies 4b=360 \implies b=90$ . Since Hiram only has $25$ sheets, this is clearly wrong and we can rule out $c=1$ .
- $c=5 \implies 10+4b-37=65 \implies 4b = 92 \implies b=23$ . Since $b+c$ is $28$ but we have only $25$ sheets, this is also implausible so we can rule out $c=5$ .
Finally, just to make sure, we test $c=13 \implies 26+4b-37=25 \implies 4b=36 \implies b=9$ .
$b$ is an integer and $b+c=22$ , so everything checks out. The number of consecutive sheets borrowed by Hiram’s friend is $c=\boxed{\textbf{(B)} ~13}$ .
~KingRavi

## Solution 6
The sum of all the page numbers is \[1+2+3+\cdots+50 = 1275.\] If we add the page numbers on each sheet, we get this sequence: \[3, 7, 11, \ldots, 99.\] So we can write the sum of the numbers on the first sheet that the roommate borrowed as $4n+3$ for some nonnegative integer, $n$ . If the roommate borrowed $k$ sheets, he borrowed sheets \[4n+3, 4n+7, \ldots, 4n+4k-1.\] The sum of the numbers in this sequence is \[\frac{k(8n+4k+2)}{2} = 4nk+2k^2+k.\] Since there are $2$ pages per sheet, there are $50-2k$ pages remaining, so the average page number of the remaining sheets is \[\frac{1275 - (4nk+2k^2+k)}{50-2k}.\] Therefore, \[\frac{1275 - (4nk+2k^2+k)}{50-2k} = 19,\] which simplifies to \[2k^2-37k-325 = -4nk.\] Factoring the left-hand side, \[(2k+13)(k-25)=-4nk.\] Since the right-hand side of this equation is divisible by $k$ , the left-hand side must also be divisible by $k$ .
In order for $(2k+13)(k-25)$ to be divisible by $k$ , either $2k+13$ or $k-25$ must be divisible by $k$ . \[\frac{2k+13}{k}=2+\frac{13}{k},\] so $2k+13$ is divisible by $k$ only if $k$ is a factor of $13$ . \[\frac{k-25}{k}=1-\frac{25}{k},\] so $k-25$ is divisible by $k$ only if $k$ is a factor of $25$ .
None of the answer choices are factors of $25$ , but answer choice B is a factor of $13$ . Hence, the answer is $\boxed{\textbf{(B)} ~13}$ .
~ azc1027

## Video Solution by OmegaLearn (Arithmetic Sequences and System of Equations)
https://youtu.be/dWOLIdTxwa4
~ pi_is_3.14

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=28te8OUiVxE
~MRENTHUSIASM
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .