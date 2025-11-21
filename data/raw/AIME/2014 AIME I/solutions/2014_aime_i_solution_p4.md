# 2014 AIME I Problem 4

## Problem

Jon and Steve ride their bicycles along a path that parallels two side-by-side train tracks running the east/west direction. Jon rides east at $20$ miles per hour, and Steve rides west at $20$ miles per hour. Two trains of equal length, traveling in opposite directions at constant but different speeds each pass the two riders. Each train takes exactly $1$ minute to go past Jon. The westbound train takes $10$ times as long as the eastbound train to go past Steve. The length of each train is $\tfrac{m}{n}$ miles, where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
For the purposes of this problem, we will use miles and minutes as our units; thus, the bikers travel at speeds of $\dfrac{1}{3}$ mi/min.
Let $d$ be the length of the trains, $r_1$ be the speed of train 1 (the faster train), and $r_2$ be the speed of train 2.
Consider the problem from the bikers' moving frame of reference. In order to pass Jon, the first train has to cover a distance equal to its own length, at a rate of $r_1 - \dfrac{1}{3}$ . Similarly, the second train has to cover a distance equal to its own length, at a rate of $r_2 + \dfrac{1}{3}$ . Since the times are equal and $d = rt$ , we have that $\dfrac{d}{r_1 - \dfrac{1}{3}} = \dfrac{d}{r_2 + \dfrac{1}{3}}$ . Solving for $r_1$ in terms of $r_2$ , we get that $r_1 = r_2 + \dfrac{2}{3}$ .
Now, let's examine the times it takes the trains to pass Steve. This time, we augment train 1's speed by $\dfrac{1}{3}$ , and decrease train 2's speed by $\dfrac{1}{3}$ . Thus, we have that $\dfrac{d}{r_2 - \dfrac{1}{3}} = 10\dfrac{d}{r_1 + \dfrac{1}{3}}$ .
Multiplying this out and simplifying, we get that $r_1 = 10r_2 - \dfrac{11}{3}$ . Since we now have 2 expressions for $r_1$ in terms of $r_2$ , we can set them equal to each other:
$r_2 + \dfrac{2}{3} = 10r_2 - \dfrac{11}{3}$ . Solving for $r_2$ , we get that $r_2 = \dfrac{13}{27}$ . Since we know that it took train 2 1 minute to pass Jon, we know that $1 = \dfrac{d}{r_2 + \dfrac{1}{3}}$ . Plugging in $\dfrac{13}{27}$ for $r_2$ and solving for $d$ , we get that $d = \dfrac{22}{27}$ , and our answer is $27 + 22 = \boxed{049}$ .

## Solution 2
Using a similar approach to Solution 1, let the speed of the east bound train be $a$ and the speed of the west bound train be $b$ .
So $a-20=b+20$ and $a+20=10(b-20)$ .
From the first equation, $a=b+40$ . Substituting into the second equation, \[b+60=10b-200\] \[260=9b\] \[b=\frac{260}{9}\text{ mph}\] This means that \[a=\frac{260}{9}+40=\frac{620}{9}\text{ mph}\] Checking, we get that the common difference in Jon's speed and trains' speeds is $\frac{440}{9}$ and the differences for Steve is $\frac{800}{9}$ and $\frac{80}{9}$ .
This question assumes the trains' lengths in MILES: \[\frac{440}{9}\cdot \frac{1}{60}=\frac{440}{540}=\frac{22}{27}\text{ miles}\] Adding up, we get $22+27=\boxed{049}$ .

## Solution 3
Let the length of the trains be $L$ , let the rate of the westward train be $W_{R}$ , ;et the rate of the eastward train be $E_{R}$ , and let the time it takes for the eastward train to pass Steve be $E_{T}$ .
We have that
$L=(\frac{1}{60})(W_{R}+20)$
$L=(\frac{1}{60})(E_{R}-20)$ .
Adding both of the equations together, we get that
$2L=\frac{W_{R}}{60}+\frac{E_{R}}{60}\implies 120L=W_{R}+E_{R}$ .
Now, from the second part of the problem, we acquire that
$L=(E_{T})(E_{R}+20)$
$L=(10E_{T})(W_{R}-20)$
Dividing the second equation by the first, we get that... $1=\frac{10(W_{R}-20)}{E_{R}+20}\implies E_{R}+20=10W_{R}-200\implies E_{R}+220=10W_{R}\implies E_{R}=10W_{R}-220$ .
Now, substituting into the $120L=W_{R}+E_{R}$ .
$120L=W_{R}+(10W_{R}-220)\implies 120L= 11W_{R}-220\implies W_{R}=\frac{120L+220}{11}$ .
Finally, plugging this back into our very first equation..
$L=(\frac{1}{60})((\frac{120L+220}{11})+20)\implies 660L=120L+440\implies 540L=440\implies L=\frac{22}{27}$ .
Hence, the answer is $22+27=\boxed{049}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .