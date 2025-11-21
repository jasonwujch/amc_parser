# 2010 AIME I Problem 10

## Problem

Let $N$ be the number of ways to write $2010$ in the form $2010 = a_3 \cdot 10^3 + a_2 \cdot 10^2 + a_1 \cdot 10 + a_0$ , where the $a_i$ 's are integers, and $0 \le a_i \le 99$ . An example of such a representation is $1\cdot 10^3 + 3\cdot 10^2 + 67\cdot 10^1 + 40\cdot 10^0$ . Find $N$ .

## Solution 1
If we choose $a_3$ and $a_1$ such that $(10^3)(a_3) + (10)(a_1) \leq 2010$ there is a unique choice of $a_2$ and $a_0$ that makes the equality hold. So $N$ is just the number of combinations of $a_3$ and $a_1$ we can pick. If $a_3 = 0$ or $a_3 = 1$ we can let $a_1$ be anything from $0$ to $99$ . If $a_3 = 2$ then $a_1 = 0$ or $a_1 = 1$ . Thus $N = 100 + 100 + 2 = \fbox{202}$ .

## Solution 2
Note that $a_2\cdot 10^2 + a_0$ is the base $100$ representation of any number from $0$ to $9999$ , and similarly $10(a_3\cdot 10^2 + a_1)$ is ten times the base $100$ representation of any number from $0$ to $9999$ . Thus, the number of solutions is just the number of solutions to $2010 = 10a+b$ where $0\le a, b\le 9999$ , which is equal to $\boxed{202}$ as $a$ can range from $0$ to $201$ .

## Solution 3
Note that $a_0 \equiv 2010\ (\textrm{mod}\ 10)$ and $a_1 \equiv 2010 - a_0\ (\textrm{mod}\ 100)$ . It's easy to see that exactly 10 values in $0 \leq a_0 \leq 99$ that satisfy our first congruence. Similarly, there are 10 possible values of $a_1$ for each choice of $a_0$ . Thus, there are $10 \times 10 = 100$ possible choices for $a_0$ and $a_1$ . We next note that if $a_0$ and $a_1$ are chosen, then a valid value of $a_3$ determines $a_2$ , so we dive into some simple casework:
- If $2010 - 10a_1 - a_0 \geq 2000$ , there are 3 valid choices for $a_3$ . There are only 2 possible cases where $2010 - 10a_1 - a_0 \geq 2000$ , namely $(a_1, a_0) = (1,0), (10,0)$ . Thus, there are $3 \times 2 = 6$ possible representations in this case.
- If $2010 - 10a_1 - a_0 < 1000$ , $a_3$ can only equal 0. However, this case cannot occur, as $10a_1+a_0\leq 990+99 = 1089$ . Thus, $2010-10a_1-a_0 \geq 921$ . However, $2010-10a_1-a_0 = 1000a_3 + 100a_2 \equiv 0\ (\textrm{mod}\ 100)$ . Thus, we have $2010-10a_1-a_0 \geq 1000$ always.
- If $1000 \leq 2010 - 10a_1 - a_0 < 2000$ , then there are 2 valid choices for $a_3$ . Since there are 100 possible choices for $a_0$ and $a_1$ , and we have already checked the other cases, it follows that $100 - 2 - 0 = 98$ choices of $a_0$ and $a_1$ fall under this case. Thus, there are $2 \times 98 = 196$ possible representations in this case.
Our answer is thus $6 + 0 + 196 = \boxed{202}$ .

## Solution 4: Casework and Brute Force
We immediately see that $a_3$ can only be $0$ , $1$ or $2$ . We also note that the maximum possible value for $10a_1 + a_0$ is $990 + 99 = 1089$ . We then split into cases:
Case 1: $a_3 = 0$ . We try to find possible values of $a_2$ . We plug in $a_3 = 0$ and $10a_1 + a_0 = 1089$ to our initial equation, which gives us $2010 = 0 + 100a_2 + 1089$ . Thus $a_2 \geq 10$ . We also see that $a_2 \leq 20$ . We now take these values of $a_2$ and find the number of pairs $(a_1, a_0)$ that work. If $a_2 = 10$ , $10a_1 + a_0 = 1010$ . We see that there are $8$ possible pairs in this case. Using the same logic, there are $10$ ways for $a_2 = 11, 12 \ldots 19$ . For $a_2 = 20$ , we get the equation $10a_1 + a_0 = 10$ , for 2 ways. Thus, for $a_3 = 0$ , there are $8 + 10 \cdot 9 + 2 = 100$ ways.
Case 2: $a_3 = 1$ . This case is almost identical to the one above, except $0 \leq a_2 \leq 10$ . We also get 100 ways.
Case 3: $a_3 = 2$ . If $a_3 = 2$ , our initial equation becomes $100a_2 + 10a_1 + a_0 = 10$ . It is obvious that $a_2 = 0$ , and we are left with $10a_1 + a_0 = 10$ . We saw above that there are $2$ ways.
Totaling everything, we get that there are $100 + 100 + 2 = \boxed{202}$ ways.

## Solution 5: Generating Functions
We will represent the problem using generating functions. Consider the generating function \[f(x) = (1+x^{1000}+x^{2000}+\cdots+x^{99000})(1+x^{100}+x^{200}+\cdots+x^{9900})(1+x^{10}+x^{20}+\cdots+x^{990})(1+x+x^2+\cdots+x^{99})\] where the first factor represents $a_3$ , the second factor $a_2$ , and so forth. We want to find the coefficient of $x^{2010}$ in the expansion of $f(x)$ . Now rewriting each factor using the geometric series yields \[f(x) = \frac{\cancel{x^{100}-1}}{x-1} \cdot \frac{\cancel{x^{1000}-1}}{x^{10}-1} \cdot \frac{x^{10000}-1}{\cancel{x^{100}-1}} \cdot \frac{x^{100000}-1}{\cancel{x^{1000}-1}}=\frac{x^{10000}-1}{x-1} \cdot \frac{x^{100000}-1}{x^{10}-1} = (1+x+x^2+\cdots + x^{9999})(1+x^{10}+x^{20}+\cdots+x^{99990})\] The coefficient of $x^{2010}$ in this is simply $\boxed{202}$ , as we can choose any of the first 202 terms from the second factor and pair it with exactly one term in the first factor.
~rzlng

## Solution 5
First note that $a_3$ has to be a single-digit number( $0$ , $1$ , or $2$ to be exact), and that $a_1$ has to be a two-digit multiple of ten. Then, $a_3$ , $a_2$ , $a_1$ and $a_0$ can be represented as follows: \begin{align*} a_3 = a \\ a_2 = 10b+c \\ a_1= 10d+e \\ a_0 = 10f \end{align*} , where $a$ , $b$ , $c$ , $d$ , $e$ , and $f$ are all(not necessarily nonzero) digits. Now, we can write our given equation as follows: \begin{align*} 2010 = 1000(a+b) + 100(c+d) + 10(e+f) \\ 201 = 100(a+b) + 10(c+d) + (e+f) \\ 201 = (100a + 10c + e) + (100b + d + f) \end{align*} Now, each integer between $0$ and $201$ inclusive can be represented in exactly one way as $100a + 10c + e$ , and this corresponds with one unique $100b + d + f$ , so it remains to count the number of integers between $0$ and $201$ inclusive. This is easily counted to be $\boxed{202}$ .

## Solution 6
Just note that this corresponds to $0 \leq 10^3 \cdot a_3 + 10^2 \cdot a_2 + 10^1 \cdot a_1 \leq 2010$ , because we can use $a_0$ to fill in the remaining gap. Then, dividing by $10$ , we have $0 \leq \overline{a_3 a_2 a_1} \leq 201$ , of which there are $\boxed{202}$ solutions.

## Video Solution
https://youtu.be/DNC2zd5rReY
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .