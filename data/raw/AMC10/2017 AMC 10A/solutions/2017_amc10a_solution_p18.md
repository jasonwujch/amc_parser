# 2017 AMC 10A Problem 18

## Problem

Amelia has a coin that lands heads with probability $\frac{1}{3}\,$ , and Blaine has a coin that lands on heads with probability $\frac{2}{5}$ . Amelia and Blaine alternately toss their coins until someone gets a head; the first one to get a head wins. All coin tosses are independent. Amelia goes first. The probability that Amelia wins is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. What is $q-p$ ?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 3\qquad\textbf{(D)}\ 4\qquad\textbf{(E)}\ 5$

## Solution 1
Let $P$ be the probability Amelia wins. Note that $P = \text{chance she wins on her first turn} + \text{chance she gets to her turn again}\cdot P$ , since if she gets to her turn again, she is back where she started with probability of winning $P$ . The chance she wins on her first turn is $\frac{1}{3}$ . The chance she makes it to her turn again is a combination of her failing to win the first turn - $\frac{2}{3}$ and Blaine failing to win - $\frac{3}{5}$ . Multiplying gives us $\frac{2}{5}$ . Thus, \[P = \frac{1}{3} + \frac{2}{5}P\] Therefore, $P = \frac{5}{9}$ , so the answer is $9-5=\boxed{\textbf{(D)}\ 4}$ .

## Solution 2
Let $P$ be the probability Amelia wins. Note that $P = \text{chance she wins on her first turn} + \text{chance she gets to her second turn}\cdot \frac{1}{3} + \text{chance she gets to her third turn}\cdot \frac{1}{3} \cdots$ This can be represented as an infinite geometric series: \[P=\frac{\frac{1}{3}}{1-\frac{2}{3}\cdot \frac{3}{5}} = \frac{\frac{1}{3}}{1-\frac{2}{5}} = \frac{\frac{1}{3}}{\frac{3}{5}} = \frac{1}{3}\cdot \frac{5}{3} = \frac{5}{9}.\] Therefore, $P = \frac{5}{9}$ , so the answer is $9-5 = \boxed{\textbf{(D)}\ 4}.$
Solution by ktong
~minor LaTeX edit by virjoy2001 ~quicky grammar edit by NSAoPS

## Solution 3
We can solve this by using 'casework,' the cases being: Case 1: Amelia wins on her first turn. Case 2 Amelia wins on her second turn. and so on.
The probability of her winning on her first turn is $\dfrac13$ . The probability of all the other cases is determined by the probability that Amelia and Blaine all lose until Amelia's turn on which she is supposed to win. So, the total probability of Amelia winning is: \[\dfrac{1}{3}+\left(\dfrac{2}{3}\cdot\dfrac{3}{5}\right)\cdot\dfrac{1}{3}+\left(\dfrac{2}{3}\cdot\dfrac{3}{5}\right)^2\cdot\dfrac{1}{3}+\cdots.\] Factoring out $\dfrac13$ we get a geometric series: \[\dfrac{1}{3}\left(1+\dfrac{2}{5}+\left(\dfrac{2}{5}\right)^2+\cdots\right) = \dfrac{1}{3}\cdot\dfrac{1}{3/5} = \boxed{\dfrac59}.\]
Extracting the desired result, we get $9-5 = \boxed{\textbf{(D)} \ 4}$ .
-ConfidentKoala4

## Video Solution
https://youtu.be/IRyWOZQMTV8?t=4552
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=umr2Aj9ViOA
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .