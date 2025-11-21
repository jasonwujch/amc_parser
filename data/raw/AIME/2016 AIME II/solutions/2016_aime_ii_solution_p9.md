# 2016 AIME II Problem 9

## Problem

The sequences of positive integers $1,a_2, a_3,...$ and $1,b_2, b_3,...$ are an increasing arithmetic sequence and an increasing geometric sequence, respectively. Let $c_n=a_n+b_n$ . There is an integer $k$ such that $c_{k-1}=100$ and $c_{k+1}=1000$ . Find $c_k$ .

## Solution 1
Since all the terms of the sequences are integers, and 100 isn't very big, we should just try out the possibilities for $b_2$ . When we get to $b_2=9$ and $a_2=91$ , we have $a_4=271$ and $b_4=729$ , which works, therefore, the answer is $b_3+a_3=81+181=\boxed{262}$ .

## Solution 2 (Some trial and error)
We have $a_k=r^{k-1}$ and $b_k=(k-1)d$ . First, $b_{k-1}<c_{k-1}=100$ implies $d<100$ , so $b_{k+1}<300$ .
It follows that $a_{k+1}=1000-b_{k+1}>700$ , i.e., \[700 < r^k < 1000.\] Moreover, since $k$ is atleast $3$ we get $r^3\le r^k <1000$ , i.e. $r<10$ . For every value of $r$ in this range, define $i(r) = \max \{x : r^x < 700\}$ , and define $j(r) = \min \{x : r^x > 1000\}$ . We are looking for values of $r$ such that $j(r) -i(r)>1$ . Let's make a table: \begin{array}[b]{ c c c c c c c c c } r & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\[2ex] i(r) & 9 & 5 & 4 & 4 & 3 & 3 & 3 & 2\\[2ex] j(r) & 10 & 7 & 5 & 5 & 4 & 4 & 4 & 4 \end{array} The only admissible values for $r^k$ are $\{3^6, 9^3\}$ . However, since $100=c_{k-1}=r^{k-2}+(k-2)d+1$ , we must have $(k-2)\mid 99-r^{k-2}$ . This does not hold for $r^k=3^6$ because $4$ does not divide $99-3^4=18$ . This leaves $r^k=9^3$ as the only option.
For $r=9$ and $k=3$ , we check: $a_{k-1}= a_2 = r =9$ implies $b_{k-1}= b_2 = 91$ , i.e. $d=90$ . Then $a_{k+1}=a_4 = r^3 = 729$ and $b_{k+1}=b_4 = 1+3d = 271$ and $c_{k+1}=c_4=a_4+b_4 = 729+271=1000$ ; so it works! Then $c_k = c_3 = 9^2+181 = 262$ .

## Solution 3
Using the same reasoning ( $100$ isn't very big), we can guess which terms will work. The first case is $k=3$ , so we assume the second and fourth terms of $c$ are $100$ and $1000$ . We let $r$ be the common ratio of the geometric sequence and write the arithmetic relationships in terms of $r$ .
The common difference is $100-r - 1$ , and so we can equate: $2(99-r)+100-r=1000-r^3$ . Moving all the terms to one side and the constants to the other yields
$r^3-3r = 702$ , or $r(r^2-3) = 702$ . Simply listing out the factors of $702$ shows that the only factor $3$ less than a square that works is $78$ . Thus $r=9$ and we solve from there to get $\boxed{262}$ .
Solution by rocketscience

## Solution 4 (More Robust Bash)
The reason for bashing in this context can also be justified by the fact 100 isn't very big.
Let the common difference for the arithmetic sequence be $a$ , and the common ratio for the geometric sequence be $b$ . The sequences are now $1, a+1, 2a+1, \ldots$ , and $1, b, b^2, \ldots$ . We can now write the given two equations as the following:
$1+(k-2)a+b^{k-2} = 100$
$1+ka+b^k = 1000$
Take the difference between the two equations to get $2a+(b^2-1)b^{k-2} = 900$ . Since 900 is divisible by 4, we can tell $a$ is even and $b$ is odd. Let $a=2m$ , $b=2n+1$ , where $m$ and $n$ are positive integers. Substitute variables and divide by 4 to get:
$m+(n+1)(n)(2n+1)^{k-2} = 225$
Because very small integers for $n$ yield very big results, we can bash through all cases of $n$ . Here, we set an upper bound for $n$ by setting $k$ as 3. After trying values, we find that $n\leq 4$ , so $b=9, 7, 5, 3$ . Testing out $b=9$ yields the correct answer of $\boxed{262}$ . Note that even if this answer were associated with another b value like $b=3$ , the value of $k$ can still only be 3 for all of the cases.

## Solution 5 (Casework)
Let $a_n$ and $b_n$ be in the form of \begin{array}[b]{ c c c c c c c } n & 1 & 2 & 3 & 4 & 5 & 6 \\[2ex] a_n & 1 & a+1 & 2a+1 & 3a+1 & 4a+1 & 5a+1 \\[2ex] b_n & 1 & b & b^2 & b^3 & b^4 & b^5 \\[2ex] c_n & 2 & b+a+1 & b^2+2a+1 & b^3+3a+1 & b^4+4a+1 & b^5+5a+1 \end{array} Case $1.\hspace{10mm} k = 3\hspace{5mm} (c_1=2 \implies k > 2).$ \[c_2 = a+1 + b = 100, c_4 = 3a+1 + b^3 = 1000 \implies b^3 -3b -2 = 1000-300 \implies b^3 - 3b = 702 \implies b = 9, a=90, c_3 = \boxed {262}.\] Case $2. \hspace{10mm} k = 4.$ \[c_3 = 2a+1 + b^2 = 100, c_5 = 4a+1 + b^4 = 1000 \implies b^4 -2b^2 -1 = 1000-200 \implies b^4 - 2b^2 = 801 \implies \O.\] Case $3. \hspace{10mm} k \ge 5.\hspace{3mm} b^5 < 1000 \implies b = \{2,3\}.$
Case $3.1.\hspace{10mm} b = 2.$ \[c_{k-1} = 2^{k-2} + (k-2) a + 1 = 100, c_{k+1} = 2^k + ka + 1 = 1000\implies a = 450-3\cdot 2^{k-3} \implies 2^k +450k -3k\cdot 2^{k-3} + 1 = 1000 \implies \O.\] Case $3.2.\hspace{10mm} b = 3.$ \[c_{k-1} = 3^{k-2} + (k-2) a + 1 = 100, c_{k+1} = 3^k + ka + 1 = 1000\implies a = 450-4\cdot 3^{k-2} \implies 3^{k-4}(9-4k) +50k = 3\cdot 37 \implies \O.\] vladimir.shelomovskii@gmail.com, vvsss
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .