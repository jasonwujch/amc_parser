# 2021 AMC 10B Problem 18

## Problem

A fair $6$ -sided die is repeatedly rolled until an odd number appears. What is the probability that every even number appears at least once before the first occurrence of an odd number?

$\textbf{(A)} ~\frac{1}{120} \qquad\textbf{(B)} ~\frac{1}{32} \qquad\textbf{(C)} ~\frac{1}{20} \qquad\textbf{(D)} ~\frac{3}{20} \qquad\textbf{(E)} ~\frac{1}{6}$

## Solution 1
Since 3 out of 6 of the numbers are even, there is a $\frac36$ chance that the first number we choose is even.
Since the number rolled first is irrelevant, we don't have to consider it. Therefore there are 2 even numbers out of the 5 choices left. There is a $\frac{2}{5}$ chance that the next number that is distinct from the first is even.
There is a $\frac{1}{4}$ chance that the next number distinct from the first two is even. (There is only one even integer left. ) With all the even integers taken, the next integer rolled must be odd.
$\frac{3}{6} \cdot \frac{2}{5} \cdot \frac{1}{4} = \frac{1}{20}$ , so the answer is $\boxed{\textbf{(C) }\frac{1}{20}}.$
~Tucker

## Solution 2
Every set of three numbers chosen from $\{1,2,3,4,5,6\}$ has an equal chance of being the first 3 distinct numbers rolled.
Therefore, the probability that the first 3 distinct numbers are $\{2,4,6\}$ is $\frac{1}{{6 \choose 3}}=\boxed{(C)~\frac{1}{20}}$
~kingofpineapplz

## Solution 3
Note that the problem is basically asking us to find the probability that in some permutation of $1,2,3,4,5,6$ that we get the three even numbers in the first three spots.
There are $6!$ ways to order the $6$ numbers and $3!(3!)$ ways to order the evens in the first three spots and the odds in the next three spots.
Therefore the probability is $\frac{3!(3!)}{6!} = \frac{1}{20} = \boxed{\textbf{(C)}}$ .
~abhinavg0627

## Solution 4
Let $P_n$ denote the probability that the first odd number appears on roll $n$ and all our conditions are met. We now proceed with complementary counting.
For $n \le 3$ , it's impossible to have all $3$ evens appear before an odd. Note that for $n \ge 4,$ \[P_n = \frac {1}{2^{n}} - \frac {1}{2^{n}} \left(\frac{\binom{3}{2}(2^{n-1}-2)+\binom{3}{1}}{3^{n-1}}\right)\] since there's a $\frac {1}{2^{n}}$ chance that the first odd appears on roll $n$ (disregarding the other conditions) and the other term is subtracting the probability that less than $3$ of the evens show up before the first odd roll. Simplifying, we arrive at \[P_n= \frac {1}{2^{n}} - \left(\frac {3(2^{n-1})-3}{2^{n} \cdot 3^{n-1}}\right) = \frac {1}{2^{n}} - \frac {1}{2 \cdot 3^{n-2}} + \frac{1}{2^{n} \cdot 3^{n-2}}.\]
Summing for all $n$ , we get our answer of \[\left (\frac {1}{2^{4}} + \frac {1}{2^{5}} + ... \right) - \left (\frac {1}{2 \cdot 3^{2}} + \frac {1}{2 \cdot 3^{3}} + ... \right) + \left (\frac {1}{2^{4} \cdot 3^{2}} + \frac {1}{2^{5} \cdot 3^{3}} + ... \right) = \left (\frac {1}{8} \right) - \left(\frac {\frac {1}{18}}{ \frac{2}{3}} \right) + \left(\frac {\frac {1}{144}}{\frac {5}{6}} \right) = \frac {1}{8} - \frac {1}{12} + \frac{1}{120} = \boxed{\textbf{(C) }\frac{1}{20}.}\]
~ike.chen

## Solution 5 (States)
Let $E_n$ be that probability that the condition in the problem is satisfied given that we need $n$ more distinct even numbers. Then, \[E_1=\frac{1}{6}+\frac{1}{3}\cdot E_1+\frac{1}{2}\cdot 0,\] since there is a $\frac{1}{3}$ probability that we will roll an even number we already have rolled and will be in the same position again. Solving, we find that $E_1=\frac{1}{4}$ .
We can apply the same concept for $E_2$ and $E_3$ . We find that \[E_2=\frac{1}{3}\cdot E_1+\frac{1}{6}\cdot E_2+\frac{1}{2}\cdot 0,\] and so $E_2=\frac{1}{10}$ . Also, \[E_3=\frac{1}{2}\cdot E_2+\frac{1}{2}\cdot 0,\] so $E_3=\frac{1}{20}$ . Since the problem is asking for $E_3$ , our answer is $\boxed{\textbf{(C) }\frac{1}{20}}$ . -BorealBear

## Solution 6 (Infinite Geometric Sequence Method)
Let's say that our even integers are found in the first $n$ numbers where n must be greater than or equal to $3$ . Then, we can form an argument based on this. There are $3^n$ total ways to assign even numbers being $($ 2 $,$ 4 $,$ 6 $)$ to each space. Furthermore, we must subtract the cases where we have only a single even integer present in the total $n$ spaces and the case where there are only $2$ distinct even integers present. There is $1$ way we can have a single even integer in the entire $n$ spaces, therefore giving us just $1$ option for each of the three integers, so we have $3$ total cases for this. Moreover, the amount of cases with just $2$ distinct even integers is $2^n$ but subtract the cases where all of the n spaces is either a single integer giving us $2^n-2$ , but we multiply by $3C2$ because of the ways to choose $2$ distinct even integers that are used in the sequence of $n$ . Finally, we have $\sum_{n=3}^{\infty} \frac{(3^n-3-3(2^n-2))}{6^n}$ note: we must divide all of this by $6^n$ for probability. Additionally, over the entire summation, we multiply by $1/2$ because of the $1/2$ probability of selecting an odd at the end of all the evens. Therefore, if you compute this using infinite geometric sequences, you get $1/20$ . $\boxed{\textbf{(C) }\frac{1}{20}.}$
~Jske25

## Solution 7 (Complementary + PIE)
We know that the sequence with odd ending will eventually add up to probability 1.
For every even number appears at least once, let's look at the complementary, i.e. without some even numbers ${2, 4, 6}$ . $A = \{ \text{without} 2\}, B = \{ \text{without} 4\}, C = \{ \text{without} 6\}$ .
$1 - A\cup B\cup C = 1 - (A + B + C - A\cap B - B\cap C - A\cap C + A\cap B\cap C)$
Let $f(x) = \frac{1}{2} + x\frac{1}{2} + x^2\frac{1}{2} + \ldots = \frac{1}{2} \frac{1}{1-x}$
2 even numbers left $|A|=|B|=|C|: f(\frac{2}{6}) = \frac{1}{2} \frac{1}{1-\frac{1}{3}} = \frac{3}{4}$ ,
1 even number left $|A\cap B| = |B\cap C| = |A\cap C|: f(\frac{1}{6}) = \frac{1}{2} \frac{1}{1-\frac{1}{6}} = \frac{3}{5}$
0 even number left $|A\cap B\cap C|: f(0) = \frac{1}{2}$
ans $= 1 - A\cup B\cup C = 1- (\frac{3}{4} * 3 - \frac{3}{5} * 3 + \frac{1}{2}) = \frac{1}{20}$
~aliciawu

## Solution 8
We don't care what happens after we pick the first three distinct even numbers. This can be done is $3! = 6$ ways. Totally there are $6 \cdot 5 \cdot 4$ ways to pick three distinct numbers. So the answer is $\frac{6}{6\cdot5\cdot4} = \frac{1}{20}$ .
~coolmath_2018

## Solution 9
We can use complementary counting for this problem by eliminating the chances that we get 0,1, and 2 even numbers before the odd number. To get 0 even numbers before the odd number has a probability of 3/6 or 1/2. To get 1 even number before the odd number has a probability of 3/6*3/5 which is 3/10 (0.3). To get the probability of 2 even numbers before the odd number it is 3/6*2/5*3/4 which is 3/20 (0.15). Now we eliminate all of these cases to get the answer to the question by doing 1-(0.5+0.3+0.15) which is equal to 0.05 or 1/20 so the answer is C 1/20
~HYPEBEAST1

## Solution 10 (Infinite Geometric Sequence 2)
We can first try to find an expression for, given $n$ dice rolls, the probability that it contains only all the even digits. Firstly, we know that it must be $\frac{1}{2^{n}}\cdot$ (the probability that it contains only even digits). We can do complementary counting to find an expression for the probability that it contains all digits. For all the cases where the sequence does not contain all digits, we know that it must be a sequence of two digits, each one being one or the other. This works out to $2^{n}$ , but it has to be multiplied by 3 (for the 3 possible choices of 2 digits) and have 3 subtracted from it (because we will double count the cases where it's only one digit repeated). Then, we can put it over the total number of cases, $3^{n}$ .
This gives $1 - \frac{3\cdot2^{n}-3}{3^{n}} = 1 - \frac{2^{n}-1}{3^{n-1}} = \frac{3^{n-1}-2^{n}+1}{3^{n-1}}$ We can then multiply this by the probability that it contains only even digits, giving $\frac{3^{n-1}-2^{n}+1}{3^{n-1}\cdot2^{n}}$ . We still need to make sure we don't double count, as we don't explicitly state that the next digit will be odd. So, the final answer will be the result of $\sum_{n=3}^{\infty}\frac{3^{n-1}-2^{n}+1}{3^{n-1}\cdot2^{n+1}}$
We can continue to simplify the expression to $\sum_{n=3}^{\infty} \frac{3^n\cdot\frac{1}{3}-2^n+1}{3^n\cdot 2^n\cdot \frac{2}{3}} = \frac{3}{2} \cdot\sum_{n=3}^{\infty} \frac{\frac{1}{3}\cdot 3^n-2^n+1}{6^n}$ .
This becomes the sum $\frac{3}{2} \cdot \sum_{n=3}^{\infty} \frac{1}{3} \cdot \frac{1}{2^n} - \frac{1}{3^n} + \frac{1}{6^n}$ , which is $\frac{3}{2} \cdot (\frac{1}{12} - \frac{1}{18} + \frac{1}{180}) = \frac{3}{2}\cdot\frac{1}{30} = \boxed{\textbf{(C) }\frac{1}{20}}$
~HI2937

## Solution 11 (Quick & Easy to Understand Infinite Geometric Sequence)
We need to have every even number from $1$ to $6$ at least once before we get an odd number. We find that the probability of the first number being even is $\dfrac{3}{6} = \dfrac{1}{2}$ . Regardless of what the first number is, the probability of the second number being distinct and even is $\dfrac{2}{5}$ , because now only $2$ even numbers are left. Next, the probability of the third number being even and distinct is $\dfrac{1}{4}$ . The final number must be odd, and it can be any of the $3$ odd numbers, thus $\dfrac{1}{2}$ . Multiplying these all out yields $\dfrac{1}{2} \cdot \dfrac{2}{5} \cdot \dfrac{1}{4} \cdot \dfrac{1}{2} = \dfrac{1}{40}$ . Now, this is the probability that all even numbers appear exactly once before the odd number, and we haven't accounted for the fact that an even number could appear more than once. Since any even number can appear more than once, we multiply $\dfrac{1}{40}$ by $\dfrac{1}{2}$ . We could keep multiplying by $\dfrac{1}{2}$ infinitely before we get an odd number, thus we use the infinite geometric sequence sum formula (we could have $3$ even numbers, all the way to $\infty$ even numbers before we get our first odd number, so that's why we're summing the probabilities). Our first term, $a_1$ is $\dfrac{1}{40}$ , and the common ratio is $\dfrac{1}{2}$ . Plugging it into the formula $\dfrac{a_1}{1-r}$ , we get $\dfrac{\dfrac{1}{40}}{1-\dfrac{1}{2}} = \dfrac{\dfrac{1}{40}}{\dfrac{1}{2}} = \dfrac{1}{40} \cdot 2 = \dfrac{1}{20}$ , and we are done. Therefore, our answer is $\boxed{\textbf{(C) }\frac{1}{20}.}$
~ cyberhacker

## Video Solution (🚀Under 1 min 🚀)
https://youtu.be/8amWKsbcjXs
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/IX-Y38KPxqs
~pi_is_3.14

## Video Solution by hurdler (complementary probability)
https://www.youtube.com/watch?v=k2Jy4ni9tK8

## Video Solution by TheBeautyofMath (da goat)
https://youtu.be/FV9AnyERgJQ?t=480
~IceMatrix

## Video Solution by Interstigation (Simple Bash With PIE)
(which stands for Principle of Inclusion and Exclusion) https://youtu.be/2SGmSYZ5bqU
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .