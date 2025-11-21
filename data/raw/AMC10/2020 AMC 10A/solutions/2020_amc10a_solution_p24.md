# 2020 AMC 10A Problem 24

## Problem

Let $n$ be the least positive integer greater than $1000$ for which

\[\gcd(63, n+120) =21\quad \text{and} \quad \gcd(n+63, 120)=60.\]

What is the sum of the digits of $n$ ?

$\textbf{(A) } 12 \qquad\textbf{(B) } 15 \qquad\textbf{(C) } 18 \qquad\textbf{(D) } 21\qquad\textbf{(E) } 24$

## Solution 1
We know that $\gcd(n+57,63)=21$ and $\gcd(n-57, 120)= 60$ by the Euclidean Algorithm. Hence, let $n+57=21\alpha$ and $n-57=60 \gamma$ , where $\gcd(\alpha,3)=1$ and $\gcd(\gamma,2)=1$ . Subtracting the two equations, $38=7\alpha-20\gamma$ . Letting $\gamma = 2s+1$ , we get $58=7\alpha-40s$ . Taking modulo $40$ , we have $\alpha \equiv{14} \pmod{40}$ . We are given that $n=21\alpha -57 >1000$ , so $\alpha \geq 51$ . Notice that if $\alpha =54$ then the condition $\gcd(\alpha,3)=1$ is violated. The next possible value of $\alpha = 94$ satisfies the given condition, giving us $n=1917$ .
Alternatively, we could have said $\alpha = 40k+14 \equiv{0} \pmod{3}$ for $k \equiv{1} \pmod{3}$ only, so $k \equiv{0,2} \pmod{3}$ , giving us our answer. Since the problem asks for the sum of the digits of $n$ , our answer is $1+9+1+7=\boxed{\textbf{(C) } 18}$ .
~Prabh1512
### Supplement
When looking at $38=7\alpha-20\gamma$ , instead of attempting to take $\alpha$ modulo $40$ , it may be more intuitively obvious to take $\alpha$ modulo $20$ :
As $7$ and $20$ are coprime, $7$ has an inverse modulo $20$ . Recall that $7 \cdot 3 \equiv 1 \pmod{20}$ , so $7^{-1} \equiv 3 \pmod{20}$ . Thus, $\alpha \equiv 54 \equiv 14 \pmod{20}$ . Furthermore, consider that $21 \alpha -57 > 1000$ , so $\alpha \geq 51$ . $\alpha = 54$ fails, as $gcd( \alpha, 3) = 1$ from $\gcd(63, n + 57 ) = 21$ . $74$ fails as well; this causes $\gamma$ to be even from $114 = 21\alpha - 60\gamma$ . $94$ is the first number not violating any restrictions, leaving $94 \cdot 21-57 = 1917$ , which has digital sum $1 + 9 + 1 + 7 = 18$ , so we choose $\boxed{ (C) }$ .
In the end, though, it is just the same steps in a different order. ~LeonQS

## Solution 2
The conditions of the problem reduce to the following: $n+120 = 21k$ and $n+63 = 60\ell$ , where $\gcd(k,3) = 1$ and $\gcd(\ell,2) = 1$ . From these equations, we see that $21k - 60\ell = 57$ . Solving this Diophantine equation gives us that $k = 20a + 17$ and $\ell = 7a + 5$ . Since, $n>1000$ , we can do some bounding and get that $k > 53$ and $\ell > 17$ . Now we start bashing by plugging in numbers that satisfy these conditions: $a=4$ is the first number that works so we get $\ell = 33$ , $k = 97$ . Therefore, we have $n=21(97)-120=60(33)-63=1917$ , and our answer is $1+9+1+7=\boxed{\textbf{(C) } 18}$ .

## Solution 3
We first find that $n\equiv6\pmod{21}$ and $n\equiv57\pmod{60}$ , then we get $n=21x+6$ and $n=60y+57$ by definitions, where $x$ and $y$ are integers. It follows that $y$ must be odd, since the GCD will be $120$ instead of $60$ if $y$ is even. Also, the unit digit of $n$ must be $7$ , since the unit digit of $60y$ is always $0$ and the unit digit of $57$ is $7$ . Therefore, we find that $x$ must end in $1$ to satisfy $n$ having a unit digit of $7$ . Also, we find that $x$ must not be a multiple of $3$ or else the GCD will be $63$ . Therefore, we test values for $x$ and find that $x=91$ satisfies all these conditions. Therefore, $n=1917$ and $1+9+1+7 = \boxed{\textbf{(C) } 18}$ .
~happykeeper

## Solution 4
After applying the Euclidean Algorithm we get $\gcd(n - 6, 63) = 21$ and $\gcd(n - 57, 120) = 60.$ So we have $n - 6 = 21a$ and $n - 57 = 60b$ , where $a$ is not a multiple of $3$ and $b$ is not a multiple of $2.$ Setting these equations equal to each other, we get $21a = 60b + 51 \implies 20b = 7a - 17.$ We note that $a$ must be $\geq 48$ (since $n$ has to be greater than $1000$ ) and the last digit of $a$ must be $1$ so that $7a - 17$ is a multiple of $10$ and has a possibility of also being a multiple of 20.
Since $a = 91$ , $n = 91 \cdot 21 + 6 = 1917$ (or since $b = 31,$ $n = 31 \cdot 60 + 57 = 1917).$ The answer is $1 + 9 + 1 + 7 = \boxed{18}.$
~ grogg007 , isabelchen

## Solution 5
We are given that $\gcd(63, n+120) =21$ and $\gcd(n+63, 120)=60.$ By applying the Euclidean algorithm in reverse, we have \[\gcd(63, n+120) = \gcd(63, n+120 + 63) = \gcd(63, n+183) = 21\] and \[\gcd(n+63, 120) = \gcd(n+63 + 120, 120) = \gcd(n+183, 120) = 60.\]
We now know that $n+183$ must be divisible by $21$ and $60,$ so it is divisible by $\text{lcm}(21, 60) = 420.$ Therefore, $n+183 = 420k$ for some integer $k.$ We know that $3 \nmid k,$ or else the first condition won't hold ( $\gcd$ will be $63$ ) and $2 \nmid k,$ or else the second condition won't hold ( $\gcd$ will be $120$ ). Since $k = 1$ gives us too small of an answer, then $k=5,$ from which $n = 1917.$ So, the answer is $1+9+1+7 = \boxed{\textbf{(C) } 18}.$

## Solution 6
$\gcd(n+63,120)=60$ tells us $n+63\equiv60\pmod {120}$ . The smallest $n+63$ that satisfies the previous condition and $n>1000$ is $1140$ , so we start from there. If $n+63=1140$ , then $n+120=1197$ . Because $\gcd(n+120,63)=21$ , $n+120\equiv21\pmod {63}$ or $n+120\equiv42\pmod {63}$ . We see that $1197\equiv0\pmod {63}$ , which does not fulfill the requirement for $n+120$ , so we continue by keep on adding $120$ to $1197$ , in order to also fulfill the requirement for $n+63$ . Soon, we see that $n+120\pmod {63}$ decreases by $6$ every time we add $120$ , so we can quickly see that $n=1917$ because at that point $n+120\equiv21\pmod {63}$ . We add up all digits of $1917$ to get $\boxed{\textbf{(C) } 18}$ .
~SmileKat32

## Solution 7
We are able to set up the following system of congruences: \begin{align*} n &\equiv 6 \pmod {21}, \\ n &\equiv 57 \pmod {60}. \end{align*} Therefore, by definition, we are able to set-up the following system of equations: \begin{align*} n &= 21a + 6, \\ n &= 60b + 57. \end{align*} Thus, we have $21a + 6 = 60b + 57,$ from which \[7a + 2 = 20b + 19.\] We know $7a \equiv 0 \pmod {7},$ and since $7a = 20b + 17,$ therefore $20b + 17 \equiv 0 \pmod{7}.$ Simplifying this congruence further, we have \[b\equiv 3 \pmod{7}.\] Thus, by definition, $b = 7x + 3.$ Substituting this back into our original equation, we get \[n = 60(7x + 3) + 57 = 420x + 237.\] By definition, we are able to set up the following congruence: \[n \equiv 237 \pmod{420}.\] Thus, $n = 1917$ , so our answer is simply $1+9+1+7=\boxed{\textbf{(C) } 18}$ .
Remark
Since $n \equiv -120 \pmod{21},$ we conclude that $n \equiv 6 \pmod{21}.$
Since $n \equiv -63 \pmod{60},$ we conclude that $n \equiv 57 \pmod{60}.$
Remember that $b \equiv 3 \pmod{7}.$
Lastly, the reason why $n \neq 1077$ is $n + 120$ would be divisible by $63$ , which is not possible due to the certain condition.
~nikenissan ~Midnight

## Solution 8
First, we find $n$ . We know that it is greater than $1000$ , so we first input $n = 1000$ . From the first equation, $\gcd(63, n + 120) = 21$ , we know that if $n$ is correct, after we add $120$ to it, it should be divisible by $21$ , but not $63$ : \[\frac{n + 120}{21} = \frac{1120}{21} = 53\text{ R }7.\] This does not work. To get to the nearest number divisible by $21$ , we have to add $14$ to cancel out the remainder. (Note that we don't subtract $7$ to get to $53$ ; $n$ is already at its lowest possible value!) Adding $14$ to $1000$ gives us $n = 1014$ . (Note: $n$ is currently divisible by 63, but that's fine since we'll be changing it in the next step.)
Now using the second equation, $\gcd(n + 63, 120) = 60$ , we know that if $n$ is correct, then $n+63$ is divisible by $60$ but not $120$ : \[\frac{n + 63}{60} = \frac{1077}{60} = 17\text{ R }57.\] Again, this does not work. This requires some guessing and checking. We can add $21$ over and over again until $n$ is valid. This changes $n$ while also maintaining that $\frac{n + 120}{21}$ has no remainders. After adding $21$ once, we get $18 r 18$ . By pure luck, adding $21$ two more times gives us $19$ with no remainders. We now have $1077 + 21 + 21 + 21 = 1140$ . However, this number is divisible by $120$ . To get the next possible number, we add the LCM of $21$ and $60$ (once again, to maintain divisibility), which is $420$ . Unfortunately, $1140 + 420 = 1560$ is still divisible by $120$ . Adding $420$ again gives us $1980$ , which is valid. However, remember that this is equal to $n + 63$ , so subtracting $63$ from $1980$ gives us $1917$ , which is $n$ .
The sum of its digits are $1 + 9 + 1 + 7 = \boxed{\textbf{(C) } 18}$ .
~primegn

## Solution 9 (Euclidean Algorithm)
By the Euclidean Algorithm, we have \begin{alignat*}{8} \gcd(63,n+120)&=\hspace{1mm}&&\gcd(63,\phantom{ }\underbrace{n+120-63k_1}_{(n+120) \ \mathrm{mod} \ 63}\phantom{ })&&=21, \\ \gcd(n+63,120)&=&&\gcd(\phantom{ }\underbrace{n+63-120k_2}_{(n+63) \ \mathrm{mod} \ 120}\phantom{ },120)&&=60. \end{alignat*} Clearly, $n+120-63k_1$ must be either $21$ or $42,$ and $n+63-120k_2$ must be $60.$
More generally, let $t\in\{1,2\},$ so we get \begin{align*} n+120-63k_1&=21t, &\hspace{55.5mm}(1) \\ n+63-120k_2&=60. &\hspace{55.5mm}(2) \end{align*} Subtracting $(2)$ from $(1)$ and then simplifying give \begin{align*} 57-63k_1+120k_2&=21t-60 \\ 117-63k_1+120k_2&=21t \\ 39-21k_1+40k_2&=7t. \hspace{54mm}(\bigstar) \end{align*} Taking $(\bigstar)$ modulo $7$ produces \begin{align*} 4+5k_2&\equiv0\pmod{7} \\ k_2&\equiv2\pmod{7}. \end{align*} Recall that $n>1000.$ From $(2),$ it follows that \[1063-120k_2<n+63-120k_2=60,\] from which $k_2>8.$ Therefore, the possible values for $k_2$ are $9,16,23,\ldots.$
We need to check whether positive integers $k_1$ and $t$ (where $t\in\{1,2\}$ ) exist in $(1):$
- If $k_2=9,$ then substituting into $(2)$ gives $n=1077.$ Next, substituting into $(1)$ produces $1197-63k_1=21t,$ or $57-3k_1=t.$ There are no solutions
- If $k_2=16,$ then substituting into $(2)$ gives $n=1917.$ Next, substituting into $(1)$ produces $2037-63k_1=21t,$ or $97-3k_1=t.$ The solution is
There are no solutions $(k_1,t).$
The solution is $(k_1,t)=(32,1).$
Finally, the least such positive integer $n$ is $1917.$ The sum of its digits is $1+9+1+7=\boxed{\textbf{(C) } 18}.$
~MRENTHUSIASM

## Solution 10 (Euclidean Algorithm)
Because we are finding value of $n$ for $n > 1000$ , let $n = 1000 + k$ .
Using the Euclidean Algorithm, \begin{align*} \gcd(63, n+120) &= \gcd(63, 1000 + k + 120) \\ &= \gcd(63, k + 1120 - 63 \cdot 18) \\ &= \gcd(63, k-14) \\ &= 21, \\ \gcd(n+63, 120) &= \gcd(k + 1000 + 63, 120) \\ &= \gcd(k + 1000 + 63 - 120 \cdot 9, 120) \\ &= \gcd(k-17, 120) \\ &= 60. \end{align*} So, we have \begin{align*} k &\equiv 14 \pmod{21}, \\ k &\equiv 17 \pmod{60}. \end{align*} Let $k = 21p + 14 = 60q + 17$ , $7p= 20q + 1$ (by the Division Algorithm), $7p = 21q - (q - 1)$ , $q - 1$ is a multiple of $7$ .
Let $q-1 = 7r$ , $q = 7r+1$ , $k = 60(7r+1) + 17 = 420r + 77$ .
$n = 1000 + k = 420r + 1077$ , $n = 1077, 1497, 1917$ .
By substituting $1077$ , $1497$ , $1917$ into $\gcd(63, n+120) =21$ and $\gcd(n+63, 120)=60$ , $1077$ and $1497$ aren't valid answers, only $1917$ is. Therefore, the answer is $1+9+1+7=\boxed{\textbf{(C) } 18}$ .
~ isabelchen (Solution)
~ Plainoldnumbertheory (Minor Edits)
~ Puck_0 (Formatting)

## Solution 11 (Chinese Remainder Theorem)
We have \begin{align*} \gcd(63, n+120) &= 21 \Longrightarrow n + 120 \equiv 0 \pmod{21}, \text{ where } 9 \nmid n + 120, \\ \gcd(n+63, 120) &= 60 \Longrightarrow n + 63 \equiv 0 \pmod{60}, \text{ where } 8 \nmid n + 63. \end{align*} So, we conclude that $n \equiv 6 \pmod{21}$ and $n \equiv 57 \pmod{60}$ , respectively.
Because the $2$ moduli $21$ and $60$ are not relatively prime, namely $\gcd{(21, 60)} = 3$ , $21 = 3 \cdot 7$ , and $60 = 3 \cdot 20$ , we convert the system of $2$ linear congruences with non-coprime moduli into a system of $3$ linear congruences with coprime moduli: \begin{align*} n &\equiv 0 \pmod{3}, \\ n &\equiv 6 \pmod{7}, \\ n &\equiv 17 \pmod{20}. \end{align*} By Chinese Remainder Theorem , the general solution of system of $3$ linear congruences is \[n = 420k + 1077.\] We construct the following table: \[\begin{array}{c|c|c|c} n & 1077 & 1497 & 1917\\ \hline n + 120 & 1197 & 1617 & 2037\\ \hline n + 63 & 1140 & 1560 & 1980\\ \end{array}\] Only $n = 1917$ satisfies $9 \nmid n + 120$ and $8 \nmid n + 63$ . Therefore, the answer is $1+9+1+7=\boxed{\textbf{(C) } 18}$ .
~ isabelchen

## Solution 12 (Logically Bashing)
We know that $n$ ends with the number $7$ , since $n+63$ is divisible by $60$ , and any number divisible by $10$ (a factor of $60$ ) must end with a $0$ . As a result, $n+120$ must also end in $7$ . Because $n+63$ must be divisible by $20$ , as well (using the same gcd), the tens value of $n$ must be odd. Also, $n+120$ cannot be divisible by $9$ , otherwise, its gcd with $63$ will be $63$ , instead of $21$ .
Now, we can start bashing, using the $\gcd(63, n+120) =21$ . We are given that $n$ must be greater than $1000$ , so we can try $n+120$ that is greater than $1120$ .
We try $21 \cdot 67$ , but it has an even tens digit. We then can try the next highest, using $77$ , but the $\gcd(n+63, 120) =120$ , instead of $60$ .
Since $87$ is divisible by $3$ , so when multiplied by $21$ , it will be divisible by $9$ , we do not have to test it.
The next biggest is $97$ , which works and gives us $n=1917$ , which, when the digits are added up, equals $\boxed{\textbf{(C) } 18}$ .
~parmani

## Solution 13 (Guess and Check)
By the Euclidean Algorithm, we have $\gcd(63, n - 6) = 21$ and $\gcd(120, n - 57) = 60$ . We know that $63 = 21 \cdot 3$ , meaning $n - 6 = 21x$ where $x$ is not divisible by $3$ . Similarly, $120 = 60 \cdot 2$ , meaning $n - 57 = 60y$ where $y$ is odd.
Setting the two expressions for $n$ equal: \[21x + 6 = 60y + 57,\] so \[21x = 60y + 51.\] We can see that $x$ must have a units digit of $1$ , since $21x - 51$ must be divisible by $10$ in order to be divisible by $60$ .
Because $n > 1000$ , we try $x = 61$ , $x = 71$ , and finally $x = 91$ , which works. Thus $21 \cdot 91 = n - 6$ , so $n = 1917$ . The sum of the digits of $n$ is $1 + 9 + 1 + 7 = \boxed{18}$ .
~Voidling

## Video Solutions

## Video Solution 1 (Richard Rusczyk)
https://www.youtube.com/watch?v=tk3yOGG2K-s&

## Video Solution 2
https://youtu.be/8mNMKH0T9W0 - Happytwin

## Video Solution 3 (Incredibly Long & Complicated)
https://youtu.be/e5BJKMEIPEM
Education The Study of Everything

## Video Solution 4
https://www.youtube.com/watch?v=gdGmSyzR908&list=PLLCzevlMcsWNcTZEaxHe8VaccrhubDOlQ&index=5 ~ MathEx

## Video Solution 5
https://youtu.be/R220vbM_my8?t=899 ~ amritvignesh0719062.0
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .