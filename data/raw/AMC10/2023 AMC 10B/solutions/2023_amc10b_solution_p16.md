# 2023 AMC 10B Problem 16

## Problem

Define an $\textit{upno}$ to be a positive integer of $2$ or more digits where the digits are strictly increasing moving left to right. Similarly, define a $\textit{downno}$ to be a positive integer of $2$ or more digits where the digits are strictly decreasing moving left to right. For instance, the number $258$ is an upno and $8620$ is a downno. Let $U$ equal the total number of $upnos$ and let $D$ equal the total number of $downnos$ . What is $|U-D|$ ?

$\textbf{(A)}~512\qquad\textbf{(B)}~10\qquad\textbf{(C)}~0\qquad\textbf{(D)}~9\qquad\textbf{(E)}~511$

## Solution 1
First, we know that $D$ is greater than $U$ , since there are less $upnos$ than $downnos$ . To see why, we examine what determines an upno or $downno$ .
We notice that, given any selection of unique digits (notice that "unique" constrains this to be a finite number), we can construct a unique downno. Similarly, we can also construct an $upno$ , but the selection can not include the digit $0$ since that isn't valid.
We then have $[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]$ as the pool of numbers that we can pick from for $downnos$ , and {1, 2, 3, 4, 5, 6, 7, 8, 9} as the pool of numbers that we can pick for $upnos$ . There are only two states each number can be in: appearing and not appearing in the arrangement. (That is why we use the number 2 as the base in the exponent!)
Thus, there are $2^{10}$ total $downnos$ and $2^9$ total $upnos$ . However, we are told that each $upno$ or $downno$ must be at least $2$ digits, so we subtract out the $0$ -digit and $1$ -digit cases (Referring back to Paragraph 2, this is when every number's state is nonappearing or every number except one has the state of nonappearing).
For the $downnos$ , there are $10$ $1$ -digit cases, and for the $upnos$ , there are $9$ $1$ -digit cases. There is $1$ $0$ -digit case for both $upnos$ and $downnos$ .
Thus, the difference is $\left(\left(2^{10}-10-1\right)-\left(2^9-9-1\right)\right)=2^9-1=\boxed{\textbf{(E) }511}.$
~Technodoggo ~added notes by Bjartskular457

## Solution 2
Set Theory can get very complicated, so let's break this down intuitively and derive answers. We have 2 cases. Upno's, and Downno's. Call them \( U \) and \( D \) respectively. Let us evaluate them independently and then deal with \( |U-D| \) later.
Case 1: \( U \) (Deriving the number of cases)
The intuition is to come up with a pattern.
We start with 9. We instantly see that 9 is the largest possible unit number, so there exists no \( U \) who's leading digit is 9.
Continuing with 8, the possible upno's are 89, which is the only case.
Now with 7, the upno's are 78, 79, and 789. Great! We have 3 cases here.
Continuing with 6, we have 67, 68, 69, 678, 679, 689, 6789. That is 7 cases.
Now, we could just assume that for 5, there will be 13 different cases (The first difference of the cases in 7 and 8 is 2, and then the difference between the cases in 6 and 7 is 4, so we say the next one is \(7+6=13\)). However, let's not jump to conclusions just yet. Let's actually compute the cases for 5 quickly.
For 5, we have 56, 57, 58, 59, 567, 568, 569, 578, 579, 589, 5678, 5679, 5689, 5789, and 56789, giving us not 13, but 15 digits.
So, our assumption that 5 was 13 cases is wrong. (A little whisper to tell you to be careful). It seems that the rule between each pattern is multiplying the difference previously by 2.
So our differences for the sequences (in order) are \( \{2, 4, 8, 16, 32, 64, 128\} \). We use this to find the number of cases for each number and quickly sum them all up (so we start with 1 from case 1, add 2, then add 4 to that, so on to get the number of cases and then add the cases together) to get 502.
Case 2: \( D \) (Deriving the number of cases)
We start with 1 this time. Unlike the \( U \) set, we can now use 0.
Starting with 1 gives us 10, 1 case.
Moving to 2 gives us 21, 20, 210, 3 cases.
3 gives us 32, 31, 30, 321, 310, 320, 3210, 7 cases.
We already see where this is going, so this time we already jump to our \( U \) set and add 1 more difference to it to get our \( D \) set (This is to include the difference between 9 and 8, because now that 0 is available, 1 is a viable option).
So our \( D \) set is \( \{2, 4, 8,16,32,64,128,256\} \). Using the set to find the number of cases gives us 1013.
Great! We have overcome the difficult part. All that is left to do is to find \( |U-D| \). We plug in our values for \( U \) and \( D \), which are 502 and 1013 respectively, to get \( |U-D| = |502-1013| = |-511| =\) $\boxed{511}$ or $\boxed{E}$ .
~Pinotation

## Solution 3
Since Upnos do not allow $0$ s to be in their first -- and any other -- digit, there will be no zeros in any digits of an Upno. Thus, Upnos only contain digits $[1,2,3,4,5,6,7,8,9]$ .
Upnos are $2$ digits in minimum and $9$ digits maximum (repetition is not allowed). Thus the total number of Upnos will be ${9\choose 2}+{9\choose 3}+ {9\choose 4}+...+{9\choose 9}$ , since every selection of distinct numbers from the set $[1,2,3,4,5,6,7,8,9]$ can be arranged so that it is an Upno. There will be ${9\choose 2}$ - $2$ digit Upnos, ${9\choose 3}$ - $3$ digit Upnos and so on.
Thus, the total number of Upnos will be $\sum_{i=2}^{9}{{9 \choose i}}=512-10=502$
Notice that the same combination logic can be done for Downnos, but Downnos DO allow zeros to be in their last digit. Thus, there are $10$ possible digits $[0,1,2,3,4,5,6,7,8,9]$ for Downnos.
Therefore, it is visible that the total number of Downnos are: \[\sum_{i=2}^{10}{{10\choose i}}= 2^{10}-{10\choose 0}-{10\choose 1} = 1024 - 11 = 1013\] .
Thus $|U-D| = |(1013-502)| =\boxed{\textbf{(E) }511}.$
~yxyxyxcxcxcx ~JISHNU4414L (Latex)

## Solution 4
Note that you can obtain a downo by reversing an upno (like $235$ is an upno, and you can obtain $532$ ). So, we need to find the amount of downos that end with 0 since if you 'flip' the numbers, the upno starts with a 0 which corresponds to a downo. We can find the cases that end with a 0: \[\sum_{n=0}^9 \dbinom{9}{n} = \dbinom{9}{0} + \dbinom{9}{1} + \cdots + \dbinom{9}{9}\] to get 512. However, 0 itself is not a valid case (since it has 1 digit) so we subtract 1. Our answer is $\boxed{\textbf{(E) }511}$ .
-aleyang
-ap246(LaTeX)

## Solution 5 (Educated Guess)
First, note that the only $downnos$ that are not contained by the set of $upnos$ is every $downno$ that ends in $0$ .
Next, listing all the two digits $downnos$ , we find that the answer is more than 10, since there are more digits to be tested and there are already 9 two digit $downnos$ . This leaves us with $512$ or $511$ .
Next, we notice that all the possibilities for $2$ through $9$ digit $downnos$ ending in $0$ pair up with one another, as the possibilities are equal (e.g. possibilities for $2$ digits = possibilities for $9$ digits, etc.).
This leaves us with one last possibility, the ten digit $downno$ $9876543210$ .
Since all the previous possibilities form an even number, adding one more possibility will make the total odd. Therefore, we need to choose the odd number from the set $[511, 512]$ .
Our answer is $\boxed{\textbf{(E) }511}$ .
~Stead (a.k.a. Aaron)

## Solution 6
We start by calculating the number of upnos. Suppose we are constructing an upno of $n$ digits such that $n \ge 2$ . An upno can't start with a " $0$ ", so there are $9$ digits to choose from. There are $\dbinom{9}{n}$ ways to choose an upno with $n$ digits. This is because for each combination of digits, only one combination can form an upno. Therefore, for $2 \le n \le 9$ , the total number of upnos is \[\binom{9}{2} + \binom{9}{3} + \binom{9}{4} + \cdots + \dbinom{9}{9} = 2^9 - \binom{9}{1} - \binom{9}{0} = 2^9 - 10.\]
Similarly, the digits of a downo of $n$ digits can be chosen among 10 digits to choose from, since $0$ can be a digit of the downo as the last digit. Thus, the number of downos is \[\binom{10}{2} + \binom{10}{3} + \binom{10}{4} + \cdots + \dbinom{10}{9} + \dbinom{10}{10} = 2^{10} - \binom{10}{1} - \binom{10}{0} = 2^{10} - 11.\] Thus, \[|U - D| = |(2^9 - 10) - (2^{10} - 11)| = (2^{10} - 11) - (2^9 - 10) = 2^{10} - 2^9 - 1 = \boxed{\textbf{(E) }511}\]
~rnatog337

## Solution 7 (1-1 Correspondence)
Notice that the number of upno integers are the number of subsets of the set $(1, 2, 3, 4, 5, 6, 7, 8, 9)$ , excluding the empty set ( $\emptyset$ ) and the one-digit integers. So, the number of upno integers is $2^9-1-9=502$ .
The number of downo numbers are similar, but with $0$ . So, the number of downo integers is the number of subsets of the set $(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)$ , excluding the empty set and the one-digit integers. So, the number of downo integers is $2^{10}-1-10=1013$ .
Therefore, the difference between the number of downo integers and upno is $1013-502=\boxed{\textbf{(E) }511}$ .
~MrThinker

## Solution 8 (Bijection)
Observe that each downno (that doesn't end with a $0$ ) maps to one upno. It suffices to count the number of downnos that end with $0$ .
Given that a downno ends with $0$ , we want to choose the remaining digits from the set $\{1, 2, \ldots, 9\}$ . We can arrange the elements of any subset so that they are increasing. We may include or exclude any of the $9$ elements, giving $2^{9}$ subsets. Subtracting $1$ to account for the empty set, we have $2^9 - 1 = \boxed{\textbf{(E) }511}$ more downnos than upnos.
-Benedict T (countmath1)

## Solution 9 (Combinations)
Like Solution $1$ , we know that there are more downnos than upnos because downnos can contain $0$ . So, we need to calculate the number of downnos ending with $0$ . We can do this by splitting this into different cases:
For a $2$ -digit downno ending with $0$ , there are $\binom{9}{1}$ ways of constructing a downno ending with $0$ . Similarly, for a $3$ -digit downno ending with $0$ , there are $\binom{9}{2}$ ways of constructing a downno ending with $0$ . We can calculate this for up to $10$ digits, or the downno $9876543210$ .
We can add the sum for all of the cases, which is $\binom{9}{1}+\binom{9}{2}+\binom{9}{3}+...+\binom{9}{9} = 2^9 - 1 = \boxed{\textbf{(E) }511}$ . ~pixelpyguy

## Solution 10 (guessish)
Note that every upno maps to one downno, just reversed. In addition, note that every downno can create another by adding a $0$ to the end. Downos can also be single digits with a following $0$ . Therefore, downno $= 2 \cdot$ upno $+ 9$ . $2 \cdot$ upno is guaranteed to be even, therefore our answer is guaranteed to be odd. From simple observation, the only valid answer is $\boxed{\textbf{(E) }511}$ .
~meikh_neiht ~formatting edits by MW2014

## Video Solution 1 by OmegaLearn
https://youtu.be/UoasqXkLJ_g

## Video Solution
https://youtu.be/H9JXizKoDcg
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .