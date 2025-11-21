# 2025 AIME I Problem 15

## Problem

Let $N$ denote the number of ordered triples of positive integers $(a, b, c)$ such that $a, b, c \leq 3^6$ and $a^3 + b^3 + c^3$ is a multiple of $3^7$ . Find the remainder when $N$ is divided by $1000$ .

## Solution
First, state the LTE Lemma for $p = 3, n = 3$ , which we might use.
Then we classify all cube numbers $\mod{3^7}$
Summarized the results:
We do the final combinatorial problem.
Total is $(3+6+2+4)3^{10}=15\times 3^{10}$ .
$3^5 = 243 \equiv 43 \mod{200},43^2=1600+240+9\equiv49\mod{200}$
Hence $15\times3^{10}\equiv15\times49\equiv735\mod{1000}$
Answer is $\boxed{735}$ .
~ Rakko12

## Solution 2 [Note: I think this solution has a critical flaw]
We are given that $N = \#\{(a,b,c) \in [1,3^6]^3 : 3^7 \mid (a^3+b^3+c^3)\},$ and we wish to compute the remainder when \(N\) is divided by 1000.
Since \(3^6=729\) and \(3^7=2187\), the variables \(a\), \(b\), and \(c\) range over the set \(\{1,2,\dots,729\}\).
A standard approach is to use exponential sums to detect the divisibility condition. For any integer \(n\) we have the identity $\frac{1}{3^7}\sum_{t=0}^{3^7-1} e^{\frac{2\pi i\,t\,n}{3^7}} = \begin{cases} 1, & \text{if } 3^7\mid n,\\[1mm] 0, & \text{otherwise.} \end{cases}$ \[\] Thus, we can write $N = \frac{1}{3^7}\sum_{t=0}^{3^7-1} \sum_{a=1}^{3^6} e^{\frac{2\pi i\,t\,a^3}{3^7}} \sum_{b=1}^{3^6} e^{\frac{2\pi i\,t\,b^3}{3^7}} \sum_{c=1}^{3^6} e^{\frac{2\pi i\,t\,c^3}{3^7}}.$ Define $S(t)=\sum_{a=1}^{3^6} e^{\frac{2\pi i\,t\,a^3}{3^7}}.$ Then, $N=\frac{1}{3^7}\sum_{t=0}^{3^7-1} \bigl(S(t)\bigr)^3.$
$\medskip$
Notice that when \(t=0\) we have $S(0)=\sum_{a=1}^{3^6} 1=3^6.$ Thus, the \(t=0\) term contributes $\frac{1}{3^7}(3^6)^3 = \frac{3^{18}}{3^7}=3^{11}.$
It turns out that for \(t\not\equiv 0\pmod{3^7}\), one can show (using properties of cubic residues modulo \(3^7\)) that $S(t)=0.$ [ Note: I don't believe this is true. Try it manually for the modulo case. ]
Therefore, only the \(t=0\) term contributes to the sum, and we obtain $N=3^{11}.$
Since $3^{11}=177147,$ we compute $(5 \cdot 177147) \mod 1000 = 735.$ [ Note: The multiplication by 5 isn't justified. The computed above is simply wrong by a factor of 5. Unfortunately, I don't know how to fix this approach. ] (context: he chat gptd the solution like recently after the test was finished so we didnt know what the real answer was. i bashed with a simple program and determined his solution was off by a factor of 5 so he just did that at the end ;-;) ~shreyan.chethan
~hashbrown2009
~ zhenghua for minor $\LaTeX$ fixes
~jrr for Notes on the flaw in the solution

## Solution 3
For $3^{7} \mid a^{3} + b^{3} + c^{3}$ to happen, we need $3 \mid a^{3} + b^{3} + c^{3}$ . So we can define classes:
$a,b,c \equiv 0\mod 3 \hspace{1 cm} \textbf{(1)}$
$a,b,c \equiv 1\mod 3 \hspace{1 cm} \textbf{(2)}$
$a,b,c \equiv 2\mod 3 \hspace{1 cm} \textbf{(3)}$
$a \equiv 0\mod 3, b \equiv 1\mod 3, c \equiv 2\mod 3 \hspace{1 cm} \textbf{(4)}$
$a \equiv 0\mod 3, b \equiv 2\mod 3, c \equiv 1\mod 3 \hspace{1 cm} \textbf{(5)}$
$a \equiv 1\mod 3, b \equiv 0\mod 3, c \equiv 2\mod 3 \hspace{1 cm} \textbf{(6)}$
$a \equiv 1\mod 3, b \equiv 2\mod, c \equiv 0\mod 3 \hspace{1 cm} \textbf{(7)}$
$a \equiv 2\mod 3, b \equiv 0\mod 3, c \equiv 1\mod 3 \hspace{1 cm} \textbf{(8)}$
$a \equiv 2\mod 3, b \equiv 1\mod 3, c \equiv 0\mod 3 \hspace{1 cm} \textbf{(9)}$
If we consider class (1), we have $a = 3a'$ and the others homogeneously. Then $a', b', c' \leq 3^{5}$ and $3^{7} \mid 3^{3}(a'^{3} + b'^{3} + c'^{3})$ . So $3^{4} \mid a'^{3} + b'^{3} + c'^{3}$ . Then we need to choose another class so we choose class (1) again. Then $a = 3a''$ and the other homogeneously. Then $a'', b'', c'' \leq 3^{4}$ and $3 \mid a''^{3} + b''^{3} + c''^{3}$ . If we choose class (1) again, we would have satisfied the inequality and it would just be a number of multiples of $3$ between $1$ and $81$ so $27^{3} = 3^{9}$ triples. Then we choose class (2) to get the number of numbers that are 1(mod 3) between $1$ and $81$ which is also $27^{3} = 3^{9}$ . In fact, we would just have $3^{9}$ triples for each of the classes so $9(3^{9}) = 3^{11}$ triples for this case for (1)-(1) classes.
Now, if we choose class (1) again, then we would have $3^{4} \mid a'^{3} + b'^{3} + c'^{3}$ and $a', b', c' \leq 3^{5}$ . But if we choose class (2) this time, then we would have $a' = 3a'' + 1$ and the others. Then $a'', b'', c'' \leq 80$ . If we expand and simplify, we would have $3^{3}$ divides a number that is 1(mod 3) which is clearly impossible. Same thing for (1)-(3) class arrangement. So we can skip to (1)-(4) class.
So we start with $3^{4} \mid a'^{3} + b'^{3} + c'^{3}$ and $a', b', c' \leq 3^{5}$ . Choosing class (4) gives $a' = 3a'', b' = 3b'' + 1, c' = 3c'' - 1$ . Expanding and simplifying we would need $3^{2} \mid a''^{3} + b''^{3} + c''^{3} + b''^{2} - c''^{2} + b'' + c''$ . Now, we would just need to do all $a'', b'', c''$ residues modular 3 such that 3 divides the expression. We can classify them as:
$a,b,c \equiv 0\mod 3$
$a,c \equiv 0\mod 3, b \equiv 1\mod 3$
$a \equiv 0\mod 3, b \equiv 1\mod 3, c \equiv 2\mod 3$
$a \equiv 0\mod 3, b \equiv 2\mod 3, c \equiv 1\mod 3$
$a,b \equiv 0\mod 3, c \equiv 2\mod 3$
$a \equiv 1\mod 3, b \equiv 2\mod 3, c \equiv 0\mod 3$
$a \equiv 1\mod 3, b,c \equiv 2\mod 3$
$a \equiv 2\mod 3, b \equiv 0\mod 3, c \equiv 1\mod 3$
$a \equiv 2\mod 3, b,c \equiv 1\mod 3$
If we consider the first case, then we have $a'' = 3a'''$ and the others. Notice $1 \leq a''' \leq 27, 0 \leq b''' \leq 26, 1 \leq c''' \leq 27$ . If we simplify with this knowledge and plug it into the original expression, we just need $3 \mid b''' + c'''$ . Then, we would have $b''', c''' \equiv 0\mod 3$ to get $9(9) = 3^{4}$ solutions. We can keep going for $b''' \equiv 1\mod 3$ and $c''' \equiv 2\mod 3$ to get another $9(9) = 3^{4}$ solutions. In total, we have $3(3^{4}) = 3^{5}$ solutions after considering all $b'''$ and $c'''$ residues mod 3. But the value of $a'''$ doesn't matter so that generates another $27 = 3^{3}$ solutions. In total, we have $3^{3} \cdot 3^{5} = 3^{8}$ solutions. Now, we move on to the next case. Choosing this case will give that $a'' = 3a''', b'' = 3b''' + 1, c'' = 3c'''$ where $1 \leq a''' \leq 27, 0 \leq b''' \leq 26, 1 \leq c''' \leq 27$ . So we need $3^{2} \mid 3^{3} a'''^{3} + 3^{3} b'''^{3} + 3^{3} b'''^{2} + 3^{2} b''' + 1 + 3^{3} c'''^{3} + 3^{2} b'''^{2} + 2 \cdot 3 \cdot b''' + 1 - 3^{2} c'''^{2} + 3b''' + 1 + 3c'''$ . Then simplifying gives $3^{2} \mid 2 \cdot 3 \cdot b''' + 3 + 3b''' + c'''$ . This yields $3 \mid 2b''' + 1 + b''' + c'''$ which gives $3 \mid c''' + 1$ so $c''' \equiv 2\mod 3$ . So $a'''$ and $b'''$ don't really matter for this case so we have $27(27) = 3^{6}$ possible pairs for $a''', b'''$ . Then we need to count the number of numbers that are 2(mod 3) between 1 and 27 inclusive which is 9. So we have $9(3^{6}) = 3^{8}$ total triples for case 2. The next case yields $3^{9}$ solutions following similar logic. In fact, all the remaining classes each give $3^{8}$ solutions for a total of $8(3^{8}) + 3^{9} = 11 \cdot 3^{8}$ . But this is just for the class (1)-(4). Since classes (5),...,(9) are the same thing except it is just permutations of class (4), we will still generate the same number of solutions as (1)-(4) arrangement. So we would have $6$ classes each giving $11(3^{8})$ solutions for a total of $22(3^{9})$ solutions.
So we have completed all class (1) cases. Now we proceed to class (2). So if we start with class (2), then we have $a = 3a' + 1$ and homogeneously the others. Then, we have $3^{6} \mid 3^{2}(a'^{3} + b'^{3} + c'^{3}) + 3^{2}(a'^{2} + b'^{2} + c'^{2}) + 3(a' + b' + c') + 1$ which is clearly impossible the $RHS$ expression is 1(mod 3). So we cannot begin with class (2). Similarly, we cannot begin with class (3). So we must proceed to class (4).
Starting with class (4) gives us that $a = 3a', b = 3b' + 1, c = 3c' - 1$ . So $a', c' \leq 3^{5}$ and $b' \leq 242$ . We would get $3^{5} \mid 3(a'^{3} + b'^{3} + c'^{3}) + 3(b'^{2} - c'^{2}) + b' + c'$ . So we need $3 \mid b' + c'$ at first. Following our logic by building on residues mod 3, we have:
$b', c' \equiv 0\mod 3$
$b' \equiv 1\mod 3, c' \equiv 2\mod 3$
$b' \equiv 2\mod 3, c' \equiv 1\mod 3$
Following case 1, we have $b' = 3b'', c' = 3c''$ . This part in essence is basically all the casework bash we did for class (1) arrangements except this time, the powers of 3 are higher. We have to substitute and consider classes mod 3 yet again(I won't go through all the steps here because it's pretty much similar to how we found the above cases). We end with $3^{9}$ total cases. This would happen for all classes (4),...,(9) so we have to multiply this by 6 to get $6 \cdot 3^{9}$ cases. The casework we did here was based on (4)-(5) class arrangements, I didn't actually consider (4)-{(1),(2),(3)} class arrangements. Doing the casework for all those classes, we end up with $8(3^{9})$ cases(I won't repeat the steps here because it's practically the same thing, bashing all modular residues mod 3. Essentially we would get another copy of the $6(3^{9})$ and then doing the casework for (4)-(2) and (4)-(3), we would get $6(3^{8})$ options for a total of $8(3^{9})$ triples). Thus, we actually have $6(3^{9}) + 8(3^{9}) = 14(3^{9})$ total cases for these subclasses. And finally, we are ready to add these all up.
We have $3^{11}$ total from class (1) trivial arrangements. Then, we have $22(3^{9})$ total cases from the (1)-(4) arrangements e.t.c. And finally, we have $14(3^{9})$ cases from the (4)-{(5)...(9)} classes. We have $3^{11} + 22(3^{9}) + 14(3^{9}) = 3^{11} + 36(3^{9}) = 3^{11} + 4(3^{11}) = 5(3^{11})$ . We can calculate this mod 1000 by simply noting $3^{10} \equiv 49\mod 1000$ because $3^{10} \equiv 243^{2}\mod 1000$ which tells us that the answer is just $5 \cdot 3 \cdot 49 = \boxed{735}$ .
~ilikemath247365
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .