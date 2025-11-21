# 2020 AMC 10A Problem 8

## Problem

What is the value of \[1+2+3-4+5+6+7-8+\cdots+197+198+199-200?\]

$\textbf{(A) } 9,800 \qquad \textbf{(B) } 9,900 \qquad \textbf{(C) } 10,000 \qquad \textbf{(D) } 10,100 \qquad \textbf{(E) } 10,200$

## Solution 1
Looking at the numbers, you see that every set of $4$ has $3$ positive numbers and 1 negative number. Calculating the sum of the first couple sets gives us $2+10+18...+394$ . Clearly, this pattern is an arithmetic sequence. By using the formula we get $\frac{2+394}{2}\cdot 50=\boxed{\textbf{(B) }9900}$ .
-ViratKohli2018

## Solution 2
Split the even numbers and the odd numbers apart. If we group every 2 even numbers together and add them, we get a total of $50\cdot (-2)=-100$ . Summing the odd numbers is equivalent to summing the first 100 odd numbers, which is equal to $100^2=10000$ . Adding these two, we obtain the answer of $\boxed{\textbf{(B) }9900}$ .

## Solution 3 (bashing)
We can break this entire sum down into $4$ integer bits, in which the sum is $2x$ , where $x$ is the first integer in this bit. We can find that the first sum of every sequence is $4x-3$ , which we plug in for the $50$ bits in the entire sequence is $1+2+3+\cdots+50=1275$ , so then we can plug it into the first term of every sequence equation we got above $4(1275)-3(50)=4950$ , and so the sum of every bit is $2x$ , and we only found the value of $x$ , the sum of the sequence is $4950\cdot2=\boxed{\textbf{(B) } 9900}$ .-middletonkids

## Solution 4
Another solution involves adding everything and subtracting out what is not needed. The first step involves solving $1+2+3+4+5+6+7+8+\cdots+197+198+199+200$ . To do this, we can simply multiply $200$ and $201$ and divide by $2$ to get us $20100$ . The next step involves subtracting out the numbers with minus signs. We actually have to do this twice, because we need to take out the numbers we weren’t supposed to add and then subtract them from the problem. Then, we can see that from $4$ to $200$ , incrementing by $4$ , there are $50$ numbers that we have to subtract. To do this we can do $50$ times $51$ divided by $2$ , and then we can multiply by $4$ , because we are counting by fours, not ones. Our answer will be $5100$ , but remember, we have to do this twice. Once we do that, we will get $10200$ . Finally, we just have to do $20100-10200$ , and our answer is $\boxed{\textbf{(B) }9900}$ .
— $\text{Phineas}1500$

## Solution 5
In this solution, we group every 4 terms. Our groups should be: $1 + 2 + 3 - 4 = 2$ , $5 + 6 + 7 - 8 = 10$ , $9 + 10 + 11 - 12 = 18$ , ... $197 + 198 + 199 - 200 = 394$ . We add them together to get this expression: $2 + 10 + 18 + ... + 394$ . This can be rewritten as $8 * (0 + 1 + 2 + ... + 49) + 100$ . We add this to get $\boxed{\textbf{(B) }9900}$ . ~Baolan

## Solution 6
We can split up this long sum into groups of four integers. Finding the first few sums, we have that $1 + 2 + 3 - 4 = 2$ , $5 + 6 + 7 - 8 = 10$ , and $9 + 10 + 11 - 12 = 18$ . Notice that this is an increasing arithmetic sequence, with a common difference of $8$ . We can find the sum of the arithmetic sequence by finding the average of the first and last terms, and then multiplying by the number of terms in the sequence. The first term is $1 + 2 + 3 - 4$ , or $2$ , the last term is $197 + 198 + 199 - 200$ , or $394$ , and there are $200\div 4$ or $50$ terms. So, we have that the sum of the sequence is $\frac{(394+2)\cdot 50}{2}$ , or $\boxed{\textbf{(B) }9900}$ . ~Arctic_Bunny

## Solution 7
Note that the original expression is equal to \[(1+2+3+\dots+199+200)-2(4(1+2+3+\dots+49+50)).\] Since the sum of the first $n$ positive integers is $\frac{n(n+1)}{2}$ , this is equal to \[\frac{200(201)}{2}-2\left(4\left(\frac{50(51)}{2}\right)\right),\] which can be simplified as \[20100-4(50)(51)=20100-10200.\] Doing the subtraction yields $\boxed{\textbf{(B) }9900}$ . -BorealBear

## Solution 8
We can split the sum into 4 groups so that the terms in these groups have the same common difference of 4 $(1+5+9+...+197)+(2+6+10+...+198)+(3+7+11+...+199)-(4+8+12+...+200)$ . Then, we can use the sum formula. It's equal to $\frac{50\cdot(1+197)}{2} + \frac{50\cdot(2+198)}{2} + \frac{50\cdot(3+199)}{2} - \frac{50\cdot(4+200)}{2}$ . This can also be expressed as $(25\cdot198) + (25\cdot200) + (25\cdot202) - (25\cdot204)$ . And it is equal to $25\cdot(198+200+202-204) = 25\cdot396 = 9900$ . Therefore, the answer is $\boxed{\textbf{(B) }9900}$ . ~kurbanlik_21

## Solution 9
We can split the answer into trios of sums and a difference: (1+2+3) + (5+6+7) + (9+10+11) ... + (197+198+199) - (4+8+12+ ... + 200). We note that each of our trios are consecutive integers so replace them by their average - e.g., 5+6+7 = 3*6.
We have 3 (2+6+10+ ... +198) - 4 (1+2+3+ ... + 50) = 3A - 4B. How we can use a "rainbow" method for A to add 2+198 = 6+194 = .... How many terms do we have? 2, 6, 10, ..., 198 has the same number of terms as the sequence 0, 4, 8, ..., 198-2 = 196, which has the same number of terms as the sequence 0, 1, 2, ..., 196/4 = 49 So there are 50 terms, which means 50/2 = 25 pairs of 200. A is 25*200 B is just 50*51/2 = 25*51
So we have 3(25*200) - 4(25*51) = 100(150-51) = 9900 ~Dilip

## Solution 10 (very similar to solution 7)
We can treat the negative numbers separately than the rest of the sequence.
The negative numbers are as follows: $-4, -8, -12,... -200$
Summing all of the negative numbers up $[-51*(25*4)]$ (first dividing the negative sequence by 4, using Gauss to add all of the numbers up, then re-multiplying by 4), we get $-5100$ .
Now, we can add up the original sequence as if there were no negative numbers (so converting all negatives into positives), to which we get $20100$ by having $201*100$ .
We then subtract $5100$ from $20100$ twice (the first time to make all of the negative numbers $0$ in the sequence, second time to obtain the answer).
And we obtain $\boxed{\textbf{(B) }9900}$ . ~martianrunner

## Video Solution 1
Education, The Study of Everything
https://youtu.be/xoIWkRr0BOo

## Video Solution 2
https://youtu.be/JEjib74EmiY
~IceMatrix

## Video Solution 3
https://youtu.be/8osKFz1CMSc
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .