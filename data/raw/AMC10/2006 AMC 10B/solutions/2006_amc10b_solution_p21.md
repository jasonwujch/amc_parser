# 2006 AMC 10B Problem 21

## Problem

For a particular peculiar pair of dice, the probabilities of rolling $1$ , $2$ , $3$ , $4$ , $5$ , and $6$ , on each die are in the ratio $1:2:3:4:5:6$ . What is the probability of rolling a total of $7$ on the two dice?

$\mathrm{(A) \ } \frac{4}{63}\qquad \mathrm{(B) \ } \frac{1}{8}\qquad \mathrm{(C) \ } \frac{8}{63}\qquad \mathrm{(D) \ } \frac{1}{6}\qquad \mathrm{(E) \ } \frac{2}{7}$

## Solution
Let $x$ be the probability of rolling a $1$ . The probabilities of rolling a $2$ , $3$ , $4$ , $5$ , and $6$ are $2x$ , $3x$ , $4x$ , $5x$ , and $6x$ , respectively.
The sum of the probabilities of rolling each number must equal 1, so
$x+2x+3x+4x+5x+6x=1$
$21x=1$
$x=\frac{1}{21}$
So the probabilities of rolling a $1$ , $2$ , $3$ , $4$ , $5$ , and $6$ are respectively $\frac{1}{21}, \frac{2}{21}, \frac{3}{21}, \frac{4}{21}, \frac{5}{21}$ , and $\frac{6}{21}$ .
The possible combinations of two rolls that total $7$ are: $(1,6) ; (2,5) ; (3,4) ; (4,3) ; (5,2) ; (6,1)$
The probability P of rolling a total of $7$ on the two dice is equal to the sum of the probabilities of rolling each combination.
$P = \frac{1}{21}\cdot\frac{6}{21}+\frac{2}{21}\cdot\frac{5}{21}+\frac{3}{21}\cdot\frac{4}{21}+\frac{4}{21}\cdot\frac{3}{21}+\frac{5}{21}\cdot\frac{2}{21}+\frac{6}{21}\cdot\frac{1}{21}=\frac{8}{63} \Rightarrow C$

## Solution 2 (Not as bashy)
(Alcumus solution) On each die the probability of rolling $k$ , for $1\leq k\leq 6$ , is $\frac{k}{1+2+3+4+5+6}=\frac{k}{21}.$ There are six ways of rolling a total of 7 on the two dice, represented by the ordered pairs $(1,6)$ , $(2,5)$ , $(3,4)$ , $(4,3)$ , $(5,2)$ , and $(6,1)$ . Thus the probability of rolling a total of 7 is $\frac{1\cdot6+2\cdot5+3\cdot4+4\cdot3+5\cdot2+6\cdot1}{21^2}=\frac{56}{21^2}=\boxed{\frac{8}{63}}.$

## Solution 3 (intuitive)
There are $6$ ways to get the sum of $7$ of the dice. Let's do case by case.
Case $1$ (Rolling a $1$ or a $6$ ): $\frac {1}{21} \cdot \frac {6}{21} = \frac {6}{441}$ .
Case $2$ (Rolling a $2$ or a $5$ ): $\frac {2}{21} \cdot \frac {5}{21} = \frac {10}{441}$ .
Case $3$ (Rolling a $3$ or a $4$ ): $\frac {3}{21} \cdot \frac {4}{21} = \frac {12}{441}$ .
The rest of the cases are symmetric to these cases above. We have $2 \cdot \frac {28}{441}$ . We have $\frac {56}{441} = \frac {8}{63}$ . Therefore, our answer is $\boxed {\frac {8}{63}}$
~Arcticturn
~Minor Edits by L314159265358979323846264

## Solution 4 (cheap)
Notice that the ways to obtain a 7 are (6,1), (5,2), (4,3). Then, because the cases are symmetrical with (3,4), (2,5) and (6,1), look through the answer choices. You see a 4/63 and an 8/63, so obviously MAA wants you to not count the other symmetrical cases, thus giving the answer (C).
~mathboy282

## Video Solution by OmegaLearn
https://youtu.be/IRyWOZQMTV8?t=3057
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=SBwVVADk1Nk ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .