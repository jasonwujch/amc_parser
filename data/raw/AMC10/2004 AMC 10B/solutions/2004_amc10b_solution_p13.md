# 2004 AMC 10B Problem 13

## Problem

In the United States, coins have the following thicknesses: penny, $1.55$ mm; nickel, $1.95$ mm; dime, $1.35$ mm; quarter, $1.75$ mm. If a stack of these coins is exactly $14$ mm high, how many coins are in the stack?

$\mathrm{(A) \ } 7 \qquad \mathrm{(B) \ } 8 \qquad \mathrm{(C) \ } 9 \qquad \mathrm{(D) \ } 10 \qquad \mathrm{(E) \ } 11$

## Solution 1
All numbers in this solution will be in hundredths of a millimeter.
The thinnest coin is the dime, with thickness $135$ . A stack of $n$ dimes has height $135n$ .
The other three coin types have thicknesses $135+20$ , $135+40$ , and $135+60$ . By replacing some of the dimes in our stack by other, thicker coins, we can clearly create exactly all heights in the set $\{135n, 135n+20, 135n+40, \dots, 195n\}$ .
If we take an odd $n$ , then all the possible heights will be odd, and thus none of them will be $1400$ . Hence $n$ is even.
If $n<8$ the stack will be too low and if $n>10$ it will be too high. Thus we are left with cases $n=8$ and $n=10$ .
If $n=10$ the possible stack heights are $1350,1370,1390,\dots$ , with the remaining ones exceeding $1400$ .
Therefore there are $\boxed{\mathrm{(B)\ }8}$ coins in the stack.
Using the above observation we can easily construct such a stack. A stack of $8$ dimes would have height $8\cdot 135=1080$ , thus we need to add $320$ . This can be done for example by replacing five dimes by nickels (for $+60\cdot 5 = +300$ ), and one dime by a penny (for $+20$ ).

## Solution 2
Let $p,n,d$ , and $q$ be the number of pennies, nickels, dimes, and quarters used in the stack.
From the conditions above, we get the following equation:
\[155p+195n+135d+175q=1400.\]
Then we divide each side by five to get
\[31p+39n+27d+35q=280.\]
Writing both sides in terms of mod 4, we have $-p-n-d-q \equiv 0 \pmod 4$ .
This means that the sum $p+n+d+q$ is divisible by 4. Therefore, the answer must be $\boxed{(B)\,\, 8}.$

## Solution 3
We notice that the thickness of 4 quarters is 7 mm. 7 is half of 14, so we multiply the 4 quarters by two and get $\boxed{(B)\,\, 8}$ .
### Note
We can easily add up $1.55\text{\ mm}$ and $1.95\text{\ mm}$ to get $3.50\text{\ mm}$ . We multiply that by $4$ to get $14\text{\ mm}$ . Since this works and it requires 8 coins, the answer is clearly $\boxed{\mathrm{(B)\ }8}$ .
Similarly, we can simply take $8$ quarters to get $8\cdot 1.75=14$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .