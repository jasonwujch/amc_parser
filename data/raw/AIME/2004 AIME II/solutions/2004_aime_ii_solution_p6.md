# 2004 AIME II Problem 6

## Problem

Three clever monkeys divide a pile of bananas. The first monkey takes some bananas from the pile, keeps three-fourths of them, and divides the rest equally between the other two. The second monkey takes some bananas from the pile, keeps one-fourth of them, and divides the rest equally between the other two. The third monkey takes the remaining bananas from the pile, keeps one-twelfth of them, and divides the rest equally between the other two. Given that each monkey receives a whole number of bananas whenever the bananas are divided, and the numbers of bananas the first, second, and third monkeys have at the end of the process are in the ratio $3: 2: 1,$ what is the least possible total for the number of bananas?

## Solution
Denote the number of bananas the first monkey took from the pile as $b_1$ , the second $b_2$ , and the third $b_3$ ; the total is $b_1 + b_2 + b_3$ . Thus, the first monkey got $\frac{3}{4}b_1 + \frac{3}{8}b_2 + \frac{11}{24}b_3$ , the second monkey got $\frac{1}{8}b_1 + \frac{1}{4}b_2 + \frac{11}{24}b_3$ , and the third monkey got $\frac{1}{8}b_1 + \frac{3}{8}b_2 + \frac{1}{12}b_3$ .
Taking into account the ratio aspect, say that the third monkey took $x$ bananas in total. Then,
$x = \frac{1}{4}b_1 + \frac{1}{8}b_2 + \frac{11}{72}b_3 = \frac{1}{16}b_1 + \frac{1}{8}b_2 + \frac{11}{48}b_3 = \frac{1}{8}b_1 + \frac{3}{8}b_2 + \frac{1}{12}b_3$
Solve this to find that $\frac{b_1}{11} = \frac{b_2}{13} = \frac{b_3}{27}$ . All three fractions must be integral. Also note some other conditions we have picked up in the course of the problem, namely that $b_1$ is divisible by $8$ , $b_2$ is divisible by $8$ , and $b_3$ is divisible by $72$ (however, since the denominator contains a $27$ , the factors of $3$ cancel, and it only really needs to be divisible by $8$ ). Thus, the minimal value is when each fraction is equal to $8$ , and the solution is $8(11 + 13 + 27) = \boxed{408}$ .

## Solution 2
Let the first monkey take $8x$ bananas, the second monkey take $8y$ , and the third monkey take $24z$ . I chose these numbers to make it so, when each monkey splits his bananas, they will get an integer amount of each variable. So, when the first monkey distributes his bananas, he gets $6x$ , and the other monkeys get $1x$ . So, we can make expressions for how many bananas each monkey gets. Also, the variables have to be integers too.
Monkey 1: $6x+3y+11z$
Monkey 2: $1x+2y+11z$
Monkey 3: $1x+3y+2z$
So, they are in a ratio $3:2:1$ . But, we can turn it into an equation by multiplying the amount of bananas each monkey has by 2, 3, 6. Now, the ratio is $6:6:6$ , so, $12x+6y+22z = 3x+6y+33z = 6x+18y+12z$ . Subtracting $3x+6y+12z$ from all, we get $9x+10z = 21z = 3x+12y$ . Let's split this into 3 equations.
\[9x+10z = 21z\] \[21z = 3x+12y\] \[9x+10z = 3x+12y\]
Let's look at the first equation. Rearranging, it gets us $9x = 11z$
We can rearrange the third equation, then divide by 2, then subtract the second equation. \[21z-6y = 12y-5z\] \[26z = 18y\] \[13z = 9y\] .
It is clear $z$ is a multiple of 9, so let $z = 9$ . Then we get the $x = 11$ , and $y = 13$ . Testing, we confirm this will get the first monkey 204 bananas, the second 136, and the third, 68. Adding them up, we get that there were $\boxed{408}$ bananas originally in the pile.
-AlexLikeMath

## Solution 3
In this solution, you start out the same as solution one. Convert everything into the fractions of largest denominator terms (this is necessary) until you get
$27x=11z$ $27y=13z$
While solving, make sure to leave a list of numbers that must divide $x$ , $y$ , and $z$ . For example, just by looking at the basic fractions you receive from writing the starting equations, 24 divides $z$ , 8 divides $y$ and $x$ . In the expression above, it's also clear that 27 divides $z$ , 13 divides $y$ , and 11 divides $z$ . You might be wondering why I wrote the expression in terms of z. That's because $z$ has the largest divisor. The LCM of all it's divisors shows that $z$ must be divisible by 216. The total amount of bananas can be found to equal to $17z/9$ . This means there are two possible solutions under 1000: 408 and 816. Trial and error can be done quickly to find the smallest possible solution to be $\boxed{408}$ .
-jackshi2006

## Solution 4 (No Thinking Required)
Let $A,B,C$ be the fraction of bananas taken by the first, second, and third monkeys respectively. Then we have the system of equations \[\frac{3}{4}A+\frac{3}{8}B+\frac{11}{24}C=\frac{1}{2}\] \[\frac{1}{8}A+\frac{1}{4}B+\frac{11}{24}C=\frac{1}{3}\] \[\frac{1}{8}A+\frac{3}{8}B+\frac{2}{24}C=\frac{1}{6}.\] Solve this your favorite way to get that \[(A,B,C)=\left( \frac{11}{51}, \frac{13}{51}, \frac{9}{17} \right).\] We need the amount taken by the first and second monkeys to be divisible by 8 and the third by 24 (but for the third, we already have divisibility by 9). Thus our minimum is $8 \cdot 51 = \boxed{408}.$
~Dhillonr25
These problems are copyrighted © by the Mathematical Association of America.