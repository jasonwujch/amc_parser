# 2022 AMC 10B Problem 9

## Problem

The sum \[\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\cdots+\frac{2021}{2022!}\] can be expressed as $a-\frac{1}{b!}$ , where $a$ and $b$ are positive integers. What is $a+b$ ?

$\textbf{(A)}\ 2020 \qquad\textbf{(B)}\ 2021 \qquad\textbf{(C)}\ 2022 \qquad\textbf{(D)}\ 2023 \qquad\textbf{(E)}\ 2024$

## Solution 1
For all positive integers $n,$ we have \[\frac{n}{(n+1)!}=\frac{(n+1)-1}{(n+1)!}=\frac{1}{n!}-\frac{1}{(n+1)!}.\] Note that the original sum is a telescoping series: \begin{align*} \frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\cdots+\frac{2021}{2022!} &= \left(\frac{1}{1!}-\frac{1}{2!}\right)+\left(\frac{1}{2!}-\frac{1}{3!}\right)+\left(\frac{1}{3!}-\frac{1}{4!}\right)+\cdots+\left(\frac{1}{2021!}-\frac{1}{2022!}\right) \\ &= \frac{1}{1!}+\left(-\frac{1}{2!}+\frac{1}{2!}-\frac{1}{3!}+\frac{1}{3!}-\frac{1}{4!}+\cdots+\frac{1}{2021!}\right)-\frac{1}{2022!} \\ &= 1-\frac{1}{2022!}. \end{align*} Therefore, the answer is $1+2022=\boxed{\textbf{(D)}\ 2023}.$
~mathboy100 ~MRENTHUSIASM

## Solution 2
We add $\frac{1}{2022!}$ to the original expression \[\left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\cdots+\frac{2021}{2022!}\right)+\frac{1}{2022!}=\left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\dots+\frac{2020}{2021!}\right)+\frac{1}{2021!}.\] This sum clearly telescopes, thus we end up with $\left(\frac{1}{2!}+\frac{2}{3!}\right)+\frac{1}{3!}=\frac{2}{2!}=1$ . Thus the original expression is equal to $1-\frac{1}{2022!}$ , and $1+2022=\boxed{\textbf{(D)}\ 2023}$ .
~not_slay (+ minor LaTeX edit ~TaeKim)

## Solution 3 (Induction)
By looking for a pattern, we see that $\tfrac{1}{2!} = 1 - \tfrac{1}{2!}$ and $\tfrac{1}{2!} + \tfrac{2}{3!} = \tfrac{5}{6} = 1 - \tfrac{1}{3!}$ , so we can conclude by engineer's induction that the sum in the problem is equal to $1 - \tfrac{1}{2022!}$ , for an answer of $\boxed{\textbf{(D)}\ 2023}$ . This can be proven with actual induction as well; we have already established $2$ base cases, so now assume that $\tfrac{1}{2!} + \tfrac{2}{3!} + \cdots \tfrac{n-1}{n!} = 1 - \tfrac{1}{n!}$ for $n = k$ . For $n = k + 1$ we get $\tfrac{1}{2!} + \tfrac{2}{3!} + \cdots \tfrac{n-1}{n!} + \tfrac{n}{(n+1)!} = 1 - \tfrac{1}{n!} + \tfrac{n}{(n+1)!} = 1 - \tfrac{n+1}{(n+1)!} + \tfrac{n}{(n+1)!} = 1 - \tfrac{1}{(n+1)!}$ , completing the proof. ~eibc

## Solution 4
Let $x=\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\dots+\frac{1}{2022!}.$
Note that \begin{align*} \left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\dots+\frac{2021}{2022!}\right)+\left(\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\dots+\frac{1}{2022!}\right)&=\frac{1}{1!}+\frac{2}{2!}+\frac{3}{3!}+\dots+\frac{2022}{2022!}\\ \left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\dots+\frac{2021}{2022!}\right)+x&=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\dots+\frac{1}{2021!}\\ \left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\dots+\frac{2021}{2022!}\right)+x&=x+1-\frac{1}{2022!}\\ \left(\frac{1}{2!}+\frac{2}{3!}+\frac{3}{4!}+\dots+\frac{2021}{2022!}\right)&=1-\frac{1}{2022!}. \end{align*} Therefore, the answer is $1+2022=\boxed{\textbf{(D) }2023}.$
~lopkiloinm

## Solution 5 (Combinatorics)
Let's examine a tuple $\sigma$ containing $2022$ distinct integers. We want to find the probability of the tuple being unsorted.
Suppose that we are looking at the first two items in our tuple. The probability of the first element being greater than the second element is $\frac{1}{2!}$ .
When we are looking at the first three items in our tuple, the probability of the second element being greater than the third element and the first element less than or equal to the second element is $\frac{2}{3!}$ .
Similarly, when we are looking at the first four items in our tuple, the probability of the third element being greater than the fourth element, the second element less than or equal to the third element, and the first element less than or equal to the second element is $\frac{3}{4!}$ .
More specifically, \begin{align*} \bigcup_{n=2}^{2022}\{\sigma \mid \sigma_{n-1}>\sigma_n\}&=\{\sigma \mid \sigma_{1}<\sigma_{2}<\ldots<\sigma_{2022}\}^\complement\\ \bigsqcup_{n=2}^{2022}\{\sigma \mid \sigma_{n-1}>\sigma_n, \sigma_{n-2}\leq\sigma_{n-1},\ldots, \sigma_{1}\leq\sigma_{2}\}&=\{\sigma \mid \sigma_{1}<\sigma_{2}<\ldots<\sigma_{2022}\}^\complement\\ \frac{\#\left(\bigsqcup_{n=2}^{2022}\{\sigma \mid \sigma_{n-1}>\sigma_n, \sigma_{n-2}\leq\sigma_{n-1},\ldots, \sigma_{1}\leq\sigma_{2}\}\right)}{\#\mathcal{S}}&=\frac{\#\left(\{\sigma \mid \sigma_{1}<\sigma_{2}<\ldots<\sigma_{2022}\}^\complement\right)}{\#\mathcal{S}}\\ \frac{\sum_{n=2}^{2022}\frac{2022!}{n!}(n-1)}{2022!}&=\frac{2022!-1}{2022!}\\ \sum_{n=2}^{2022}\frac{n-1}{n!}&=1-\frac{1}{2022!} \end{align*}
This series ends up being the probability of having the list unsorted and that is of course $1-\frac{1}{2022!}$
~lopkiloinm

## Solution 6 (Desperate)
Because the fractions get smaller, it is obvious that the answer is less than $1$ , so we can safely assume that $a=1$ (this can also be guessed by intuition using similar math problems). Looking at the answer choices, $2018<b<2024$ . Because the last term consists of $2022!$ (and the year was $2022$ ) we can guess that $b=2022$ . Adding them yields $1+2022=\boxed{\textbf{(D) }2023}$ .
~iluvme and andy_lee

## Solution 7 (Partial Fractions)
Knowing that the answer will be in the form $a-\frac{1}{b!}$ , we can guess that the sum telescopes. Using partial fractions, we can hope to rewrite $\frac{n-1}{n!}$ as $\frac{A}{(n-1)!}-\frac{B}{n}$ . Setting these equal and multiplying by $n!$ , we get $n-1=An-B(n-1)!$ . Since $An$ is the only term with $n$ with degree $1$ , we can conclude that $A=1$ . This means that $B=\frac{1}{(n-1)!}$ . Substituting, we find that $\frac{n-1}{n!}=\frac{1}{(n-1)!}-\frac{1}{n!}$ . This sum clearly telescopes and we obtain $1-\frac{1}{2022!}$ . This means that our desired answer is $1+2022=\boxed{\textbf{(D) }2023}.$
~kn07

## Solution 8 (Taylor Series)
We calculate the Taylor series error to be $\frac{1}{2023!}$ and this error happens $2023$ times so it is $\frac{2023}{2023!}$ which is $\frac{1}{2022!}$

## Solution 9 (Really Really Fast and Cheesy)
Note that $\frac{1}{2!} = 1-\frac{1}{2!}$ , so we guess $a=1$ and $b=2022$ . We get $1+2022=\boxed{\textbf{(D) }2023}.$

## Video Solution
by Ismail.maths https://www.youtube.com/watch?v=lt34QscjTf4&list=PLmpPPbOoDfgj5BlPtEAGcB7BR_UA5FgFj

## Video Solution by Interstigation
https://youtu.be/_KNR0JV5rdI?t=1102
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .