# 2020 AMC 8 Problem 7

## Problem

How many integers between $2020$ and $2400$ have four distinct digits arranged in increasing order? (For example, $2347$ is one integer.).

$\textbf{(A) }\text{9} \qquad \textbf{(B) }\text{10} \qquad \textbf{(C) }\text{15} \qquad \textbf{(D) }\text{21}\qquad \textbf{(E) }\text{28}$

## Solution 1
Firstly, we can observe that the second digit of such a number cannot be $1$ or $2$ because the digits must be distinct and in increasing order. The second digit also cannot be $4$ as the number must be less than $2400$ , so the second digit must be $3$ . It remains to choose the latter two digits, which must be $2$ distinct digits from $\left\{4,5,6,7,8,9\right\}$ . That can be done in $\binom{6}{2} = \frac{6 \cdot 5}{2 \cdot 1} = 15$ ways; there is then only $1$ way to order the digits, namely in increasing order. This means the answer is $\boxed{\textbf{(C) }15}$ .

## Solution 2 (without using the "choose" function)
As in Solution 1, we find that the first two digits must be $23$ , and the third digit must be at least $4$ because the digits can not repeat. If it is $4$ , then there are $5$ choices for the last digit, namely $5$ , $6$ , $7$ , $8$ , or $9$ . Similarly, if the third digit is $5$ , there are $4$ choices for the last digit, namely $6$ , $7$ , $8$ , and $9$ ; if $6$ , there are $3$ choices; if $7$ , there are $2$ choices; and if $8$ , there is $1$ choice. It follows that the total number of such integers is $5+4+3+2+1=\boxed{\textbf{(C) }15}$ .

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=8hgK6rESdek&t=9s
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=xBEcgPkL367f3Zp8&t=713
~Math-X

## Video Solution (🚀Fast🚀)
https://youtu.be/QqBpLTQojHg
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/FjmBtgrGfCs
~savannahsolver

## Video Solution
https://youtu.be/61c1MR9tne8 ~ The Learning Royal

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=251
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/U27z1hwMXKY?list=PLFcinOE4FNL0TkI-_yKVEYyA_QCS9mBNS&t=85
~STEMbreezy