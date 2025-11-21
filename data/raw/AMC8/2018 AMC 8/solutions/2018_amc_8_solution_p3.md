# 2018 AMC 8 Problem 3

## Problem

Students Arn, Bob, Cyd, Dan, Eve, and Fon are arranged in that order in a circle. They start counting: Arn first, then Bob, and so forth. When the number contains a 7 as a digit (such as 47) or is a multiple of 7 that person leaves the circle and the counting continues. Who is the last one present in the circle?

$\textbf{(A) } \text{Arn}\qquad\textbf{(B) }\text{Bob}\qquad\textbf{(C) }\text{Cyd}\qquad\textbf{(D) }\text{Dan}\qquad \textbf{(E) }\text{Eve}\qquad$

## Solution 1(Simulation)
The five numbers which cause people to leave the circle are $7, 14, 17, 21,$ and $27.$
The most straightforward way to do this would be to draw out the circle with the people, and cross off people as you count.
Assuming the six people start with $1$ , Arn counts $7$ so he leaves first. Then, Cyd counts $14$ as there are $7$ numbers to be counted from this point. Then, Fon, Bob, and Eve, count, $17,$ $21,$ and $27$ , respectively, so the last one standing is Dan. Hence, the answer would be $\boxed{\textbf{(D) }\text{Dan}}$ .
~Nivaar

## Solution 2
Assign each person a position: Arn is in position $1$ , Bob in $2$ , etc. Note that if there are $n$ people standing in a circle, a person will say a number that is congruent to their position modulo $n$ . It follows that if there are $k$ numbers to be said (with someone leaving on the $kth$ ), the person that leaves will stand in position $k\pmod{n}.$
The five numbers which cause people to leave the circle are $7, 14, 17, 21,$ and $27.$ Since there are initially $6$ people in the circle, so the person who leaves stands in position $7\equiv 1\pmod 6$ , or position $1$ .
Arn now leaves, and because Bob is the next person to say a number, we reassign the positions such that Bob is in position $1$ , Cyd in $2$ , and Fon in $5$ . There are $7$ more numbers to be said, and someone leaves on the $7th$ . It follows that the person who leaves stands in position $7\equiv 2\pmod 5$ .
Cyd leaves the circle, and $4$ people remain, namely Bob, Dan, Eve, and Fon. Assign the position numbers such that Dan has $1$ , Eve $2$ , etc. There are $3$ more numbers to be said, and someone leaves on the $3rd$ . The person standing in position $3$ (Fon) now leaves.
There are two people left, Eve and Dan, with Dan in position $1$ now. There are $6$ more numbers to be said, and Eve is standing in position $6\equiv 0\pmod 2$ , so she leaves.
The last person standing is $\boxed{\textbf{(D) }\text{Dan}}$ .
-Benedict T (countmath1) Why? Why would you do this?

## Video Solution (CRITICAL THINKING!!!)
https://youtu.be/wziaWxZmjgg
~Education, the Study of Everything

## Video Solution
https://youtu.be/uK4bbVpwHGc
~savannahsolver
### See Also