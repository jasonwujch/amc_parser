# 2014 AIME I Problem 8

## Problem

The positive integers $N$ and $N^2$ both end in the same sequence of four digits $abcd$ when written in base $10$ , where digit $a$ is not zero. Find the three-digit number $abc$ .

## Solution 1 (similar to Solution 3)
We have that $N^2 - N = N(N - 1)\equiv 0\mod{10000}$
Thus, $N(N-1)$ must be divisible by both $5^4$ and $2^4$ . Note, however, that if either $N$ or $N-1$ has both a $5$ and a $2$ in its factorization, the other must end in either $1$ or $9$ , which is impossible for a number that is divisible by either $2$ or $5$ . Thus, one of them is divisible by $2^4 = 16$ , and the other is divisible by $5^4 = 625$ . Noting that $625 \equiv 1\mod{16}$ , we see that $625$ would work for $N$ , except the thousands digit is $0$ . The other possibility is that $N$ is a multiple of $16$ and $N-1$ is a multiple of $625$ . In order for this to happen, \[N-1 \equiv -1 \pmod {16}.\] Since $625 \equiv 1 \pmod{16}$ , we know that $15 \cdot 625 = 9375 \equiv 15 \equiv -1 \mod{16}$ . Thus, $N-1 = 9375$ , so $N = 9376$ , and our answer is $\boxed{937}$ .

## Solution 2 (bashing)
let $N= 10000t+1000a+100b+10c+d$ for positive integer values $t,a,b,c,d$ . When we square $N$ we get that \begin{align*} N^2 &=(10000t+1000a+100b+10c+d)^2\\ &=10^8t^2+10^6a^2+10^4b^2+10^2c^2+d^2+2(10^7ta+10^6tb+10^5tc+10^4td+10^5ab+10^4ac+10^3bc+10^ad+10^2bd+10cd) \end{align*}
However, we don't have to deal with this whole expression but only with its last 4 digits so it is suffices to consider only: \[2000ad+2000bc+100c^2+200bd+20cd+d^2.\] Now we need to compare each decimal digit with $1000a+100b+10c+d$ and see whether the digits are congruent in base 10. we first consider the ones digits:
$d^2\equiv d \pmod{10}.$
This can happen for only 3 values : 1, 5 and 6.
We can try to solve each case:
- Case 1 $(d=1)$
Considering the tenths place, we have that:
$20cd=20c\equiv 10c \pmod {100}$ so $c= 0$ .
Considering the hundreds place we have that
$200bd+100c^2= 200b \equiv 100b \pmod{1000}$ so again $b=0$
now considering the thousands place we have that
$2000ad+2000bc = 2000a \equiv 1000a \pmod {10000}$ so we get $a=0$ but $a$ cannot be equal to $0$ so we consider $d=5.$
- Case 2 $(d=5)$
considering the tenths place we have that:
$20cd+20=100c+20\equiv 20 \equiv 10c \mod {100}$ ( the extra $20$ is carried from $d^2$ which is equal to $25$ ) so $c=2$
considering the hundreds place we have that
$200bd+100c^2+100c= 1000b+600 \equiv600\equiv 100b \pmod{1000}$ ( the extra $100c$ is carried from the tenths place) so $b=6$
now considering the thousands place we have that
$2000ad+2000bc +1000b= 10000a+24000+ 6000\equiv0\equiv 1000a \pmod {10000}$ ( the extra $1000b$ is carried from the hundreds place) so a is equal 0 again
- Case 3 $(d=6)$
considering the tenths place we have that:
$20cd+30=120c+30\equiv 30+20c \equiv 10c \pmod {100}$ ( the extra $20$ is carried from $d^2$ which is equal to $25$ ) if $c=7$ then we have
$30+20 \cdot 7 \equiv 70\equiv7 \cdot 10 \pmod{100}$
so $c=7$
considering the hundreds place we have that
$200bd+100c^2+100c+100= 1200b+4900+800 \equiv200b+700\equiv 100b \pmod{1000}$ ( the extra $100c+100$ is carried from the tenths place)
if $b=3$ then we have
$700+200 \cdot 3 \equiv 300\equiv3 \cdot 100 \pmod {1000}$
so $b=3$
now considering the thousands place we have that
$2000ad+2000bc +1000b+5000+1000= 12000a+42000+ 3000+6000\equiv0\equiv 2000a+1000\equiv 1000a \pmod {10000}$ ( the extra $1000b+6000$ is carried from the hundreds place)
if $a=9$ then we have
$2000 \cdot 9+1000 \equiv 9000\equiv9 \cdot 1000 \pmod {1000}$
so $a=9$
so we have that the last 4 digits of $N$ are $9376$ and $abc$ is equal to $\boxed{937}$

## Solution 3 (general)
By the Chinese Remainder Theorem, the equation $N(N-1)\equiv 0\pmod{10000}$ is equivalent to the two equations: \begin{align*} N(N-1)&\equiv 0\pmod{16},\\ N(N-1)&\equiv 0\pmod{625}. \end{align*} Since $N$ and $N-1$ are coprime, the only solutions are when $(N\mod{16},N\mod{625})\in\{(0,0),(0,1),(1,0),(1,1)\}$ .
Let \[\varphi:\mathbb Z/10000\mathbb Z\to\mathbb Z/16\mathbb Z\times\mathbb Z/625\mathbb Z,\] \[x\mapsto (x\mod{16},x\mod{625}).\] The statement of the Chinese Remainder theorem is that $\varphi$ is an isomorphism between the two rings. In this language, the solutions are $\varphi^{-1}(0,0)$ , $\varphi^{-1}(0,1)$ , $\varphi^{-1}(1,0)$ , and $\varphi^{-1}(1,1)$ . Now we easily see that \[\varphi^{-1}(0,0)=0\] and \[\varphi^{-1}(1,1)=1.\] Noting that $625\equiv 1\pmod{16}$ , it follows that \[\varphi^{-1}(1,0)=625.\] To compute $\varphi^{-1}(0,1)$ , note that \[(0,1)=15(1,0)+(1,1)\] in \[\mathbb Z/16\mathbb Z\times\mathbb Z/625\mathbb Z,\] so since $\varphi^{-1}$ is linear in its arguments (by virtue of being an isomorphism), \[\varphi^{-1}(0,1)=15\varphi^{-1}(1,0)+\varphi^{-1}(1,1)=15\times 625+1=9376.\]
The four candidate digit strings $abcd$ are then $0000,0001,0625,9376$ . Of those, only $9376$ has nonzero first digit, and therefore the answer is $\boxed{937}$ .

