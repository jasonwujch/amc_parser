# 2020 AMC 10B Problem 11

## Problem

Ms. Carr asks her students to read any $5$ of the $10$ books on a reading list. Harold randomly selects $5$ books from this list, and Betty does the same. What is the probability that there are exactly $2$ books that they both select?

$\textbf{(A)}\ \frac{1}{8} \qquad\textbf{(B)}\ \frac{5}{36} \qquad\textbf{(C)}\ \frac{14}{45} \qquad\textbf{(D)}\ \frac{25}{63} \qquad\textbf{(E)}\ \frac{1}{2}$

## Solution 1
We don't care about which books Harold selects. We just care that Betty picks $2$ books from Harold's list and $3$ that aren't on Harold's list.
The total amount of combinations of books that Betty can select is $\binom{10}{5}=252$ .
There are $\binom{5}{2}=10$ ways for Betty to choose $2$ of the books that are on Harold's list.
From the remaining $5$ books that aren't on Harold's list, there are $\binom{5}{3}=10$ ways to choose $3$ of them.
$\frac{10\cdot10}{252}=\boxed{\textbf{(D) }\frac{25}{63}}$ ~quacker88

## Solution 2
We can analyze this as two containers with $10$ balls each, with the two people grabbing $5$ balls each. First, we need to find the probability of two of the balls being the same among five: $\frac{1}{3} \cdot \frac{4}{9} \cdot \frac{3}{8} \cdot \frac{5}{7} \cdot \frac{2}{4}$ . After that we must multiply this probability by ${5 \choose 2}$ , for choosing the 2 balls that are the same chosen among 5 balls. The answer will be $\frac{5}{126}*10 = \frac{25}{63}$ . $\boxed{\textbf{(D) }\frac{25}{63}}$

## Solution 3
Firstly, we know that the denominator will be $\dbinom{10}{5} \cdot \dbinom{10}{5}$ . To calculate the numerator, or successful events, we first find the number of ways both Betty and Harold can choose the same 2 books. Then we find the number of ways for Betty to choose 3 different other books and the number of ways for Harold to choose 3 different other books. That is $\dfrac{\binom{10}{2} \cdot \binom{8}{3} \cdot \binom{5}{3}}{\tbinom{10}{5} \cdot \tbinom{10}{5}} = \dfrac{45 \cdot 56 \cdot 10}{252 \cdot 252}$ . From here, do not multiply, instead cancel common factors, then simplify. In fact, to make this expression even more manageable, leave the combinations in simplest factored form (for example, $\tbinom{10}{2}$ is $5 \cdot 3 \cdot 3$ ). After doing so, we get, $\boxed{\textbf{(D) } \dfrac{25}{63}}$ .
~BakedPotato66

## Solution 4
Say that there is a set $S$ ${a,b,c,...,j}$ which represent the 10 books. We know that intersection of the subsets that Bob and Alice choose has 2 elements. Thus there are $\dbinom{10}{2}$ ways for that to happen. Out of the 8 remaining in the set $S$ , Bob and Alice both need to choose 3 different elements = $\dbinom{8}{3} * \dbinom{5}{3}$ . Thus the number of ways this works is $\dbinom{10}{2} * \dbinom{8}{3} * \dbinom{5}{3}$ . The denominator for the fraction is just $\dbinom{10}{5} * \dbinom{10}{5}$ . Simplifying, you get $\boxed{\frac{25}{63}}$ .
~YBSuburbanTea

## Solution 5 (similar to 3 but way faster & cheese)
Following the same method as solution 3, you end up getting $\dfrac{\binom{10}{2} \cdot \binom{8}{3} \cdot \binom{5}{3}}{\tbinom{10}{5} \cdot \tbinom{10}{5}} = \dfrac{45 \cdot 56 \cdot 10}{252 \cdot 252}$ . However you notice that there are two $5$ s in the numerator which can't cancel out. The only answer with two $5$ in the numerator is $\boxed{\textbf{(D) }\frac{25}{63}}$ .
~ neeyakkid23

## Video Solution (HOW TO CRITICALLY THINK!!!)
https://youtu.be/wwKJBG5zCAE
~Education, the Study of Everything

## Video Solution
https://youtu.be/wopflrvUN2c?t=118 -Sohil Rathi ~Juicer100

## Video Solution
https://youtu.be/t6yjfKXpwDs by BeautyofMath
https://youtu.be/RbKdVmZRxkk
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .