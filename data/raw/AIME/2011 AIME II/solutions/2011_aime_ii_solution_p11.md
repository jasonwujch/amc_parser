# 2011 AIME II Problem 11

## Problem

Let $M_n$ be the $n \times n$ matrix with entries as follows: for $1 \le i \le n$ , $m_{i,i} = 10$ ; for $1 \le i \le n - 1$ , $m_{i+1,i} = m_{i,i+1} = 3$ ; all other entries in $M_n$ are zero. Let $D_n$ be the determinant of matrix $M_n$ . Then $\sum_{n=1}^{\infty} \frac{1}{8D_n+1}$ can be represented as $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p + q$ .

Note: The determinant of the $1 \times 1$ matrix $[a]$ is $a$ , and the determinant of the $2 \times 2$ matrix $\left[ {\begin{array}{cc} a & b \\ c & d \\ \end{array} } \right] = ad - bc$ ; for $n \ge 2$ , the determinant of an $n \times n$ matrix with first row or first column $a_1$ $a_2$ $a_3$ $\dots$ $a_n$ is equal to $a_1C_1 - a_2C_2 + a_3C_3 - \dots + (-1)^{n+1}a_nC_n$ , where $C_i$ is the determinant of the $(n - 1) \times (n - 1)$ matrix formed by eliminating the row and column containing $a_i$ .

## Solution
\[D_{1}=\begin{vmatrix} 10 \end{vmatrix} = 10, \quad D_{2}=\begin{vmatrix} 10 & 3 \\ 3 & 10 \\ \end{vmatrix} =(10)(10) - (3)(3) = 91, \quad D_{3}=\begin{vmatrix} 10 & 3 & 0 \\ 3 & 10 & 3 \\ 0 & 3 & 10 \\ \end{vmatrix}.\] Using the expansionary/recursive definition of determinants (also stated in the problem):
$D_{3}=\left| {\begin{array}{ccc} 10 & 3 & 0 \\ 3 & 10 & 3 \\ 0 & 3 & 10 \\ \end{array} } \right|=10\left| {\begin{array}{cc} 10 & 3 \\ 3 & 10 \\ \end{array} } \right| - 3\left| {\begin{array}{cc} 3 & 3 \\ 0 & 10 \\ \end{array} } \right| + 0\left| {\begin{array}{cc} 3 & 10 \\ 0 & 3 \\ \end{array} } \right| = 10D_{2} - 9D_{1} = 820$
This pattern repeats because the first element in the first row of $M_{n}$ is always 10, the second element is always 3, and the rest are always 0. The ten element directly expands to $10D_{n-1}$ . The three element expands to 3 times the determinant of the the matrix formed from omitting the second column and first row from the original matrix. Call this matrix $X_{n}$ . $X_{n}$ has a first column entirely of zeros except for the first element, which is a three. A property of matrices is that the determinant can be expanded over the rows instead of the columns (still using the recursive definition as given in the problem), and the determinant found will still be the same. Thus, expanding over this first column yields $3D_{n-2} + 0(\text{other things})=3D_{n-2}$ . Thus, the $3 \det(X_{n})$ expression turns into $9D_{n-2}$ . Thus, the equation $D_{n}=10D_{n-1}-9D_{n-2}$ holds for all n > 2.
This equation can be rewritten as $D_{n}=10(D_{n-1}-D_{n-2}) + D_{n-2}$ . This version of the equation involves the difference of successive terms of a recursive sequence. Calculating $D_{0}$ backwards from the recursive formula and $D_{4}$ from the formula yields $D_{0}=1, D_{4}=7381$ . Examining the differences between successive terms, a pattern emerges. $D_{0}=1=9^{0}$ , $D_{1}-D_{0}=10-1=9=9^{1}$ , $D_{2}-D_{1}=91-10=81=9^{2}$ , $D_{3}-D_{2}=820-91=729=9^{3}$ , $D_{4}-D_{3}=7381-820=6561=9^{4}$ . Thus, $D_{n}=D_{0} + 9^{1}+9^{2}+ . . . +9^{n}=\sum_{i=0}^{n}9^{i}=\frac{(1)(9^{n+1}-1)}{9-1}=\frac{9^{n+1}-1}{8}$ .
Thus, the desired sum is $\sum_{n=1}^{\infty}\frac{1}{8\frac{9^{n+1}-1}{8}+1}=\sum_{n=1}^{\infty}\frac{1}{9^{n+1}-1+1} = \sum_{n=1}^{\infty}\frac{1}{9^{n+1}}$
This is an infinite geometric series with first term $\frac{1}{81}$ and common ratio $\frac{1}{9}$ . Thus, the sum is $\frac{\frac{1}{81}}{1-\frac{1}{9}}=\frac{\frac{1}{81}}{\frac{8}{9}}=\frac{9}{(81)(8)}=\frac{1}{(9)(8)}=\frac{1}{72}$ .
Thus, $p + q = 1 + 72 = \boxed{073}$ .

## Solution 2 (Engineer's Induction - not rigorous)
Manually, we can find \( D_1 = 10 \), \( D_2 = 91 \), \( D_3 = 820 \). \[ \frac{1}{8D_1+1} = \frac{1}{81}, \quad \frac{1}{8D_2+1} = \frac{1}{729}, \quad \frac{1}{8D_3+1} = \frac{1}{6561}. \] We notice that \( 81 = 9^2 \), \( 729 = 9^3 \), and \( 6561 = 9^4 \), and believe that this cannot be a coincidence. Assume \( \frac{1}{8D_n+1} = \frac{1}{9^{n+1}} \). Then this problem asks us to find the sum of a geometric series with first term \( \frac{1}{81} \) and common ratio \( \frac{1}{9} \). \[ \frac{\frac{1}{81}}{1 - \frac{1}{9}} = \frac{\frac{1}{81}}{\frac{8}{9}} = \frac{1}{72}. \] Thus, the answer is \(\boxed{73}\).

## Solution 3 (Uses first half of Solution 1)
From Solution 1, \( D_n = 10D_{n-1} - 9D_{n-2} \). From Solution 1, we also know \( D_2 = 91 \). We can manually compute \( D_1 = 10 \). Iterating backwards, \(D_0 = 1 \).
The characteristic polynomial of this recurrence is \[x^2 - 10x + 9,\] which has roots \( 1 \) and \( 9 \). Therefore, the explicit formula for \( D_n \) is: \[D_n = \alpha_1 + 9^n \alpha_2.\]
We can solve for \( \alpha_1 \) and \( \alpha_2 \) by setting \( n=0 \) and \( n=1 \) respectively. This gives the following equations: \[\alpha_1 + \alpha_2 = 1,\] \[\alpha_1 + 9\alpha_2 = 10.\]
Solving these equations, we find \[\alpha_1 = -\frac{1}{8}, \quad \alpha_2 = \frac{9}{8}.\]
Substituting these back into the explicit formula, we find \[D_n = \frac{9^{n+1} - 1}{8}.\]
Notice that \[\frac{1}{8D_{n+1} + 1} = 9^{-(n+1)}.\]
The summation asks us to find the sum of a geometric series with ratio \( \frac{1}{9} \) and first term \( \frac{1}{81} \). The sum of this series is \[\frac{\frac{1}{81}}{1 - \frac{1}{9}} = \frac{\frac{1}{81}}{\frac{8}{9}} = \frac{1}{72}.\]
Thus, the answer is $\boxed{73}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .