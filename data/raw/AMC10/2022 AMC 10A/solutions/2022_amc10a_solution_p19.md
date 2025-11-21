# 2022 AMC 10A Problem 19

## Problem

Define $L_n$ as the least common multiple of all the integers from $1$ to $n$ inclusive. There is a unique integer $h$ such that \[\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{17}=\frac{h}{L_{17}}\] What is the remainder when $h$ is divided by $17$ ?

$\textbf{(A) } 1 \qquad \textbf{(B) } 3 \qquad \textbf{(C) } 5 \qquad \textbf{(D) } 7 \qquad \textbf{(E) } 9$

## Solution 1
Notice that $L_{17}$ contains the highest power of every prime below $17$ since higher primes cannot divide $L_{17}$ . Thus, $L_{17}=16\cdot 9 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17$ .
When writing the sum under a common fraction, we multiply the denominators by $L_{17}$ divided by each denominator. However, since $L_{17}$ is a multiple of $17$ , all terms will be a multiple of $17$ until we divide out $17$ , and the only term that will do this is $\frac{1}{17}$ . Thus, the remainder of all other terms when divided by $17$ will be $0$ , so the problem is essentially asking us what the remainder of $\frac{L_{17}}{17} = L_{16}$ divided by $17$ is. This is equivalent to finding the remainder of $16 \cdot 9 \cdot 5 \cdot 7 \cdot 11 \cdot 13$ divided by $17$ .
We use modular arithmetic to simplify our answer:
This is congruent to $-1 \cdot 9 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \pmod{17}$ .
Evaluating, we get: \begin{align*} (-1) \cdot 9 \cdot 35 \cdot 11 \cdot 13 &\equiv (-1) \cdot 9 \cdot 1 \cdot 11 \cdot 13 \pmod{17} \\ &\equiv 9 \cdot 11 \cdot (-13) \pmod{17} \\ &\equiv 9 \cdot 11 \cdot 4\pmod{17} \\ &\equiv 2 \cdot 11 \pmod{17} \\ &\equiv 5\pmod{17} \end{align*} Therefore the remainder is $\boxed{\textbf{(C) } 5}$ .
~KingRavi ~mathboy282 ~Scarletsyc ~wangzrpi

## Solution 2
As in solution 1, we express the LHS as a sum under one common denominator. We note that \[\frac{1}{1} + \frac{1}{2} + \dots + \frac{1}{17} = \frac{\frac{17!}{1}}{17!} + \frac{\frac{17!}{2}}{17!} + \frac{\frac{17!}{3}}{17!} + \dots + \frac{\frac{17!}{17}}{17!}\]
Now, we have $h = L_{17}\left(\frac{\frac{17!}{1} + \frac{17!}{2} + \frac{17!}{3} + \dots + \frac{17!}{17}}{17!}\right)$ . We'd like to find $h \pmod{17},$ so we can evaluate our expression $\pmod{17}.$ Since $\frac{\frac{17!}{1}}{17!}, \frac{\frac{17!}{2}}{17!}, \dots, \frac{\frac{17!}{16}}{17!}$ don't have a factor of $17$ in their denominators, and since $L_{17}$ is a multiple of $17,$ multiplying each of those terms and adding them will get a multiple of $17.$ $\pmod{17}$ , that result is $0.$ Thus, we only need to consider $L_{17}\cdot \frac{\frac{17!}{17}}{17!} = \frac{L_{17}}{17} \pmod{17}.$ Proceed with solution $1$ to get $\boxed{\textbf{(C) }5}$ .
~sirswagger21

## Solution 3
Using Wolstenholmes' Theorem, we can rewrite $1 + \frac{1}{2} \dots + \frac{1}{16}$ as $\frac{17^2 n}{(17 - 1)!} = \frac{17^2 n}{16!}$ (for some $n \in \mathbb{Z}$ ). Adding the $\frac{1}{17}$ to $\frac{17^2 n}{16!}$ , we get $\frac{17^3 n + 16!}{17!}$ .
Now we have $\frac{17^3 n + 16!}{17!} = \frac{h}{L_{17}}$ and we want $h \pmod{17}$ . We find that $\frac{L_{17}(17^3 n + 16!)}{17!} = \frac{L_{16}(17^3 n + 16!)}{16!} = h$ . Taking $\pmod{17}$ and multiplying, we get $L_{16}(17^3 n + 16!) \equiv 16! \cdot h \pmod{17}$ .
Applying Wilson's Theorem on $16!$ and reducing, we simplify the congruence to $L_{16}(0 - 1) \equiv -L_{16} \equiv -h \pmod{17}$ . Now we proceed with Solution 1 and find that $L_{16} \equiv 5 \pmod{17}$ , so our answer is $\boxed{\textbf{(C) }5}$ .
~kn07

## Video Solution (⚡️3 min⚡️)
https://youtu.be/3g39lB6XLAE
~Education, the Study of Everything

## Video Solution By ThePuzzlr
https://youtu.be/TGcGamPXdNc
~ MathIsChess

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=Wz19lcfF_m8
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .