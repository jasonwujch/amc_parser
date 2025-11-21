# 2011 AMC 10B Problem 23

## Problem

What is the hundreds digit of $2011^{2011}?$

$\textbf{(A) } 1 \qquad \textbf{(B) } 4 \qquad \textbf{(C) }5 \qquad \textbf{(D) } 6 \qquad \textbf{(E) } 9$

## Solution 1
Since $2011 \equiv 11 \pmod{1000},$ we know that $2011^{2011} \equiv 11^{2011} \pmod{1000}.$
To compute this, we use a clever application of the binomial theorem .
$\begin{aligned} 11^{2011} &= (1+10)^{2011} \\ &= 1 + \dbinom{2011}{1} \cdot 10 + \dbinom{2011}{2} \cdot 10^2 + \cdots \end{aligned}$
In all of the other terms, the power of $10$ is greater than $2$ and so is equivalent to $0$ modulo $1000,$ which means we can ignore it. We have:
$\begin{aligned}11^{2011} &\equiv 1 + 2011\cdot 10 + \dfrac{2011 \cdot 2010}{2} \cdot 100 \\ &\equiv 1+20110 + \dfrac{11\cdot 10}{2} \cdot 100\\ &= 1 + 20110 + 5500\\ &\equiv 1 + 110 + 500\\&=611 \pmod{1000} \end{aligned}$
Therefore, the hundreds digit is $\boxed{\textbf{(D) } 6}.$
Side note: By Euler's Totient Theorem , $a^{\phi (1000)} \equiv 1 \pmod{1000}$ for any $a$ relatively prime with 1000, so $a^{400} \equiv 1 \pmod{1000}$ and $11^{2011} \equiv 11^{11} \pmod{1000}$ . We can then proceed using the clever application of the Binomial Theorem, or we can just proceed with solution 6 from here.

## Solution 2 (Cleaner Modular Arithmetic)
We wish to find \[2011^{2011} \mod 1000\] Which is equivalent of saying \[11^{2011} \mod 1000\] In which we have \[11^{2011} \mod 1000 \equiv 11^{\text{rem}(2011, \phi(1000))} \mod 1000 \equiv 11^{\text{rem}(2011, 400)} \mod 1000 \equiv 11^{11} \mod 1000.\] \[11^{11} = 11^6 \times 11^5\]
We begin by simplifying $11^6 \mod 1000$
\[11^6 \mod 1000 = 11^2 \times 11^2 \times 11^2 \mod 1000 \equiv 121 \times 121 \times 121 \mod 1000\] which is to say \[641 \times 121 \mod 1000\] which is equivalent of saying \[561 \mod 1000.\]
Now, we continue with the $11^5$ term.
\[11^5 \mod 1000 \equiv 11^2 \times 11^2 \times 11 \mod 1000\] \[\equiv 641 \times 11 \mod 1000\] \[\equiv 641 \times (10+1) \mod 1000\] \[\equiv 6410 + 641 \mod 1000\] \[\equiv 51 \mod 1000.\] We then have $561 \times 51 \mod 1000 \equiv 611 \mod 1000 = 611$ .
The hundreds digit is clearly $\boxed{\textbf{(D) } 6}.$
~Pinotation
Happy Halloween!

## Solution 3
We need to compute $2011^{2011} \pmod{1000}.$ By the Chinese Remainder Theorem , it suffices to compute $2011^{2011} \pmod{8}$ and $2011^{2011} \pmod{125}.$
In modulo $8,$ we have $2011^4 \equiv 1 \pmod{8}$ by Euler's Theorem, and also $2011 \equiv 3 \pmod{8},$ so we have \[2011^{2011} = (2011^4)^{502} \cdot 2011^3 \equiv 1^{502} \cdot 3^3 \equiv 3 \pmod{8}.\]
In modulo $125,$ we have $2011^{100} \equiv 1 \pmod{125}$ by Euler's Theorem, and also $2011 \equiv 11 \pmod{125}.$ Therefore, we have $\begin{aligned} 2011^{2011} &= (2011^{100})^{20} \cdot 2011^{11} \\ &\equiv 1^{20} \cdot 11^{11} \\ &= 121^5 \cdot 11 \\ &= (-4)^5 \cdot 11 = -1024 \cdot 11 \\ &\equiv -24 \cdot 11 = -264 \\ &\equiv 111 \pmod{125}. \end{aligned}$
After finding the solution $2011^{2011} \equiv 611 \pmod{1000},$ we conclude it is the only one by the Chinese Remainder Theorem. Thus, the hundreds digit is $\boxed{\textbf{(D) } 6}.$

## Solution 4
Notice that the hundreds digit of $2011^{2011}$ won't be affected by $2000$ . Essentially we could solve the problem by finding the hundreds digit of $11^{2011}$ . Powers of $11$ are special because they can be represented by the Pascal's Triangle. Drawing the triangle, there is a theorem that states the powers of $11$ can be found by reading rows of the triangle and adding extra numbers up. [add source] For example, the sixth row of the triangle is $1, 5, 10, 10, 5,$ and $1$ . Adding all numbers from right to left, we get $161051$ , which is also $11^5$ . In other words, each number is $10^n$ steps from the right side of the row. The hundreds digit is $0$ . We can do the same for $11^{2011}$ , but we only need to find the $3$ digits from the right. Observing, every $3$ number from the right is $1 + 2 + 3... + n$ . So to find the third number from the right on the row of $11^{2011}$ , \[f(11^n) = 1 + 2 + 3... + (n-1),\] or $\frac{(2010 \cdot 2011)}{2}$ , or $2021055$ . The last digit is five, but we must remember to add the number on the right of it, which, by observing other rows is obviously $2011$ . We must carry the $1$ in $2011$ 's tens digit to the $5$ in $2021055$ 's unit digit to get $\boxed{\textbf{(D) } 6}$ . The one at the very end of the row doesn't affect anything, so we can leave it alone.
-jackshi2006

## Solution 5 (naive solution)
Since we are only looking at the last 3 digits and $2011^2$ has the same last 3 digits as $11^2$ , we can find $11^{2011}$ instead. After this, we can repeatedly multiply the last 3 digits by 11 and take the last 3 digits of that product. We discover that $11^{51}$ 's last 2 digits are -11, the same as $11^1$ .
From this information, we can figure out $11^{11}$ and $11^{61}$ end in 611. Adding various multiples of 50 to the exponent gives us the fact that $11^{2011}$ 's last digits are 611. We get $\boxed{\textbf{(D) } 6}$ . -ThisUsernameIsTaken

## Solution 6 (modular bash)
We know that the hundreds digit of $2011^{2011}$ is just the hundreds digit of $11^{2011} \equiv 011 \pmod{1000}$ . If we actually take a look at the powers of $11 \pmod{1000}$ , we notice a pattern:
\[11^{1} \equiv 011 \pmod{1000}\] \[11^{2} \equiv 121 \pmod{1000}\] \[11^{3} \equiv 331 \pmod{1000}\] \[11^{4} \equiv 641 \pmod{1000}\] \[11^{5} \equiv 051 \pmod{1000}\] \[11^{6} \equiv 561 \pmod{1000}\] Notice how the units digit is always one, the tens digit is always the previous tens digit plus the ones digit (or one) and the hundreds digit is always the previous hundreds digit plus the previous tens digit. Knowing this, we confidently repeat this pattern without actually multiply the previous term by $11$ out (if you generally multiply a few numbers by $11$ , you can see why this pattern holds).
\[11^{7} \equiv 171 \pmod{1000}\] \[11^{8} \equiv 881 \pmod{1000}\] \[11^{9} \equiv 691 \pmod{1000}\] \[11^{10} \equiv 601 \pmod{1000}\] \[11^{11} \equiv 611 \pmod{1000}\] Since $11^{11}$ ends in _ $11$ , the pattern "cycles" every $10$ times. $\frac{2011}{10}=201$ remainder $1$ , meaning that $2011^{2011} \equiv 11^{2011} \equiv 611 \pmod{1000}$ , giving us a hundreds digit of $\boxed{\textbf{(D) } 6}$ .
-mattwang2014 I think this solution is wrong, since you seem to be saying that it cycles every 10 numbers, although I've tried it out and found it cycles every 50 numbers instead. For example, $11^{21} \equiv 211 \pmod{1000}$ , not 611.

## Solution 7 (Super Easy) (Wrong)
We know that the hundreds digit of $2011^{11}$ is just the hundreds digit of $11^{11}$ (mod 1000). If we actually take a look at the powers of 11, we notice a pattern:
\[11^{1} = 11\]
\[11^{2} = 121\]
\[11^{3} = 1331\]
\[11^{4} = 14641\]
We notice that the hundreds digit just increases by 1 starting from 1(the hundreds digit of $11^{1}$ ). All we have to do now is add all the numbers from 1 to 11 (since the hundreds digit increases by 1 with every power of 11 that comes after) to get the hundreds digit of $11^{11}$ .
$1 + 2 + 3 + 4.... + 11 = 66$ . Thus the answer is $\boxed{\textbf{(D) } 6}$ .
-TheOfficalPro
Ilovebender I believe this solution is wrong, as I can see that the hundreds digit doesn't increase by 1, it goes from 0 to 1 to 3 to 6. A more accurate solution would be the hundreds digit are triangular numbers.
-Extremelysupercooldude: In your solution, you find the hundreds digit of $2011^{11}$ , but the problem asks for the hundreds digit of $2011^{2011}$ , but you never cite way the two hundreds digits are the same.
-Wesserwes7254: I think this is a more revised version of this solution: We know that the hundreds digit of $2011^{2011}$ is just the hundreds digit of $11^{2011} \equiv 011 \pmod{1000}$ . If we actually take a look at the powers of $11 \pmod{1000}$ , we notice a pattern:
\[11^{1} \equiv 011 \pmod{1000}\]
\[11^{2} \equiv 121 \pmod{1000}\]
\[11^{3} \equiv 331 \pmod{1000}\]
\[11^{4} \equiv 641 \pmod{1000}\]
\[11^{5} \equiv 051 \pmod{1000}\]
\[11^{6} \equiv 561 \pmod{1000}\]
Notice how the units digit is always one, the tens digit is always the previous tens digit plus the ones digit (or one) and the hundreds digit is always the previous hundreds digit plus the previous tens digit. Knowing this, we confidently repeat this pattern without actually multiply the previous term by $11$ out (if you generally multiply a few numbers by $11$ , you can see why this pattern holds).
\[11^{7} \equiv 171 \pmod{1000}\]
\[11^{8} \equiv 881 \pmod{1000}\]
\[11^{9} \equiv 691 \pmod{1000}\]
\[11^{10} \equiv 601 \pmod{1000}\]
\[11^{11} \equiv 611 \pmod{1000}\]
Since $11^{11}$ ends in _ $11$ , the pattern "cycles" every $10$ times. $\frac{2011}{10}=201$ remainder $1$ , meaning that $2011^{2011} \equiv 11^{2011} \equiv 611 \pmod{1000}$ , giving us a hundreds digit of $\boxed{\textbf{(D) } 6}$ .

## Solution 8
First, see that 2011 is a prime number. Therefore 2011 and 1000 are coprime.
$\gcd{(2011, 1000)} = 1$
$2011^{400} \equiv 1 \pmod{1000 }$
$2011^{2000} \equiv 1 \pmod{1000}$
$2011^{11} \equiv 11^{11} \pmod{1000}$
$661 \equiv 2011^{11}$ mod (1000)
Therefore, the answer is 6.
~euriley ~unfinished latex by megacleverstarfish15.

## Video Solution by TheBeautyofMath
https://youtu.be/7rosJnqLhs8?t=323
~IceMatrix

## Video Solution by OmegaLearn
https://youtu.be/-H4n-QplQew?t=1423
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .