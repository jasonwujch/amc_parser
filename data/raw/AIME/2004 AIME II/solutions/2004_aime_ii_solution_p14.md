# 2004 AIME II Problem 14

## Problem

Consider a string of $n$ $7$ 's, $7777\cdots77,$ into which $+$ signs are inserted to produce an arithmetic expression . For example, $7+77+777+7+7=875$ could be obtained from eight $7$ 's in this way. For how many values of $n$ is it possible to insert $+$ signs so that the resulting expression has value $7000$ ?

## Solution 1
Suppose we require $a$ $7$ s, $b$ $77$ s, and $c$ $777$ s to sum up to $7000$ ( $a,b,c \ge 0$ ). Then $7a + 77b + 777c = 7000$ , or dividing by $7$ , $a + 11b + 111c = 1000$ . Then the question is asking for the number of values of $n = a + 2b + 3c$ .
Manipulating our equation, we have $a + 2b + 3c = n = 1000 - 9(b + 12c) \Longrightarrow 0 \le 9(b+12c) < 1000$ . Thus the number of potential values of $n$ is the number of multiples of $9$ from $0$ to $1000$ , or $112$ .
However, we forgot to consider the condition that $a \ge 0$ . For a solution set $(b,c): n=1000-9(b+12c)$ , it is possible that $a = n-2b-3c < 0$ (for example, suppose we counted the solution set $(b,c) = (1,9) \Longrightarrow n = 19$ , but substituting into our original equation we find that $a = -10$ , so it is invalid). In particular, this invalidates the values of $n$ for which their only expressions in terms of $(b,c)$ fall into the inequality $9b + 108c < 1000 < 11b + 111c$ .
For $1000 - n = 9k \le 9(7 \cdot 12 + 11) = 855$ , we can express $k$ in terms of $(b,c): n \equiv b \pmod{12}, 0 \le b \le 11$ and $c = \frac{n-b}{12} \le 7$ (in other words, we take the greatest possible value of $c$ , and then "fill in" the remainder by incrementing $b$ ). Then $11b + 111c \le 855 + 2b + 3c \le 855 + 2(11) + 3(7) = 898 < 1000$ , so these values work.
Similarily, for $855 \le 9k \le 9(8 \cdot 12 + 10) = 954$ , we can let $(b,c) = (k-8 \cdot 12,8)$ , and the inequality $11b + 111c \le 954 + 2b + 3c \le 954 + 2(10) + 3(8) = 998 < 1000$ . However, for $9k \ge 963 \Longrightarrow n \le 37$ , we can no longer apply this approach.
So we now have to examine the numbers on an individual basis. For $9k = 972$ , $(b,c) = (0,9)$ works. For $9k = 963, 981, 990, 999 \Longrightarrow n = 37, 19, 10, 1$ , we find (using that respectively, $b = 11,9,10,11 + 12p$ for integers $p$ ) that their is no way to satisfy the inequality $11b + 111c < 1000$ .
Thus, the answer is $112 - 4 = \boxed{108}$ .
A note: Above, we formulated the solution in a forward manner (the last four paragraphs are devoted to showing that all the solutions we found worked except for the four cases pointed out; in a contest setting, we wouldn't need to be nearly as rigorous). A more natural manner of attacking the problem is to think of the process in reverse, namely seeing that $n \equiv 1 \pmod{9}$ , and noting that small values of $n$ would not work.
Looking at the number $7000$ , we obviously see the maximum number of $7's$ : a string of $1000 \ 7's$ . Then, we see that the minimum is $28 \ 7's: \ 777*9 + 7 = 7000$ . The next step is to see by what interval the value of $n$ increases. Since $777$ is $3 \ 7's, \ 77*10 + 7$ is $21 \ 7's$ , we can convert a $777$ into $77's$ and $7's$ and add $18$ to the value of $n$ . Since we have $9 \ 777's$ to work with, this gives us $28,46,64,82,100,118,136,154,172,190 ( = 28 + 18n | 1\leq n\leq 9)$ as values for $n$ . Since $77$ can be converted into $7*11$ , we can add $9$ to $n$ by converting $77$ into $7's$ . Our $n = 190$ , which has $0 \ 777's \ 90 \ 77's \ 10 7's$ . We therefore can add $9$ to $n \ 90$ times by doing this. All values of $n$ not covered by this can be dealt with with the $n = 46 \ (8 \ 777's \ 10 \ 77's \ 2 \ 7's)$ up to $190$ .

## Solution 2
To simplify, replace all the $7$ ’s with $1$ ’s. Because the sum is congruent to $n \pmod 9$ and \[1000 \equiv 1 \pmod 9 \implies n \equiv 1 \pmod 9\] Also, $n \leq 1000$ . There are $\big\lfloor \tfrac{1000}{9} \big\rfloor + 1 = 112$ positive integers that satisfy both conditions i.e. $\{1, 10, 19, 28, 37, 46, . . . , 1000\}.$
For $n = 1, 10, 19$ , the greatest sum that is less than or equal to $1000$ is \[6 \cdot 111 + 1 = 667 \implies 112-3 = 109.\]
Thus $n \geq 28$ and let $S = \{28, 37, 46, . . . , 1000\}$ .
Note that $n=28$ is possible because $9 \cdot 111+1 \cdot 1 = 1000$ .
When $n = 37$ , the greatest sum that is at most $1000$ is $8 \cdot 111+6\cdot 11+1 \cdot 1 = 955$ .
All other elements of $S$ are possible because if any element $n$ of $S$ between $46$ and $991$ is possible, then $(n+ 9)$ must be too.
$\textbf{Case 1:}$ Sum has no $11$ 's
It must have at least one $1$ . If it has exactly one $1$ , there must be nine $111$ ’s and $n = 28$ . Thus, for $n \geq 46$ , the sum has more than one $1$ , so it must have at least $1000 - 8 \cdot 111 = 112$ number of $1$ ’s. For $n \leq 1000$ , at least one $111$ . To show that if $n$ is possible, then $(n + 9)$ is possible, replace a $111$ with $1 + 1 + 1$ , replace eleven $(1 + 1)$ ’s with eleven $11$ ’s, and include nine new $1$ ’s as $+1$ ’s. The sum remains $1000$ .
$\textbf{Case 2:}$ Sum has at least one $11$ .
Replace an $11$ with $1 + 1$ , and include nine new $1$ ’s as $+1$ ’s. Now note that $46$ is possible because $8 \cdot 111 + 10 \cdot 11 + 2 \cdot 1 = 1000$ . Thus all elements of $S$ except $37$ are possible.
Thus there are $\boxed{108}$ possible values for $n$ .
~phoenixfire

## Solution 3
It's obvious that we cannot have any number $\ge 7777$ because $7777 > 7000$ so the max number that an occur is $777$
Let's say we have $a$ 777's , $b$ 77's and $c$ 7's
From here we get our required equation as $777a + 77b + 7c = 7000$
Now comes the main problem , one might think that if we find number of $(a,b,c)$ then we're done , but in reality we are over-counting our number of $n$ 's. This is because $n$ is the total number of 7's and from our equation we'll get $n$ as $3a + 2b + c$ (because there are three 7's , two 7's and one 7)
The reason why we're over-counting is because , say $a_1 , b_1 , c_1$ be a solution of our original equation and $a_2 , b_2 , c_2$ be another solution of our original equation , then there can be a possibility that $3a_1 + 2b_1 + c_1 = 3a_2 + 2b_2 + c_2$ where $a_1 \neq a_2 , b_1 \neq b_2 , c_1 \neq c_2$ (example : $2 + 3 + 4 = 1 + 5 + 3$ but $2 \neq 1 , 3 \neq 5 , 4 \neq 3$
We know that $0 \le a \le 9$ , $0 \le b \le 90$ , $0 \le c \le 1000$ The bound on $a$ is easier to handle with , so lets start putting values on $a$ and calculate $b , c , n$ by making cases
Reduced equation : $111a + 11b + c = 1000$
Case 1 : $a = 9$
We get $11b + c = 1 \implies b = 0 , c = 1$ is our only solution thus only $\boxed{1}$ value of $n$
Case 2 : $a = 8$
We get $11b + c = 112 \implies b = 0,1,2,\cdots ,10$ and $c = 112 , 101 , 90,\cdots ,2$ From here we get different $n$ 's as $24 + 112 , 24 + 103 , 24 + 94, \cdots ,24 + 22$ (remember $n = 3a + 2b + c$ and if you have difficulty in understanding how we got $n = 24 + (\cdots)$ then just put the values of $a,b,c$ i am sure you will get it :) )
Let's write the sequences of $n$ 's in a compact form , $T_p = 24 + 22 + 9(p-1)$ (This will be helpful later on) There are $\boxed{11}$ values of $n$
Case 3 : $a = 7$
We get $11b + c = 223 \implies b=0,1,2, \cdots ,20$ and $c = 223,212,201, \cdots ,3$ From here we get different $n$ 's as $21 + 223, 21 + 214 , 21 + 205, \cdots ,21 + 43$
Let's also write the sequences of $n$ 's in a compact form , $T_q = 21 + 43 + 9(q-1)$
Now comes the major part , since we need to find distinct $n$ 's so let's subtract the cases where we find common values , from the total number of values.
To do this we need to make $T_p = T_q \implies p - q = 2$ (after some calculations you'll get $p - q = 2$ ) . Now we know that $0 \le p \le 10$ and $0 \le q \le 20$ so we get $p$ as $10,9,\cdots,2$ and $q$ as $8,7,\cdots,0$ so there are 9 common solutions out of 21(diff values of $q$ ) total , so there are $\boxed{21 - 9}$ values of $n$
Case 4 : $a = 6$
We get $11b + c = 334 \implies b = 0,1,2, \cdots ,30$ and $c = 334,323,312, \cdots ,4$ From here we get the different $n$ 's as $18 + 334,18 + 325,18 + 316, \cdots ,18 + 64$
Compact form of terms is $T_r = 18 + 64 + 9(r-1)$ Now let's repeat the process of eliminating common solutions (one thing to notice is that we've removed common solutions of case 2 from case 3 so if we check case 4 with case 3 we'll remove common solutions from all previous cases and hence we do not have to handle common solutions of case 4 with case 2,1 and in general case X with case X-2,X-3,...2,1 , {basically means checking case X with case X-1 is enough})
$T_q = T_r \implies 21 + 43 + 9(q-1) = 18 + 64 + 9(r-1) \implies q - r = 2$ $\implies q = 20,19,18, \cdots ,2$ and $r = 18,17,16, \cdots ,0$ so there are 19 common solutions out of 31 (diff values of r) so there are $\boxed{31 - 19}$ values of $n$
Now hopefully you've seen a pattern , if not try another case 5 with $a = 5$ you'll get $\boxed{41 - 29}$ values of $n$
Like this we get the value of "distinct" $n$ by summing all the sub-values from the cases that we've solved.
$n = 1 + 11 + (21 - 9) + (31 - 19) + (41 - 29) + \cdots + (91 - 79)$
$\implies n = (1 + 11 + 21 + 31 + 41 + \cdots + 91) - (0 + 0 + 9 + 19 + 29 + \cdots + 79)$
$\implies \boxed{n = 108}$
~MrOreoJuice

## Solution 4 (Construction, not counting)
First, we note that by the sun of digits and modulo 9 formula, $n \equiv 1000 \equiv 1 \pmod {9}$ . Obviously, $1000 = 111+111+111+111+111+111+111+111+111+1$ with $n=28$ is the smallest possible $n$ . Now, $111=10 \cdot 11 +1$ , $11= 11 \cdot 1$ . The first equation applied on a representation with $n$ 1's (i.e. replacing a $111$ , if available, with 10 $11$ 's and one 1) will increase $n$ by 18, while the second equation applied onto a representation will increase $n$ by 9 only. Thus, there are representations of $n= 46,55,64, \dots , 1000$ , since for $46$ we can just replace a $111$ in $n=28$ representation with 10 $11$ 's and one 1, and for the rest we use the first equation $111= 10 \cdot 11 +1$ to "increase the range" and the second equation to "fill in the gaps" of the first equation. Essentially we use the first equation for every other multiple of nine and the second for the other multiples of nine and for once the $111$ 's run out. Next, obviously $n=1000$ is the maximum $n$ one can achieve. Thus, the solutions $n=28,46,55,64, \dots ,1000$ is all the solutions (one can check there are $\boxed{108}$ ) if we can show $37$ is impossible. But it is, since $a+b+c=37, 111a+11b+c=1000$ have no Diophantine solution, so we're done.
~ Ddk001
Alternate solutions are always welcome. If you have a different, elegant solution to this problem, please add it to this page.
These problems are copyrighted © by the Mathematical Association of America.