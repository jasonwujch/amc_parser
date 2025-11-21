# 2023 AIME I Problem 10

## Problem

There exists a unique positive integer $a$ for which the sum \[U=\sum_{n=1}^{2023}\left\lfloor\dfrac{n^{2}-na}{5}\right\rfloor\] is an integer strictly between $-1000$ and $1000$ . For that unique $a$ , find $a+U$ .

(Note that $\lfloor x\rfloor$ denotes the greatest integer that is less than or equal to $x$ .)

## Solution (Bounds and Decimal Part Analysis, Rigorous)
Define $\left\{ x \right\} = x - \left\lfloor x \right\rfloor$ .
First, we bound $U$ .
We establish an upper bound of $U$ . We have \begin{align*} U & \leq \sum_{n=1}^{2023} \frac{n^2 - na}{5} \\ & = \frac{1}{5} \sum_{n=1}^{2023} n^2 - \frac{a}{5} \sum_{n=1}^{2023} n \\ & = \frac{1012 \cdot 2023}{5} \left( 1349 - a \right) \\ & \triangleq UB . \end{align*}
We establish a lower bound of $U$ . We have \begin{align*} U & = \sum_{n=1}^{2023} \left( \frac{n^2 - na}{5} - \left\{ \frac{n^2 - na}{5} \right\} \right) \\ & = \sum_{n=1}^{2023} \frac{n^2 - na}{5} - \sum_{n=1}^{2023} \left\{ \frac{n^2 - na}{5} \right\} \\ & = UB - \sum_{n=1}^{2023} \left\{ \frac{n^2 - na}{5} \right\} \\ & \geq UB - \sum_{n=1}^{2023} \mathbf 1 \left\{ \frac{n^2 - na}{5} \notin \Bbb Z \right\} . \end{align*}
We notice that if $5 | n$ , then $\frac{n^2 - na}{5} \in \Bbb Z$ . Thus, \begin{align*} U & \geq UB - \sum_{n=1}^{2023} \mathbf 1 \left\{ \frac{n^2 - na}{5} \notin \Bbb Z \right\} \\ & \geq UB - \sum_{n=1}^{2023} \mathbf 1 \left\{ 5 \nmid n \right\} \\ & = UB - \left( 2023 - \left\lfloor \frac{2023}{5} \right\rfloor \right) \\ & = UB - 1619 \\ & \triangleq LB . \end{align*}
Because $U \in \left[ - 1000, 1000 \right]$ and $UB - LB = 1619 < \left( 1000 - \left( - 1000 \right) \right)$ , we must have either $UB \in \left[ - 1000, 1000 \right]$ or $LB \in \left[ - 1000, 1000 \right]$ .
For $UB \in \left[ - 1000, 1000 \right]$ , we get a unique $a = 1349$ . For $LB \in \left[ - 1000, 1000 \right]$ , there is no feasible $a$ .
Therefore, $a = 1349$ . Thus $UB = 0$ .
Next, we compute $U$ .
Let $n = 5 q + r$ , where $r = {\rm Rem} \ \left( n, 5 \right)$ .
We have \begin{align*} \left\{ \frac{n^2 - na}{5} \right\} & = \left\{ \frac{\left( 5 q + r \right)^2 - \left( 5 q + r \right)\left( 1350 - 1 \right)}{5} \right\} \\ & = \left\{ 5 q^2 + 2 q r - \left( 5 q + r \right) 270 + q + \frac{r^2 + r}{5} \right\} \\ & = \left\{\frac{r^2 + r}{5} \right\} \\ & = \left\{ \begin{array}{ll} 0 & \mbox{ if } r = 0, 4 \\ \frac{2}{5} & \mbox{ if } r = 1, 3 \\ \frac{1}{5} & \mbox{ if } r = 2 \end{array} \right. . \end{align*}
Therefore, \begin{align*} U & = \sum_{n=1}^{2023} \left( \frac{n^2 - na}{5} - \left\{ \frac{n^2 - na}{5} \right\} \right) \\ & = UB - \sum_{n=1}^{2023} \left\{ \frac{n^2 - na}{5} \right\} \\ & = - \sum_{n=1}^{2023} \left\{ \frac{n^2 - na}{5} \right\} \\ & = - \sum_{q=0}^{404} \sum_{r=0}^4 \left\{\frac{r^2 + r}{5} \right\} + \left\{ \frac{0^2 - 0 \cdot a}{5} \right\} + \left\{ \frac{2024^2 - 2024a}{5} \right\} \\ & = - \sum_{q=0}^{404} \left( 0 + 0 + \frac{2}{5} + \frac{2}{5} + \frac{1}{5} \right) + 0 + 0 \\ & = - 405 . \end{align*}
Therefore, $a + U = 1349 - 405 = \boxed{\textbf{944}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
~minor edits by KevinChen_Yay

## Solution 2
We define $U' = \sum^{2023}_{n=1} {\frac{n^2-na}{5}}$ . Since for any real number $x$ , $\lfloor x \rfloor \le x \le \lfloor x \rfloor + 1$ , we have $U \le U' \le U + 2023$ . Now, since $-1000 \le U \le 1000$ , we have $-1000 \le U' \le 3023$ .
Now, we can solve for $U'$ in terms of $a$ . We have: \begin{align*} U' &= \sum^{2023}_{n=1} {\frac{n^2-na}{5}} \\ &= \sum^{2023}_{n=1} {\frac{n^2}{5} - \frac{na}{5}} \\ &= \sum^{2023}_{n=1} {\frac{n^2}{5}} - \sum^{2023}_{n=1} {\frac{na}{5}} \\ &= \frac{\sum^{2023}_{n=1} {{n^2}} - \sum^{2023}_{n=1} {na}}{5} \\ &= \frac{\frac{2023(2023+1)(2023 \cdot 2 + 1)}{6} - \frac{a \cdot 2023(2023+1)}{2} }{5} \\ &= \frac{2023(2024)(4047-3a)}{30} \\ \end{align*} So, we have $U' = \frac{2023(2024)(4047-3a)}{30}$ , and $-1000 \le U' \le 3023$ , so we have $-1000 \le \frac{2023(2024)(4047-3a)}{30} \le 3023$ , or $-30000 \le 2023(2024)(4047-3a) \le 90690$ . Now, $2023 \cdot 2024$ is much bigger than $90690$ or $30000$ , and since $4047-3a$ is an integer, to satsify the inequalities, we must have $4047 - 3a = 0$ , or $a = 1349$ , and $U' = 0$ .
Now, we can find $U - U'$ . We have: \begin{align*} U - U' &= \sum^{2023}_{n=1} {\lfloor \frac{n^2-1349n}{5} \rfloor} - \sum^{2023}_{n=1} {\frac{n^2-1349n}{5}} \\ &= \sum^{2023}_{n=1} {\lfloor \frac{n^2-1349n}{5} \rfloor - \frac{n^2-1349n}{5}} \end{align*}. Now, if $n^2-1349n \equiv 0 \text{ (mod 5)}$ , then $\lfloor \frac{n^2-1349n}{5} \rfloor - \frac{n^2-1349n}{5} = 0$ , and if $n^2-1349n \equiv 1 \text{ (mod 5)}$ , then $\lfloor \frac{n^2-1349n}{5} \rfloor - \frac{n^2-1349n}{5} = -\frac{1}{5}$ , and so on. Testing with $n \equiv 0,1,2,3,4, \text{ (mod 5)}$ , we get $n^2-1349n \equiv 0,2,1,2,0 \text{ (mod 5)}$ respectively. From 1 to 2023, there are 405 numbers congruent to 1 mod 5, 405 numbers congruent to 2 mod 5, 405 numbers congruent to 3 mod 5, 404 numbers congruent to 4 mod 5, and 404 numbers congruent to 0 mod 5. So, solving for $U - U'$ , we get: \begin{align*} U - U' &= \sum^{2023}_{n=1} {\lfloor \frac{n^2-1349n}{5} \rfloor - \frac{n^2-1349n}{5}} \\ &= 404 \cdot 0 - 405 \cdot \frac{2}{5} - 405 \cdot \frac{1}{5} - 405 \cdot \frac{2}{5} - 404 \cdot 0 \\ &= -405(\frac{2}{5}+\frac{1}{5}+\frac{2}{5}) \\ &= -405 \end{align*} Since $U' = 0$ , this gives $U = -405$ , and we have $a + U = 1349-405 = \boxed{944}$ .
~ genius_007

## Solution 3 (Quick)
We can view the floor function in this problem as simply subtracting the remainder of $n^2 - na$ (mod $5$ ) from the numerator of $\frac{n^2-na}{5}$ . For example, $\left\lfloor \frac{7}{5} \right\rfloor = \frac{7-2}{5} = 1$ .
Note that the congruence of $n^2 - na$ (mod $5$ ) loops every time $n$ increases by 5. Also, note that the congruence of $a$ (mod $5$ ) determines the set of congruences of $n^2 - na$ for each congruence of $n$ (mod $5$ ).
For example, if $a \equiv 1$ (mod $5$ ), the set of remainders is $(0, 2, 1, 2, 0)$ for $n \equiv 1,2,3,4,0$ (mod $5$ ). Let the sum of these elements be $s$ . Note that for each “loop” of the numerator (mod $5$ ), each element of the set will be subtracted exactly once, meaning $s$ is subtracted once for each loop. The value of the numerator will loop $404$ times (mod $5$ ) throughout the sum, as $5 \cdot 404=2020$ . Then
$U \approx \frac {\left( \frac {n(n+1)(2n+1)}{6} - \frac{(a)(n)(n+1)}{2} -404s \right)}{5}$
Where $n=2023$ . Note that since $5 \cdot 404=2020$ , this is an approximation for $U$ because the equation disregards the remainder (mod $5$ ) when $n=2021, 2022$ , and $2023$ so we must subtract the first 3 terms of our set of congruences one extra time to get the exact value of $U$ (*). However, we will find that this is a negligible error when it comes to the inequality $-1000<U<1000$ , so we can proceed with this approximation to solve for $a$ .
Factoring our approximation gives $U \approx \frac {\frac{(n)(n+1)(2n+1 - 3a)}{6}-404s}{5}$
We set $a= \frac{(2n+1)}{3} = 1349$ to make $\frac{(n)(n+1)(2n+1 - 3a)}{6}=0$ , accordingly minimizing $|U|$ , yielding $U \approx \frac{-404s}{5}$
If $a$ increases or decreases by $1$ , then $U$ changes by $\frac {(n)(n+1)}{2 \cdot 5} = \frac {2023 \cdot 2024}{10}$ which clearly breaks the inequality on $U$ . Therefore $a=1349 \equiv 4$ (mod $5$ ) giving the set of remainders $(2,1,2,0,0)$ , so $s=5$ and our approximation yields $U \approx -404$ . However, we must subtract 2, 1, and 2 (*) giving us $U = - 404 - \frac{(2+1+2)}{5} = - 405$ , giving an answer of $1349-405= \boxed{944}$
~Spencer Danese

## Solution 4 (Calculus)
Consider the integral \[\int_{0}^{2023} \dfrac{n^2-na}{5} \, dn.\] We hope this will give a good enough appoximation of $U$ to find $a.$ However, this integral can be easily evaluated to be \[\dfrac{1}{15}2023^3-\dfrac{a}{10}2023^2=2023^2\left(\dfrac{2023}{15}-\dfrac{a}{10}\right).\] Because we want this to be as close to $0$ as possible, we find that $a$ should equal $1349.$ Then, evaluating the sum becomes trivial. Set \[U'=\sum_{n=1}^{2023}\dfrac{n^2-1349n}{5}\] and \[U''=\sum_{n=1}^{2023}\{\dfrac{n^2-1349n}{5}\}.\] Then $U=U'-U''.$ We can evaluate $U'$ to be $0$ and $U''$ to be $-405$ (using some basic number theory). Thus, $U=-405$ and the answer is \[1349+(-405)=\boxed{944}.\] ~BS2012

## Video Solution
2023 AIME I #10
MathProblemSolvingSkills.com

## Video Solution by Punxsutawney Phil
https://youtu.be/jQVbNJr0tX8

## Video Solution by Steven Chen
https://youtu.be/fxsPmL6wuW4

## Video Solution by Mathematical Dexterity
https://www.youtube.com/watch?v=49XIe2jx9zg
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .