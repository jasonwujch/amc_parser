# 2015 AIME I Problem 2

## Problem

The nine delegates to the Economic Cooperation Conference include $2$ officials from Mexico, $3$ officials from Canada, and $4$ officials from the United States. During the opening session, three of the delegates fall asleep. Assuming that the three sleepers were determined randomly, the probability that exactly two of the sleepers are from the same country is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Video Solution For Problems 1-3
https://www.youtube.com/watch?v=5HAk-6qlOH0

## Video Solution by OmegaLearn
https://youtu.be/IRyWOZQMTV8?t=1802
~ pi_is_3.14

## Solution 1 (Principle of Inclusion-Exclusion)
One of the best ways to solve this problem is to use PIE, or the Principle of Inclusion and Exclusion.
To start off, we know that the denominator, or the total ways to pick $3$ officials, is $\binom{9}{3} = 84$ . Now, we find the number of ways that at least $2$ officials are from the same country and then subtract the number of ways all $3$ officials are from the same country. To start with at least $2$ officials, we know:
- There are $7$ different ways to pick $3$ delegates such that $2$ are from Mexico, simply because there are $9-2=7$ "extra" delegates to choose to be the third sleeper once both from Mexico are sleeping.
- There are $3\times7=21$ ways to pick from Canada, as we choose $2$ of the $3$ Canadians ( $\binom{3}{2} = 3$ ) and then there are $7$ other options for the third sleeper.
- Lastly, there are $6\times7=42$ ways to choose for the United States. We can choose two American officials with $\binom{4}{2} = 6$ . Then, there are $7$ options for the third sleeper.
Now, we want to find the number of ways to have three sleepers from the same country.
- There are no ways for the $3$ sleepers to be from Mexico because there are only $2$ Mexican officials. Hence, we get $0$ ways.
- There is only $1$ way to pick all $3$ from Canada because there are exactly $3$ Canadian officials. We now consider the number of times we originally counted this, which after inspection, is $3$ , so we have $1 * 3 = 3$ .
- Lastly, there are $4$ ways to choose all $3$ officials from the United States ( $\binom{4}{3} = 4$ ). Once again, we counted this $3$ times, so we have $4*3 = 12$ .
Thus, the fraction is $\frac{7+21+42-0-3-12}{84} = \frac{55}{84}$ , and our answer is $55+84=\boxed{139}$ .
Note: Similar to Solution 2, we could also have grouped each of the countries in terms of the ways we have for at least $2$ officials to sleep and for all $3$ to sleep. Mexico would have $7 - 0 = 7$ ways for exactly 2 officials to be there, Canada with $21 - 3 = 18$ ways, and the United States with $42 - 12 = 30$ ways.
Solution by: armang32324

## Solution 2
The total number of ways to pick $3$ officials from $9$ total is $\binom{9}{3} = 84$ , which will be our denominator. Now we can consider the number of ways for exactly two sleepers to be from the same country for each country individually and add them to find our numerator:
- There are $7$ different ways to pick $3$ delegates such that $2$ are from Mexico, simply because there are $9-2=7$ "extra" delegates to choose to be the third sleeper once both from Mexico are sleeping.
- There are $3\times6=18$ ways to pick from Canada, as each Canadian can be left out once and each time one is left out there are $9-3=6$ "extra" people to select one more sleeper from.
- Lastly, there are $6\times5=30$ ways to choose for the United States. It is easy to count $6$ different ways to pick $2$ of the $4$ Americans, and each time you do there are $9-4=5$ officials left over to choose from.
Thus, the fraction is $\frac{7+18+30}{84} = \frac{55}{84}$ . Since this does not reduce, the answer is $55+84=\boxed{139}$ .

## Solution 3
Like in the solution above, there are $84$ ways to pick $3$ delegates. We can use casework to find the probability that there aren't exactly $2$ sleepers from a county, then subtract from $1$ .
- If no country has at least $2$ delegates sleeping, then every country must have $1$ delegate sleeping. There are $2*3*4=24$ ways for this to happen.
- If all $3$ sleeping delegates are from Canada, there are $\binom{3}{3} = 1$ way.
- If all $3$ are from the US, there are $\binom{4}{3} = 4$ ways.
So, the probability that there are not exactly $2$ sleepers from one country is $\frac{24+1+4}{84} = \frac{29}{84}$ , and the probability that exactly $2$ are from the same country is $1- \frac{29}{84} = \frac{55}{84}.$ Our answer is $55+84=\boxed{139}$ .

## Solution 4 (Easy Casework)
Let us take this step-by-step.
The probability of having exactly 2 Mexican sleepers is $\frac{2}{9} \cdot \frac{1}{8} \cdot 3$ .
The probability of having exactly 2 Canadian sleepers is $\frac{3}{9} \cdot \frac{2}{8} \cdot \frac{6}{7} \cdot 3$ .
The probability of having exactly 2 American sleepers is $\frac{4}{9} \cdot \frac{3}{8} \cdot \frac{5}{7} \cdot 3$ .
Thus, adding these up our total probability is $\frac{55}{84}$ . Adding the numerator and denominator gives us our desired $55+84=\boxed{139}.$
~SirAppel
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .