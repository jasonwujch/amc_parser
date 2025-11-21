# 2022 AIME II Problem 10

## Problem

Find the remainder when \[\binom{\binom{3}{2}}{2} + \binom{\binom{4}{2}}{2} + \dots + \binom{\binom{40}{2}}{2}\] is divided by $1000$ .

## Video Solution by OmegaLearn
https://youtu.be/pGkLAX381_s?t=1035
~ pi_is_3.14

## Video solution
https://www.youtube.com/watch?v=4O1xiUYjnwE

## Solution 1 (Telescoping)
We first write the expression as a summation. \begin{align*} \sum_{i=3}^{40} \binom{\binom{i}{2}}{2} & = \sum_{i=3}^{40} \binom{\frac{i \left( i - 1 \right)}{2}}{2} \\ & = \sum_{i=3}^{40} \frac{\frac{i \left( i - 1 \right)}{2} \left( \frac{i \left( i - 1 \right)}{2}- 1 \right)}{2} \\ & = \frac{1}{8} \sum_{i=3}^{40} i \left( i - 1 \right) \left( i \left( i - 1 \right) - 2 \right) \\ & = \frac{1}{8} \sum_{i=3}^{40} i(i - 1)(i^2-i-2) \\ & = \frac{1}{8} \sum_{i=3}^{40} i(i-1)(i+1)(i-2) \\ & = \frac{1}{8}\sum_{i=3}^{40} (i-2)(i-1)i(i+1) \\ & = \frac{1}{40}\sum_{i=3}^{40}[(i-2)(i-1)i(i+1)(i+2)-(i-3)(i-2)(i-1)i(i+1)]* \\ & = \frac{38\cdot39\cdot40\cdot41\cdot42-0}{40}\\ & = 38 \cdot 39 \cdot 41 \cdot 42 \\ & = \left( 40 - 2 \right) \left( 40 - 1 \right) \left( 40 + 1 \right) \left( 40 + 2 \right) \\ & = \left( 40^2 - 2^2 \right) \left( 40^2 - 1^2 \right) \\ & = \left( 40^2 - 4 \right) \left( 40^2 - 1 \right) \\ & = 40^4 - 40^2 \cdot 5 + 4 \\ & \equiv \boxed{004}\pmod{1000}\ \end{align*} $*(i-2)(i-1)i(i+1)=\frac{1}{5}[(i-2)(i-1)i(i+1)(i+2)-(i-3)(i-2)(i-1)i(i+1)]$ is how we force the expression to telescope. ~qyang

## Solution 2 (Hockey Stick)
Doing simple algebra calculation will give the following equation: \begin{align*} \binom{\binom{n}{2}}{2} &= \frac{\frac{n(n-1)}{2} \cdot (\frac{n(n-1)}{2}-1)}{2}\\ &= \frac{n(n-1)(n^2-n-2)}{8}\\ &= \frac{(n+1)n(n-1)(n-2)}{8}\\ &= \frac{(n+1)!}{8\cdot (n-3)!} = 3 \cdot \frac{(n+1)!}{4!\cdot (n-3)!}\\ &= 3 \binom{n+1}{4} \end{align*}
Next, by using Hockey-Stick Identity , we have: \[3 \cdot \sum_{i=3}^{40} \binom{i+1}{4} = 3 \binom{42}{5} = 42 \cdot 41 \cdot 39 \cdot 38\] \[=(40^2-2^2)(40^2-1^2) \equiv \boxed{004} ~(\text{mod}~ 1000)\]

## Solution 3
Since $40$ seems like a completely arbitrary number, we can use Engineer's Induction by listing out the first few sums. These are, in the order of how many terms there are starting from $1$ term: $3$ , $18$ , $63$ , $168$ , $378$ , and $756$ . Notice that these are just $3 \cdot \dbinom50$ , $3 \cdot \dbinom61$ , $3 \cdot \dbinom72$ , $3 \cdot \dbinom83$ , $3 \cdot \dbinom94$ , $3 \cdot \dbinom{10}5$ . It's clear that this pattern continues up to $38$ terms, noticing that the "indexing" starts with $\dbinom32$ instead of $\dbinom12$ . Thus, the value of the sum is $3 \cdot \dbinom{42}{37}=2552004 \equiv \boxed{\textbf{004}} \pmod{1000}$ .
~A1001

## Solution 4
As in solution 1, obtain $\sum_{i=3}^{40} \binom{\binom{i}{2}}{2} = \frac{1}{8} \sum_{i=3}^{40} i^4-2i^3-i^2+2i.$ Write this as \[\frac{1}{8}\left(\sum_{i=3}^{40} i^4 - 2\sum_{i=3}^{40}i^3 - \sum_{i=3}^{40}i^2 + 2\sum_{i=3}^{40}i\right).\]
We can safely write this expression as $\frac{1}{8}\left(\sum_{i=1}^{40} i^4 - 2\sum_{i=1}^{40}i^3 - \sum_{i=1}^{40}i^2 + 2\sum_{i=1}^{40}i\right)$ , since plugging $i=1$ and $i=2$ into $i^4-2i^3-i^2+2i$ both equal $0,$ meaning they won't contribute to the sum.
Use the sum of powers formulae. We obtain \[\frac{1}{8}\left(\frac{i(i+1)(2i+1)(3i^2+3i-1)}{30} - \frac{i^2(i+1)^2}{2} - \frac{i(i+1)(2i+1)}{6} + i(i+1)\right) \text{ where i = 40.}\]
We can factor the following expression as $\frac{1}{8}\left(\frac{i(i+1)(2i+1)(3i^2+3i-6)}{30} - \frac{i(i+1)}{2} (i(i+1)-2)\right),$ and simplifying, we have \[\sum_{i=3}^{40} \binom{\binom{i}{2}}{2} = \frac{i(i+1)(2i+1)(i^2+i-2)}{80}-\frac{i^2(i+1)^2-2i(i+1)}{16} \text{ where i = 40.}\]
Substituting $i=40$ and simplifying gets $41\cdot 81\cdot 819 - 5\cdot 41\cdot 819,$ so we would like to find $819\cdot 76\cdot 41 \pmod{1000}.$ To do this, get $819\cdot 76\equiv 244 \pmod{1000}.$ Next, $244\cdot 41 \equiv \boxed{004} \pmod{1000}.$
-sirswagger21

## Solution 5
To solve this problem, we need to use the following result:
\[ \sum_{i=n}^m \binom{i}{k} = \binom{m+1}{k+1} - \binom{n}{k+1} . \]
Now, we use this result to solve this problem.
We have \begin{align*} \sum_{i=3}^{40} \binom{\binom{i}{2}}{2} & = \sum_{i=3}^{40} \binom{\frac{i \left( i - 1 \right)}{2}}{2} \\ & = \sum_{i=3}^{40} \frac{\frac{i \left( i - 1 \right)}{2} \left( \frac{i \left( i - 1 \right)}{2}- 1 \right)}{2} \\ & = \frac{1}{8} \sum_{i=3}^{40} i \left( i - 1 \right) \left( i \left( i - 1 \right) - 2 \right) \\ & = \frac{1}{8} \sum_{i=3}^{40} i \left( i - 1 \right) \left( \left( i - 2 \right) \left( i - 3 \right) + 4 \left( i - 2 \right) \right) \\ & = 3 \left( \sum_{i=3}^{40} \binom{i}{4} + \sum_{i=3}^{40} \binom{i}{3} \right) \\ & = 3 \left( \binom{41}{5} - \binom{3}{5} + \binom{41}{4} - \binom{3}{4} \right) \\ & = 3 \left( \binom{41}{5} + \binom{41}{4} \right) \\ & = 3 \cdot \frac{41 \cdot 40 \cdot 39 \cdot 38}{5!} \left( 37 + 5 \right) \\ & = 3 \cdot 41 \cdot 13 \cdot 38 \cdot 42 \\ & = 38 \cdot 39 \cdot 41 \cdot 42 \\ & = \left( 40 - 2 \right) \left( 40 - 1 \right) \left( 40 + 1 \right) \left( 40 + 2 \right) \\ & = \left( 40^2 - 2^2 \right) \left( 40^2 - 1^2 \right) \\ & = \left( 40^2 - 4 \right) \left( 40^2 - 1 \right) \\ & = 40^4 - 40^2 \cdot 5 + 4 . \end{align*}
Therefore, modulo 1000, $\sum_{i=3}^{40} \binom{\binom{i}{2}}{2} \equiv \boxed{\textbf{(004) }}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 6 (Combinatorial Method)
We examine the expression $\binom{\binom{n}{2}}{2}$ . Imagine we have a set $S$ of $n$ integers. Then the expression can be translated to the number of pairs of $2$ element subsets of $S$ .
To count this, note that each pair of $2$ element subsets can either share $1$ value or $0$ values. In the former case, pick three integers $a$ , $b$ , and $c$ . There are $\binom{n}{3}$ ways to select these integers and $3$ ways to pick which one of the three is the shared integer. This gives $3\cdot \binom{n}{3}$ .
In the latter case, we pick $4$ integers $a$ , $b$ , $c$ , and $d$ in a total of $\binom{n}{4}$ ways. There are $\frac{1}{2}\binom{4}{2} = 3$ ways to split this up into $2$ sets of $2$ integers — $\binom{4}{2}$ ways to pick which $2$ integers are together and dividing by $2$ to prevent overcounting. This gives $3\cdot \binom{n}{4}$ .
So we have \[\binom{\binom{n}{2}}{2} = 3\cdot \binom{n}{3} + 3\cdot \binom{n}{4}\] We use the Hockey Stick Identity to evaluate this sum: \begin{align*} \sum_{n=3}^{40} \binom{\binom{n}{2}}{2} &= \sum_{n=3}^{40} \left( 3 \binom{n}{3} + 3 \binom{n}{4} \right) \\ &= 3 \left( \sum_{n=3}^{40} \binom{n}{3} \right) + 3\left( \sum_{n=4}^{40} \binom{n}{4} \right) \\ &= 3\left( \binom{41}{4} + \binom{41}{5} \right) \end{align*} Evaluating while accounting for mod $1000$ gives the final answer to be $\boxed{004}$ .
~ GoatPotato
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .