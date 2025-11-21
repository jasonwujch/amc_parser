# 2023 AMC 10B Problem 14

## Problem

How many ordered pairs of integers $(m, n)$ satisfy the equation $m^2+mn+n^2 = m^2n^2$ ?

$\textbf{(A) }7\qquad\textbf{(B) }1\qquad\textbf{(C) }3\qquad\textbf{(D) }6\qquad\textbf{(E) }5$

## Solution 1
Let's use 10th grade math to solve this. After all, it is called the AMC 10 for a reason!
We have \[m^2 + mn + n^2 = m^2n^2.\] We subtract \( mn \) on both sides to get
\( m^2 + n^2 = m^2n^2 - mn \).
Fun Fact! You can write \( m^2 + n^2 \) as \( (m+n)^2 - 2mn \)! Let's use this!
We convert the Left Hand Side into \( (m+n)^2 - 2mn \) to get \( (m+n)^2 - 2mn = m^2n^2 - mn \).
Adding by \( 2mn \) gives us \( (m+n)^2 = m^2n^2 + mn \).
We aren't done yet though! \( m^2n^2 + mn \) can be simplified into \( mn(mn+1) \), giving us \( (m+n)^2 = mn(mn+1) \).
Okay so now we're done, but, Pinotation, this doesn't do anything! Well, now we can use the Zero Product Property!
How? I'll show you!
We subtract \( mn(mn+1) \) on both sides of the equation to get \( (m+n)^2 - mn(mn+1) = 0 \). Now we do a bit of casework.
Notice how \( (m+n)^2 - mn(mn+1) = 0 \) is just \( (m+n)(m+n) - mn(mn+1) = 0 \). So, either \( m+n = 0 \) and \( mn = 0 \), or \( m +n = 0 \) and \( mn+1 = 0 \). Let's look at it through both cases.
Case 1: \( m+n = 0 \) and \( mn = 0 \). If \( m+n = 0 \) and \( mn = 0 \), then that must mean that either \( m = 0 \) or \( n = 0 \), and if we substitute either \( m=0 \) or \( n=0 \) in, we still get either \( m=0 \) or \( n=0 \), so therefore we have 1 ordered pair, \( (0,0) \).
Case 2: \( m +n = 0 \) and \( mn+1 = 0 \). \( mn+1 =0 \) means that \( mn=-1 \). So, for this to be possible, either \( m = -1 \) and \( n=1 \), or \( m=1 \) and \( n=-1 \). Let's check for contradictions quickly. We see that \( m + n = 0 \), and \( -1 + 1 = 0 \) and \( 1 - 1 =0 \), so we know the ordered pairs \( (-1,1) \) and \( (1,-1) \) both work.
We have a total of $\boxed{\textbf{(C) 3}}.$ ordered pairs. \( (-1,1) \), \( (0,0) \), and \( (1,-1) \).
~Pinotation

## Solution 2
Clearly, $m=0,n=0$ is one of the solutions. However, we can be quite sure that there are more, so we apply Simon's Favorite Factoring Trick to get the following:
\begin{align*} m^2+mn+n^2 &= m^2n^2\\ m^2+mn+n^2 +mn &= m^2n^2 +mn\\ (m+n)^2 &= m^2n^2 +mn\\ (m+n)^2 &= mn(mn+1).\\ \end{align*}
Essentially, this says that the product of two consecutive numbers $mn,mn+1$ must be a perfect square. This is impossible except for when $mn=0$ or $mn+1=0$ . $mn=0$ gives $(0,0)$ . $mn=-1$ gives $(1,-1), (-1,1)$ . Answer: $\boxed{\textbf{(C) 3}}.$
~Technodoggo ~minor edits by lucaswujc ~minor edits by luke22

## Solution 3
Case 1: $mn = 0$ .
In this case, $m = n = 0$ .
Case 2: $mn \neq 0$ .
Denote $k = {\rm gcd} \left( m, n \right)$ . Denote $m = k u$ and $n = k v$ . Thus, ${\rm gcd} \left( u, v \right) = 1$ .
Thus, the equation given in this problem can be written as \[ u^2 + uv + v^2 = k^2 u^2 v^2 . \]
Modulo $u$ , we have $v^2 \equiv 0 \pmod{u}$ . Because ${\rm gcd} \left( u, v \right) = 1$ ., we must have $|u| = |v| = 1$ . Plugging this into the above equation, we get $2 + uv = k^2$ . Thus, we must have $uv = -1$ and $k = 1$ .
Thus, there are two solutions in this case: $\left( m , n \right) = \left( 1, -1 \right)$ and $\left( m , n \right) = \left( -1, 1 \right)$ .
Putting all cases together, the total number of solutions is $\boxed{\textbf{(C) 3}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com) ~ sravya_m18

## Solution 4 (Discriminant)
We can move all terms to one side and write the equation as a quadratic in terms of $n$ to get \[(1-m^2)n^2+(m)n+(m^2)=0.\] The discriminant of this quadratic is \[\Delta = m^2-4(1-m^2)(m^2)=m^2(4m^2-3).\] For $n$ to be an integer, we must have $m^2(4m^2-3)$ be a perfect square. Thus, either $(2m)^2-3$ is a perfect square or $m^2 = 0$ and $m = 0$ . The first case gives $m=-1,1$ (larger squares are separated by more than 3), which result in the equations $-n+1=0$ and $n-1=0$ , for a total of two pairs: $(-1,1)$ and $(1,-1)$ . The second case gives the equation $n^2=0$ , so it's only pair is $(0,0)$ . In total, the total number of solutions is $\boxed{\textbf{(C) 3}}$ .
~A_MatheMagician

## Solution 5 (Nice Substitution)
Let $x=m+n, y=mn$ then \[x^2-y=y^2\]
Completing the square in $y$ and multiplying by 4 then gives \[4x^2+1=(2y+1)^2\]
Since the RHS is a square, clearly the only solutions are $x=0,y=0$ and $x=0,y=-1$ .
The first gives $(0,0)$ .
The second gives $(-1,1)$ and $(1,-1)$ by solving it as a quadratic with roots $m$ and $n$ .
Thus there are $\boxed{\textbf{(C) 3}}$ solutions.
~ Grolarbear

## Solution 6 (Alternative Method for Manipulation)
$m^2 + mn + n^2 = m^2n^2$
$mn = m^2n^2 - m^2 - n^2$
$mn + 1 = m^2(n^2 - 1) - 1(n^2 - 1)$
$mn + 1 = (m + 1)(m - 1)(n + 1)(n - 1)$
Notice that the right side can be zero or one. If the right side is zero, m and n can be $(-1,1)$ and $(1,-1)$ . If the right side is one, m and n can be $(0,0)$ . There are $\boxed{\textbf{(C) 3}}$ solutions.
~unhappyfarmer

## Solution 7 (Obtaining ranges)
Set $m\leq n$ . Then, we can say that
\[3n^2\geq m^2n^2\]
\[3\geq m^2\]
Or $-\sqrt{3} \leq m \leq \sqrt{3}$ , and since we are dealing with integers, $m=-1$ , $0$ or $1$ . Testing these numbers, we get $n=1$ , $n=0$ and $n=-1$ respectively. Although the solution $(1,-1)$ is a solution in the end, our initial condition for this case was $m\leq n$ . For better rigour, we can just consider the other case $m>n$ to validate solution $(1,-1)$ .
-lisztepos

## Solution 8 (Inequality)
If $mn = 0$ , then $m^2 + 0 + n^2 = 0$ , $(m, n) = (0, 0)$ .
If $mn \neq 0$ , then
\[\frac{m^2 + mn + n^2}{m^2n^2} = 1\]
\[\frac{1}{m^2} + \frac{1}{mn} + \frac{1}{n^2} = 1\]
\[\frac{1}{m^2} + \frac{2}{|mn|} + \frac{1}{n^2} > 1\]
\[\left(\frac{1}{|m|} + \frac{1}{|n|}\right)^2 > 1\]
\[\frac{1}{|m|} + \frac{1}{|n|} > 1\]
Obviously, at least one of $|m|, |n|$ is 1. If $m = 1$ , $1 + n + n^2 = n^2 \Rightarrow n = -1$ . If $m = -1$ , $1 - n + n^2 = n^2 \Rightarrow n = 1$ . We omit the discussion of $n = \pm 1$ .
Finally, we get $(m, n) = (0, 0), (1, -1), (-1, 1)$ , there are $\boxed{\textbf{(C) 3}}$ solutions.
~ reda_mandymath

## Video Solution by OmegaLearn
https://youtu.be/5a5caco_YTo

## Video Solution
https://youtu.be/Dh1lDI1fHrw
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/Vq7kevsWlHk
~Interstigation
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .