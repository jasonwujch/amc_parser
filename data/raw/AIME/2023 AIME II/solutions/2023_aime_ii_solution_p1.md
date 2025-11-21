# 2023 AIME II Problem 1

## Problem

The numbers of apples growing on each of six apple trees form an arithmetic sequence where the greatest number of apples growing on any of the six trees is double the least number of apples growing on any of the six trees. The total number of apples growing on all six trees is $990.$ Find the greatest number of apples growing on any of the six trees.

## Solution 1
In the arithmetic sequence, let $a$ be the first term and $d$ be the common difference, where $d>0.$ The sum of the first six terms is \[a+(a+d)+(a+2d)+(a+3d)+(a+4d)+(a+5d) = 6a+15d.\] We are given that \begin{align*} 6a+15d &= 990, \\ 2a &= a+5d. \end{align*} The second equation implies that $a=5d.$ Substituting this into the first equation, we get \begin{align*} 6(5d)+15d &=990, \\ 45d &= 990 \\ d &= 22. \end{align*} It follows that $a=110.$ Therefore, the greatest number of apples growing on any of the six trees is $a+5d=\boxed{220}.$
~MRENTHUSIASM

## Solution 2
Let the terms in the sequence be defined as \[a_1, a_2, ..., a_6.\]
Since this is an arithmetic sequence, we have $a_1+a_6=a_2+a_5=a_3+a_4.$ So, \[\sum_{i=1}^6 a_i=3(a_1+a_6)=990.\] Hence, $(a_1+a_6)=330.$ And, since we are given that $a_6=2a_1,$ we get $3a_1=330\implies a_1=110$ and $a_6=\boxed{220}.$
~Kiran

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=nNhfDCX5-bw

## Video Solution by the Power of Logic(both #1 and #2)
https://youtu.be/VcEulZ3nvSI
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .