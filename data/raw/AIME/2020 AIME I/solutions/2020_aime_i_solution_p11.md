# 2020 AIME I Problem 11

## Problem

For integers $a,b,c$ and $d,$ let $f(x)=x^2+ax+b$ and $g(x)=x^2+cx+d.$ Find the number of ordered triples $(a,b,c)$ of integers with absolute values not exceeding $10$ for which there is an integer $d$ such that $g(f(2))=g(f(4))=0.$

## Solution 1 (Strategic Casework)
There can be two different cases for this problem, either $f(2)=f(4)$ or not. If it is, note that by Vieta's formulas $a = -6$ . Then, $b$ can be anything. However, $c$ can also be anything, as we can set the root of $g$ (not equal to $f(2) = f(4)$ ) to any integer, producing a possible integer value of $d$ . Therefore there are $21^2 = 441$ in this case*. If it isn't, then $f(2),f(4)$ are the roots of $g$ . This means by Vieta's, that:
\[f(2)+f(4) = -c \in [-10,10]\] \[20 + 6a + 2b \in [-10,10]\] \[3a + b \in [-15,-5].\]
Solving these inequalities while considering that $a \neq -6$ to prevent $f(2) = f(4)$ , we obtain $69$ possible tuples and adding gives $441+69=\boxed{510}$ . ~awang11

## Solution 2 (Bash)
Define $h(x)=x^2+cx$ . Since $g(f(2))=g(f(4))=0$ , we know $h(f(2))=h(f(4))=-d$ . Plugging in $f(x)$ into $h(x)$ , we get $h(f(x))=x^4+2ax^3+(2b+a^2+c)x^2+(2ab+ac)x+(b^2+bc)$ . Setting $h(f(2))=h(f(4))$ , \[16+16a+8b+4a^2+4ab+b^2+4c+2ac+bc=256+128a+32b+16a^2+8ab+b^2+16c+4ac+bc\] . Simplifying and cancelling terms, \[240+112a+24b+12a^2+4ab+12c+2ac=0\] \[120+56a+12b+6a^2+2ab+6c+ac=0\] \[6a^2+2ab+ac+56a+12b+6c+120=0\] \[6a^2+2ab+ac+20a+36a+12b+6c+120=0\] \[a(6a+2b+c+20)+6(6a+2b+c+20)=0\] \[(a+6)(6a+2b+c+20)=0\]
Therefore, either $a+6=0$ or $6a+2b+c=-20$ . The first case is easy: $a=-6$ and there are $441$ tuples in that case. In the second case, we simply perform casework on even values of $c$ , to get $77$ tuples, subtracting the $8$ tuples in both cases we get $441+77-8=\boxed{510}$ .
-EZmath2006

## Solution 3 (Official MAA)
For a given ordered triple $(a, b, c)$ , the value of $g(f(4)) - g(f(2))$ is uniquely determined, and a value of $d$ can be found to give $g(f(2))$ any prescribed integer value. Hence the required condition can be satisfied provided that $a$ , $b$ , and $c$ are chosen so that \begin{align*} 0 &= g(f(4)) - g(f(2)) = \big(f(4)\big)^{\!2} - \big(f(2)\big)^{\!2} + c\big(f(4) - f(2)\big)\\ &= \big(f(4) - f(2)\big)\big(f(4) + f(2) + c\big)\\ &= (12 + 2a)(20 + 6a + 2b + c). \end{align*} First suppose that $12 + 2a = 0$ , so $a = -6$ . In this case there are $21$ choices for each of $b$ and $c$ with $-10 \le b \le 10$ and $-10 \le c \le 10$ , so this case accounts for $21^2 = 441$ ordered triples.
Next suppose that $a \ne -6$ and $20 + 6a + 2b + c = 0$ , so $c = -6a - 2b - 20$ . Because $-10 \le c \le 10$ , it follows that $-30 \le 6a + 2b \le -10$ , and because $-10\le b \le10$ , it follows that $-8 \le a \le 1$ . Then $-15 - 3a \le b \le -5 - 3a$ . The number of ordered triples for various values of $a$ are presented in the following table.
\[\begin{tabular}{|c|c|c|r|} \hline a & b & c & triples \\ \hline -8 & \{9,10\} & -6a - 2b - 20 & 2 \\ -7 & \{6, 7, 8, 9, 10\} & -6a - 2b - 20 & 5 \\ -6 & \{-10, \ldots, 10\} & \{-10, \ldots, 10\} & 441 \\ -5 & \{0, \ldots, 10\} & -6a - 2b - 20 & 11 \\ -4 & \{-3, \ldots, 7\} & -6a - 2b - 20 & 11 \\ -3 & \{-6, \ldots, 4\} & -6a - 2b - 20 & 11 \\ -2 & \{-9, \ldots, 1\} & -6a - 2b - 20 & 11 \\ -1 & \{-10, \ldots, -2\} & -6a - 2b - 20 & 9 \\ 0 & \{-10, \ldots, -5\} & -6a - 2b - 20 & 6 \\ 1 & \{-10, -9, -8\} & -6a - 2b - 20 & 3 \\ \hline Total & & & 510\\ \hline \end{tabular}\] The total number of ordered triples that satisfy the required condition is $\boxed{510}$ .
### Notes For *
In case anyone is confused by this (as I initially was). In the case where $f(2)=f(4)$ , this does not mean that g has a double root of $f(2)=f(4)=k$ , ONLY that $k$ is one of the roots of g. So basically since $a=-6$ in this case, $f(2)=f(4)=b-8$ , and we have $21$ choices for b and we still can ensure c is an integer with absolute value less than or equal to 10 simply by having another integer root of g that when added to $b-8$ ensures this, and of course an integer multiplied by an integer is an integer so $d$ will still be an integer. In other words, you have can have $b$ and $c$ be any integer with absolute value less than or equal to 10 with $d$ still being an integer. Now refer back to the 1st solution. ~First

## Video Solution
https://www.youtube.com/watch?v=ftqYFzzWKv8&list=PLLCzevlMcsWN9y8YI4KNPZlhdsjPTlRrb&index=8 ~ MathEx
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .