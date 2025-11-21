# 2023 AMC 10A Problem 12

## Problem

How many three-digit positive integers $N$ satisfy the following properties?

- The number $N$ is divisible by $7$ .

- The number formed by reversing the digits of $N$ is divisible by $5$ .

$\textbf{(A) } 13 \qquad \textbf{(B) } 14 \qquad \textbf{(C) } 15 \qquad \textbf{(D) } 16 \qquad \textbf{(E) } 17$

## Solution 1
Multiples of $5$ will always end in $0$ or $5$ , and since the numbers have to be a three-digit numbers, it cannot start with 0 (otherwise it would be a two-digit number), narrowing our choices to 3-digit numbers starting with $5$ . Since the numbers must be divisible by 7, all possibilities have to be in the range from $7 \cdot 72$ to $7 \cdot 85$ inclusive(504 to 595).
(Add 1 to include 72)
$85 - 72 + 1 = 14$ . $\boxed{\textbf{(B) } 14}$ .
You can also take 497 away from each of the numbers(removing the hundreds digit and adding three to each of the numbers), resulting in the numbers {7, 14, 21..., 84, 91, 98}. Dividing each of them by 7, you get the numbers {1, 2, 3..., 12, 13, 14}. Therefore, the answer is $\boxed{\textbf{(B) 14}}$
~walmartbrian ~Shontai ~andliu766 ~andyluo ~ESAOPS ~NXC

## Solution 2 (solution 1 but more thorough)
Let $N=\overline{cab}=100c+10a+b.$ We know that $\overline{bac}$ is divisible by $5$ , so $c$ is either $0$ or $5$ . However, since $c$ is the first digit of the three-digit number $N$ , it can not be $0$ , so therefore, $c=5$ . Thus, $N=\overline{5ab}=500+10a+b.$ There are no further restrictions on digits $a$ and $b$ aside from $N$ being divisible by $7$ .
The smallest possible $N$ is $504$ . The next smallest $N$ is $511$ , then $518$ , and so on, all the way up to $595$ . Thus, our set of possible $N$ is $\{504,511,518,\dots,595\}$ . Dividing by $7$ for each of the terms will not affect the cardinality of this set, so we do so and get $\{72,73,74,\dots,85\}$ . We subtract $71$ from each of the terms, again leaving the cardinality unchanged. We end up with $\{1,2,3,\cdots,14\}$ , which has a cardinality of $14$ . Therefore, our answer is $\boxed{\textbf{(B) } 14.}$
~ Technodoggo

## Solution 3 (modular arithmetic)
We first proceed as in the above solution, up to $N=500+10a+b$ . We then use modular arithmetic:
\begin{align*} 0&\equiv N \:(\text{mod }7)\\ &\equiv500+10a+b\:(\text{mod }7)\\ &\equiv3+3a+b\:(\text{mod }7)\\ 3a+b&\equiv-3\:(\text{mod }7)\\ &\equiv4\:(\text{mod }7)\\ \end{align*}
We know that $0\le a,b<10$ . We then look at each possible value of $a$ :
If $a=0$ , then $b$ must be $4$ .
If $a=1$ , then $b$ must be $1$ or $8$ .
If $a=2$ , then $b$ must be $5$ .
If $a=3$ , then $b$ must be $2$ or $9$ .
If $a=4$ , then $b$ must be $6$ .
If $a=5$ , then $b$ must be $3$ .
If $a=6$ , then $b$ must be $0$ or $7$ .
If $a=7$ , then $b$ must be $4$ .
If $a=8$ , then $b$ must be $1$ or $8$ .
If $a=9$ , then $b$ must be $5$ .
Each of these cases are unique, so there are a total of $1+2+1+2+1+1+2+1+2+1=\boxed{\textbf{(B) } 14.}$
~ Technodoggo

## Solution 4
The key point is that when reversed, the number must start with a $0$ or a $5$ based on the second restriction. But numbers can't start with a $0$ .
So the problem is simply counting the number of multiples of $7$ in the $500$ s.
$7 \times 72 = 504$ , so the first multiple is $7 \times 72$ .
$7 \times 85 = 595$ , so the last multiple is $7 \times 85$ .
Now, we just have to count $7\times 72, 7\times 73, 7\times 74,\cdots, 7\times 85$ .
We have a set that numbers $85-71=\boxed{\textbf{(B) 14}}$
~Dilip ~boppitybop ~ESAOPS ( $\LaTeX$ )

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=xKgx8T-n-Y1ELLZF&t=2669 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=t4QMuoYyk2u5n64a&t=3140
~Math-X

## Video Solution ⚡️ 2 min solution ⚡️
https://youtu.be/YdaQIdxyBSg
~Education, the Study of Everything

## Video Solution
https://youtu.be/UYHCNlRDZBo
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution
https://www.youtube.com/watch?v=Mg6JUanYNJY
### Note
According to the official answer key, choice (B) is correct. However, some have argued that it is ambiguous whether the number $560$ should be included in the count, since its reversal, $065$ , has a leading zero. It is assumed that $065$ denotes the two-digit number $65$ , which is divisible by $5$ , but it is said that N is a 3-digit Number. ~A_MatheMagician ~ESAOPS ~sdpandit ~Ipimath
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .