# 2002 AIME I Problem 4

## Problem

Consider the sequence defined by $a_k =\dfrac{1}{k^2+k}$ for $k\geq 1$ . Given that $a_m+a_{m+1}+\cdots+a_{n-1}=\dfrac{1}{29}$ , for positive integers $m$ and $n$ with $m<n$ , find $m+n$ .

## Solution 1
Using partial fraction decomposition yields $\dfrac{1}{k^2+k}=\dfrac{1}{k(k+1)}=\dfrac{1}{k}-\dfrac{1}{k+1}$ . Thus,
$a_m+a_{m+1}+\cdots +a_{n-1}=\dfrac{1}{m}-\dfrac{1}{m+1}+\dfrac{1}{m+1}-\dfrac{1}{m+2}+\cdots +\dfrac{1}{n-1}-\dfrac{1}{n}=\dfrac{1}{m}-\dfrac{1}{n}$
Which means that
$\dfrac{n-m}{mn}=\dfrac{1}{29}$
Since we need a factor of 29 in the denominator, we let $n=29t$ .* Substituting, we get
$29t-m=mt$
so
$\frac{29t}{t+1} = m$
Since $m$ is an integer, $t+1 = 29$ , so $t=28$ . It quickly follows that $n=29(28)$ and $m=28$ , so $m+n = 30(28) = \fbox{840}$ .

## Solution 2
Note that $a_1 + a_2 + \cdots + a_i = \dfrac{i}{i+1}$ . This can be proven by induction. Thus, $\sum\limits_{i=m}^{n-1} a_i = \sum\limits_{i=1}^{n-1} a_i - \sum\limits_{i=1}^{m-1} a_i = \dfrac{n-1}{n} - \dfrac{m-1}{m} = \dfrac{n-m}{mn} = 1/29$ . Cross-multiplying yields $29n - 29m - mn = 0$ , and adding $29^2$ to both sides gives $(29-m)(29+n) = 29^2$ . Clearly, $m < n \implies 29 - m = 1$ and $29 + n = 29^2$ . Hence, $m = 28$ , $n = 812$ , and $m+n = \fbox{840}$ .
~ keeper1098

## Solution 3
To solve this problem, I need to find two positive integers $m$ and $n$ where $m < n$ and the sum of sequence terms equals $\frac{1}{29}$ .
First, let me simplify $a_k = \frac{1}{k^2 + k}$ using partial fractions. $a_k = \frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$
Express the sum $a_m + a_{m+1} + \cdots + a_{n-1}$ using this simplification. $a_m + a_{m+1} + \cdots + a_{n-1} = \sum_{k=m}^{n-1} \left(\frac{1}{k} - \frac{1}{k+1}\right)$
This is a telescoping series where intermediate terms cancel: $a_m + a_{m+1} + \cdots + a_{n-1} = \frac{1}{m} - \frac{1}{n}$
Use the given condition that this sum equals $\frac{1}{29}$ . $\frac{1}{m} - \frac{1}{n} = \frac{1}{29}$
Multiplying both sides by $mn$ : $n - m = \frac{mn}{29}$
Rearranging: $29(n - m) = mn$ $29n - 29m = mn$ $29n - mn = 29m$ $n(29 - m) = 29m$
Solve for $n$ in terms of $m$ . $n = \frac{29m}{29-m}$
Since $n$ must be a positive integer, $29-m$ must divide $29m$ evenly. Since $29$ is prime, for $29-m$ to divide $29m$ (when $m < 29$ ), we need $29-m$ to divide $m$ .
This means $m = k(29-m)$ for some positive integer $k$ . $m = k(29-m)$ $m = 29k - km$ $m(1+k) = 29k$ $m = \frac{29k}{1+k}$
For $m$ to be an integer, $1+k$ must divide $29k$ . When $k = 28$ , we get $m = \frac{29(28)}{29} = 28$
Calculate $n$ using our value of $m$ . $n = \frac{29(28)}{29-28} = \frac{812}{1} = 812$
Therefore, $m + n = 28 + 812 = \boxed{840}$
~ brandonyee

## Video Solution by OmegaLearn
https://youtu.be/lH-0ul1hwKw?t=134
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.