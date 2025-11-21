# 2021 AIME II Problem 13

## Problem

Find the least positive integer $n$ for which $2^n + 5^n - n$ is a multiple of $1000$ .

## Solution 1
Recall that $1000$ divides this expression if $8$ and $125$ both divide it. It should be fairly obvious that $n \geq 3$ ; so we may break up the initial condition into two sub-conditions.
(1) $5^n \equiv n \pmod{8}$ . Notice that the square of any odd integer is $1$ modulo $8$ (proof by plugging in $1^2,3^2,5^2,7^2$ into modulo $8$ ), so the LHS of this expression goes $5,1,5,1,\ldots$ , while the RHS goes $1,2,3,4,5,6,7,8,1,\ldots$ . The cycle length of the LHS is $2$ , RHS is $8$ , so the cycle length of the solution is $\operatorname{lcm}(2,8)=8$ . Indeed, the $n$ that solve this congruence are exactly those such that $n \equiv 5 \pmod{8}$ .
(2) $2^n \equiv n \pmod{125}$ . This is extremely computationally intensive if we try to calculate all $2^1,2^2,\ldots,2^{100} \pmod{125}$ , so we take a divide-and-conquer approach instead. In order for this expression to be true, $2^n \equiv n \pmod{5}$ is necessary; it shouldn't take too long for us to go through the $20$ possible LHS-RHS combinations, considering that $n$ must be odd. We only need to test $10$ values of $n$ and obtain $n \equiv 3 \pmod{20}$ or $n \equiv 17 \pmod{20}$ .
With this in mind we consider $2^n \equiv n \pmod{25}$ . By the Generalized Fermat's Little Theorem, $2^{20} \equiv 1 \pmod{25}$ , but we already have $n$ modulo $20$ . Our calculation is greatly simplified. The LHS's cycle length is $20$ and the RHS's cycle length is $25$ , from which their least common multiple is $100$ . In this step we need to test all the numbers between $1$ to $100$ that $n \equiv 3 \pmod{20}$ or $n \equiv 17 \pmod{20}$ . In the case that $n \equiv 3 \pmod{20}$ , the RHS goes $3,23,43,63,83$ , and we need $2^n \equiv n \equiv 2^3 \pmod{25}$ ; clearly $n \equiv 83 \pmod{100}$ . In the case that $n \equiv 17 \pmod{20}$ , by a similar argument, $n \equiv 97 \pmod{100}$ .
In the final step, we need to calculate $2^{97}$ and $2^{83}$ modulo $125$ :
Note that $2^{97}\equiv2^{-3}$ ; because $8\cdot47=376\equiv1\pmod{125},$ we get $2^{97} \equiv 47\pmod{125}$ .
Note that $2^{83}$ is $2^{-17}=2^{-16}\cdot2^{-1}$ . We have \begin{align*} 2^{-1}&\equiv63, \\ 2^{-2}&\equiv63^2=3969\equiv-31, \\ 2^{-4}&\equiv(-31)^2=961\equiv-39, \\ 2^{-8}&\equiv1521\equiv21, \\ 2^{-16}&\equiv441, \\ 2^{-17}&\equiv63\cdot441\equiv7\cdot(-31)=-217\equiv33. \end{align*} This time, LHS cycle is $100$ , RHS cycle is $125$ , so we need to figure out $n$ modulo $500$ . It should be $n \equiv 283,297 \pmod{500}$ .
Put everything together. By the second subcondition, the only candidates less than $1000$ are $283,297,783,797$ . Apply the first subcondition, $n=\boxed{797}$ is the desired answer.
~Ross Gao (Solution)
~MRENTHUSIASM (Minor Reformatting)

## Solution 2
We have that $2^n + 5^n \equiv n\pmod{1000}$ , or $2^n + 5^n \equiv n \pmod{8}$ and $2^n + 5^n \equiv n \pmod{125}$ by CRT. It is easy to check $n < 3$ don't work, so we have that $n \geq 3$ . Then, $2^n \equiv 0 \pmod{8}$ and $5^n \equiv 0 \pmod{125}$ , so we just have $5^n \equiv n \pmod{8}$ and $2^n \equiv n \pmod{125}$ . Let us consider both of these congruences separately.
First, we look at $5^n \equiv n \pmod{8}$ . By Euler's Totient Theorem (ETT), we have $5^4 \equiv 1 \pmod{8}$ , so $5^5 \equiv 5 \pmod{8}$ . On the RHS of the congruence, the possible values of $n$ are all nonnegative integers less than $8$ and on the RHS the only possible values are $5$ and $1$ . However, for $5^n$ to be $1 \pmod{8}$ we must have $n \equiv 0 \pmod{4}$ , a contradiction. So, the only possible values of $n$ are when $n \equiv 5 \pmod{8} \implies n = 8k+5$ .
Now we look at $2^n \equiv n \pmod{125}$ . Plugging in $n = 8k+5$ , we get $2^{8k+5} \equiv 8k+5 \pmod{125} \implies 2^{8k} \cdot 32 \equiv 8k+5 \pmod{125}$ . Note, for $2^n \equiv n\pmod{125}$ to be satisfied, we must have $2^n \equiv n \pmod{5}$ and $2^n \equiv n\pmod{25}$ . Since $2^{8k} \equiv 1\pmod{5}$ as $8k \equiv 0\pmod{4}$ , we have $2 \equiv -2k \pmod{5} \implies k = 5m-1$ . Then, $n = 8(5m-1) + 5 = 40m-3$ . Now, we get $2^{40m-3} \equiv 40m-3 \pmod{125}$ . Using the fact that $2^n \equiv n\pmod{25}$ , we get $2^{-3} \equiv 15m-3 \pmod{25}$ . The inverse of $2$ modulo $25$ is obviously $13$ , so $2^{-3} \equiv 13^3 \equiv 22 \pmod{25}$ , so $15m \equiv 0 \pmod{25} \implies m = 5s$ . Plugging in $m = 5s$ , we get $n = 200s - 3$ .
Now, we are finally ready to plug $n$ into the congruence modulo $125$ . Plugging in, we get $2^{200s-3} \equiv 200s - 3 \pmod{125}$ . By ETT, we get $2^{100} \equiv 1 \pmod{125}$ , so $2^{200s- 3} \equiv 2^{-3} \equiv 47 \pmod{125}$ . Then, $200s \equiv 50 \pmod{125} \implies s \equiv 4 \pmod{5} \implies s = 5y+4$ . Plugging this in, we get $n = 200(5y+4) - 3 = 1000y+797$ , implying the smallest value of $n$ is simply $\boxed{797}$ .
~rocketsri

## Solution 3 (Chinese Remainder Theorem and Binomial Theorem)
We wish to find the least positive integer $n$ for which $2^n+5^n-n\equiv0\pmod{1000}.$ Rearranging gives \[2^n+5^n\equiv n\pmod{1000}.\] Applying the Chinese Remainder Theorem, we get the following system of congruences: \begin{align*} 2^n+5^n &\equiv n \pmod{8}, \\ 2^n+5^n &\equiv n \pmod{125}. \end{align*} It is clear that $n\geq3,$ from which we simplify to \begin{align*} 5^n &\equiv n \pmod{8}, \hspace{15mm} &(1) \\ 2^n &\equiv n \pmod{125}. &(2) \end{align*} We solve each congruence separately:
1. For $(1),$ quick inspections produce that $5^1,5^2,5^3,5^4,\ldots$ are congruent to $5,1,5,1,\ldots$ modulo $8,$ respectively. More generally, $5^n \equiv 5 \pmod{8}$ if $n$ is odd, and $5^n \equiv 1 \pmod{8}$ if $n$ is even. As $5^n$ is always odd (so is $n$ ), we must have $n\equiv5\pmod{8}.$ That is, for some nonnegative integer
1. For $(2),$ we substitute the result from $(1)$ and simplify:
That is, for some nonnegative integer
Substituting this back into $(*),$ we get \begin{align*} 25(5s+4)^2+2(5s+4)+27&\equiv0\pmod{125} \\ 625s^2+1010s+435&\equiv0\pmod{125} \\ 10s+60&\equiv0\pmod{125} \\ 10(s+6)&\equiv0\pmod{125} \\ s+6&\equiv0\pmod{25}. \end{align*} Therefore, the least such nonnegative integer is
Finally, combining the bolded results from above generates the least such positive integer $n$ at $s=19:$ \begin{align*} n&=8r+5 \\ &=8(5s+4)+5 \\ &=40s+37 \\ &=\boxed{797}. \end{align*} ~MRENTHUSIASM (inspired by Math Jams's 2021 AIME II Discussion )

## Solution 4 (Minimal Computation)
\[5^n \equiv n \pmod{8}\] Note that $5^n \equiv 5,1,5,1,...$ and $n \equiv 0,..,7$ so $n$ is periodic every $[2,8]=8$ . Easy to check that only $n\equiv 5 \pmod{8}$ satisfy. Let $n=8a+5$ . Note that by binomial theorem, \[2^{8a+5}=32\cdot 2^{8a} \equiv 7(1+15)^{2a} \equiv 7(1+30a)\pmod{25}\] So we have $7(1+30a) \equiv 8a+5\pmod{25} \implies 202a \equiv 23 \implies 2a \equiv 23+25 \implies a \equiv 24 \pmod{25}$ . Combining $a\equiv 24\pmod{25}$ with $n \equiv 5 \pmod{8}$ gives that $n$ is in the form of $197+200k$ , $n=197,397,597,797$ . Note that since $\phi(125)=100$ \[2^{197+200k} \equiv 2^{197} \equiv 2^{-3} \equiv \underbrace{47}_{\text{Extended Euclidean Algorithm}}\pmod{125}\] Easy to check that only $\boxed{797}\equiv 47\pmod{125},{1797}\equiv 47\pmod{125},{2797}\equiv 47\pmod{125},...$
~Afo

## Solution 5 (STEP by step transform)
1. The desired $n$ has the form $n = m + 20l + 100p,$ where $m, l, p$ are integers and $m < 20.$
Really: \[(2^{m+ 20} – (m + 20)) – (2^m – m) = (2^{m+ 20} – 2^m) – 20.\] The first term is a multiple of $100$ ( Claim ).
We denote step an increase in $m$ by 20. At each step , the divisibility by $10$ is preserved, the number of tens is reduced by $2$ .
\[(2^{m+ 100} – (m + 100)) – (2^m – m) = (2^{m+ 100} – 2^m) – 100.\] We denote STEP an increase in $m$ by $100.$ At each STEP , the first term is a multiple of $1000,$ which means that at each STEP the divisibility by $100$ is preserved, the number of hundreds decreases by $1.$
2. If the expression $2^n + 5^n – n$ is a multiple of $1000,$ the number $n$ is odd ( $2^n$ is even, $5^n$ is odd), which means that $5^n$ ends in $125.$ Therefore, the number $2^n – n$ ends in $875.$
3. $2^3 – 3 = 8 – 3 = 5.$ The tens digit is even $(0),$ it cannot be transformed into $7$ in several steps, since at each step this digit changes by $2.$
$17 = 20 – 3,$ so $2^{17} + 2^3$ is a multiple of $10,$ $(2^{17} – 17) + (2^3 – 3) = 2^{17} + 2^3 – 20$ is a multiple of $10.$ \[2^{17} \pmod {100} = ((2^{10} \pmod {100}) \cdot (2^7 \pmod {100})) \pmod {100} = (24 \cdot 28) \pmod {100} = 72.\] \[(2^{17} – 17 ) \pmod {100} = 55.\] The tens digit $5$ is odd, subtracting $2$ at each step in $4$ steps of $20$ will turn it into $7.$ So \[(2^{97} – 97 ) \pmod {100} = 75.\] \[2^{97} \pmod {1000} = ((2^{49} \pmod {1000}) \cdot 2^7) \pmod {1000} = 672.\] \[(2^{97} – 97 ) \pmod {1000} = 575.\] We transform $5$ into $8$ in $7$ STEPS , so \[(2^{797} – 797 ) \pmod {1000} = 875.\] \[(5^{797} + 2^{797} – 797 ) \pmod {1000} = 0.\] Note, that for $n = 797 + 1000k, k$ is an integer, the expression $2^n + 5^n – n$ is a multiple of $1000.$
Claim
The numbers $2^{n+2\cdot 5^k}+2^n=2^n(2^{2\cdot 5^k}+1)$ and $2^{n+4\cdot 5^k}-2^n=2^n(2^{4\cdot 5^k}-1)$
are a multiple of $10^{k+1}$ for any $n > k$ , where $n,k$ are an integer.
Proof
First, if $m \pmod{10} \equiv 4,$ then $(m^4 – m^3 + m^2 – m + 1) \pmod{10} \equiv 6 – 4 + 6 – 4 + 1 = 5.$
$2^{4n+2}\pmod{10} \equiv 4.$ So, if the number $2^{4n+2} + 1$ is a multiple of $5^k$ , then $2^{20n+10} + 1$ is a multiple of $5^{k +1}.$
Really, denote $m = 2^{4n+2},$ then, $2^{20n+10} + 1 = m^5 + 1 = (m + 1)\cdot (m^4 – m^3 + m^2 – m + 1).$
The first factor is a multiple of $5^k$ , the second factor is a multiple of $5.$ Their product is a multiple of $5^{k +1}.$
For odd $n,$ using Newton's binomial for $4^n$ , we get $2^{2n} + 1$ is a multiple of $5.$ \begin{align*} 2^{2n} + 1 = 4^n + 1 = (5 - 1)^n + 1 = 5^n -n\cdot 5^{n-1} +...+5n\end{align*} If $n = 5^k,$ then $n > k,$ each term is a multiple of $5n$ .
Therefore, the number $4^{5^k}+1$ is a multiple of $5^{k+1}$ and $2^{k+1} (2^{2\cdot 5^k}+1)$ is a multiple of $10^{k+1}$ .
The difference \[2^{n+4\cdot 5^k}-2^n=2^n(2^{4\cdot 5^k}-1) = 2^n(2^{2\cdot 5^k}-1)(2^{2\cdot 5^k}+1)\] is a multiple of $10^{k+1}.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 6 (Art of Enumeration)
Problem require us to find minimum $n$ where $2^n + 5^n - n$ is a multiple of $1000$ .
Since we already know that multiplication does not affect mod,we can simply just focus on enumerating and hope to find some pattern.
The pattern of $5^n$ is pretty simple, it starts with 5,25, and then repeat the pattern 125,625, in other words, $5^n\equiv 125 \mod{1000}$ when n is odd, and $5^n\equiv 625 \mod{1000}$ when n is even if we ignore $n=1$ and $n=2$ .
The pattern of $2^n$ , however, is quite long. In fact, it happens when $n=103$ , where $2^{103} \equiv 008 \mod{1000}$ . More specifically, the pattern starts with $n=3$ , which means for every 100 n, $2^n \mod 1000$ will repeat in a loop:
$008{,}016{,}032{,}064{,}128{,}256{,}512{,}024{,}048{,}096{,}$ $192{,}384{,}768{,}536{,}072{,}144{,}288{,}576{,}152{,}304{,}$ $608{,}216{,}432{,}864{,}728{,}456{,}912{,}824{,}648{,}296{,}$ $592{,}184{,}368{,}736{,}472{,}944{,}888{,}776{,}552{,}104{,}$ $208{,}416{,}832{,}664{,}328{,}656{,}312{,}624{,}248{,}496{,}$ $992{,}984{,}968{,}936{,}872{,}744{,}488{,}976{,}952{,}904{,}$ $808{,}616{,}232{,}464{,}928{,}856{,}712{,}424{,}848{,}696{,}$ $392{,}784{,}568{,}136{,}272{,}544{,}088{,}176{,}352{,}704{,}$ $408{,}816{,}632{,}264{,}528{,}056{,}112{,}224{,}448{,}896{,}$ $792{,}584{,}168{,}336{,}672{,}344{,}688{,}376{,}752{,}504$
Moreover, we might found that for every 20 consequtive integer, $2^n \mod 100$ will repeat in a loop. Thus, by adding $5^n$ to first twenty element, which is $n=3$ to $n=22$ , we can get a pattern of last two digit of $2^n + 5^n \mod{1000}$ , which is
$33{,}41{,}57{,}89{,}53{,}$
$81{,}37{,}49{,}73{,}21{,}$
$17{,}09{,}93{,}61{,}97{,}$
$69{,}13{,}01{,}77{,}29$
By subtracting n, we can also get following sequence:
$30{,}37{,}52{,}83{,}46{,}$
$73{,}28{,}39{,}62{,}09{,}$
$04{,}95{,}78{,}45{,}80{,}$
$51{,}94{,}81{,}56{,}07$
Noticing that only when $n=3$ and $n=17$ , $2^n+5^n-n \equiv 0 \mod{10}$ , so $n=3+20k$ and $17+20k$ are our possible candidates. However, since the length of our pattern is 20, we know that $n=3+20k$ is definetely not answer, which only left us $n=17+20k$ .
Now, we calculate the last three digit of $2^n+5^n-n$ at $n=17, n=37, n=57, n=77, n=97$ , which is $180{,}560{,}940{,}320{,}700$ .
Since the pattern will repeat for every 100 consequtive integer, the only thing that could possibly change last three digit is -n, noticing that only when $n=97$ , $2^n+5^n-n \equiv 0 \mod 100$ . So the answer only could be $n=97+100k_2$ , by subtracting 700, which means adding 700 to n, we can get our final answer $n=\boxed{797}$ .
Also, by this method we can ensure that $\frac{2^n+5^n-n}{1000}$ is an integer only if $n=797+1000k$ , all the calculation can be done without a calculator (about 15 minutes or so), need some patience though.
If you are wondering, $2^{103} = 10{,}141{,}204{,}801{,}825{,}835{,}211{,}973{,}625{,}643{,}008$ .
~henry_in_out
### Note
If you are wondering, $\frac{2^{797}+5^{797}-797}{1000}$ is equal to the following $555$ -digit number:
$119{,}975{,}745{,}111{,}650{,}476{,}385{,}411{,}555{,}010{,}245{,}228{,}283{,}196{,}935{,}699{,}128{,}663{,}834{,}$ $986{,}755{,}809{,}416{,}868{,}468{,}175{,}224{,}221{,}677{,}450{,}271{,}793{,}186{,}899{,}399{,}171{,}810{,}240{,}$ $468{,}879{,}630{,}691{,}320{,}210{,}517{,}618{,}332{,}910{,}064{,}430{,}017{,}422{,}410{,}572{,}497{,}874{,}327{,}$ $116{,}662{,}273{,}049{,}144{,}209{,}532{,}072{,}513{,}248{,}821{,}826{,}125{,}454{,}909{,}131{,}367{,}242{,}561{,}$ $087{,}064{,}439{,}357{,}641{,}814{,}942{,}784{,}478{,}465{,}638{,}163{,}997{,}895{,}630{,}266{,}780{,}260{,}171{,}$ $070{,}180{,}244{,}384{,}687{,}160{,}174{,}154{,}618{,}815{,}254{,}719{,}975{,}476{,}350{,}789{,}415{,}969{,}908{,}$ $281{,}131{,}044{,}034{,}581{,}864{,}573{,}596{,}962{,}567{,}993{,}948{,}922{,}431{,}587{,}652{,}735{,}290{,}158{,}$ $293{,}666{,}986{,}616{,}531{,}419{,}688{,}663{,}485{,}548{,}648{,}995{,}509{,}247{,}893{,}796{,}528{,}146{,}109{,}$ $144{,}143{,}744{,}650{,}882{,}271{,}050{,}771{,}309{,}301{,}498{,}467{,}898{,}226{,}649{,}089{,}924{,}520{,}539{,}$ $820{,}344{,}035{,}886{,}481{,}987{,}499{,}589{,}845{,}734{,}228{,}834{,}491{,}187.$

## Video Solution
2021 AIME II #13
MathProblemSolvingSkills.com

## Video Solution by Interstigation
Did not use any advanced method, easily understandable:
https://youtu.be/ThF67J8iaS0
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .