# 2019 AIME I Problem 1

## Problem

Consider the integer \[N = 9 + 99 + 999 + 9999 + \cdots + \underbrace{99\ldots 99}_\text{321 digits}.\] Find the sum of the digits of $N$ .

## Solution 1
Let's express the number in terms of $10^n$ . We can obtain $(10-1)+(10^2-1)+(10^3-1)+\cdots+(10^{321}-1)$ . By the commutative and associative property, we can group it into $(10+10^2+10^3+\cdots+10^{321})-321$ . We know the former will yield $1111....10$ , so we only have to figure out what the last few digits are. There are currently $321$ 1's. We know the last four digits are $1110$ , and that the others will not be affected if we subtract $321$ . If we do so, we get that $1110-321=789$ . This method will remove three $1$ 's, and add a $7$ , $8$ and $9$ . Therefore, the sum of the digits is $(321-3)+7+8+9=\boxed{342}$ .
-eric2020 -another Eric in 2020
A similar and simpler way to consider the initial manipulations is to observe that adding $1$ to each term results in $(10+100+... 10^{320}+10^{321})$ . There are $321$ terms, so it becomes $11...0$ , where there are $322$ digits in $11...0$ . Then, subtract the $321$ you initially added.
~ BJHHar

## Solution 2
We can see that $9=9$ , $9+99=108$ , $9+99+999=1107$ , all the way to ten nines when we have $11111111100$ . Then, when we add more nines, we repeat the same process, and quickly get that the sum of digits is $\boxed{342}$ since we have to add $9\lfloor \log 321 \rfloor$ to the sum of digits, which is $9\lceil \frac{321}9 \rceil$ .

## Solution 3 (Pattern)
Observe how adding results in the last term but with a $1$ concatenated in front and also a $1$ subtracted ( $09$ , $108$ , $1107$ , $11106$ ). Then for any index of terms, $n$ , the sum is $11...10-n$ , where the first term is of length $n+1$ . Here, that is $\boxed{342}$ .
~BJHHar

## Solution 4 (Official MAA)
Write \begin{align*}N &=(10-1)+(10^2-1)+\cdots+(10^{321}-1)\\ &=10+10^2+10^3+10^4+10^5+10^6+\cdots 10^{321}-321 \\ &=1110-321+10^4+10^5+10^6+\cdots+10^{321}\\ &=789+10^4+10^5+10^6+\cdots+10^{321}\\ \end{align*} The sum of the digits of $N$ is therefore equal to $7+8+9+(321-3)=342$ .

## Video Solution #1(Using Smart Manipulation)
https://youtu.be/JQdad7APQG8?t=22

## Video Solution 2
https://www.youtube.com/watch?v=JFHjpxoYLDk

## Video Solution 3
https://youtu.be/TSKcjht8Rfk
~IceMatrix

## Video Solution 4
https://youtu.be/9X18wCiYw9M
~Shreyas S

## Video Solution 5
https://youtu.be/hzbzEAo9ezA
~savannahsolver

## Video Solution 6 by Steakmath (fast and simple)
https://youtu.be/XNGRjxpPw6I
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .