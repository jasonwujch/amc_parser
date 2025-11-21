# 2017 AIME II Problem 2

## Problem

The teams $T_1$ , $T_2$ , $T_3$ , and $T_4$ are in the playoffs. In the semifinal matches, $T_1$ plays $T_4$ , and $T_2$ plays $T_3$ . The winners of those two matches will play each other in the final match to determine the champion. When $T_i$ plays $T_j$ , the probability that $T_i$ wins is $\frac{i}{i+j}$ , and the outcomes of all the matches are independent. The probability that $T_4$ will be the champion is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
There are two scenarios in which $T_4$ wins. The first scenario is where $T_4$ beats $T_1$ , $T_3$ beats $T_2$ , and $T_4$ beats $T_3$ , and the second scenario is where $T_4$ beats $T_1$ , $T_2$ beats $T_3$ , and $T_4$ beats $T_2$ . Consider the first scenario. The probability $T_4$ beats $T_1$ is $\frac{4}{4+1}$ , the probability $T_3$ beats $T_2$ is $\frac{3}{3+2}$ , and the probability $T_4$ beats $T_3$ is $\frac{4}{4+3}$ . Therefore the first scenario happens with probability $\frac{4}{4+1}\cdot\frac{3}{3+2}\cdot\frac{4}{4+3}$ . Consider the second scenario. The probability $T_4$ beats $T_1$ is $\frac{4}{1+4}$ , the probability $T_2$ beats $T_3$ is $\frac{2}{2+3}$ , and the probability $T_4$ beats $T_2$ is $\frac{4}{4+2}$ . Therefore the second scenario happens with probability $\frac{4}{1+4}\cdot\frac{2}{2+3}\cdot\frac{4}{4+2}$ . By summing these two probabilities, the probability that $T_4$ wins is $\frac{4}{4+1}\cdot\frac{3}{3+2}\cdot\frac{4}{4+3}+\frac{4}{1+4}\cdot\frac{2}{2+3}\cdot\frac{4}{4+2}$ . Because this expression is equal to $\frac{256}{525}$ , the answer is $256+525=\boxed{781}$ .

## Solution 2
Clearly $T_4$ has to win its game with $T_1$ , which has probability $\frac{4}{5}$ . There are two cases, depending on who its opponent is. Case 1: $T_4$ faces $T_2$ . So $T_2$ won its first game with probability $\frac{2}{5}$ , and $T_4$ wins the finals with probability $\frac{4}{6}=\frac{2}{3}$ . Case 2: $T_4$ faces $T_3$ . So $T_3$ won its first game with probability $\frac{3}{5}$ , and $T_4$ wins the finals with probability $\frac{4}{7}$ .
The total probability is therefore $\frac{4}{5} \times \left(\frac{4}{15} + \frac{12}{35}\right) = \frac{4}{5} \cdot \frac{64}{105} = \frac{256}{525} \implies 256+525 = \boxed{781}$ . ~First
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .