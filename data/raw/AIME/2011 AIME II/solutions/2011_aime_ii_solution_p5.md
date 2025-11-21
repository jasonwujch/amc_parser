# 2011 AIME II Problem 5

## Problem

The sum of the first $2011$ terms of a geometric sequence is $200$ . The sum of the first $4022$ terms is $380$ . Find the sum of the first $6033$ terms.

## Solution
Since the sum of the first $2011$ terms is $200$ , and the sum of the first $4022$ terms is $380$ , the sum of the second $2011$ terms is $180$ . This is decreasing from the first 2011, so the common ratio is less than one.
Because it is a geometric sequence and the sum of the first 2011 terms is $200$ , second $2011$ is $180$ , the ratio of the second $2011$ terms to the first $2011$ terms is $\frac{9}{10}$ . Following the same pattern, the sum of the third $2011$ terms is $\frac{9}{10}*180 = 162$ .
Thus, $200+180+162=542$ , so the sum of the first $6033$ terms is $\boxed{542}$ .

## Solution 2
Solution by e_power_pi_times_i
The sum of the first $2011$ terms can be written as $\dfrac{a_1(1-k^{2011})}{1-k}$ , and the first $4022$ terms can be written as $\dfrac{a_1(1-k^{4022})}{1-k}$ . Dividing these equations, we get $\dfrac{1-k^{2011}}{1-k^{4022}} = \dfrac{10}{19}$ . Noticing that $k^{4022}$ is just the square of $k^{2011}$ , we substitute $x = k^{2011}$ , so $\dfrac{1}{x+1} = \dfrac{10}{19}$ . That means that $k^{2011} = \dfrac{9}{10}$ . Since the sum of the first $6033$ terms can be written as $\dfrac{a_1(1-k^{6033})}{1-k}$ , dividing gives $\dfrac{1-k^{2011}}{1-k^{6033}}$ . Since $k^{6033} = \dfrac{729}{1000}$ , plugging all the values in gives $\boxed{542}$ .

## Solution 3
The sum of the first 2011 terms of the sequence is expressible as $a_1 + a_1r + a_1r^2 + a_1r^3$ .... until $a_1r^{2010}$ . The sum of the 2011 terms following the first 2011 is expressible as $a_1r^{2011} + a_1r^{2012} + a_1r^{2013}$ .... until $a_1r^{4021}$ . Notice that the latter sum of terms can be expressed as $(r^{2011})(a_1 + a_1r + a_1r^2 + a_1r^3...a_1r^{2010})$ . We also know that the latter sum of terms can be obtained by subtracting 200 from 380, which then means that $r^{2011} = 9/10$ . The terms from 4023 to 6033 can be expressed as $(r^{4022})(a_1 + a_1r + a_1r^2 + a_1r^3...a_1r^{2010})$ , which is equivalent to $((9/10)^2)(200) = 162$ . Adding 380 and 162 gives the answer of $\boxed{542}$ .

## Solution 4
Let $S_n$ be equal to the sum of the first $n$ terms of the geometric sequence. $S_{2011} = 200$ and $S_{4022} = 380$ . Let $a$ be the first term and $r$ be the common difference. So $a(\frac{1-r^{2011}}{1-r}) = 200$ and $a(\frac{1-r^{4022}}{1-r}) = 380$ . We take the positive difference between the two equations. $a(\frac{r^{2011}-r^{4022}}{r-1}) = 180$ . Now, we'll factor out $r^{2011}$ so the equation becomes $ar^{2011}(\frac{1-r^{2011}}{r-1}) = 180$ . Divide this equation by the first equation and we get $r^{2011} = 9/10$ . We now just need to find the ratio of $S_{6033}$ to $S_{2011}$ multiplied by $S_{2011}$ (It's easy to find the ratio because of common terms). \[\frac{S_{6033}}{S_{2011}} = \frac{\frac{a(1-r^{6033})}{1-r}}{\frac{a(1-r^{2011})}{1-r}} = \frac{1-r^{6033}}{1-r^{2011}} = \frac{1-(\frac{9}{10})^{3}}{1-\frac{9}{10}} = \frac{\frac{271}{1000}}{\frac{1}{10}} = \frac{271}{100}\] Now it's simple, we just need to multiply this value by $S_{2011}$ (which is $200$ ) and we get our final answer of $\boxed{542}$ .
~ROGER8432V3

## Video Solution
https://www.youtube.com/watch?v=rpYphKOIKRs&t=186s ~anellipticcurveoverq
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .