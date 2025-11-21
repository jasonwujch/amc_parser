# 2021 AIME I Problem 3

## Problem

Find the number of positive integers less than $1000$ that can be expressed as the difference of two integral powers of $2.$

## Solution 1
We want to find the number of positive integers $n<1000$ which can be written in the form $n = 2^a - 2^b$ for some non-negative integers $a > b \ge 0$ (note that if $a=b$ , then $2^a-2^b = 0$ ). We first observe $a$ must be at most 10; if $a \ge 11$ , then $2^a - 2^b \ge 2^{10} > 1000$ . As $2^{10} = 1024 \approx 1000$ , we can first choose two different numbers $a > b$ from the set $\{0,1,2,\ldots,10\}$ in $\binom{11}{2}=55$ ways. This includes $(a,b) = (10,0)$ , $(10,1)$ , $(10,2)$ , $(10,3)$ , $(10,4)$ which are invalid as $2^a - 2^b > 1000$ in this case. For all other choices $a$ and $b$ , the value of $2^a - 2^b$ is less than 1000.
We claim that for all other choices of $a$ and $b$ , the values of $2^a - 2^b$ are pairwise distinct. More specifically, if $(a_1,b_1) \neq (a_2,b_2)$ where $10 \ge a_1 > b_1 \ge 0$ and $10 \ge a_2 > b_2 \ge 0$ , we must show that $2^{a_1}-2^{b_1} \neq 2^{a_2} - 2^{b_2}$ . Suppose otherwise for sake of contradiction; rearranging yields $2^{a_1}+2^{b_2} = 2^{a_2}+2^{b_1}$ . We use the fact that every positive integer has a unique binary representation:
If $a_1 \neq b_2$ then $\{a_1,b_2\} = \{a_2,b_1\}$ ; from here we can deduce either $a_1=a_2$ and $b_1=b_2$ (contradicting the assumption that $(a_1,b_1) \neq (a_2,b_2)$ , or $a_1=b_1$ and $a_2=b_2$ (contradicting the assumption $a_1>b_1$ and $a_2>b_2$ ).
If $a_1 = b_2$ then $2^{a_1}+2^{b_2} = 2 \times 2^{a_1}$ , and it follows that $a_1=a_2=b_1=b_2$ , also contradicting the assumption $(a_1,b_1) \neq (a_2,b_2)$ . Hence we obtain contradiction.*
Then there are $\binom{11}{2}-5$ choices for $(a,b)$ for which $2^a - 2^b$ is a positive integer less than 1000; by the above claim, each choice of $(a,b)$ results in a different positive integer $n$ . Then there are $55-5 = \boxed{050}$ integers which can be expressed as a difference of two powers of 2.
- Note: The uniqueness of binary representation could be rather easily proven, but if you cannot convince yourself on the spot that this is the case, consider the following alternative proof. Let $(a_1,b_1) \neq (a_2,b_2)$ where $10 \ge a_1 > b_1 \ge 0$ and $10 \ge a_2 > b_2 \ge 0$ and $2^{a_1}-2^{b_1} = 2^{a_2} - 2^{b_2}$ , for the sake of contradiction. Therefore $\deg_{2}(2^{a_1}-2^{b_1})=\deg_{2}(2^{a_2}-2^{b_2})$ , or $b_1=b_2$ . Plugging in, we see that $2^{a_1}=2^{a_2}$ , or $a_1=a_2$ , contradiction.
Note by Ross Gao

## Solution 2 (Casework)
Case 1: When our answer is in the form $2^n-2^i$ , where $i$ is an integer such that $0\le i\le 4$ .
We start with the subcase where it is $2^n-2^0$ , for some integer $n$ where $n>0$ (this is because the case where $n=0$ yields $2^0-2^0=0$ , which doesn't work because it must be a positive integer.) Note that $2^{10}=1024$ , and $2^9=512$ . Our answer needs to be less than $1000$ , so the maximum possible result (in this case) is $2^9-2^0$ . Our lowest result is $2^1-2^0$ . All the positive powers of two less than $1024$ work, so we have $9$ possibilities for this subcase. For subcases $i=1, i=2, i=3,$ and $i=4$ , we have $8, 7, 6,$ and $5$ possibilities, respectively.
Case 2: When our answer is in the form of $2^n-2^j$ , where $j$ is an integer such that $5\le j\le 9$ .
We can start with the subcase where $j=5$ . We notice that $2^5=32$ , and $2^{10}-2^5=992$ which is less than $1000$ , so the greatest result in this subcase is actually $2^{10}-2^5$ , and the lowest is $2^6-2^5$ . Thus, we have $5$ possibilities. For the other four subcases, we have $4, 3, 2,$ and $1$ possibilities, respectively.
Answer: We note that these are our only cases, as numbers in the form of $2^n-2^{10}$ and beyond are greater than $1000$ .
Thus, our result is $9+8+7+6+5+5+4+3+2+1=(9+8+7+6+5+4+3+2+1)+5=\boxed{50}$ . ~jehu26

## Solution 3 (Bash)
We look for all positive integers of the form $2^a-2^b<1000,$ where $0\leq b<a.$ Performing casework on $a,$ we can enumerate all possibilities in the table below: \[\begin{array}{c|c} & \\ [-2.25ex] \boldsymbol{a} & \boldsymbol{b} \\ \hline & \\ [-2ex] 1 & 0 \\ 2 & 0,1 \\ 3 & 0,1,2 \\ 4 & 0,1,2,3 \\ 5 & 0,1,2,3,4 \\ 6 & 0,1,2,3,4,5 \\ 7 & 0,1,2,3,4,5,6 \\ 8 & 0,1,2,3,4,5,6,7 \\ 9 & 0,1,2,3,4,5,6,7,8 \\ 10 & \xcancel{0},\xcancel{1},\xcancel{2},\xcancel{3},\xcancel{4},5,6,7,8,9 \\ [0.5ex] \end{array}\] As indicated by the X-marks, the ordered pairs $(a,b)=(10,0),(10,1),(10,2),(10,3),(10,4)$ generate $2^a-2^b>1000,$ which are invalid.
Note that each of the remaining ordered pairs generates one unique desired positive integer.
We prove this statement as follows:
1. The positive integers generated for each value of $a$ are clearly different.
1. For all integers $k$ such that $1\leq k\leq9,$ the largest positive integer generated for $a=k$ is $1$ less than the smallest positive integer generated for $a=k+1.$
Together, we have justified our claim in bold. The answer is \[1+2+3+4+5+6+7+8+9+5=\boxed{050}.\]
~MRENTHUSIASM

## Solution 4 (Faster Way)
Because the difference is less than $1000$ , we can simply list out all numbers that satisfy $2^n < 1000$ . We get $0 \le n < 10$ , where n is an integer. Because the sequence $2^n$ is geometric, the difference of any two terms will be unique. $\binom{10}{2}$ will be the number of differences for $0\le n < 10$ . However, we also need to consider the case in which $n=10$ . With simple counting, we find that $5$ numbers: $(32, 64, 128, 256, 512)$ could be subtracted from $1024$ , which makes another 5 cases. There is no need to check for higher exponents since the lowest difference would be $2^{11} - 2^{10} = 1024$ , which exceeds $1000$ .
Thus, the final answer is $\binom{10}{2} + 5 = \boxed{050}.$
~TOMYANG

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=H17E9n2nIyY&t=569s

## Video Solution
https://youtu.be/M3DsERqhiDk?t=749

## Video Solution by Power of Logic
https://youtu.be/FdB0XMlVC7A

## Video Solution by WhyMath
https://youtu.be/7q83bqTP7Qg
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .