# 2002 AIME I Problem 8

## Problem

Find the smallest integer $k$ for which the conditions

(1) $a_1,a_2,a_3\cdots$ is a nondecreasing sequence of positive integers

(2) $a_n=a_{n-1}+a_{n-2}$ for all $n>2$

(3) $a_9=k$

are satisfied by more than one sequence.

## Solution
From $(2)$ , $a_9=$ $a_8+a_7=2a_7+a_6=3a_6+2a_5=5a_5+3a_4=8a_4+5a_3=13a_3+8a_2=21a_2+13a_1$ $=k$
Suppose that $a_1=x_0$ is the smallest possible value for $a_1$ that yields a good sequence, and $a_2=y_0$ in this sequence. So, $13x_0+21y_0=k$ .
Since $\gcd(13,21)=1$ , the next smallest possible value for $a_1$ that yields a good sequence is $a_1=x_0+21$ . Then, $a_2=y_0-13$ .
By $(1)$ , $a_2 \ge a_1 \Rightarrow y_0-13 \ge x_0+21 \Rightarrow y_0 \ge x_0+34 \ge 35$ . So the smallest value of $k$ is attained when $(x_0,y_0)=(1,35)$ which yields $(a_1,a_2)=(1,35)$ or $(22,22)$ .
Thus, $k=13(1)+21(35)=\boxed{748}$ is the smallest possible value of $k$ .
These problems are copyrighted © by the Mathematical Association of America.