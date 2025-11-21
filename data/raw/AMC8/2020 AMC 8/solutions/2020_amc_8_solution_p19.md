# 2020 AMC 8 Problem 19

## Problem

A number is called flippy if its digits alternate between two distinct digits. For example, $2020$ and $37373$ are flippy, but $3883$ and $123123$ are not. How many five-digit flippy numbers are divisible by $15?$

$\textbf{(A) }3 \qquad \textbf{(B) }4 \qquad \textbf{(C) }5 \qquad \textbf{(D) }6 \qquad \textbf{(E) }8$

## Solution 1
A number is divisible by $15$ precisely if it is divisible by $3$ and $5$ . The latter means the last digit must be either $5$ or $0$ , and the former means the sum of the digits must be divisible by $3$ . If the last digit is $0$ , the first digit would be $0$ (because the digits alternate), which is not possible. Hence the last digit must be $5$ , and the number is of the form $5\square 5\square 5$ . If the unknown digit is $x$ , we deduce $5+x+5+x+5 \equiv 0 \pmod{3} \Rightarrow 2x \equiv 0 \pmod{3}$ . We know $2^{-1}$ exists modulo $3$ because 2 is relatively prime to 3, so we conclude that $x$ (i.e. the second and fourth digit of the number) must be a multiple of $3$ . It can be $0$ , $3$ , $6$ , or $9$ , so there are $\boxed{\textbf{(B) }4}$ options: $50505$ , $53535$ , $56565$ , and $59595$ .

## Solution 2 (variant of Solution 1)
As in Solution 1, we find that such numbers must start with $5$ and alternate with $5$ (i.e. must be of the form $5\square 5\square 5$ ), where the two digits between the $5$ s need to be the same. Call that digit $x$ . For the number to be divisible by $3$ , the sum of the digits must be divisible by $3$ ; since the sum of the three $5$ s is $15$ , which is already a multiple of $3$ , it must also be the case that $x+x=2x$ is a multiple of $3$ . Thus, the problem reduces to finding the number of digits from $0$ to $9$ for which $2x$ is a multiple of $3$ . This leads to $x=0$ , $3$ , $6$ , or $9$ , so there are $\boxed{\textbf{(B) }4}$ possible numbers (namely $50505$ , $53535$ , $56565$ , and $59595$ ).

## Solution 3
After finding out that the last digit must be $5$ , the number is of the form $5\square 5\square 5$ . If the unknown digit is $x$ , we can find that one of the solutions to $x$ is $0$ , since $5+5+5$ is equal to $15$ , which is divisible by $3$ . After trying every one digit number, you'll notice that $x$ must be a multiple of $3$ , meaning that $x=0$ , $3$ , $6$ , or $9$ . $50505$ , $53535$ , $56565$ , and $59595$ are the $\boxed{\textbf{(B) }4}$ solutions to this question.

## Solution 4 (mods)
assume the number is $ababa$ $10101a+1010b=0 (mod 15)\newline$ $6a+5b=0 (mod 15)\newline$ $a=0 (mod 5)\newline$ $5b=0 (mod 15)\newline$ $b=0 (mod 3)\newline$ Solutions: $(5,0),(5,3),(5,6),(5,9)\newline$ $\boxed{4}$

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=bHNrBwwUCMI
~NiuniuMaths

## Video Solution by EzLx(CookeMonster)
https://youtu.be/G889MeNX3t4
~@SirCookies

## Video Solution (🚀Very Fast🚀)
https://youtu.be/4Mvm5u4RT6E
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/At4w8uylvv8?t=692
~ pi_is_3.14

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=5Qo4pG3Uk_U
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/8nVSeTx5rro
~savannahsolver

## Video Solution
https://www.youtube.com/watch?v=a3Z7zEc7AXQ

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=980
~Interstigation