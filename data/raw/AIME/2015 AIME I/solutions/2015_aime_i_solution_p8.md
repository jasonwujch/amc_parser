# 2015 AIME I Problem 8

## Problem

For positive integer $n$ , let $s(n)$ denote the sum of the digits of $n$ . Find the smallest positive integer satisfying $s(n) = s(n+864) = 20$ .

## Solution 1
You know whatever $n$ is, it has to have 3 digits, because if it had only two, the maximum of $s(n)$ is 18 and because in AIME all answers are up to three digits.
Now let $n=100a_2+10a_1+a_0$
So first we know, $a_2+a_1+a_0=20$ . Okay now we have to split into cases based on which digit gets carried. This meaning, when you add a 3 digit number to 864, we have to know when to carry the digits. Note that if you don't understand any of the steps I take, just try adding any 3-digit number to 864 regularly (using the old-fashioned "put one number over the other" method, not mental calculation), and observe what you do at each step.
(1) $\textcolor{red}{*}$ None of the digits get carried over to the next space: So this means $a_2<2, a_1<4$ and $a_0<6$ . So
$s(864+n)=(8+a_2)+(6+a_1)+(4+a_0)=38$ So it doesn't work. Now:
(2) $a_2+8$ is the only one that carries over So this means $a_2>1, a_1<4$ and $a_0<6$ . So
$s(864+n)=1+(8+a_2-10)+(6+a_1)+(a_0+4)=29$
(3) $\textcolor{red}{*}$ $a_0+4$ is the only one that carries over. So
$s(864+n)=(8+a_2)+(6+a_1+1)+(4+a_0-10)=29$
(4)The first and second digit carry over (but not the third)
$s(864+n)=1+(8+a_2-10+1)+(6+a_1-10)+(4+a_0)=20$
Aha! This case works but we still have to make sure it's possible for $a_2+a_1+a_0=20$ (We assumed this is true, so we have to find a number that works.) Since only the second and first digit carry over, $a_2>0, a_1>3$ and $a_0<6$ . The smallest value we can get with this is 695. Let's see if we can find a smaller one:
(5)The first and third digit carry over (but not the second)
$s(864+n)=1+(8+a_2-10)+(7+a_1)+(4+a_0-10)=20$
The largest value for the middle digit is 2, so the other digits have to be both 9's. So the smallest possible value is 929
(6) All the digits carry over
$s(864+n)=1+(9+a_2-10)+(7+a_1-10)+(4+a_0-10)=\text{Way less than 20}$
So the answer is $\boxed{695}$ which after a quick test, does indeed work.
Note: This problem is VERY easy to bash out. I did this when I mocked this test, it gave me the answer in 5 min. Basically you just bash out all of the three digit numbers whose digit sum is 20 and you'll find (quickly) that the answer is $\boxed{695}$
$\textcolor{red}{*}$ Note to author: Since we have $a_2+a_1+a_0=20$ , this implies that $a_2$ must be at least $2$ (since $a_1+a_0 \le 18$ ), and therefore the first digit must ALWAYS carry. This is presumably the reason where the case where the second and third digits were carried but not the first was omitted, but for this reason cases (1) and (3) are also unnecessary.

## Solution 2
First, it is easy to verify that $695$ works and that no other numbers beginning with the digit 6 work (i.e. $686, 677, 668, 659$ do not work).
Suppose by contradiction that there is a smaller valid $n$ , where the leading digit of the three-digit number $n$ is 5 or less. (Two-digit $n$ obviously do not work because 9 + 9 < 20.) Clearly $n > 200$ because the smallest three-digit number whose digits sum to 20 is $299$ . Also, because the second digit is at most 9, the units digit is at least 6, which means that the addition $N = n + 864$ regroups in the ones place. Then the units digit of $N$ is clearly less than 4. But as $1000 < 200 + 864 < N < 600 + 864 = 1464$ , the sum of the thousands digit and the hundredth digit is at most 5. Because the second digit is at most 9, the sum of the digits of $N$ is at most $5 + 9 + 4 < 20$ , contradiction. Hence $\boxed{695}$ is the answer.

## Modification for Solution 2
During the real test, I immediately noticed that $n$ must be less than 1000 (AIME problem) and that $n$ must be a three-digit number. Therefore, I began casework on the leading digit of $n$ . The casework was not intensive (how many ways are there to have digits sum to 20?) and I eventually got 695 as my answer. The rigorous proof that 695 was the smallest came afterwards.

## Solution 3
First of all, notice that the smallest $n$ with $s(n) = 20$ is $299$ . Also, if $s(n + 864) = 20$ , $s(n - 136) = 19$ (because subtracting $1000$ from the number removes the $1$ in the thousands place). After checking $s(n - 136)$ for various $n$ with $s(n) = 20$ , we see that we need to have a carry when subtracting $136$ . To have this, we must either have a $2$ in the tens place or a $5$ in the units place. The minimum $n$ for the former is $929$ , and for the latter it is $695$ . We check and see that $s(695-136) = s(559) = 19$ , so our answer is $\boxed{695}$ .

## Solution 4
Observation (Lemma) : If r is the number of regroups in the addition of n+k, $S(n+k) = S(n)+S(k)-9r$ .
Proof : When you add two numbers, and you do a carry, you are taking away 10 from 1 column, and adding 1 to another column, giving a net loss of 9 to the total.
Thus, we can see that we need to regroup exactly twice when we add 864. And, the lowest possible n is 299, so let's start from there.
299 gets three regroups, so we are going to need to take away from digits, and dump the excess in the hundred's place, since the hundreds are going to regroup anyways.
So, if we take away from the tens digit, we need to take away until we get 2 in the tens digit(since the ones will regroup). So, we get the number 929, which works (929+864 = 1793), but is not the smallest.
If we take away from the ones digit, we only have to take away 4, turning the unit's place to 5. 5+4 is 9, so it won't regroup. Dump the ones into the hundred's place, and we get the number $\boxed{695}$
-AlexLikeMath

## Solution 5
Although this solution doesn't directly solve the problem, it greatly hastens the bashing process.
Call the three digits a, b, and c.
When you add each of 8, 6, and 4 to a, b, and c the resultant will either get smaller or larger, depending on the original number.
e.g. If c is 7, then adding 4 will reduce the 7 to a 1, whilst leaving a one for b.
If c is 3, then adding 4 will simply add four to the total, and make the 3 a 7.
Each of 8, 6, and 4 all can reduce the original number by a certain amount and can increase the original number by a certain amount.
8 can reduce by 2 for all numbers greater than 1, 6 can reduce numbers by 4, and 4 can reduce numbers by 6.
Possibilities:
-2, +8, (although this becomes obviously impossible later on) -4, +6, -6, +4
Also, realize that if the number is reduced, then a one will be carried to the following decimal place on the left, consequently reducing that amount they reduce. It's like a puzzle! Within no time you should find that if you add 4 to c, subtract 4 from b, subtract 1 from a, and leave a 1 in the thousands place, the total is equated to zero. This is optimal because most of the addition is kept to the left, where the effect to real value is less. (e.g. 299 is smaller than 992)
Now you have +1, -1, -4, +4 in the decimals, and a VERY fast trial and error gives $\boxed{695}.$
-Jackshi2006
Postscript by Jackshi2006
When I revisited the problem I realized that you can actually list out every possible number for n. 695 stands out very clearly as the smallest, because the only other possibility is 595, which doesn’t add to 20 to begin with.

## Solution 6 (Fast)
First, note that to compute $s(m+n)$ (for any positive integers $m$ and $n$ ), one can simply find the sum of $s(m)$ and $s(n)$ minus 9 times the number of times one regroups when adding $m$ to $n$ . One can see why this is by noticing that if one were to "forget" to regroup, and leave, say, a 10 in the ones' place, the sum of the digits would be 9 higher than if one did regroup. Anyway, one can see that the smallest 3-digit number (on AIME, all the answers are integers from 0 to 999) whose digits sum to 20 is 299. If we add this number to 864, we have to regroup 3 times, so $s(299+864)$ will be $9=9\cdot3-(8+6+4)$ smaller than $s(299)$ . We want this difference to be 0, so we need to find a way to only regroup two times.
We now notice that regrouping the hundreds is inevitable, so we must either prevent regrouping the ones or the tens. Preventing regrouping the tens would require moving many of the tens to the hundreds' place (the ones' place is already full), which is bad when we are trying to minimize the number, but preventing regrouping the ones requires moving fewer ones to the hundreds' place.
We find that to preventing regrouping the ones, the ones' place of our number must be at most 5 (a larger number would sum to ten when added to 4). Because we want to minimize the number of ones we move to the hundreds' place, we leave exactly 5 by moving four ones to the hundreds' place: $299\to\boxed{695}$ .
~ SymbolicPermutation

## Solution 7 (Bad Solution)
Bashing out modulo $9$ and getting lucky we get that if the $8$ and $6$ carry over when adding $n$ and $864$ , that $100a+10b+c \equiv 1+100(a-1)+10(b-4)+c+4 \pmod{9}$ such that $n=100a+10b+c$ and after maximizing $b$ and $c$ such that $c<6$ to not make the $4$ carry over to minimize $a$ we get that $\boxed{695}$ is our answer after confirming there are no lesser solutions.
Note: If the sum of the digits are equal, they are also the same modulo $9$ . ~SirAppel

## Solution 8 (not realistic but works)
Alternatively, you can use python to solve the problem:
~yeetdayeet

## Video Solution
https://youtu.be/2K2SYGVLkJA
~savannahsolver
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .