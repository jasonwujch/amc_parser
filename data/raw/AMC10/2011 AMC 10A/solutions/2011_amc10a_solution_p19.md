# 2011 AMC 10A Problem 19

## Problem

In 1991 the population of a town was a perfect square. Ten years later, after an increase of 150 people, the population was 9 more than a perfect square. Now, in 2011, with an increase of another 150 people, the population is once again a perfect square. Which of the following is closest to the percent growth of the town's population during this twenty-year period?

$\textbf{(A)}\ 42 \qquad\textbf{(B)}\ 47 \qquad\textbf{(C)}\ 52\qquad\textbf{(D)}\ 57\qquad\textbf{(E)}\ 62$

## Solution
Let the population of the town in $1991$ be $p^2$ . Let the population in $2001$ be $q^2+9$ . It follows that $p^2+150=q^2+9$ . Rearrange this equation to get $141=q^2-p^2=(q-p)(q+p)$ . Since $q$ and $p$ are both positive integers with $q>p$ , $(q-p)$ and $(q+p)$ also must be, and thus, they are both factors of $141$ . We have two choices for pairs of factors of $141$ : $1$ and $141$ , and $3$ and $47$ . Assuming the former pair, since $(q-p)$ must be less than $(q+p)$ , $q-p=1$ and $q+p=141$ . Solve to get $p=70, q=71$ . Since $p^2+300$ is not a perfect square, this is not the correct pair. Solve for the other pair to get $p=22, q=25$ . This time, $p^2+300=22^2+300=784=28^2$ . This is the correct pair. Now, we find the percent increase from $22^2=484$ to $28^2=784$ . Since the increase is $300$ , the percent increase is $\frac{300}{484}\times100\%\approx\boxed{\textbf{(E)}\ 62\%}$ .

## Solution 2
Proceed through the difference of squares for $p$ and $q$ : $141=q^2-p^2=(q-p)(q+p)$
However, instead of testing both pairs of factors we take a more certain approach. Here $r^2$ is the population of the town in 2011. $r^2-p^2=300$ $(r-p)(r+p)=300$ Test through pairs of $r$ and $p$ that makes sure $p=22$ or $p=70$ . Then go through the same routine as demonstrated above to finish this problem.
Note that this approach might take more testing if one is not familiar with finding factors.

## Solution 3 (Answer choices)
Since all the answer choices are around $50\%$ , we know the town's starting population must be around $600$ . We list perfect squares from $400$ to $1000$ . \[441, 484, 529,576,625,676,729,784,841,900,961\] We see that $484$ and $784$ differ by $300$ , and we can confirm that $484$ is the correct starting number by noting that $484+150=634=25^2+9$ . Thus, the answer is $484/784\approx \boxed{\textbf{(E) } 62\%}$ .

## Solution 4
Let the population of the town in 1991 be $a^2$ and the population in 2011 be $b^2$ . We know that $a^2+150+150=b^2 \implies a^2-b^2=-300 \implies b^2-a^2=300 \implies (b-a)(b+a)=300$ . Note that $b-a$ must be even. Testing, we see that $a=22$ and $b=28$ works, as $484+150-9=625=25^2$ , so $\frac{784-484}{484} \approx \boxed{\textbf{(E) } 62\%}$ .
~MrThinker

## Video Solution
https://youtu.be/arsFJaUhsbs
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .