# 2016 AIME I Problem 10

## Problem

A strictly increasing sequence of positive integers $a_1$ , $a_2$ , $a_3$ , $\cdots$ has the property that for every positive integer $k$ , the subsequence $a_{2k-1}$ , $a_{2k}$ , $a_{2k+1}$ is geometric and the subsequence $a_{2k}$ , $a_{2k+1}$ , $a_{2k+2}$ is arithmetic. Suppose that $a_{13} = 2016$ . Find $a_1$ .

## Solution 1
We first create a similar sequence where $a_1=1$ and $a_2=2$ . Continuing the sequence,
\[1, 2,4,6,9,12,16,20,25,30,36,42,49,\cdots\]
Here we can see a pattern; every second term (starting from the first) is a square, and every second term (starting from the third) is the end of a geometric sequence. This can be proven by induction. Similarly, $a_{13}$ would also need to be the end of a geometric sequence (divisible by a square). We see that $2016$ is $2^5 \cdot 3^2 \cdot 7$ , so the squares that would fit in $2016$ are $1^2=1$ , $2^2=4$ , $3^2=9$ , $2^4=16$ , $2^2 \cdot 3^2 = 36$ , and $2^4 \cdot 3^2 = 144$ . By simple inspection $144$ is the only plausible square, since the other squares in the sequence don't have enough elements before them to go all the way back to $a_1$ while still staying as positive integers. $a_{13}=2016=14\cdot 144$ , so $a_1=14\cdot 36=\fbox{504}$ .
~IYN~

## Solution 2
Setting $a_1 = a$ and $a_2 = ka$ , the sequence becomes:
\[a, ka, k^2a, k(2k-1)a, (2k-1)^2a, (2k-1)(3k-2)a, (3k-2)^2a, \cdots\] and so forth, with $a_{2n+1} = (nk-(n-1))^2a$ . Then, $a_{13} = (6k-5)^2a = 2016$ . Keep in mind, $k$ need not be an integer, only $k^2a, (k+1)^2a,$ etc. does. $2016 = 2^5*3^2*7$ , so only the squares $1, 4, 9, 16, 36,$ and $144$ are plausible for $(6k-5)^2$ . But when that is anything other than $2$ , $k^2a$ is not an integer. Therefore, $a = 2016/2^2 = 504$ .
Thanks for reading, Rowechen Zhong.

## Solution 3
Instead of setting $a_1$ equal to something and $a_2$ equal to something, note that it is rather easier to set $a_1=x^2$ and $a_3=y^2$ so that $a_2=xy,a_4=y(2y-x),a_5=(2y-x)^2$ and so on until you reached $a_{13}=(6y-5x)^2$ (Or simply notice the pattern), so $6y-5x=\sqrt{2016}=12\sqrt{14}$ . Note that since each of the terms has degree 2 so if you multiply $x$ and $y$ by $\sqrt{14}$ you multiply each term by $14$ so each term is still a integer if the terms are already integers before you multiply $x$ and $y$ by $\sqrt{14}$ , so let $w=\frac{x}{\sqrt{14}}$ and $z=\frac{y}{\sqrt{14}}$ so $6z-5w=12$ . Then, for the sequence to be strictly increasing positive integers we have $(w,z)=(6,7)$ so $x=6\sqrt{14}$ and $a_1=x^2=6^2 \cdot 14=\boxed{504}$ ~ Ddk001

## Solution 4(very risky and very stupid)
The thirteenth term of the sequence is $2016$ , which makes that fourteenth term of the sequence $2016+r$ and the $15^{\text{th}}$ term $\frac{(2016+r)^2}{2016}$ . We note that $r$ is an integer so that means $\frac{r^2}{2016}$ is an integer. Thus, we assume the smallest value of $r$ , which is $168$ . We bash all the way back to the first term and get our answer of $\boxed{504}$ .
-Pleaseletmewin

## Solution 5
Let $a_{2k-1}=s$ where $k=1$ . Then, $a_{2k}=sr \Longrightarrow a_{2k+1}=sr^2$ . Continuing on, we get $a_{2k+2}=sr(r-1)+sr^2=sr(2r-1) \Longrightarrow a_{2k+3}=sr^2(\frac{2r-1}{r})^2=s(2r-1)^2$ . Moreover, $a_{2k+4}=s(2r-1)(r-1)+s(2r-1)^2=s(2r-1)(3r-2) \Longrightarrow a_{2k+5}=s(2r-1)^2(\frac{3r-2}{2r-1})^2=s(3r-2)^2$ .
It is clear now that $a_{2k+2c}=s(cr-(c-1))((c+1)r-c)$ and $a_{2k+2c-1}=s(cr-(c-1))^2$ . Plugging in $c=6$ , $a_{13}=s(6r-5)^2=2016$ . The prime factorization of $2016=2^5\cdot3^2\cdot7$ so we look for perfect squares.
$6r-5\equiv (6r-5)^2\equiv 1\pmod{6}$ if $r$ is an integer, and $\frac{\omega+5}{6}=r \Longrightarrow 6\mid{s}$ if $r$ is not an integer and $\omega$ is rational, so $6\mid{s}$ . This forces $s=2\cdot3^2\cdot7\cdot{N}$ . Assuming $(6r-5)$ is an integer, it can only be $2^x$ , $x\in{1,2}$ .
If $6r-5=2^1$ , $r=\frac{7}{6}$ . If $6r-5=2^2$ , $r=\frac{3}{2}$ . Note that the latter cannot work since $a_{2k+1}=s(\frac{9}{4}) \Longrightarrow 4\mid{s}$ but $N=1 \Longrightarrow s=2\cdot3^2\cdot7$ in this scenario. Therefore, $r=\frac{7}{6} \Longrightarrow s=\frac{2016}{2^2}=504$ . Plugging back $k=1$ , $a_1=s=\boxed{504}$
~ Magnetoninja

## Solution 6 (Headache)
Bash all the way from $a_1$ and $a_2$ to $a_{13}=2016$ to get to the equation $a_1\left(\frac{6a_2}{a_1}-5\right)^2=2016$ and then $a_2=2\sqrt{14a_1}+\frac{5}{6}a_1$ (direct consequence). Notice that from the two equations we can deduce that:
1) $a_1\mid2016$ ,
2) $6\mid a_1$ , and
3) $\sqrt{\frac{a_1}{14}}\in\mathbb{Z}$ .
Since $2016=2^5\cdot3^2\cdot7=14(2^4\cdot 3^2)$ , the only possible values of $a_1$ that satisfy the conditions are $126$ , $504$ , and $2016$ itself. Obviously $2016$ cannot be a correct answer choice (from AIME rules), and if $a_1=126$ , $a_3\not\in\mathbb{Z}$ , so $\boxed{504}$ is the solution.
~eevee9406

## Solution 7
Let $a_{11} = x$ . Then, $a_{12} = xr$ and $a_{13} = xr^2 = 2016$ . Note, in order to alternate between arithmetic and geometric sequences, you would want $r$ to be as small as possible so our sequence is always positive as stated in the question. Since $2016 = 2^5 \cdot 3^2 \cdot 7$ , the smallest ratio, r, (which must be greater than 1 as the sequence is strictly increasing) must satisfy that $a_12 = \frac{2016}{r}$ and $a_11 = \frac{2016}{r^2}$ are both integers. Therefore, $\frac{1}{r}$ can at min be $\frac{m}{2^2 \cdot 3}$ . To minimize this we have $m = 11$ so $r = \frac{12}{11}$ . Doing this and working backwards, we get the sequence $a_1 = 504 a_2 = 588 a_3 = 686 a_4 = 784 a_5 = 896 a_6 = 1008 a_7 = 1134 a_8 = 1260 a_9 = 1400 a_{10} = 1540 a_{11} = 1694 a_{12} = 1848 a_{13} = 2016$ so $a_1 = \boxed{504}$ ~Sid-darth-vater

## Video Solution
https://youtu.be/fVRHaPE88Cg
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .