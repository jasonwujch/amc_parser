# 2000 AIME I Problem 5

## Problem

Each of two boxes contains both black and white marbles, and the total number of marbles in the two boxes is $25.$ One marble is taken out of each box randomly. The probability that both marbles are black is $27/50,$ and the probability that both marbles are white is $m/n,$ where $m$ and $n$ are relatively prime positive integers. What is $m + n$ ?

## Solution 1
If we work with the problem for a little bit, we quickly see that there is no direct combinatorics way to calculate $m/n$ . The Principle of Inclusion-Exclusion still requires us to find the individual probability of each box.
Let $a, b$ represent the number of marbles in each box, and without loss of generality let $a>b$ . Then, $a + b = 25$ , and since the $ab$ may be reduced to form $50$ on the denominator of $\frac{27}{50}$ , $50|ab$ . It follows that $5|a,b$ , so there are 2 pairs of $a$ and $b: (20,5),(15,10)$ .
- Case 1 : Then the product of the number of black marbles in each box is $54$ , so the only combination that works is $18$ black in first box, and $3$ black in second. Then, $P(\text{both white}) = \frac{2}{20} \cdot \frac{2}{5} = \frac{1}{25},$ so $m + n = 26$ .
- Case 2 : The only combination that works is 9 black in both. Thus, $P(\text{both white}) = \frac{1}{10}\cdot \frac{6}{15} = \frac{1}{25}$ . $m + n = 26$ .
Thus, $m + n = \boxed{026}$ .

## Solution 2
Let $w_1, w_2, b_1,$ and $b_2$ represent the white and black marbles in boxes 1 and 2.
Since there are $25$ marbles in the box:
$w_1 + w_2 + b_1 + b_2 = 25$
From the fact that there is a $\frac{27}{50}$ chance of drawing one black marble from each box:
$\frac{b_1 \cdot b_2}{(b_1 + w_1)(b_2 + w_2)} = \frac{27}{50} = \frac{54}{100} = \frac{81}{150}$
Thinking of the numerator and denominator separately, if $\frac{27}{50}$ was not a reduced fraction when calculating out the probability, then $b_1 \cdot b_2 = 27$ . Since $b_1 < 25$ , this forces the variables to be $3$ and $9$ in some permutation. Without loss of generality, let $b_1 = 3$ and $b_2 = 9$ .
The denominator becomes: $(3 + w_1)(9 + w_2) = 50$
Since there have been $12$ black marbles used, there must be $13$ white marbles. Substituting that in:
$(3 + w_1)(9 + (13 - w_1)) = 50$
$(3 + w_1)(22 - w_1) = 50$
Since the factors of $50$ that are greater than $3$ are $5, 10, 25,$ and $50$ , the quantity $3 + w_1$ must equal one of those. However, since $w_1 < 13$ , testing $2$ and $7$ for $w_1$ does not give a correct product. Thus, $\frac{27}{50}$ must be a reduced form of the actual fraction.
First assume that the fraction was reduced from $\frac{54}{100}$ , yielding the equations $b_1\cdot b_2 = 54$ and $(b_1 + w_1)(b_2 + w_2) = 100$ . Factoring $b_1 \cdot b_2 = 54$ and saying WLOG that $b_1 < b_2 < 25$ gives $(b_1, b_2) = (3, 18)$ or $(6, 9)$ . Trying the first pair and setting the denominator equal to 100 gives: $(3 + w_1)(18 + w_2) = 100$
Since $w_1 + w_2 = 4$ , the pairs $(w_1, w_2) = (1, 3), (2,2),$ and $(3,1)$ can be tried, since each box must contain at least one white marble. Plugging in $w_1 = w_2 = 2$ gives the true equation $(3 + 2)(18 + 2) =100$ , so the number of marbles are $(w_1, w_2, b_1, b_2) = (2, 2, 3, 18)$
Thus, the chance of drawing 2 white marbles is $\frac{w_1 \cdot w_2 }{(w_1+ b_1)(w_2 + b_2)} = \frac{4}{100} = \frac{1}{25}$ in lowest terms, and the answer to the problem is $1 + 25 = \boxed{026}.$
For completeness, the fraction $\frac{81}{150}$ may be tested. $150$ is the highest necessary denominator that needs to be tested, since the maximum the denominator $(w_1+ b_1)(w_2 + b_2)$ can be when the sum of all integer variables is $25$ is when the variables are $6, 6, 6,$ and $7$ , in some permutation, which gives $154$ . If $b_1 \cdot b_2 = 81$ , this forces $b_1 = b_2 = 9$ , since all variables must be integers under $25$ . The denominator becomes $(9 + w_1)(9 + w_2) = 150$ , and since there are now $25 - 18 = 7$ white marbles total, the denominator becomes $(9 + w_1)(16 - w_1) = 150$ . Testing $w_1 = 1$ gives a solution, and thus $w_2 = 6$ . The complete solution for this case is $(w_1, w_2, b_1, b_2) = (1, 6, 9, 9)$ . Although the distribution and colors of the marbles is different from the last case, the probability of drawing two white marbles is $\frac{6 \cdot 1}{ 150}$ , which still simplifies to $\frac {1}{25}$ .

## Solution 3
We know that $\frac{27}{50} = \frac{b_1}{t_1} \cdot \frac{b_2}{t_2}$ , where $b_1$ and $b_2$ are the number of black marbles in the first and the second box respectively, and $t_1$ and $t_2$ is the total number of marbles in the first and the second boxes respectively. So, $t_1 + t_2 = 25$ . Then, we can realize that $\frac{27}{50} = \frac{9}{10} \cdot \frac{3}{5} = \frac{9}{10} \cdot \frac{9}{15}$ , which means that having 9 black marbles out of 10 total in the first box and 9 marbles out of 15 total the second box is valid. Then there is 1 white marble in the first box and 6 in the second box. So, the probability of drawing two white marbles becomes $\frac{1}{10} \cdot \frac{6}{15} = \frac{1}{25}$ . The answer is $1 + 25 = \boxed{026}$
Note: Note that if $t_1=5, t_2=20$ , and $b_1=3, b_2=18$ , it also works since $\frac{b_1}{t_1} \cdot \frac{b_2}{t_2} = \frac{3}{5} \cdot \frac{18}{20} = \frac{27}{50}$ , so the probability of drawing a white marble is $\frac{2}{5} \cdot \frac{2}{20} = \frac{1}{25}$ . Therefore, our answer is $1+25=\boxed{026}.$
~Yiyj1
These problems are copyrighted © by the Mathematical Association of America.