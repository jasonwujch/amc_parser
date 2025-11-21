# 2018 AMC 10A Problem 22

## Problem

Let $a, b, c,$ and $d$ be positive integers such that $\gcd(a, b)=24$ , $\gcd(b, c)=36$ , $\gcd(c, d)=54$ , and $70<\gcd(d, a)<100$ . Which of the following must be a divisor of $a$ ? (gcd means greatest common factor)

$\textbf{(A)} \text{ 5} \qquad \textbf{(B)} \text{ 7} \qquad \textbf{(C)} \text{ 11} \qquad \textbf{(D)} \text{ 13} \qquad \textbf{(E)} \text{ 17}$

## Solution 1
The GCD information tells us that $24$ divides $a$ , both $24$ and $36$ divide $b$ , both $36$ and $54$ divide $c$ , and $54$ divides $d$ . Note that we have the prime factorizations: \begin{align*} 24 &= 2^3\cdot 3,\\ 36 &= 2^2\cdot 3^2,\\ 54 &= 2\cdot 3^3. \end{align*}
Hence we have \begin{align*} a &= 2^3\cdot 3\cdot w\\ b &= 2^3\cdot 3^2\cdot x\\ c &= 2^2\cdot 3^3\cdot y\\ d &= 2\cdot 3^3\cdot z \end{align*} for some positive integers $w,x,y,z$ . Now if $3$ divides $w$ , then $\gcd(a,b)$ would be at least $2^3\cdot 3^2$ which is too large, hence $3$ does not divide $w$ . Similarly, if $2$ divides $z$ , then $\gcd(c,d)$ would be at least $2^2\cdot 3^3$ which is too large, so $2$ does not divide $z$ . Therefore, \[\gcd(a,d)=2\cdot 3\cdot \gcd(w,z)\] where neither $2$ nor $3$ divide $\gcd(w,z)$ . In other words, $\gcd(w,z)$ is divisible only by primes that are at least $5$ . The only possible value of $\gcd(a,d)$ between $70$ and $100$ and which fits this criterion is $78=2\cdot3\cdot13$ , so the answer is $\boxed{\textbf{(D) }13}$ .

## Solution 2
We can say that $a$ and $b$ 'have' $2^3 \cdot 3$ , that $b$ and $c$ have $2^2 \cdot 3^2$ , and that $c$ and $d$ have $3^3 \cdot 2$ . Combining $1$ and $2$ yields $b$ has (at a minimum) $2^3 \cdot 3^2$ , and thus $a$ has $2^3 \cdot 3$ (and no more powers of $3$ because otherwise $\gcd(a,b)$ would be different). In addition, $c$ has $3^3 \cdot 2^2$ , and thus $d$ has $3^3 \cdot 2$ (similar to $a$ , we see that $d$ cannot have any other powers of $2$ ). We now assume the simplest scenario, where $a = 2^3 \cdot 3$ and $d = 3^3 \cdot 2$ . According to this base case, we have $\gcd(a, d) = 2 \cdot 3 = 6$ . We want an extra factor between the two such that this number is between $70$ and $100$ , and this new factor cannot be divisible by $2$ or $3$ . Checking through, we see that $6 \cdot 13$ is the only one that works. Therefore the answer is $\boxed{\textbf{(D) } 13}$ .
Solution by JohnHankock

## Solution 3 (Better notation)
First off, note that $24$ , $36$ , and $54$ are all of the form $2^x\times3^y$ . The prime factorizations are $2^3\times 3^1$ , $2^2\times 3^2$ and $2^1\times 3^3$ , respectively. Now, let $a_2$ and $a_3$ be the number of times $2$ and $3$ go into $a$ , respectively. Define $b_2$ , $b_3$ , $c_2$ , and $c_3$ similarly. Now, translate the $lcm$ s into the following: \[1) \min(a_2,b_2)=3\] \[2) \min(a_3,b_3)=1\] \[3) \min(b_2,c_2)=2\] \[4) \min(b_3,c_3)=2\] \[5) \min(c_2,d_2)=1\] \[6) \min(c_3,d_3)=3\]
From $4)$ , we see that $b_3 \geq 2$ , thus from $2)$ , $a_3 = 1$ . Similarly, from $3)$ , $c_2 \geq 2$ , thus from $5)$ , $d_2 = 1$ .
Note also that $d_3 \geq 3$ and $a_2 \geq 3$ . Therefore \[\min(a_2, d_2) = 1\] \[\min(a_3, d_3) = 1\] Thus, $\gcd(a, d) = 2 \times 3 \times k$ for some $k$ having no factors of $2$ or $3$ .
Since $70 < \gcd(a, d) < 100$ , the only values for k are $12, 13, 14, 15, 16$ , but all have either factors of $2$ or $3$ , except $\boxed{\textbf{(D)} 13}$ . And we're done.
~Rowechen Zhong ~MannsNotHot

## Solution 4 (Fastest)
Notice that $\gcd (a,b,c,d)=\gcd(\gcd(a,b),\gcd(b,c),\gcd(c,d))=\gcd(24,36,54)=6$ , so $\gcd(d,a)$ must be a multiple of $6$ . The only answer choice that gives a value between $70$ and $100$ when multiplied by $6$ is $\boxed{\textbf{(D) } 13}$ . - mathleticguyyy + einstein
In the case where there can be 2 possible answers, we can do casework on $\gcd(d,a)$ ~Williamgolly

## Solution 5
Since $\gcd (a,b) = 24$ , $a = 24j$ and $b = 24k$ for some positive integers $j,k$ such that $j$ and $k$ are relatively prime.
Similarly , since $\gcd (b,c) = 36$ , we have $b = 24k$ and $c=36m$ with the same criteria. However, since $24$ is not a multiple of $36$ , we must contribute an extra $3$ to $b$ in order to make it a multiple of $36$ . So, $k$ is a multiple of three, and it is relatively prime to $m$ .
Finally, $\gcd (c,d) = 54$ , so using the same logic, $m$ is a multiple of $3$ and is relatively prime to $n$ where $d = 54n$ .
Since we can't really do anything with these messy expressions, we should try some sample cases of $a,b,c$ and $d$ . Specifically, we let $j = 5, 7, 11, 13$ or $17$ , and see which one works.
First we let $j= 5$ . Note that all of these values of $j$ work for the first $\gcd$ expression because they are all not divisible by $3$ .
Without the loss of generality, we let $k=m=3$ for all of our sample cases. We can also adjust the value of $n$ in $d=54n$ , since there is no fixed value for $\gcd(a,d)$ ; there is only a bound.
So we try to make our bound $70 < \gcd(a,d) < 100$ satisfactory. We do so by letting $j=n$ .
Testing our first case $a=24 \cdot 5$ and $d = 54 \cdot 5$ , we find that $\gcd(a,d) = 30$ . To simplify our work, we note that $\gcd(24,54) = 6$ , so $\gcd(24k, 54k)$ for all $k>1$ is equal to $6k$ .
So now, we can easily find our values of $\gcd(a,b)$ :
\[\gcd(24 \cdot 5, 54 \cdot 5) = 6 \cdot 5 = 30\]
\[\gcd(24 \cdot 7, 54 \cdot 7) = 6 \cdot 7 = 42\]
\[\gcd(24 \cdot 11, 54 \cdot 11) = 6 \cdot 11 = 66\]
\[\boxed{\gcd(24 \cdot 13, 54 \cdot 13) = 6 \cdot 13 = 78}\]
\[\gcd(24 \cdot 17, 54 \cdot 17) = 6 \cdot 17 = 104\]
We can clearly see that only $j=n=13$ is in the bound $70 < \gcd(a,d) < 100$ . So, $13$ must be a divisor of $a$ , which is answer choice $\boxed{\textbf{(D)}}$ .
-FIREDRAGONMATH16

## Solution 6
[asy] //Variable Declarations defaultpen(0.45); size(200pt); fontsize(15pt); pair X, Y, Z, W; real R; path quad; //Variable Definitions R = 1; X = R*dir(45); Y = R*dir(135); Z = R*dir(-135); W = R*dir(-45); quad = X--Y--Z--W--cycle; //Diagram draw(quad); label("$b$",X,NE); label("$a=2^3 \cdot 3 \cdot p$",Y,NW); label("$d=2 \cdot 3^3 \cdot q$",Z,SW); label("$c$",W,SE); label("$2^3 \cdot 3$",X--Y); label("$2^2 \cdot 3^2$",X--W); label("$2 \cdot 3^3$",Z--W); label("$2 \cdot 3 \cdot k$",Z--Y); [/asy]
The relationship of $a$ , $b$ , $c$ , and $d$ is shown in the above diagram. $gcd(a,d)=2 \cdot 3 \cdot k$ . $70 < 6k < 100$ , $12 \le k \le 16$ , $k=\boxed{\textbf{(D) }13}$
Note that $gcd(b,c)=36$ is not required to solve the problem.
~ isabelchen

## Solution 7 (Easier version of Solution 1)
Just as in solution $1$ , we prime factorize $a, b, c$ and $d$ to observe that
$a=2^3\cdot{3}\cdot{w}$
$b=2^3\cdot{3^2}\cdot{x}$
$c=2^2\cdot{3^3}\cdot{y}$
$d=2\cdot{3^3}\cdot{z}.$
Substituting these expressions for $a$ and $d$ into the final given,
$70<\text{gcd}(2\cdot{3^3}\cdot{z}, 2^3\cdot{3}\cdot{w})<100.$
The greatest common divisor of these two numbers is already $6$ . If $k$ is what we wish to multiply $6$ by to obtain the gcd of these two numbers, then
$70<6k<100$ . Testing the answer choices, only $13$ works for $k$ (in order for the compound inequality to hold). so our gcd is $78$ , which means that $\boxed{\textbf{(D) }13}$ must divide $a$ .
-Benedict T (countmath1)

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2018amc10a/467
~ dolphin7

## Video Solution
https://youtu.be/yjrqINsQP5c
~savannahsolver

## Video Solution by OmegaLearn (Meta-Solving Technique)
https://youtu.be/GmUWIXXf_uk?t=1003
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .