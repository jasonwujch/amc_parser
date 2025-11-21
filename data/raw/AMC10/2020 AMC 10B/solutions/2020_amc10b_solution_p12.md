# 2020 AMC 10B Problem 12

## Problem

The decimal representation of \[\dfrac{1}{20^{20}}\] consists of a string of zeros after the decimal point, followed by a $9$ and then several more digits. How many zeros are in that initial string of zeros after the decimal point?

$\textbf{(A)} \text{ 23} \qquad \textbf{(B)} \text{ 24} \qquad \textbf{(C)} \text{ 25} \qquad \textbf{(D)} \text{ 26} \qquad \textbf{(E)} \text{ 27}$

## Solution 1
We have
\[\dfrac{1}{20^{20}} = \dfrac{1}{(10\cdot2)^{20}}=\dfrac{1}{10^{20}\cdot2^{20}}\]
Now we do some estimation. Notice that $2^{20} = 1024^2$ , which means that $2^{20}$ is a little more than $1000^2=1,000,000$ . Multiplying it with $10^{20}$ , we get that the denominator is about $1\underbrace{00\dots0}_{26 \text{ zeros}}$ . Notice that when we divide $1$ by an $n$ digit number as long as n is not a power of 10, there are $n-1$ zeros before the first nonzero digit. This means that when we divide $1$ by the $27$ digit integer $1\underbrace{00\dots0}_{26 \text{ zeros}}$ , there are $\boxed{\textbf{(D) } \text{26}}$ zeros in the initial string after the decimal point. -PCChess

## Solution 2
First rewrite $\frac{1}{20^{20}}$ as $\frac{5^{20}}{10^{40}}$ . Then, we know that when we write this in decimal form, there will be 40 digits after the decimal point. Therefore, we just have to find the number of digits in ${5^{20}}$ .
$\log{5^{20}} = 20\log{5}$ and memming $\log{5}\approx0.69$ (alternatively use the fact that $\log{5} = 1 - \log{2}$ ), $\lfloor{20\log{5}}\rfloor+1=\lfloor{20\cdot0.69}\rfloor+1=13+1=14$ digits.
Our answer is $\boxed{\textbf{(D) } \text{26}}$ .

## Solution 3 (Brute Force)
Just as in Solution $2,$ we rewrite $\dfrac{1}{20^{20}}$ as $\dfrac{5^{20}}{10^{40}}.$ We then calculate $5^{20}$ entirely by hand, first doing $5^5 \cdot 5^5,$ then multiplying that product by itself, resulting in $95,367,431,640,625.$ Because this is $14$ digits, after dividing this number by $10$ fourteen times, the decimal point is before the $9.$ Dividing the number again by $10$ twenty-six more times allows a string of $\boxed{\textbf{(D) } \text{26}}$ zeroes to be formed. -OreoChocolate

## Solution 4 (Alternate Brute Force)
Just as in Solutions $2$ and $3,$ we rewrite $\dfrac{1}{20^{20}}$ as $\dfrac{5^{20}}{10^{40}}.$ We can then look at the number of digits in powers of $5$ . $5^1=5$ , $5^2=25$ , $5^3=125$ , $5^4=625$ , $5^5=3125$ , $5^6=15625$ , $5^7=78125$ and so on. We notice after a few iterations that every power of five with an exponent of $1 \mod 3$ , the number of digits doesn't increase. This means $5^{20}$ should have $20 - 6$ digits since there are $6$ numbers which are $1 \mod 3$ from $0$ to $20$ , or $14$ digits total. This means our expression can be written as $\dfrac{k\cdot10^{14}}{10^{40}}$ , where $k$ is in the range $[1,10)$ . Canceling gives $\dfrac{k}{10^{26}}$ , or $26$ zeroes before the $k$ since the number $k$ should start on where the one would be in $10^{26}$ . ~aop2014

## Solution 5 (Scientific Notation)
We see that $\frac{1}{20^{20}} = 9.5367432 \cdot \cdot \cdot \times 10^{-27}$ . We see that this has $27-1=26$ zeros after the decimal point before coming to $9$ .
Therefore, the answer is $\boxed{\textbf{(D)} ~26}$
but how would this be possible without the use of a calculator?
(Brute Force)

## Solution 6 (Logarithms Without Words)
\begin{align*}|\lceil \log \dfrac{1}{20^{20}} \rceil| &= |\lceil \log 20^{-20} \rceil| \\ &= |\lceil -20 \log(20) \rceil| \\ &= |\lceil -20(\log 10 + \log 2) \rceil| \\ &= |\lceil -20(1 + 0.301) \rceil| \\ &= |\lceil -26.02 \rceil| \\ &= |-26| \\ &= \boxed{\textbf{(D) } \text{26}} \end{align*}
~phoenixfire

## Solution 7 (Algebra)
Define $n$ as the number of consecutive $0$ s after the decimal point in the decimal representation of $\frac{1}{20^{20}}.$ Thus, $\frac{1}{10^n}$ has $n-1$ zeroes followed by a $1$ when expressed as a decimal, and is greater than $\frac{1}{20^{20}}.$ So, we have that \[\frac{1}{10^n} > \frac{1}{20^{20}}.\] Taking the reciprocal and switching signs grants \[20^{20}>10^n.\] We can express $20^{20}$ as $10^{20} \cdot 1024^2.$ We know that \begin{align*} (1000 + 24)^2 &= 1024^2 \\ 1000000 + 48000 + 576 &= 1048576. \end{align*} Multiplying this with $10^{20}$ adds $20$ more zeroes at the end, which means the left side of our inequality has $27$ digits. Then, the $10$ on the right side must have an exponent less than $27,$ meaning that $n<27.$
We are also given that the initial string of zeroes in the decimal representation of $\frac{1}{20^{20}}$ is followed by a $9.$ If we consider just these $n+1$ digits after the decimal point, we can express it as the fraction $\frac{9}{10^{n+1}}.$ Since there are more digits after this $9$ in the decimal representation of $\frac{1}{20^{20}},$ it is true that \[\frac{1}{20^{20}} > \frac{9}{10^{n+1}}.\] Rinse and repeat and we have \[20^{20} < \frac{10^{n+1}}{9}.\] Multiplying both sides by $\frac{9}{10^{20}}$ gives \[9 \cdot 2^{20} < 10^{n-19}.\] We previously found that $2^{20} = 1048576,$ which has $7$ digits. Multiplying this by $9$ will keep the number of digits the same (make sure to see why). Thus, \[n-19>6 \qquad \text{or} \qquad n > 25.\]
If $n<27$ and $n>25,$ then $n= \boxed{\textbf{(D)} \ 26}.$
~happyhari, mathbrek

## Solution 8 (reworded Solution 1)
We split $\frac{1}{20^{20}}$ into $\frac{1}{2^{20}} \cdot \frac{1}{10^{20}}$ . Memorizing(or just multiplying $1024 \cdot 1024$ ) $2^{20} = 1048576$ , we know that
\[\frac{1}{1000000} < \frac{1}{2^{20}} = \frac{1}{1048576}.\]
Taking notice of the fact that $\frac{1}{1000000} = 10^{-6}$ and has $5$ zeroes following the decimal point, we know that $\frac{1}{1048576}$ must be a bit smaller than that and therefore have $6$ of them. So, multiplying that up with $\frac{1}{10^{20}}$ would give another $20$ zeroes from $10^{-20}$ , and therefore there are $20 + 6 = \boxed{26}$ zeroes following the decimal point in the original fraction.
by DearPrince

## Solution 9

## Video Solution by TheBeautyofMath
https://youtu.be/t6yjfKXpwDs
~IceMatrix

## Video Solution (HOW TO CRITICALLY THINK)
https://youtu.be/qnznImCDSW4
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .