# 2017 AIME I Problem 5

## Problem

A rational number written in base eight is $\underline{ab} . \underline{cd}$ , where all digits are nonzero. The same number in base twelve is $\underline{bb} . \underline{ba}$ . Find the base-ten number $\underline{abc}$ .

## Solution 1
First, note that the first two digits will always be a positive number. We will start with base twelve because of its repetition. List all the positive numbers in base eight that have equal tens and ones digits in base 12.
$11_{12}=15_8$
$22_{12}=32_8$
$33_{12}=47_8$
$44_{12}=64_8$
$55_{12}=101_8$
We stop because we only can have two-digit numbers in base 8 and 101 is not a 2 digit number. Compare the ones places to check if they are equal. We find that they are equal if $b=2$ or $b=4$ . Evaluating the places to the right side of the decimal point gives us $22.23_{12}$ or $44.46_{12}$ . When the numbers are converted into base 8, we get $32.14_8$ and $64.30_8$ . Since $d\neq0$ , the first value is correct. Compiling the necessary digits leaves us a final answer of $\boxed{321}$

## Solution 2
The parts before and after the decimal points must be equal. Therefore $8a + b = 12b + b$ and $c/8 + d/64 = b/12 + a/144$ . Simplifying the first equation gives $a = (3/2)b$ . Plugging this into the second equation gives $3b/32 = c/8 + d/64$ . Multiplying both sides by 64 gives $6b = 8c + d$ . $a$ and $b$ are both digits between 1 and 7 (they must be a single non-zero digit in base eight) so using $a = 3/2b$ , $(a,b) = (3,2)$ or $(6,4)$ . Testing these gives that $(6,4)$ doesn't work, and $(3,2)$ gives $a = 3, b = 2, c = 1$ , and $d = 4$ . Therefore $abc = \boxed{321}$

## Solution 3
Converting to base $10$ we get
$4604a+72c+9d=6960b$
Since $72c$ and $9d$ are much smaller than the other two terms, dividing by $100$ and approximating we get
$46a=70b$
Writing out the first few values of $a$ and $b$ , the first possible tuple is
$a=3, b=2, c=1, d=4$
and the second possible tuple is
$a=6, b=4, c=3, d=0$
Note that $d$ can not be $0$ , therefore the answer is $\boxed{321}$
By maxamc

## Solution 4 (modular congruency/nt bash)
In the problem, we are given that \[8a+b+\dfrac c8+\dfrac d{64}=12b+b+\dfrac b{12}+\dfrac a{144}.\] We multiply by the LCM of the denominators, which is $576$ to get \[4608a+576b+72c+9d=6912b+576b+48b+4a.\] We then group like terms and factor to get \[4604a+72c+9d=48b(144+1)=145\cdot48b=24\cdot290b.\]
Observe that the coefficients of $a$ , $c$ , and $b$ are all divisible by $4$ . Therefore, we know that $d$ must also be divisible by $4$ to compensate. (To observe this, one could rearrange the terms to see $9d=24\cdot290b-4604a-72c=4(6\cdot290b-1151a-18c)$ . At this point, it is obvious that $9d$ must be divisible by $4$ , so $d$ must be divisible by $4$ .) Thus, we let $d=4y$ to see $4604a+72c+9\cdot4y=24\cdot290b$ . We divide by $4$ in the equation to get \[1151a+18c+9y=6\cdot290b.\]
Observe that the coefficients of $c$ , $y$ , and $b$ are all divisible by $3$ . By similar reasoning, $a$ must be divisible by $3$ , so we let $a=3x$ . Substituting and dividing by $3$ , we get \[1151x+6c+3y=2\cdot290b.\] We observe that this can no longer be reduced by similar means.
We know that $0<a,b,c<8\implies0<3x,b,4y<8$ . We examine $0<4y<8$ ; this becomes $0<y<2$ . It is apparent that $y=1\implies d=4$ . However, the problem does not even ask for $d$ , so it may appear that this find is meaningless. However, we substitute our value of $y$ in to get \[1151x+6c+3=580b.\]
We know that $x$ is either $1$ or $2$ , since $0<3x<8$ . We take our equation modulo $6$ to find \[5x+3\equiv4b\pmod{6}\implies3\equiv4b+x\pmod{6}.\] If $x=2$ , then $1\equiv4b\pmod{6}$ - this is equivalent to saying that $1+6n=4b\implies 1=4b-6n$ . However, $4b-6n$ is always even, and $1$ is odd. Thus, this case is not possible, so $x=1\implies a=3$ . We know that $x=1$ ; thus, $3\equiv4b+1\pmod{6}\implies2\equiv4b\pmod{6}\implies1\equiv2b\pmod{3}$ . Obviously, $b=2$ and $b=5$ work; however, if $b=5$ , then the RHS of our original equation ( $2\cdot290b$ ) is much too large to be equal to the LHS (the maximum possible value of the LHS is $1151\cdot1+6\cdot7+3\cdot1$ , which is less than $1200$ while the RHS would become $2\cdot290\cdot5=2900$ ), so we have $b=2$ .
We recall our equation of $1151x+6c+3=580b$ . Plugging in what we know, we have $1151\cdot1+6c+3=580\cdot2\implies6c=6\implies c=1$ .
Therefore, $\overline{abc}=\boxed{321}$ .
by Technodoggo
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .