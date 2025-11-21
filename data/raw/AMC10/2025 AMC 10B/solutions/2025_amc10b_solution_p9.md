# 2025 AMC 10B Problem 9

## Problem

How many ordered triples of integers $(x, y, z)$ satisfy the following system of inequalities? \begin{align*} -x-y-z\le -2\\ -x+y+z\le 2\\ x-y+z\le 2\\ x+y-z\le 2 \end{align*} $\textbf{(A)}\ 4 \qquad \textbf{(B)}\ 8 \qquad \textbf{(C)}\ 11 \qquad \textbf{(D)}\ 15 \qquad \textbf{(E)}\ 17 \qquad$

## Solution 1
We have: \[\begin{cases} x+y+z \ge 2, \\ -x+y+z \le 2, \\ x-y+z \le 2, \\ x+y-z \le 2. \end{cases}\] Subtract the second inequality from the first: \[(x+y+z)-(-x+y+z) \ge 2-2 \quad\Rightarrow\quad 2x \ge 0 \Rightarrow x\ge 0.\] By symmetry in $x,y,z,$ we also obtain \[y\ge 0,\qquad z\ge 0.\] WLOG & by symmetry, let \[0 \le x \le y \le z.\] up to permutation. From the second inequality of we have $y+z \le 2+x.$ Using $x\le y$ , we get \[y+z \le 2+y \quad\Rightarrow\quad z \le 2.\] Hence, $0 \le x \le y \le z \le 2.$ Divide into casework on $x:$ Case 1: $x=0$ Then the first two inequalities become \[y+z \ge 2,\qquad y+z \le 2 \Rightarrow y+z=2\] And because we have $0\le y\le z\le 2, (y,z)=(0,2), (1,1).$
Case 2: $x=1$ \[1+y+z \ge 2 \Rightarrow y+z\ge 1,\qquad -1+y+z \le 2 \Rightarrow y+z \le 3.\] $1\le y\le z\le 2$ , so $(y,z)=(1,1)\ \text{or}\ (1,2).$
Case 3: $x=2$ \[2+y+z \ge 2 \qquad -2+y+z \le 2 \Rightarrow y+z \le 4.\] $2\le y\le z\le 2$ so the only combination $(y,z)=(2,2).$
Thus up to permutation we have $(0,0,2),\ (0,1,1),\ (1,1,1),\ (1,1,2),\ (2,2,2)$
Now count distinct ordered triples for each set of three numbers under symmetry: $3+3+3+1+1=\boxed{11}.$
~mathboy282

## Solution 2 (complementary counting)
From the beginning of Solution 1, we know that \[0 \le x, y, z \le 2\] Since each variable has to be an integer, the number of permutations of $(x, y, z)$ is \[3 \cdot 3 \cdot 3 = 27\] Simplifying the first equation, we get \[x+y+z \ge 2\] , which is false only if $x+y+z$ is $0$ or $1$ . There is $1$ permutation for $x, y, z$ all being $0$ and $3$ permutations for each of the variables being $1$ while the rest are $0$ .
The only values for $-x+y+z$ that don't satisfy the second equation are $3$ and $4$ .
Case 1: $y$ and $z$ are both $2$
$x$ can be either $0$ or $1$ , which yields two cases. Since the last two equations are symmetric to the second one, there are a total of $2 \cdot 3=6$ permutations.
Case 2: One of either $y$ or $z$ is $1$ , and the other is $2$
In this case, $-x+y+z$ can only reach $3$ when $x$ is $0$ . Since the last three equations are all symmetric as stated in the first case, there are a total of (since $y$ and $z$ can be $1$ and $2$ and vice versa) $2 \cdot 3=6$ permutations.
$27-1-3-6-6=\boxed{11}$ solutions.
~rionoh2

## Video Solution 1 (Fast and Easy)
https://www.youtube.com/watch?v=TEKcHZjUcQ4
~ Pi Academy

## Video Solution 2 by OmegaLearn.org
https://youtu.be/kIl_dkRN-Tc

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .