# 2021 AIME I Problem 7

## Problem

Find the number of pairs $(m,n)$ of positive integers with $1\le m<n\le 30$ such that there exists a real number $x$ satisfying \[\sin(mx)+\sin(nx)=2.\]

## Solution 1
It is trivial that the maximum value of $\sin \theta$ is $1$ , is achieved at $\theta = \frac{\pi}{2}+2k\pi$ for some integer $k$ .
This implies that $\sin(mx) = \sin(nx) = 1$ , and that $mx = \frac{\pi}{2}+2a\pi$ and $nx = \frac{\pi}{2}+2b\pi$ , for integers $a, b$ .
Taking their ratio, we have \[\frac{mx}{nx} = \frac{\frac{\pi}{2}+2a\pi}{\frac{\pi}{2}+2b\pi} \implies \frac{m}{n} = \frac{4a + 1}{4b + 1} \implies \frac{m}{4a + 1} = \frac{n}{4b + 1} = k.\] It remains to find all $m, n$ that satisfy this equation.
If $k = 1$ , then $m \equiv n \equiv 1 \pmod 4$ . This corresponds to choosing two elements from the set $\{1, 5, 9, 13, 17, 21, 25, 29\}$ . There are $\binom 82$ ways to do so.
If $k < 1$ , by multiplying $m$ and $n$ by the same constant $c = \frac{1}{k}$ , we have that $mc \equiv nc \equiv 1 \pmod 4$ . Then either $m \equiv n \equiv 1 \pmod 4$ , or $m \equiv n \equiv 3 \pmod 4$ . But the first case was already counted, so we don't need to consider that case. The other case corresponds to choosing two numbers from the set $\{3, 7, 11, 15, 19, 23, 27\}$ . There are $\binom 72$ ways here. (This argument seems to have a logical flaw *check note at bottom*)
Finally, if $k > 1$ , note that $k$ must be an integer. This means that $m, n$ belong to the set $\{k, 5k, 9k, \dots\}$ , or $\{3k, 7k, 11k, \dots\}$ . Taking casework on $k$ , we get the sets $\{2, 10, 18, 26\}, \{6, 14, 22, 30\}, \{4, 20\}, \{12, 28\}$ . Some sets have been omitted; this is because they were counted in the other cases already. This sums to $\binom 42 + \binom 42 + \binom 22 + \binom 22$ .
In total, there are $\binom 82 + \binom 72 + \binom 42 + \binom 42 + \binom 22 + \binom 22 = \boxed{063}$ pairs of $(m, n)$ .
This solution was brought to you by ~Leonard_my_dude~
### Note: Detailed Explanation for
Many of the solutions I see here lack an explicit explanation for why every solution to $m \equiv n \equiv 3 \pmod 4$ constitutes a valid solution to the problem, so I will explain it here. The reason why all solutions where $m \equiv n \equiv 1 \pmod 4$ works is pretty intuitive, as $\frac{m}{n}$ would then be able to be expressed as $\frac{4a + 1}{4b + 1}$ . Similarly, note that $-(4x + 1) \equiv 3 \pmod 4$ . Thus, when solving the equation for $\frac{m}{n} = \frac{4a + 1}{4b + 1}$ , every case in which $m \equiv n \equiv 3 \pmod 4$ will produce a valid solution when $a$ and $b$ are both negative. For example, when $m = 7$ and $n = 11$ , $a = -2$ and $b = -3$ gives $\frac{4a + 1}{4b + 1} = \frac{-7}{-11} = \frac{7}{11}$ . Thus, we add $\binom 72$ as every case where $m \equiv n \equiv 3 \pmod 4$ produces a valid solution.
- yangomango

## Solution 2
In order for $\sin(mx) + \sin(nx) = 2$ , $\sin(mx) = \sin(nx) = 1$ .
This happens when $mx \equiv nx \equiv \frac{\pi}{2} ($ mod $2\pi).$
This means that $mx = \frac{\pi}{2} + 2\pi\alpha$ and $nx = \frac{\pi}{2} + 2\pi\beta$ for any integers $\alpha$ and $\beta$ .
As in Solution 1, take the ratio of the two equations: \[\frac{mx}{nx} = \frac{\frac{\pi}{2}+2\pi\alpha}{\frac{\pi}{2}+2\pi\beta} \implies \frac{m}{n} = \frac{\frac{1}{2}+2\alpha}{\frac{1}{2}+2\beta} \implies \frac{m}{n} = \frac{4\alpha+1}{4\beta+1}\]
Now notice that the numerator and denominator of $\frac{4\alpha+1}{4\beta+1}$ are both odd, which means that $m$ and $n$ have the same power of two (the powers of 2 cancel out).
Let the common power be $p$ : then $m = 2^p\cdot a$ , and $n = 2^p\cdot b$ where $a$ and $b$ are integers between 1 and 30.
We can now rewrite the equation: \[\frac{2^p\cdot a}{2^p\cdot b} = \frac{4\alpha+1}{4\beta+1} \implies \frac{a}{b} = \frac{4\alpha+1}{4\beta+1}\]
Now it is easy to tell that $a \equiv 1 ($ mod $4)$ and $b \equiv 1 ($ mod $4)$ . However, there is another case: that
$a \equiv 3 ($ mod $4)$ and $b \equiv 3 ($ mod $4)$ . This is because multiplying both $4\alpha+1$ and $4\beta+1$ by $-1$ will not change the fraction, but each congruence will be changed to $-1 ($ mod $4) \equiv 3 ($ mod $4)$ .
From the first set of congruences, we find that $a$ and $b$ can be two of $\{1, 5, 9, \ldots, 29\}$ .
From the second set of congruences, we find that $a$ and $b$ can be two of $\{3, 7, 11, \ldots, 27\}$ .
Now all we have to do is multiply by $2^p$ to get back to $m$ and $n$ . Let’s organize the solutions in order of increasing values of $p$ , keeping in mind that $m$ and $n$ are bounded between 1 and 30.
For $p = 0$ we get $\{1, 5, 9, \ldots, 29\}, \{3, 7, 11, \ldots, 27\}$ .
For $p = 1$ we get $\{2, 10, 18, 26\}, \{6, 14, 22, 30\}$
For $p = 2$ we get $\{4, 20\}, \{12, 28\}$
Note that $16\mid{a}$ since $m$ will cancel out a factor of 4 from $a$ , and $\frac{a}{m}$ must contain a factor of 4. Again, $1-4X$ will never contribute a factor of 2. Simply inspecting, we see two feasible values for $a$ and $m$ such that $a+m\leq30$ .
If we increase the value of $p$ more, there will be less than two integers in our sets, so we are done there.
There are 8 numbers in the first set, 7 in the second, 4 in the third, 4 in the fourth, 2 in the fifth, and 2 in the sixth.
In each of these sets we can choose 2 numbers to be $m$ and $n$ and then assign them in increasing order. Thus there are:
\[\dbinom{8}{2}+\dbinom{7}{2}+\dbinom{4}{2}+\dbinom{4}{2}+\dbinom{2}{2}+\dbinom{2}{2} = 28+21+6+6+1+1 = \boxed{063}\] possible pairs $(m,n)$ that satisfy the conditions.
-KingRavi

## Solution 3
We know that the range of sine is between $-1$ and $1$ , inclusive.
Thus, the only way for the sum to be $2$ is for $\sin(mx)=\sin(nx)=1$ .
Note that $\sin(90+360k)=1$ .
Assuming $mx$ and $nx$ are both positive, $m$ and $n$ could be $1,5,9,13,17,21,25,29$ . There are $8$ ways, so $\dbinom{8}{2}$ .
If both are negative, $m$ and $n$ could be $3,7,11,15,19,23,27$ . There are $7$ ways, so $\dbinom{7}{2}$ .
However, the pair $(1,5)$ could also be $(2, 10)$ and so on. The same goes for some other pairs.
In total there are $14$ of these extra pairs.
The answer is $28+21+14 = \boxed{063}$ .

## Solution 4
The equation implies that $\sin(mx)=\sin(nx)=1$ . Therefore, we can write $mx$ as $2{\pi}k_1+\frac{\pi}{2}$ and $nx$ as $2{\pi}k_2+\frac{\pi}{2}$ for integers $k_1$ and $k_2$ . Then, $\frac{mx}{nx}=\frac{m}{n}=\frac{2k_1+\frac{1}{2}}{2k_2+\frac{1}{2}}$ . Cross multiplying, we get $m\cdot{(2k_2+\frac{1}{2})}=n\cdot{(2k_1+\frac{1}{2})} \Longrightarrow 4k_2m-4k_1n=n-m$ . Let $n-m=a$ so the equation becomes $4(m(k_2-k_1)+k_1a)=a$ . Let $k_2-k_1=X$ and $k_1=Y$ , then the equation becomes $a=4Ym+4Xa \Longrightarrow \frac{a(1-4X)}{m}=4Y$ . Note that $X$ and $Y$ can vary accordingly, and $4\mid{a}$ . Next, we do casework on $m\pmod{4}$ :
If $m\equiv 1\pmod{4}$ :
Once $a$ and $m$ are determined, $n$ is determined, so $a+m\leq30$ . $a\in \{4,8,12,\dots,28\}$ and $m\in \{1,5,9,\dots,29\}$ . Therefore, there are $\sum_{i=1}^{7}{i}=28$ ways for this case such that $a+m\leq30$ .
If $m\equiv 3\pmod{4}$ :
$a\in \{4,8,12,\dots,28\}$ and $m\in \{3,7,11,\dots,27\}$ . Therefore, there are $\sum_{i=1}^{6}{i}=21$ ways such that $a+m\leq30$ .
If $m\equiv 2\pmod{4}$ :
Note that $8\mid{a}$ since $m$ in this case will have a factor of 2, which will cancel out a factor of 2 in $a$ , and we need the left hand side to divide 4. Also, $1-4X\equiv 1\pmod{4}$ so it is odd and will therefore never contribute a factor of 2. $a\in \{8,16,24\}$ and $m\in \{2,6,10,\dots,30\}$ . Following the condition $a+m\leq30$ , we conclude that there are $6+4+2=12$ ways for this case.
If $m\equiv 0\pmod{4}$ :
Adding all the cases up, we obtain $28+21+12+2=\boxed{063}$
~ Magnetoninja
### Remark
The graphs of $r\leq\sin(m\theta)+\sin(n\theta)$ and $r=2$ are shown here in Desmos: https://www.desmos.com/calculator/busxadywja
Move the sliders around for $1\leq m \leq 29$ and $2\leq m+1\leq n\leq30$ to observe the geometric representation generated by each pair $(m,n).$
~MRENTHUSIASM (inspired by TheAMCHub)

## Video Solution
https://youtu.be/O84aJ5OTZ2E
~mathproblemsolvingskills

## Video Solution
https://www.youtube.com/watch?v=LUkQ7R1DqKo
~Mathematical Dexterity
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .