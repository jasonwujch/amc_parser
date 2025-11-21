# 2018 AMC 10A Problem 19

## Problem

A number $m$ is randomly selected from the set $\{11,13,15,17,19\}$ , and a number $n$ is randomly selected from $\{1999,2000,2001,\ldots,2018\}$ . What is the probability that $m^n$ has a units digit of $1$ ?

$\textbf{(A) } \frac{1}{5} \qquad \textbf{(B) } \frac{1}{4} \qquad \textbf{(C) } \frac{3}{10} \qquad \textbf{(D) } \frac{7}{20} \qquad \textbf{(E) } \frac{2}{5}$

## Solution 1
Since we only care about the units digit, our set $\{11,13,15,17,19 \}$ can be turned into $\{1,3,5,7,9 \}$ . Call this set $A$ and call $\{1999, 2000, 2001, \cdots , 2018 \}$ set $B$ . Let's do casework on the element of $A$ that we choose. Since $1\cdot 1=1$ , any number from $B$ can be paired with $1$ to make $1^n$ have a units digit of $1$ . Therefore, the probability of this case happening is $\frac{1}{5}$ since there is a $\frac{1}{5}$ chance that the number $1$ is selected from $A$ . Let us consider the case where the number $3$ is selected from $A$ . Let's look at the unit digit when we repeatedly multiply the number $3$ by itself: \[3\cdot 3=9\] \[9\cdot 3=7\] \[7\cdot 3=1\] \[1\cdot 3=3\] We see that the unit digit of $3^x$ , for some integer $x$ , will only be $1$ when $x$ is a multiple of $4$ . Now, let's count how many numbers in $B$ are divisible by $4$ . This can be done by simply listing: \[2000,2004,2008,2012,2016.\] There are $5$ numbers in $B$ divisible by $4$ out of the $2018-1999+1=20$ total numbers. Therefore, the probability that $3$ is picked from $A$ and a number divisible by $4$ is picked from $B$ is $\frac{1}{5}\cdot \frac{5}{20}=\frac{1}{20}.$ Similarly, we can look at the repeating units digit for $7$ : \[7\cdot 7=9\] \[9\cdot 7=3\] \[3\cdot 7=1\] \[1\cdot 7=7\] We see that the unit digit of $7^y$ , for some integer $y$ , will only be $1$ when $y$ is a multiple of $4$ . This is exactly the same conditions as our last case with $3$ so the probability of this case is also $\frac{1}{20}$ . Since $5\cdot 5=25$ and $25$ ends in $5$ , the units digit of $5^w$ , for some integer, $w$ will always be $5$ . Thus, the probability in this case is $0$ . The last case we need to consider is when the number $9$ is chosen from $A$ . This happens with probability $\frac{1}{5}.$ We list out the repeating units digit for $9$ as we have done for $3$ and $7$ : \[9\cdot 9=1\] \[1\cdot 9=9\] We see that the units digit of $9^z$ , for some integer $z$ , is $1$ only when $z$ is an even number. From the $20$ numbers in $B$ , we see that exactly half of them are even. The probability in this case is $\frac{1}{5}\cdot \frac{1}{2}=\frac{1}{10}.$ Finally, we can add all of our probabilities together to get \[\frac{1}{5}+\frac{1}{20}+\frac{1}{20}+\frac{1}{10}=\boxed{\textbf{(E)} ~\frac{2}{5}}.\]
(I did not prove yet) {1999, 2000, 2001,..., 2018} is the same as {1,2,3,4,1,2,...,4}, which can be turned into {1,2,3,4}
~Nivek
~very minor edits by virjoy2001
~sidenote by pungent_muskrat

## Solution 2
Since only the units digit is relevant, we can turn the first set into $\{1,3,5,7,9\}$ . Note that $x^4 \equiv 1 \mod 10$ for all odd digits $x$ , except for 5. Looking at the second set, we see that it is a set of all integers between 1999 and 2018. There are 20 members of this set, which means that, $\mod 4$ , this set has 5 values which correspond to $\{0,1,2,3\}$ , making the probability equal for all of them. Next, check the values for which it is equal to $1 \mod 10$ . There are $4+1+0+1+2=8$ values for which it is equal to 1, remembering that $5^{4n} \equiv 1 \mod 10$ only if $n=0$ , which it is not. There are 20 values in total, and simplifying $\frac{8}{20}$ gives us $\boxed{\textbf{(E)} ~\frac{2}{5}}$ .

## Solution 3
By Euler's Theorem, we have that $a^{4} \equiv 1 \pmod {10}$ , if $\gcd(a,10)=1$ . Hence $m=11,13,17,19$ , $n=2000,2004,2008,2012,2016$ work.
Also note that $11^{\text{any positive integer}}\equiv 1 \pmod {10}$ because $11^b=(10+1)^b=10^b+10^{b-1}1+...+10(1)+1$ , and the latter $\pmod {10}$ is clearly $1$ . So $m=11$ , $n=1999,2001,2002,2003,2005,...,2018$ work (not counting multiples of 4 as we would be double counting if we did).
We can also note that $19^{2a}\equiv 1 \pmod {10}$ because $19^{2a}=361^{a}$ , and by the same logic as why $11^{\text{any positive integer}}\equiv 1 \pmod {10}$ , we are done. Hence $m=19$ , and $n=2002, 2006, 2010, 2014, 2018$ work (not counting any of the aforementioned cases as that would be double counting).
We cannot make any more observations that add more $m^n$ with unit digit $1$ , hence the number of $m^n$ that have units digit one is $4\cdot 5+1\cdot 15+1\cdot 5=40$ . And the total number of combinations of an element of the set of all $m$ and an element of the set of all $n$ is $5\cdot 20=100$ . Hence the desired probability is $\frac{40}{100}=\frac{2}{5}$ , which is answer choice $\boxed{\textbf{(E)} ~\frac{2}{5}}$ . ~vsamc

## Solution 4 (Easy)
When a number's unit's digit is $1$ , then any power to this number will also end in $1$ (since $1^{n}$ for any $n$ is always $1$ ), so we have $20$ choices for $11$ .
When a number's unit's digit is $3$ , then $3^{4n}$ for any $n$ will produce a number ending with 1. So, $20 \div 4 = 5$ choices for $13$ .
$5^{n}$ always ends in 5, so there are $0$ possibilities for $15$ .
When a number's unit's digit is $7$ , then this is also the same thing with $3$ , so we have $5$ choices.
When a number's unit's digit is $9$ , then $9^{2n}$ will produce a number ending in $1$ , so we have $20 \div 2 = 10$ possibilities.
Hence, we have a total of $5 \cdot 20 = 100$ ways, so the probability is $\frac{20+5+0+5+10}{100} = \frac {40}{100} = \boxed{\textbf{(E)} ~\frac{2}{5}}$ .
~MrThinker

## Video Solution by TheBeautyofMath
https://youtu.be/M22S82Am2zM?t=630 ~IceMatrix

## Video Solution 2
https://youtu.be/njyn611TJi0
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .