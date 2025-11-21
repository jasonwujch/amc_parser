# 2025 AMC 12B Problem 1

## Problem

The instructions on a $350$ -gram bag of coffee beans say that proper brewing of a large mug of pour-over coffee requires $20$ grams of coffee beans. What is the greatest number of properly brewed large mugs of coffee that can be made from the coffee beans in that bag?

$\textbf{(A) } 16 \qquad\textbf{(B) } 17 \qquad\textbf{(C) } 18 \qquad\textbf{(D) } 19 \qquad\textbf{(E) } 20$

## Solution 1
$\frac{350}{20}$ is $17.5$ . We round down to find the maximum he can make (he cannot brew half of a cup), so the answer is $\boxed{\text{(B) }17}$ .
~mingbaboo (this is my first time doing this so it could be very wrong)
~NumberNinja1234 (Minor Latex and grammar edit for clarity) :)
~Sumeete (Minor grammar edits)
~SharkBlueHorse (Minor grammar edits)

## Solution 2
We can use $340$ -grams if we use $17$ mugs. This is because $20 \cdot 17 = 340$ . We cannot use $18$ because that would mean using $360$ -grams. The answer is $\boxed{17}$ .
Note that you can also find this by finding $\lfloor \frac{350}{20} \rfloor = 17.$
~lprado

## Solution 3
Dividing $350$ by $20$ , we get $17$ with a remainder of $10$ . However, $10$ grams cannot make a properly brewed large mug of coffee, as stated in the problem. We can only count fully brewed mugs of coffee, hence the answer is $\boxed{\text{(B) }17}$ .
~Yoonyoung11 ~Minor edits and Latex by Yvz2900

## Solution 4 - Easiest, Intuitive
Model the bag as a finite measure space \( (\Omega, \mathcal{F}, \mu) \) with \( \mu(\Omega) = M_{\text{bag}} \) grams.
Partition \( \Omega \) into disjoint measurable atoms: \( \Omega = (A_1 \sqcup A_2 \sqcup \dots \sqcup A_N) \sqcup R \) with \( \mu(A_i) = m_{\text{mug}} \) for \( i = 1 \dots N \) and \( \mu(R) = \) residual mass \( 0 \le \mu(R) < m_{\text{mug}} \).
Additivity of \( \mu \) gives \( M_{\text{bag}} =\displaystyle\sum_{i=1}^N \mu(A_i) + \mu(R) = N \cdot m_{\text{mug}} + \mu(R) \).
Thus \( N = (M_{\text{bag}} - \mu(R)) / m_{\text{mug}} \le M_{\text{bag}} / m_{\text{mug}} \). Maximum integer \( N \) is \( \lfloor M_{\text{bag}} / m_{\text{mug}} \rfloor \).
To do \( \lfloor 350 / 20 \rfloor \): Write 350 divided by 17 as \( 350 = 20q + r \) with \( 0 \le r < 20 \).
Compute \(350\) \( \pmod{20}\). Compute \( 20 \times 17 = 340 \). Compute \( 350 - 340 = 10 \).
So \( 350 \equiv 10 \pmod{20} \).
Therefore \( r = 10 \) and \( q = 17 \). \( \text{Floor}(350 / 20) = q = \boxed{\text{(B) }17} \).
~N0lan

## Solution 5 - Cheese (sort of)
We multiply $20$ by each of the answer choices to see if we can find which one is closest and under $350.$ First, we try solution $\text{A}$ , which is $16$ . $16 \cdot 20 = 320,$ which is $30$ off from 350, so $\text{A}$ cannot be the answer, because we can add another $20$ . Moving on to answer choice $\text{B},$ $17 \cdot 20 = 340.$ We notice that $350-340=10,$ and so we cannot add another $20$ to get closer but less than $350.$ (The next number, $18$ , would result in $20 \cdot 18=360,$ which is more than $350$ .) So, the answer is $\boxed{\text{(B) }17}.$
(note - the actual cheese solution would likely include every single answer choice, but I use a bit of intellect in this solution)
~zoyashaikh

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=aZS3YClnhFY
~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution by Daily Dose of Math
https://youtu.be/s-Wimgu9wto
~Thesmartgreekmathdude
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .