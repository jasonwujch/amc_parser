# 2024 AMC 10B Problem 12

## Problem

A group of $100$ students from different countries meet at a mathematics competition. Each student speaks the same number of languages, and, for every pair of students $A$ and $B$ , student $A$ speaks some language that student $B$ does not speak, and student $B$ speaks some language that student $A$ does not speak. What is the least possible total number of languages spoken by all the students?

$\textbf{(A) } 9 \qquad\textbf{(B) } 10 \qquad\textbf{(C) } 12 \qquad\textbf{(D) } 51 \qquad\textbf{(E) } 100$

## Solution 1 (Pure Logic)
We think of this problem like boxes. First start with 9. We see that we can arrange the groups of people into the 9 boxes. We take 9 people of different languages and arrange them in each of the boxes. This means we have $100 - 9 \times 9 = 19$ people remaining. We then take 18 people of different language (as they can be put in a pair and still qualify) and put them in the boxes. This gives us 1 person left over. Now, this is where MAA wants you to choose 10, but one can quickly see that the last person can be put into any group of three (except a group that includes their language) and still qualify whilst maintaining all the constraints. Therefore our answer is $\boxed{\textbf{(A) } 9}$ .
This solution is a basic introduction/summary of the Pigeonhole Principle
~Pinotation

## Solution 2 (Clever intuition)
There are 100 students at the mathematics convention.
For any pair of students $AB$ we see that $AB \in \{X,Y\}$ with WLOG, $(X, Y)$ being a unique language individual to either $A$ or $B$ .
In other words, either student $A$ or student $B$ received language $X$ or language $Y$ , in which the order they receive their language is unimportant.
Given this the number of languages must divide the number of students evenly in order to achieve unique $X,Y$ pairs that satisfy the conditions stated in the problem.
The question now is "What is the number of languages that divide the number of students?", which is equivalent to asking "How many numbers divide 100?", in which we use the number of factors theorem of the prime factorization of 100, being $2^2 \times 5^2$ , and the number of factors being $(2+1)(2+1) = (3)(3) = 9$ .
Therefore our answer is $\boxed{\textbf{(A) } 9}$ .
~Pinotation

## Solution 3
Let's say we have some number of languages. Then each student will speak some amount of those languages, and no two people can have the same combination of languages or else the conditions will no longer be satisfied. Notice that $\dbinom94=126\geq100$ . So each of the $100$ students can speak some $4$ of the $9$ languages. Thus, $\boxed{9}$ is our answer.
~lprado ~LaTeX edits by Elephant200

## Solution 4 (Rigorous)
Let $n$ be the total number of languages spoken by all the students, and let $k$ be the number of languages that each student speaks. Since all students speak the same number of languages, the condition given in the question can be modified as -
"If $N$ is the $n$ -element subset containing the union of the languages spoken by all students, each of the 100 students speaks a different (unique) $k$ -element subset of $N$ combination of languages."
In more mathematical terms, this means ${n \choose k} \ge 100$ . (Using PHP )
Because we need the least value of $n$ , $k$ must be the closest integer to $\frac{n}{2}$
$\Rightarrow {n \choose \frac{n}{2}} \ge 100$ for $n = 2m$ , ${n \choose \frac{n-1}{2}} \ge 100$ for $n=2m-1$ , $m \in \mathbb{N}$
In the context of this question, it will be fastest to just substitute $\normalsize n$ to each of the option values to find the least value possible as $\boxed{\textbf{(A) } 9}$
For a more rigorous proof, where options are not an option, one can manually count up from $n=1$ as $100$ is a small number.
~laythe_enjoyer211

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/YqKmvSR1Ckk?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=N46YcQPc4ro&t=0s

## Video Solution 3 by TheBeautyofMath
https://youtu.be/dfF39udgqc8?t=274 in Rapid Fire
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .