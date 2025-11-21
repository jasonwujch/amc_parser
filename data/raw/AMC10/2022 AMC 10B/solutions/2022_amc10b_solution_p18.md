# 2022 AMC 10B Problem 18

## Problem

Consider systems of three linear equations with unknowns $x$ , $y$ , and $z$ , \begin{align*} a_1 x + b_1 y + c_1 z & = 0 \\ a_2 x + b_2 y + c_2 z & = 0 \\ a_3 x + b_3 y + c_3 z & = 0 \end{align*} where each of the coefficients is either $0$ or $1$ and the system has a solution other than $x=y=z=0$ . For example, one such system is \[\{ 1x + 1y + 0z = 0, 0x + 1y + 1z = 0, 0x + 0y + 0z = 0 \}\] with a nonzero solution of $\{x,y,z\} = \{1, -1, 1\}$ . How many such systems of equations are there? (The equations in a system need not be distinct, and two systems containing the same equations in a different order are considered different.)

$\textbf{(A)}\ 302 \qquad\textbf{(B)}\ 338 \qquad\textbf{(C)}\ 340 \qquad\textbf{(D)}\ 343 \qquad\textbf{(E)}\ 344$

## Solution 1 (Casework)
Let $M_1=\begin{bmatrix}a_1 & b_1 & c_1\end{bmatrix}, M_2=\begin{bmatrix}a_2 & b_2 & c_2\end{bmatrix},$ and $M_3=\begin{bmatrix}a_3 & b_3 & c_3\end{bmatrix}.$
We wish to count the ordered triples $(M_1,M_2,M_3)$ of row matrices. We perform casework:
1. $M_1=M_2=M_3.$
1. Exactly two of $M_1,M_2,$ and $M_3$ are equal.
1. All of $M_1,M_2,$ and $M_3$ are different.
There are $2^3=8$ options for $M_1.$ Once $M_1$ is chosen, $M_2$ and $M_3$ are uniquely determined.
In this case, we have ordered triples
For $M_1=M_2\neq M_3,$ there are $2^3=8$ options for $M_1.$ Once $M_1$ is chosen, $M_2$ is uniquely determined, and $M_3$ has $2^3-1=7$ options. So, there are $8\cdot7=56$ ordered triples $(M_1,M_2,M_3).$
Similarly, for each of $M_1=M_3\neq M_2$ and $M_2=M_3\neq M_1,$ there are $56$ ordered triples $(M_1,M_2,M_3).$
In this case, we have ordered triples
There are two subcases:
1. Exactly one of $M_1,M_2,$ and $M_3$ is $\begin{bmatrix}0 & 0 & 0\end{bmatrix}.$
1. The sum of two of $M_1,M_2,$ and $M_3$ is equal to the third matrix.
For $M_1=\begin{bmatrix}0 & 0 & 0\end{bmatrix},$ there are $2^3-1=7$ options for $M_2$ and $2^3-2=6$ options for $M_3.$ So, there are $7\cdot6=42$ ordered triples $(M_1,M_2,M_3).$
Similarly, for each of $M_2=\begin{bmatrix}0 & 0 & 0\end{bmatrix}$ and $M_3=\begin{bmatrix}0 & 0 & 0\end{bmatrix},$ there are $42$ ordered triples $(M_1,M_2,M_3).$
In this subcase, we have ordered triples
For $M_1+M_2=M_3:$
- If $M_1=\begin{bmatrix}1 & 0 & 0\end{bmatrix},$ then $M_2\in\{\begin{bmatrix}0 & 1 & 1\end{bmatrix},\begin{bmatrix}0 & 1 & 0\end{bmatrix},\begin{bmatrix}0 & 0 & 1\end{bmatrix}\}.$
- If $M_1=\begin{bmatrix}1 & 1 & 0\end{bmatrix},$ then $M_2=\begin{bmatrix}0 & 0 & 1\end{bmatrix}.$
More generally, if $M_1$ consists of one $1$ and two $0$ 's, then $M_2$ has $3$ options, and $M_3$ is uniquely determined. So, there are $\binom31\cdot3=9$ ordered triples $(M_1,M_2,M_3).$
More generally, if $M_1$ consists of two $1$ 's and one $0,$ then $M_2$ and $M_3$ are uniquely determined. So, there are $\binom32=3$ ordered triples $(M_1,M_2,M_3).$
There are $9+3=12$ ordered triples $(M_1,M_2,M_3).$
Similarly, for each of $M_1+M_3=M_2$ and $M_2+M_3=M_1,$ there are $12$ ordered triples $(M_1,M_2,M_3).$
In this subcase, we have ordered triples
Together, the answer is $8+168+126+36=\boxed{\textbf{(B)}\ 338}.$
~MRENTHUSIASM

## Solution 2
Let $n$ V represent an equation in the system with $n$ variables. There are $2^9 = 512$ total possible systems (each coefficient can either be $0$ or $1$ ). We will subtract off the invalid ones (the equations with solution $x = y = z = 0$ ) using casework.
We have $1$ case of selecting a 3-variable, 2-variable, and 1-variable equation, $6$ cases of selecting two $n$ -variable equations and one different $m$ -variable equation, and $3$ cases of selecting 3 of the same $m$ -variable equations. However, we can't pick two 3-variable equations in our system because then it's impossible to get to the solution $x = y = z = 0.$ So there are $3$ invalid cases. Then we need to look for a total of $1 + 6 + 3 - 3 = 7$ different cases. (Doing this beforehand makes sure we don’t accidentally skip a case.)
Case 1: 3V-2V-2V: WLOG say we have $x + y + z = 0$ , $y + z = 0$ , and $x + y = 0$ . We are choosing two variables out of the 3 to be in the second equation, and we have 1 choice for the third. There are 6 ways to rearrange them. In total we get $6 \times \binom{3}{2} = 18$ systems for this case.
Case 2: 1V-1V-1V: When we have $x = 0$ , $y = 0$ , and $z = 0$ . There are 6 systems for this case.
Case 3: 2V-1V-1V: We have 3 choices for the first equation: $x + y = 0$ , $y + z = 0$ , or $x + z = 0$ . WLOG if $x + z = 0$ is the first equation, the second equation can either be $x = 0$ or $z = 0$ , and the third equation must be $y = 0$ . So we have 2 choices for the second equation and 1 choice for the third. $6 \times 3 \times 2$ gives us 36 systems for this case.
Case 4: 3V-2V-1V: There is obviously one choice for the first equation ( $x + y + z = 0$ ). For the second equation, we can choose any 2 of the 3 variables (in 3 ways). For the third, we must choose one of the two variables we included in our second equation (in 2 ways). In total, we get $6 \times 3 \times 2 = 36$ systems for this case.
Case 5: 2V-2V-2V: There is only 1 combination of equations: $x + y = 0$ , $y + z = 0$ , and $x + z = 0$ . These can be rearranged in 6 ways, giving us 6 systems.
Case 6: 3V-1V-1V: Again, there's only one choice for the first equation ( $x + y + z = 0$ ). For the second and third, we can choose any two of the three variables in 3 ways, giving us $6 \times 3 = 18$ systems.
Case 7: 2V-2V-1V: We want to choose a variable to appear twice in both of the two variable equations. This can be done in 3 ways. The second equation will be the variable appearing twice added to the variable left out of the first (so only 1 choice), and 3 choices for the one variable equation. The system can be rearranged in 6 ways. This gives us $6 \times 3 \times 3 = 54$ systems.
Our final answer is $512 - (18 + 6 + 36 + 36 + 6 + 18 + 54) = \boxed{\textbf{(B)}\ 338}.$
~ grogg007

## Solution 3 (Complementary Counting)
We will use complementary counting and do casework on the equations.
There are $8$ possible equations:
Equation 1: $0 = 0$
Equation 2: $x = 0$
Equation 3: $y = 0$
Equation 4: $z = 0$
Equation 5: $x + y = 0$
Equation 6: $x + z = 0$
Equation 7: $y + z = 0$
Equation 8: $x + y + z = 0$
We will continue to refer to the equations by their number on this list.
$8^3 = 512$ total systems. Note that no two equations by themselves can force $x = y = z = 0$ . Therefore no system with Equation 1 or with repeated equations can force $x = y = z = 0$ .
Case 1: Equation 8 ( $x + y + z = 0$ ) is present.
Case 1a: Equation 8, and two equations from $\{5, 6, 7\}$ .
There are $\binom{3}{2} = 3$ ways to choose two equations from $\{5, 6, 7\}$ and $3! = 6$ ways to arrange each case. The number of options that force $x = y = z = 0$ is $3 \cdot 3! = 18$ .
Case 1b: Equation 8, one equation from $\{5, 6, 7\}$ , and one equation from $\{2, 3, 4\}$ .
There are $\binom{3}{1} = 3$ ways to choose one equation from $\{5, 6, 7\}$ . WLOG let us choose Equation 7. Given $x + y + z = 0$ and $y + z = 0$ , we conclude that $x = 0$ . The third equation can be either $y = 0$ or $z = 0$ . There are $3!$ ways to arrange each case. The number of options that force $x = y = z = 0$ is $3 \cdot 2 \cdot 3! = 36$ .
Case 1c: Equation 8, and two equations from $\{2, 3, 4\}$ .
There are $\binom{3}{2} = 3$ ways to choose two equations from $\{2, 3, 4\}$ and $3! = 6$ ways to arrange each case. Each of these cases forces $x = y = z = 0$ . $3 \cdot 3! = 18$ total options.
Case 2: Equation 8 is $\textbf{not}$ present, at least one equation from $\{5, 6, 7\}$ is present.
Case 2a: Equations $\{5, 6, 7\}$ are all present.
There are $3!$ ways to arrange the three equations. $6$ options.
Case 2b: Two equations from $\{5, 6, 7\}$ are present. One equation from $\{2, 3, 4\}$ is present.
There are $\binom{3}{2}$ ways to choose two equations from $\{5, 6, 7\}$ . WLOG let Equations 5 and 6 be in our system: $x + y = 0$ and $x + z = 0$ . Any equation from $\{2, 3, 4\}$ will force $x = y = z = 0$ . There are $3!$ ways to arrange the equations. The number of options that force $x = y = z = 0$ is $\binom{3}{2} \cdot \binom{3}{1} \cdot 3! = 54$ .
Case 2c: One equation from $\{5, 6, 7\}$ is present. Two equations from $\{2, 3, 4\}$ are present.
There are $\binom{3}{1}$ ways to choose one equation from $\{5, 6, 7\}$ . WLOG let Equation 5 ( $x + y = 0$ ) be present. One of the two equations from $\{2, 3, 4\}$ must be Equation 4, $z = 0$ , since it is the only equation that restricts $z$ . The last equation can be either 2 or 3. There are $3!$ ways to arrange the equations. The number of options that force $x = y = z = 0$ is $\binom{3}{1} \cdot \binom{2}{1} \cdot 3! = 36$ .
Case 3: Only equations $\{2, 3, 4\}$ are present.
There are $3!$ ways to arrange the three equations. $6$ options.
We add up the cases: $18 + 36 + 18 + 6 + 54 + 36 + 6 = 174$ total systems force $x = y = z = 0$ . Thus $512 - 174 = \boxed{\textbf{(B)}\ 338}$ do not.
~numerophile

## Solution 4 (Complementary Counting)
The total number of possible systems is $2^9 = 512$ , with $8$ possible sets of coefficients per equation. We will use complementary counting to find the number of systems which only have the solution $(0, 0, 0)$ and subtract that from the total. Similar to what is observed in Solution 3, if any equation is repeated or $0x + 0y + 0z = 0$ , there will only be two or fewer equations for three variables, making one unique solution impossible. Therefore, we must choose $3$ different equations from $7$ possible ones, giving $7 \cdot 6 \cdot 5 = 210$ systems. However, there are two exceptions to consider, which will have more than one solution. The first is of the form $x + y + z = 0$ , $x + y = 0$ , $z = 0$ ; the second is of the form $x = 0$ , $y = 0$ , $x + y = 0$ . In both cases, there are $3$ ways to choose the variables in the equations, and then $6$ ways to arrange them, giving $2 \cdot 3 \cdot 6 = 36$ exceptions. Subtracting this gives $210 - 36 = 174$ systems with only one solution, and the answer is then $512 - 174 = \boxed{\textbf{(B)}\ 338}$ .
~phillipzeng

## Solution 5 (Complementary Counting, Linear Dependence, Vector Analysis)
Denote vector $\overrightarrow{i} = \left( i_1, i_2, i_3 \right)^T$ for $i \in \left\{ a, b, c \right\}$ . Thus, we need to count how many vector tuples $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ are linearly dependent.
We do complementary counting.
First, the total number of vector tuples $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ is $\left( 2^3 \right)^3 = 512$ .
Second, we count how many many vector tuples $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ are linearly independent.
To meet this condition, no vector can be a zero vector $\overrightarrow{0} = \left( 0, 0, 0 \right)^T$ .
Next, we do the casework analysis.
Case $1^c$ : Three vectors are all on axes.
In this case, the number of $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ is $3!$ .
Case $2^c$ : Two vectors are on axes and the third vector is not.
We construct such an instance in the following steps.
Step 1: We determine which two vectors lie on axes.
The number of ways is $3$ .
Step 2: For two vectors selected in Step 1, we determine which two axes they lie on.
The number of ways is $3 \cdot 2$ .
Step 3: For the third unselected vector, we determine its value.
To make three vectors linear independent, the third vector cannot be on the plane formed by the first two vectors. So the number of ways is $3$ .
Following from the rule of product, the number of $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ in this case is $3 \cdot 3 \cdot 2 \cdot 3$ .
Case $3^c$ : One vector is on an axis and the other two are not.
We construct such an instance in the following steps.
Step 1: We determine which vector lies on an axis.
The number of ways is $3$ .
Step 2: For the selected vector, we determine which axis it lies on.
The number of ways is $3$ .
Step 3: We determine the values of the two unselected vectors.
First, to be linearly independent, these two vectors are distinct. Second, to be linearly independent, we cannot have one vector $(1,1,1)$ and another one that is a diagonal vector on the plane that is perpendicular to the first selected vector.
Thus, the number or ways in this step is $4 \cdot 3-2 = 10$ .
Following from the rule of product, the number of $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ in this case is $3 \cdot 3 \cdot 10$ .
Case $(4.4)^c$ : No vector is on any axis.
In this case, any three distinct vectors are linearly independent. So the number of $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ in this case is $4 \cdot 3 \cdot 2$ .
Putting all cases together, the number of vector tuples $\left( \overrightarrow{a} , \overrightarrow{b} , \overrightarrow{c} \right)$ that are linearly independent is \[ 8^3 - 3! - 3 \cdot 3 \cdot 2 \cdot 3 - 3 \cdot 3 \cdot 10 - 4 \cdot 3 \cdot 2 = \boxed{\textbf{(B)}\ 338}. \] ~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 6 (Casework, but more intuitive)
Case 1: At least one of the equations is $0=0$ . By complementary counting, there are $512-343=\boxed{169}$ possible systems which satisfy this condition.
Case 2: Exactly 2 of the equations are equal. By directly counting, we have $\tbinom{3}{2} \cdot 7 \cdot 6=\boxed{126}$ , where there is $\tbinom{3}{2}$ places to put the two identical equations, and $7,6$ ways to choose the nonzero equations.
Case 3: The sum of two different equations is equal to the last equation. The equation which serves as the total sum of the other two can either be $x+y,x+z,y+z,$ which each have $1$ way respectively to pick a set of equations, and $x+y+z$ has $3$ ways to pick a set of equations. Then, we have $6 \cdot 6=\boxed{36}$ for this case accounting for permutations.
Case 4: All 3 of the equations are equal. There are $2^3-1=\boxed{7}$ systems which satisfy this case (they cannot all be $0$ because it's already counted in Case 1).
Thus, there are $169+126+36+7=\boxed{\textbf{(B)}\ 338}$ total ways to pick such a system.
~SirAppel

## Video Solution
https://youtu.be/pDYFn26LND0
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by OmegaLearn Using Casework
https://youtu.be/caM35PDT0bM
~ pi_is_3.14

## Video Solution by Interstigation
https://youtu.be/Z9qYTUEn3Ig
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .