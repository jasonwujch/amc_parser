# 2022 AIME II Problem 13

## Problem

There is a polynomial $P(x)$ with integer coefficients such that \[P(x)=\frac{(x^{2310}-1)^6}{(x^{105}-1)(x^{70}-1)(x^{42}-1)(x^{30}-1)}\] holds for every $0<x<1.$ Find the coefficient of $x^{2022}$ in $P(x)$ .

## Solution 1
Because $0 < x < 1$ , we have \begin{align*} P \left( x \right) & = \sum_{a=0}^6 \sum_{b=0}^\infty \sum_{c=0}^\infty \sum_{d=0}^\infty \sum_{e=0}^\infty \binom{6}{a} x^{2310a} \left( - 1 \right)^{6-a} x^{105b} x^{70c} x^{42d} x^{30e} \\ & = \sum_{a=0}^6 \sum_{b=0}^\infty \sum_{c=0}^\infty \sum_{d=0}^\infty \sum_{e=0}^\infty \left( - 1 \right)^{6-a} x^{2310 a + 105 b + 70 c + 42 d + 30 e} . \end{align*}
Denote by $c_{2022}$ the coefficient of $P \left( x \right)$ . Thus, \begin{align*} c_{2022} & = \sum_{a=0}^6 \sum_{b=0}^\infty \sum_{c=0}^\infty \sum_{d=0}^\infty \sum_{e=0}^\infty \left( - 1 \right)^{6-a} \Bbb I \left\{ 2310 a + 105 b + 70 c + 42 d + 30 e = 2022 \right\} \\ & = \sum_{b=0}^\infty \sum_{c=0}^\infty \sum_{d=0}^\infty \sum_{e=0}^\infty \left( - 1 \right)^{6-0} \Bbb I \left\{ 2310 \cdot 0 + 105 b + 70 c + 42 d + 30 e = 2022 \right\} \\ & = \sum_{b=0}^\infty \sum_{c=0}^\infty \sum_{d=0}^\infty \sum_{e=0}^\infty \Bbb I \left\{ 105 b + 70 c + 42 d + 30 e = 2022 \right\} . \end{align*}
Now, we need to find the number of nonnegative integer tuples $\left( b , c , d , e \right)$ that satisfy \[ 105 b + 70 c + 42 d + 30 e = 2022 . \hspace{1cm} (1) \]
Modulo 2 on Equation (1), we have $b \equiv 0 \pmod{2}$ . Hence, we can write $b = 2 b'$ . Plugging this into (1), the problem reduces to finding the number of nonnegative integer tuples $\left( b' , c , d , e \right)$ that satisfy \[ 105 b' + 35 c + 21 d + 15 e = 1011 . \hspace{1cm} (2) \]
Modulo 3 on Equation (2), we have $2 c \equiv 0 \pmod{3}$ . Hence, we can write $c = 3 c'$ . Plugging this into (2), the problem reduces to finding the number of nonnegative integer tuples $\left( b' , c' , d , e \right)$ that satisfy \[ 35 b' + 35 c' + 7 d + 5 e = 337 . \hspace{1cm} (3) \]
Modulo 5 on Equation (3), we have $2 d \equiv 2 \pmod{5}$ . Hence, we can write $d = 5 d' + 1$ . Plugging this into (3), the problem reduces to finding the number of nonnegative integer tuples $\left( b' , c' , d' , e \right)$ that satisfy \[ 7 b' + 7 c' + 7 d' + e = 66 . \hspace{1cm} (4) \]
Modulo 7 on Equation (4), we have $e \equiv 3 \pmod{7}$ . Hence, we can write $e = 7 e' + 3$ . Plugging this into (4), the problem reduces to finding the number of nonnegative integer tuples $\left( b' , c' , d' , e' \right)$ that satisfy \[ b' + c' + d' + e' = 9 . \hspace{1cm} (5) \]
The number of nonnegative integer solutions to Equation (5) is $\binom{9 + 4 - 1}{4 - 1} = \binom{12}{3} = \boxed{\textbf{(220) }}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 2
Note that $2022 = 210\cdot 9 +132$ . Since the only way to express $132$ in terms of $105$ , $70$ , $42$ , or $30$ is $132 = 30+30+30+42$ , we are essentially just counting the number of ways to express $210*9$ in terms of these numbers. Since $210 = 2*105=3*70=5*42=7*30$ , it can only be expressed as a sum in terms of only one of the numbers ( $105$ , $70$ , $42$ , or $30$ ). Thus, the answer is (by sticks and stones) \[\binom{12}{3} = \boxed{\textbf{(220)}}\]
~Bigbrain123

## Solution 3
We know that $\frac{a^n-b^n}{a-b}=\sum_{i=0}^{n-1} a^{n-1-i}b^i$ . Applying this, we see that \[P(x)=(1+x^{105}+x^{210}+...)(1+x^{70}+x^{140}+...)(1+x^{42}+x^{84}+...)(1+x^{30}+x^{60}+...)(x^{4620}-2x^{2310}+1)\] The last factor does not contribute to the $x^{2022}$ term, so we can ignore it. Thus we only have left to solve the equation $105b+70c+42d+30e=2022$ , and we can proceed from here with Solution 1.
~MathIsFun286

## Solution 4 (Generating Function Bash)
Essentially we want the coefficient of $x^{2022}$ in the expansion
\[\frac{1}{(1 - x^{105})(1 - x^{70})(1 - x^{42})(1 - x^{30})}\]
As $(x^{2310} -1)^{6}$ does not contribute to the expansion, we omit it.
Notice $\text{lcm}(105,70,42,30) = 210$ , so we can rewrite the generating function as
\[\frac{(1 + x^{105})(1 + x^{70} + x^{140})(1 + x^{42} + ... + x^{168})(1 + x^{30} + ... + x^{180})}{(1-x^{210})^{4}}\]
Notice to obtain a $x^{2022}$ value, the $x^{42}$ must be used, so we can reduce the problem to finding the coefficient of $x^{1980}$ in
\[\frac{(1 + x^{105})(1 + x^{70} + x^{140})(1 + x^{30} + ... + x^{180})}{(1-x^{210})^{4}}\]
If $(1 - x^{210})^{-4}$ is expanded, it will only generate multiples of 210. To compensate this, notice $1980 \equiv 90 \pmod{210}$ , which means we need terms with a power of a 90 to acheive what we want (300 and larger values can be shown to be impossible upon inspection). This implies that the first two brackets do not contribute and we are left with
\[\frac{x^{90}}{(1-x^{210})^{4}}\]
This reduces to finding the coefficient of $x^{1890}$ for the expansion $(1 - x^{210})^{-4}$ , which is $\binom{12}{3} = \fbox{220}$

## Solution 5 (Similar to solution 1)
Expand the numerator and divide each term in the denominator separately to get
Since the factor of $(x^{2310}-1)^{2}$ is too big so we choose the -1 from both the 2 factors to get a 1. So now we need to find the number of quadruples of non negative integers $(a,b,c,d)$ such that $\textbf{105a + 70b + 42c + 30d = 2022}$ . By considering modulo $2$ , $3$ , $5$ , $7$ we can reduce the above expression to something that can be solved using stars-and-bars.
Now we put in $a=2x$ , $b=3y$ , $c=5z+1$ and $d=7w+3$ to get
By stars-and-bars the answer is $\binom{9+4-1}{4-1} = \boxed{\textbf{220}}$ .
~Lakshya Pamecha

## Video Solution
https://youtu.be/v2SFCqWOBjs
~MathProblemSolvingSkills.com

## Video Solution by The Power of Logic
https://youtu.be/oJ1witTvG3A
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .