# 2021 Fall AMC 12A Problem 16

## Problem

An organization has $30$ employees, $20$ of whom have a brand A computer while the other $10$ have a brand B computer. For security, the computers can only be connected to each other and only by cables. The cables can only connect a brand A computer to a brand B computer. Employees can communicate with each other if their computers are directly connected by a cable or by relaying messages through a series of connected computers. Initially, no computer is connected to any other. A technician arbitrarily selects one computer of each brand and installs a cable between them, provided there is not already a cable between that pair. The technician stops once every employee can communicate with each other. What is the maximum possible number of cables used?

$\textbf{(A)}\ 190 \qquad\textbf{(B)}\ 191 \qquad\textbf{(C)}\ 192 \qquad\textbf{(D)}\ 195 \qquad\textbf{(E)}\ 196$

## Solution
We claim that to maximize the number of cables used, we isolate one computer and connect all cables for the remaining $29$ computers, then connect one more cable for the isolated computer.
If a brand A computer is isolated, then the technician can use at most $19\cdot10+1=191$ cables. If a brand B computer is isolated instead, then the technician can use at most $20\cdot9+1=181$ cables. Therefore, the answer is $\boxed{\textbf{(B)}\ 191}.$
Remark
Suppose that the computers are labeled $A_1, A_2, \ldots, A_{20}$ and $B_1, B_2, \ldots, B_{10}.$ We will prove the claim in the first paragraph of this solution:
1. With exactly cables, it is possible that some computers cannot communicate with each other.
1. With exactly cables, all computers must be able to communicate with each other.
From this solution, it is clear that this claim is true: We isolate $A_{20}$ and connect all cables for $A_1, A_2, \ldots, A_{19}$ and $B_1, B_2, \ldots, B_{10}$ to get $19\cdot10=190$ cables. However, $A_{20}$ cannot communicate with any of these $29$ computers.
By the Pigeonhole Principle, we conclude that at least one brand B computer connects to all $20$ brand A computers. Without loss of generality, we assume that $B_1$ connects to all $20$ brand A computers. On the other hand, we conclude that at least $11$ brand A computers connect to all $10$ brand B computers. Without loss of generality, we assume that $A_1, A_2, \ldots, A_{11}$ connect to all $10$ brand B computers.
Therefore, any two computers must be able to communicate with each other:
- Between $A_i$ and $A_j,$ where $i,j\in\{1,2,\ldots,20\}$ and $i\neq j$
- Between $B_i$ and $B_j,$ where $i,j\in\{1,2,\ldots,10\}$ and $i\neq j$
- Between $A_i$ and $B_j,$ where $i\in\{1,2,\ldots,20\}$ and $j\in\{1,2,\ldots,10\}$
The relay is $A_i\leftrightarrow B_1\leftrightarrow A_j.$
The relay is $B_i\leftrightarrow \{A_1, A_2, \ldots, A_{11}\}\leftrightarrow B_j.$
The relay is $A_i\leftrightarrow B_1\leftrightarrow \{A_1, A_2, \ldots, A_{11}\}\leftrightarrow B_j.$
~MRENTHUSIASM
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .