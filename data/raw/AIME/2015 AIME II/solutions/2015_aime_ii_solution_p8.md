# 2015 AIME II Problem 8

## Problem

Let $a$ and $b$ be positive integers satisfying $\frac{ab+1}{a+b} < \frac{3}{2}$ . The maximum possible value of $\frac{a^3b^3+1}{a^3+b^3}$ is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
Let us call the quantity $\frac{a^3b^3+1}{a^3+b^3}$ as $N$ for convenience. Knowing that $a$ and $b$ are positive integers, we can legitimately rearrange the given inequality so that $a$ is by itself, which makes it easier to determine the pairs of $(a, b)$ that work. Doing so, we have \[\frac{ab+1}{a+b} < \frac{3}{2}\] \[\implies 2ab + 2 < 3a + 3b \implies 2ab - 3a < 3b - 2\] \[\implies a < \frac{3b - 2}{2b - 3}.\] Now, observe that if $b = 1$ we have that $N = \frac{a^3 + 1}{a^3 + 1} = 1$ , regardless of the value of $a$ . If $a = 1$ , we have the same result: that $N = \frac{b^3 + 1}{b^3 + 1} = 1$ , regardless of the value of $b$ . Hence, we want to find pairs of positive integers $(a, b)$ existing such that neither $a$ nor $b$ is equal to $1$ , and that the conditions given in the problem are satisfied in order to check that the maximum value for $N$ is not $1$ .
To avoid the possibility that $a = 1$ , we want to find values of $b$ such that $\frac{3b - 2}{2b - 3} > 2$ . If we do this, we will have that $a < \frac{3b - 2}{2b - 3} = k$ , where $k$ is greater than $2$ , and this allows us to choose values of $a$ greater than $1$ . Again, since $b$ is a positive integer, and we want $b > 1$ , we can legitimately multiply both sides of $\frac{3b - 2}{2b - 3} > 2$ by $2b - 3$ to get $3b - 2 > 4b - 6 \implies b < 4$ . For $b = 3$ , we have that $a < \frac{7}{3}$ , so the only possibility for $a$ greater than $1$ is obviously $2$ . Plugging these values into $N$ , we have that $N = \frac{8(27) + 1}{8 + 27} = \frac{217}{35} = \frac{31}{5}$ . For $b = 2$ , we have that $a < \frac{4}{1} = 4$ . Plugging $a = 3$ and $b = 2$ in for $N$ yields the same result of $\frac{31}{5}$ , but plugging $a = 2$ and $b = 2$ into $N$ yields that $N = \frac{8(8) + 1}{8 + 8} = \frac{65}{16}$ . Clearly, $\frac{31}{5}$ is the largest value we can have for $N$ , so our answer is $31 + 5 = \boxed{036}$ .
(Technically, we would have to find that b > 1 before dividing both sides of the inequality by 2b - 3, but otherwise this solution is correct)

## Solution 2 (nifty solution)
\[\frac{ab + 1}{a + b} < \frac{3}{2} \rightarrow 2ab + 2 < 3a + 3b \rightarrow 4ab - 6a - 6b + 4 < 0 \rightarrow (2a - 3)(2b - 3) < 5.\]
\[2a - 3, 2b - 3 \in \{x \neq 2k, k \in Z \} \rightarrow\] $(2a-3)$ and $(2b-3)$ each cannot be even or else $a$ and $b$ will not be integers \[(2a - 3)(2b - 3) = 1, 3 \rightarrow (2a - 3, 2b - 3) = (1, 1), (1, 3), (3, 1).\] \[(a, b) = (2, 2), (2, 3), (3, 2).\] \[\frac{a^3 b^3 + 1}{a^3 + b^3} = \frac{65}{16}, \frac{31}{5}.\] \[\frac{31}{5} \rightarrow \boxed{036}.\]
( $a=1 \rightarrow b=1, 2, 3... \rightarrow \frac{b^3+1}{b^3+1}=1$ ; $1<31/5$ ).

## Solution 3
Notice that for $\frac{a^3b^3+1}{a^3+b^3}$ to be maximized, $\frac{ab+1}{a+b}$ has to be maximized. We simplify as above to $2ab + 2 < 3a + 3b$ , which is $(a-\frac{3}{2})(b-\frac{3}{2}) < \frac{5}{4}$ . To maximize, $a$ has to be as close to $b$ as possible, making $a$ close to $\frac{3+\sqrt{5}}{2}$ . Because $a$ and $b$ are positive integers, $a = 3$ , and checking back gives $b = 2$ as the maximum or the other way around, which the answer is thus $\frac{216+1}{27+8} = \frac{217}{35} = \frac{31}{5} \rightarrow \boxed{036}$ .

## Solution 4
Guess and check a few values of $a$ and $b$ you will find two things. One, that the highest values of $a$ and $b$ are the closest to $\frac{3}{2}$ . Two, that the pair $(2,3)$ is the highest possible value of $a, b$ . So plugging in $a=2$ and $b=3$ we get $((2*3)^3)+1/(8+27)$ = $\frac{217}{35}$ = $\frac{31}{5}$ , and $31+5 = 36$ . Solution by Helloitsaaryan

## Solution 5
WLOG, assume $a \geq b$ . We solve for $a$ from the original equation to get $a < \frac{3b - 2}{2b - 3}$ . Since $b \leq a$ , we can solve $b < \frac{3b - 2}{2b - 3}$ . Solving, we get $\frac{3 - \sqrt{5}}{2} < b < \frac{3 + \sqrt{5}}{2}$ . Approximating values, we get $1 \leq b < 3$ . Thus, $b = 1, 2$ . Now, plugging back $a < \frac{3b - 2}{2b - 3}$ , we see that $b = 1$ doesn't work. Thus, we plug in $b = 2$ to get $2 \leq a < 4$ . Thus, $a = 2, 3$ . Clearly, we can plug in $(a, b) = (2, 2), (3, 2)$ and see that $(3, 2)$ gives you the maximum of $\frac{31}{5}$ . Thus, the answer is $\boxed{036}$ .
~ilikemath247365

## Solution 6
Firstly, if we assume that $a=1$ , we see that $\frac{a^{3}b^{3}+1}{a^{3}+b^{3}} = \frac{b^{3}+1}{1+b^{3}} = 1$ , which is not a fraction. Therefore, we know that neither $a$ nor $b$ can equal 1.
Starting with $\frac{ab+1}{a+b}<\frac{3}{2}$ , cross multiply and move the variables to the right to obtain $2ab-3a-3b<-2$ . After multiplying both sides by 2, Simon's favorite factoring trick (SFFT) is applicable, giving us $(2a-3)(2b-3)<5$ . Now, we assume $a=2$ . Then we see that $b$ can equal 2 or 3. If $a=3$ , the only possible $b$ value is 2, and there are no other possible values for $b$ if $a>3$ . So the possible ordered pairs for $(a,b)$ are $(2,2), (2,3)$ , and $(3,2)$ . It is easily noticeable that $(2,3)$ and $(3,2)$ both produce $\frac{a^{3}b^{3}+1}{a^{3}+b^{3}}=\frac{31}{5}$ , which is the maximum value. We then add $31+5=\fbox{036}$
~justeau9

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=653s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .