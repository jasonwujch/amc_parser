# 2024 AMC 10B Problem 16

## Problem

Jerry likes to play with numbers. One day, he wrote all the integers from $1$ to $2024$ on the whiteboard. Then he repeatedly chose four numbers on the whiteboard, erased them, and replaced them by either their sum or their product. (For example, Jerry's first step might have been to erase $1$ , $2$ , $3$ , and $5$ , and then write either $11$ , their sum, or $30$ , their product, on the whiteboard.) After repeatedly performing this operation, Jerry noticed that all the remaining numbers on the whiteboard were odd. What is the maximum possible number of integers on the whiteboard at that time?

$\textbf{(A) } 1010 \qquad \textbf{(B) } 1011 \qquad \textbf{(C) } 1012 \qquad \textbf{(D) } 1013 \qquad \textbf{(E) } 1014$

## Solution 1
Consider the numbers as $1,0,1,0,...,1,0$ . Note that the number of odd integers is monotonously decreasing.
We need to get rid of $1012$ $0$ 's, so we either add or multiply four $0$ s together to get $1012\rightarrow 253 \rightarrow 63+1=64 \rightarrow 16 \rightarrow 4 \rightarrow 1.$
To get rid of the final $0$ , we need to consume three other $1$ 's to result in one $1$ . Thus the answer is $1012-2=\boxed{\textbf{(A) } 1010 }$ ,
~Mintylemon66

## Solution 2
(I will denote even numbers as $e$ and odd numbers as $\normalsize o$ for the purpose of this question, and $x$ as the answer we need)
First, we observe that each time Jerry replaces four number with one (let's call this an " $operation$ "), we lose exactly three numbers regardless of the type of $operation$ ( $Additive$ or $Multiplicative$ ).
$\Rightarrow x \equiv 2024 \equiv 2\pmod3$
Already, we see that the only possible options are $\textbf{(A) } 1010$ or $\textbf{(D) } 1013$
We need there to be no $e$ 's on the board at the end, so we attempt to convert them into $\normalsize o$ while retaining as many existing $\normalsize o$ 's as possible.
Notice that converting 4 $e$ 's into an $\normalsize o$ is not possible. We can apply an $Additive \, operation$ on 3 $e$ 's and 1 $\normalsize o$ to get back 1 $\normalsize o$ ( $e+e+e+\normalsize o=\normalsize o$ ) By doing so, we retain all the $\normalsize o$ 's we use in an $operation$ (and don't generate any new ones). In the first $2024$ numbers, there are $1012$ $\normalsize o$ 's. This means that $x \le 1012$ , and the only option left is $\boxed{\textbf{(A) } 1010}$
Note: For the exact steps to arrive at 1010 odd numbers, perform
$e+e+e+o=o$ (337 times)
$e+o+o+o=o$ (1 time)
~laythe_enjoyer211
~minor edit by MathCrafter314

## Solution 3 (guessing strategy)
Notice that with every step, Jerry removes $4$ numbers and adds $1$ number to the board. Thus, $3$ numbers are removed from the board in every step. Since $2024\equiv2\pmod{3}$ , the answer choice must also be congruent to $2$ mod $3$ . Only $1010$ and $1013$ among the answer choices satisfy this condition. This alone eliminates three choices, and one can guess from here for a 3 point expected value.
However, we start out with $1012$ even numbers and $1012$ odd numbers, and it is is not possible to get more odds than there were initially (every time we add or multiply four numbers, we can only produce one odd number, which cannot occur if only even numbers are used; therefore, there cannot be more odd numbers after an operation than before it). Thus, we choose $\boxed{\textbf{(A) } 1010.}$
~Elephant200

## Solution 4 (OEEE)
There are $1012$ odd numbers and $1012$ even numbers. In order to maximize the remaining numbers, then we must minimize the number of times the operation is performed.
Since we want to be left with all odd numbers, then we must get rid of the even numbers as quick as possible, which implies $EEEE$ . This doesn't give an odd product or sum, so our next best option is $OEEE$ , which gives an odd sum.
The maximum number of times this operation can be performed with $OEEE$ is $\left\lfloor{\dfrac{1012}{3}}\right\rfloor=337$ . This will eliminate $3\cdot337=1011$ even numbers and no odd numbers (because each time the operation is performed, one odd number is eliminated but another one is created).
Therefore after the operation is performed $337$ times with $OEEE$ , there will be $1$ even number left and $1012$ odd numbers left. Performing this operation one more time with $EOOO$ will give $0$ even numbers and $\boxed{\text{(A) }1010}$ odd numbers. ~Tacos_are_yummy_1

## Solution 5 (EEEE)
There are $1012$ odd numbers and $1012$ even numbers. Our goal is to get rid of all the even numbers. By performing the operation with $EEEE$ , we will remove $4$ even numbers and create one simultaneously.
First, we can perform $EEEE$ a maximum of $\dfrac{1012}{4}=253$ times, to end up with $1012-4\cdot253+253=253$ even numbers. Performing $EEEE$ again $\left\lfloor{\dfrac{253}{4}}\right\rfloor=63$ times will result in $253-4\cdot63+63=64$ even numbers left. Repeating this process, eventually there will be $1$ even number left and still $1012$ odd numbers. Performing $OOOE$ gives the answer of $\boxed{\text{(A) }1010}$ . ~Tacos_are_yummy_1 ~ AVTV MINOR EDITS

## Solution 6 (Monovariants)
Note that the number of odd integers is monotonically decreasing, and further observe that the number of odd integers is preserved after an operation where Jerry adds three evens and one odd together, producing an odd number. To maximise the number of odd integers, we will use this operation whenever possible.
There are $1012$ even integers; to perform the specific procedure outlined above, we remove $3$ even integers each time. Therefore, we will arrive in a situation where there is $1$ even integers and $1012$ odd integers. To ensure that after the final operation, there will only be odd integers, we add the even integer and three odd integers, yielding one odd integer. There are now $1010$ integers, all of them odd, so we select $\fbox{ (A) 1010 }$ .
~LeonQS

## Monovariant Casework (Sidenote for All Solutions)
To see why the number of odd integers must monotonically decrease, we can do casework. Similarly to above solutions, represent odd integers with $O$ and even integers with $E$ . We have five different possible sums: \[E+E+E+E = E\] \[E+E+E+O = O\] \[E+E+O+O = E\] \[E+O+O+O = O\] \[O+O+O+O = E\] Note that the only sum where the number of odd integers does not decrease is $E+E+E+O = O$ . This is employed in Solution 4 and 6.
For products, using similar strategies, we observe that the only process that will not change the number of odds is $E \cdot E \cdot E \cdot E = E$ . This is used in Solution 1 and 5.
The number of odd integers can never increase beyond the original $1012$ , and we perform one of the two operations above to ensure that we do no unnecessarily remove odd integers, so as to arrive at the maximum number.
~LeonQS

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/c6nhclB5V1w?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=uKT6ormxQYE
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .