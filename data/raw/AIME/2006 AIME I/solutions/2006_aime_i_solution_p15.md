# 2006 AIME I Problem 15

## Problem

Given that a sequence satisfies $x_0=0$ and $|x_k|=|x_{k-1}+3|$ for all integers $k\ge 1,$ find the minimum possible value of $|x_1+x_2+\cdots+x_{2006}|.$

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4

- 3 Solution 5

- 4 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

## Solutions

## Solution 1
Suppose $b_{i} = \frac {x_{i}}3$ . We have \[\sum_{i = 1}^{2006}b_{i}^{2} = \sum_{i = 0}^{2005}(b_{i} + 1)^{2} = \sum_{i = 0}^{2005}(b_{i}^{2} + 2b_{i} + 1)\] So \[\sum_{i = 0}^{2005}b_{i} = \frac {b_{2006}^{2} - 2006}2\] Now \[\sum_{i = 1}^{2006}b_{i} = \frac {b_{2006}^{2} + 2b_{2006} - 2006}2\] Therefore \[\left|\sum_{i = 1}^{2006}b_{i}\right| = \left|\frac {(b_{2006} + 1)^{2} - 2007}2\right|\geq \left|\frac{2025 - 2007}{2}\right| = 9\] This lower bound can be achieved if we use $b_1 = -1$ , $b_2 = 0$ , $b_3 = -1$ , $b_4 = 0$ , and so on until $b_{1962} = 0$ , after which we let $b_k = b_{k - 1} + 1$ so that $b_{2006} = 44$ . So \[\left|\sum_{i = 1}^{2006}x_{i}\right|\geq \boxed{027}\]

## Solution 2
First, we state that iff $x_{i - 1}\ge0$ , $|x_i| = |x_{i - 1}| + 3$ and iff $x_{i - 1} < 0$ , $|x_i| = |x_{i - 1}| - 3$ . Now suppose $x_i = x_j$ for some $0\le i < j\le2006$ . Now, this means that $|x_i| = |x_j|$ , and so the number of positive numbers in the set $\{x_i,x_{i + 1},\ldots,x_{j - 1}\}$ equals the number of negative numbers. Now pair the numbers in this list up in the following way: Whenever a positive and a negative number are adjacent in this progression, pair them up and remove them from this list. We claim that every pair will sum to -3.
If the positive number comes first, then the negative number will have a magnitude three greater, so this is true. If the negative number comes first, then the positive number will have magnitude three smaller, and this will also be true. Now let us examine what happens when we remove those two from the sequence. WLOG, let the numbers be $x_k$ and $x_{k + 1}$ . Since one is positive and the other is negative, $|x_{k + 2}| = |x_{k + 1}|\pm3 = |x_k|\pm3\mp3 = |x_k| = |x_{k - 1} + 3|$ . So the new sequence works under the same criteria as the old one. In this way, we can pair all of the numbers up in this subsequence so the sums of the pairs are -3. Thus, the average of these numbers will be -3/2 for all subsequences that start and end with the same number (not including one of those).
Now, take all of the repeating subsequences out of the original sequence. The only thing that will be left will be a sequence $\{0,3,6,9,\cdots,3k\}$ for some even $k$ . Since we started with 2006 terms, we removed $2006 - k$ (an even number) with an average of -3/2. Thus, the sum of both this remaining sequence and the removed stuff is $(2006 - k)( - 3/2) + \sum_{i = 1}^k3k = (3/2)(k - 2006 + k(k + 1)) = 3/2(k^2 + 2k - 2006)$ . This must be minimized, so we find the roots: $k^2 + 2k = 2006\implies (k + 1)^2 = 2007$ and $44^2 = 1936 < 2007 < 2025 = 45^2$ . Plugging in $k = 44$ yields $(3/2)(2025 - 2007) = 27$ (and $k = 42$ yields $- 237$ , a worse result). Thus, $\fbox{027}$ is the closest to zero this sum can get.

## Solution 3
We know $|x_k| = |x_{k - 1} + 3|$ . We get rid of the absolute value by squaring both sides: ${x_k}^2 = {x_{k - 1}}^2 + 6{x_{k - 1}} + 9\Rightarrow {x_k}^2 - {x_{k - 1}}^2 = 6{x_{k - 1}} + 9$ . So we set this up:
\begin{align*} {x_1}^2 - {x_0}^2 & = 6{x_0} + 9 \\ {x_2}^2 - {x_1}^2 & = 6{x_1} + 9 \\ & \vdots \\ {x_{2007}}^2 - {x_{2006}}^2 & = 6{x_{2006}} + 9 \end{align*} There are $2007$ equations. Sum them. We get: ${x_{2007}}^2 = 6\left(x_1 + x_2 + \cdots + x_{2006}\right) + 9\cdot{2007}$
So $|x_1 + x_2 + \cdots + x_{2006}| = \tfrac 16 \left|{x_{2007}}^2 - 9\cdot{2007}\right|$
We know $3\ |\ x_{2007}$ and we want to minimize $\left|{x_{2007}}^2 - 9\cdot{2007}\right|$ , so $x_{2007}$ must be $3\cdot{45}$ for it to be minimal ( $45^2 = 2025$ which is closest to $2007$ ). We can achieve this with $x_k=3k$ till $x_{45}=135$ and then alternating $x_{46}=-138$ , $x_{47}=135$ and so on ... Then $x_{2k}=-138$ and $x_{2k+1}=135$ for all $k>22$ . Since $2007$ is odd, we have $x_{2007}=135$ .
This means that $|x_1 + x_2 + \cdots + x_{2006}| = \tfrac 16 \left|9(2025 - 2007)\right| = \boxed{027}$

## Solution 4
Playing around with a couple numbers, we see that we can generate the sequence $0, 3, -6, 3, -6, \cdots$ , and we can also generate the sequence $3, 6, 9, 12, \cdots$ after each $-6$ value. Thus, we will apply this to try and find some bounds. We can test if the first $1000$ pairs of numbers each sum up to $-3$ , and the rest form an arithmetic sequence, if the first $990$ pairs sum up to $-3$ , and so on. When we get to $980$ , we find that $980(-3) + 3 + 6 + \cdots + 3\cdot 46 = 303$ . If we shift the number of pairs up by $1$ , we get $981(-3) + 3 + 6 + \cdots + 3\cdot 44 = \boxed{027}$ .
~ Spacesam

## Solution 5
We will work our way from $|x_0|$ to $|x_0+x_1|$ to $|x_0+x_1+x_2+\dots+x_{2006}|$ . Let the sum $|x_0+x_1+x_2+\dots+x_i|=S_i$ .
Seeing as the value for the sum we want is always nonnegative, the best pseudo-strategy would be to stay as close to $0$ as possible as we increase $i$ to eventually get to $i=2006$ . It turns out that a greedy algorithm works here. Let us start with some smaller values of $i$ .
Note that we can describe $x_{k+1}$ in terms of $x_k$ in the following way: take $x_k$ , add $3$ , and either multiply by $-1$ or not.
We know that $S_0=0$ . When we get to $S_1$ , we add in $x_1$ , which is either $3$ or $-3$ . It does not make a difference which one we choose, so we can choose $3$ for convenience. Now, $S_1=3$ . $x_2$ is either $\pm6$ ; adding $6$ would take us farther away from $0$ , but adding $-6$ is an okay move. Thus, let $x_2=-6$ , so $S_2=-3$ .
$x_3$ is $\pm3$ . Adding $3$ is clearly the right choice here, which takes us to $0$ . Thus, $x_3=3$ and $S_3=0$ .
Let us look at how this greedy algorithm performs in general.
$\begin{tabular}[t]{c|ccccccc} S_i&3a&-3&3a-3&-6&3a-6&-9&\cdots\\ x_i&3a&-3a-3&3a&-3a-3&3a&-3a-3&\cdots\\ \end{tabular}$ (Error compiling LaTeX. Unknown error_msg)
(the table doesn't work; if you desire, please to go https://artofproblemsolving.com/texer/zzyacvnp to view)
The sums alternate between separate arithmetic sequences. One of them is of particular interest to us: specifically, the one that goes $3a,3a-3,3a-6,\cdots$ , because it will eventually become $0$ . One can then derive using simple algebra how long it will take to reach zero, depending on $a$ ; it turns out that it takes $2a+1$ for each cycle to complete. We can then see that $S_{k^2-1}=0$ for positive integers $k$ ; thus, $S_{1935}=0$ . We can then go through our algorithm, and it turns out that $S_{2006}=\boxed{027}$ .
~Technodoggo (sorry for the rushed solution!)
These problems are copyrighted © by the Mathematical Association of America.