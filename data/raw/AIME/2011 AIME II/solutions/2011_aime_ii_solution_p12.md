# 2011 AIME II Problem 12

## Problem

Nine delegates, three each from three different countries, randomly select chairs at a round table that seats nine people. Let the probability that each delegate sits next to at least one delegate from another country be $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution
Use complementary probability and Principle of Inclusion-Exclusion . If we consider the delegates from each country to be indistinguishable and number the chairs, we have \[\frac{9!}{(3!)^3} = \frac{9\cdot8\cdot7\cdot6\cdot5\cdot4}{6\cdot6} = 6\cdot8\cdot7\cdot5 = 30\cdot56\] total ways to seat the candidates.
Of these, there are $3 \times 9 \times \frac{6!}{(3!)^2}$ ways to have the candidates of at least some one country sit together. This comes to \[\frac{27\cdot6\cdot5\cdot4}6 = 27\cdot 20.\]
Among these there are $3 \times 9 \times 4$ ways for candidates from two countries to each sit together. This comes to $27\cdot 4.$
Finally, there are $9 \times 2 = 18.$ ways for the candidates from all the countries to sit in three blocks (9 clockwise arrangements, and 9 counter-clockwise arrangements).
So, by PIE, the total count of unwanted arrangements is $27\cdot 20 - 27\cdot 4 + 18 = 16\cdot27 + 18 = 18\cdot25.$ So the fraction \[\frac mn = \frac{30\cdot 56 - 18\cdot 25}{30\cdot 56} = \frac{56 - 15}{56} = \frac{41}{56}.\] Thus $m + n = 56 + 41 = \fbox{097}.$

## Setup Solution
We should give a specific setup for the table so to simplify. Call countries A, B, C. Someone from A (let me call him/her the "Master A") sits at the northernmost place for configurations. In my solution I choose to represent people by countries, because all the problem says about distinction among delegates is their country. Now, we can see that the total number of ways to arrange is nCr(8, 2) * nCr(6, 3) = 560 (8 seats choose 2 for the rest of the A country, 6 seats choose 3 for B).
It is not difficult to see that the configurations we don't want are those which put three delegates in a row. Note also that despite my (arbitrary) setting A at the front, cases for A, B, C to be together are symmetric. Now, we use some Principle of Inclusion-Exclusion . For A three in a row: two cases. First. A, Master A, A: nCr(6, 3) for B seats = $20$ . There's also $20$ for each of the "slant" A sets (i.e. A, A, Master A and Master A, A, A). = $60. *3=180$ . For both A and B: Two cases again! A, Master A, A: we see 4 ways for B to have 3-in-a-row. Same for slant = $12. *3$ (AB, BC, or CA) = $36$ . For all three: This time, we have 2 for each of the 3 aforementioned A situations = 6. Finally, 180-36+6=150. Those are the ones we don't want. The ones we do want are 410 of 560, so our answer is $\fbox{097}$ .

## Solution 3
We use complementary counting.
We can order the $9$ people around a circle in $\frac{9!}{9} = 8!$ ways. Now we count when there is at least one delegate surrounded by people from only his/her country.
Let the countries be $A,B,C$ . Suppose that the group $XXX$ (for some country $X$ ) appears. To account for circular over counting we fix this group at the top. There are $6!$ ways to arrange the rest of the delegates and $3!$ ways to arrange inside the group. Since there are three countries this group can belong to, the total is $6!*3!*3$ .
But notice that when the group $XXX$ AND $YYY$ both appear is over counted. So, fix one group at the top. for the last country, we can insert $0,1,2,3$ people in between the two groups. Since we can choose two countries in $\binom{3}{2} = 3$ ways, the total is $3!*3!*3!*4*3$ ways.
Unfortunately, there is over count in the over count. If each country has their delegates together, this case must be added back. Think of these three groups as a whole, and there are $3!/3 = 2$ ways of arranging. In each group there is $3!$ ways of arrangements. So, $3!*3!*3!*2$ is the total for this case.
We now find the complementary probability total. This is \[\frac{6!*3!*3 - 3!*3!*3!*4*3 + 3!*3!*3!*2}{8!} = \frac{15}{56}\] so the actual probability is $1-\frac{15}{56} = \frac{41}{56}$ for an answer of $\boxed{097}$ .
~Leonard_my_dude~

## Solution 4 (PIE)
$1680= \binom{9}{3} \binom{6}{3}$ is the total.
$540 = 3* 9* \binom{6}{3}$ is the case where one country has three people in a row. (Three is for selection of country and nine is for rotation of the seats.)
$108 = 3* 9* 4$ is the case where two countries has three people in a row. (Three and nine are for the same reasons above and four is for putting three people in a row for the remaining six seats.)
$18$ is the case where three countries has three people in a row.
$\frac{1680-540+108-18}{1680}=\frac{41}{56}$ so the answer is $\boxed{097}$
By maxamc
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .