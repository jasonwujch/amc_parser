# 2006 AIME I Problem 9

## Problem

The sequence $a_1, a_2, \ldots$ is geometric with $a_1=a$ and common ratio $r,$ where $a$ and $r$ are positive integers. Given that $\log_8 a_1+\log_8 a_2+\cdots+\log_8 a_{12} = 2006,$ find the number of possible ordered pairs $(a,r).$

## Solution 1
\[\log_8 a_1+\log_8 a_2+\ldots+\log_8 a_{12}= \log_8 a+\log_8 (ar)+\ldots+\log_8 (ar^{11}) \\ = \log_8(a\cdot ar\cdot ar^2\cdot \cdots \cdot ar^{11}) = \log_8 (a^{12}r^{66})\]
So our question is equivalent to solving $\log_8 (a^{12}r^{66})=2006$ for $a, r$ positive integers . $a^{12}r^{66}=8^{2006} = (2^3)^{2006} = (2^6)^{1003}$ so $a^{2}r^{11}=2^{1003}$ .
The product of $a^2$ and $r^{11}$ is a power of 2. Since both numbers have to be integers, this means that $a$ and $r$ are themselves powers of 2. Now, let $a=2^x$ and $r=2^y$ :
\begin{eqnarray*}(2^x)^2\cdot(2^y)^{11}&=&2^{1003}\\ 2^{2x}\cdot 2^{11y}&=&2^{1003}\\ 2x+11y&=&1003\\ y&=&\frac{1003-2x}{11} \end{eqnarray*}
For $y$ to be an integer, the numerator must be divisible by $11$ . This occurs when $x=1$ because $1001=91*11$ . Because only even integers are being subtracted from $1003$ , the numerator never equals an even multiple of $11$ . Therefore, the numerator takes on the value of every odd multiple of $11$ from $11$ to $1001$ . Since the odd multiples are separated by a distance of $22$ , the number of ordered pairs that work is $1 + \frac{1001-11}{22}=1 + \frac{990}{22}=46$ . (We must add 1 because both endpoints are being included.) So the answer is $\boxed{046}$ .
For the step above, you may also simply do $1001/11 + 1 = 91 + 1 = 92$ to find how many multiples of $11$ there are in between $11$ and $1001$ . Then, divide $92/2$ = $\boxed{046}$ to find only the odd solutions. $-XxHalo711$
Another way is to write
$x = \frac{1003-11y}2$
Since $1003/11 = 91 + 2/11$ , the answer is just the number of odd integers in $[1,91]$ , which is, again, $\boxed{046}$ .

## Solution 2
Using the above method, we can derive that $a^{2}r^{11} = 2^{1003}$ . Now, think about what happens when r is an even power of 2. Then $a^{2}$ must be an odd power of 2 in order to satisfy the equation which is clearly not possible. Thus the only restriction r has is that it must be an odd power of 2, so $2^{1}$ , $2^{3}$ , $2^{5}$ .... all work for r, until r hits $2^{93}$ , when it gets greater than $2^{1003}$ , so the greatest value for r is $2^{91}$ . All that's left is to count the number of odd integers between 1 and 91 (inclusive), which yields $\boxed{046}$ .

## Solution 3
Using the method from Solution 1, we get $\log_8a^{12}r^{66}=2006 \implies a^{12}r^{66}=8^{2006}=2^{6018}$ .
Since $a$ and $r$ both have to be powers of $2$ , we can rewrite this as $12x+66y=6018$ .
$6018 \equiv 66 \equiv 6\pmod{12}$ . So, when we subtract $12$ from $6018$ , the result is divisible by $66$ . Evaluating that, we get $(1,91)$ as a valid solution. Since $66 \cdot 2 = 12 \cdot 11$ , when we add $11$ to the value of $a$ , we can subtract $2$ from the value of $r$ to keep the equation valid. Using this, we get $(1,91),(12,89),(23,87), \cdots (541,1)$ . In order to count the number of ordered pairs, we can simply count the number of $y$ values. Every odd number from $1$ to $91$ is included, so we have $\boxed{046}$ solutions.
-Phunsukh Wangdu
These problems are copyrighted © by the Mathematical Association of America.