## Solution 4 (semi-bashing)
- Note - $\overline{abcd}$ means the number formed when the digits represented by $a$ , $b$ , $c$ , and $d$ are substituted in. $\overline{abcd}\ne a\times b\times c\times d$ .
WLOG, we can assume that $N$ is a 4-digit integer $\overline{abcd}$ . Note that the only $d$ that will satisfy $N$ will also satisfy $d^2\equiv d\pmod{10}$ , as the units digit of $\overline{abcd}^2$ is affected only by $d$ , regardless of $a$ , $b$ , or $c$ .
By checking the numbers 0-9, we see that the only possible values of $d$ are $d=0, 1, 5, 6$ .
Now, we seek to find $c$ . Note that the only $\overline{cd}$ that will satisfy $N$ will also satisfy $\overline{cd}^2 \equiv \overline{cd}\pmod{100}$ , by the same reasoning as above - the last two digits of $\overline{abcd}^2$ are only affected by $c$ and $d$ . As we already have narrowed choices for $d$ , we start reasoning out.
First, we note that if $d=0$ , then $c=0$ , as a number ending in 0, and therefore divisible by 10, is squared, the result is divisible by 100, meaning it ends in two 0's. However, if $N$ ends in $00$ , then recursively, $a$ and $b$ must be $0$ , as a number divisible by 100 squared ends in four zeros. As $a$ cannot be 0, we throw out this possibility, as the only solution in this case is $0$ .
Now, let's assume that $d=1$ . $\overline{cd}$ is equal to $10c + d = 10c + 1$ . Squaring this gives $100c^2 + 20c + 1$ , and when modulo 100 is taken, it must equal $10c + 1$ . As $c$ is an integer, $100c^2$ must be divisible by 100, so $100c^2+20c+1 \equiv 20c + 1\pmod{100}$ , which must be equivalent to $10c + 1$ . Note that this is really $\overline{(2c)1}$ and $\overline{c1}$ , and comparing the 10's digits. So really, we're just looking for when the units digit of $2c$ and $c$ are equal, and a quick check reveals that this is only true when $c=0$ .However, if we extend this process to find $b$ and $a$ , we'd find that they are also 0. The only solution in this case is $1$ , and since $a=0$ here, this is not our solution. Therefore, there are no valid solutions in this case.
Let's assume that $d=5$ . Note that $(10c + 5)^2 = 100c^2 + 100c + 25$ , and when modulo $100$ is taken, $25$ is the remainder. So all cases here have squares that end in 25, so $\overline{cd}=25$ is our only case here. A quick check reveals that $25^2=625$ , which works for now.
Now, let $d=6$ . Note that $(10c + 6)^2 = 100c^2 + 120c + 36$ . Taking modulo 100, this reduces to $20c+36$ , which must be equivalent to $10c+6$ . Again, this is similar to $\overline{(2c+3)6}$ and $\overline{c6}$ , so we see when the units digits of $2c+3$ and $c$ are equal. To make checking faster, note that $2c$ is necessarily even, so $2c+3$ is necessarily odd, so $c$ must be odd. Checking all the odds reveals that only $c=3$ works, so this case gives $76$ . Checking quickly $76^2 = 5776$ , which works for now.
Now, we find $b$ , given two possibilities for $\overline{cd}$ .
Start with $\overline{cd} = 25$ . $\overline{bcd} = 100b + \overline{cd} = 100b + 25.$ Note that if we square this, we get $10000b^2 + 5000b + 625$ , which should be equivalent to $100b + 25$ modulo 1000. Note that, since $b$ is an integer, $10000b^2 + 5000 + 625$ simplifies modulo 1000 to $625$ . Therefore, the only $\overline{bcd}$ that works here is $625$ . $625^2 = 390625$ .
Now, assume that $\overline{cd}=76$ . We have $100b + 76$ , and when squared, becomes $10000b^2 + 15200b + 5776$ , which, modulo 1000, should be equivalent to $100b+76$ . Reducing $10000b^2 + 15200b + 5776$ modulo $1000$ gives $200b + 776$ . Using the same technique as before, we must equate the hundreds digit of $\overline{(2b+7)76}$ to $\overline{b76}$ , or equate the units digit of $2b+7$ and $b$ . Since $2b+7$ is necessarily odd, any possible $b$ 's must be odd. A quick check reveals that $b=3$ is the only solution, so we get a solution of $376$ . $376^2 = 141376$ .
Finally, we solve for $a$ . Start with $\overline{bcd}=625$ . We have $1000a + 625$ , which, squared, gives \[1000000a^2 + 1250000a + 390625,\] and reducing modulo 10000 gives simply 625. So $\overline{abcd}=625$ . However, that makes $a=0$ . Therefore, no solutions exist in this case.
We turn to our last case, $\overline{bcd}=376$ . We have \[1000a + 376^2 = 1000000a^2 + 752000a + 141376,\] and reducing modulo $10000$ gives $2000a + 1376$ , which must be equivalent to $1000a + 376$ . So we must have $\overline{(2a+1)376}$ being equivalent to $\overline{a376}$ modulo 1000. So, the units digit of $2a+1$ must be equal to $a$ . Since $2a+1$ is odd, $a$ must be odd. Lo and behold, the only possibility for $a$ is $a=3$ . Therefore, $\overline{abcd}=9376$ , so our answer is $\boxed{937}$ .

## Solution 5 (easy observations)
We are given that $abcd^2$ ends in $abcd$ , which means that $d^2$ ends in $d$ . The only possible values for which this works is $d=0,1,5,6$ . Notice that if we set $d=0$ , we will have $c=0, b=0, a=0$ , which is not valid since $a\neq0$ . Furthermore, we can see that $d\neq1$ by quickly going over $11^2, 12^2, ..., 19^2$ and seeing that none of those numbers work. From number sense, we know that $B25^2$ ends in $...625$ regardless of $B$ . So, in this case, $b=6$ . However, notice that $76^2$ ends in $...76$ , and we can quickly find that $376^2=141376$ . Going back to $A625^2$ , we notice that no matter what $A$ is, $A625^2=...0625$ . Since $A\neq0$ , this case is not valid (write out $A625^2$ and multiply to see that the thousands digit is $5a+3+2+5+5a=10a+10$ which always ends in $0$ ). We turn our focus to $A376^2$ . Write out $376^2$ and multiply it out to see that the thousands digit is $6a+2+6+2+6a+1=12a+1$ . There is an extra $1$ due to carry over. Quickly testing numbers, the only possible value for $A$ is $9$ . So, $abcd=9376$ and our answer is $abc=\boxed{937}$ .
~hwan

## Video Solution by OmegaLearn
https://youtu.be/gP5pejfcUl8?t=483
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .