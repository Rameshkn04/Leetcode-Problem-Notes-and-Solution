Positives and Negatives
Satyam is counting the sins and virtues he had done in his life. He's too scared to go to hell. So he arranged a magic stick to decrease his sins.

He has given an array a consisting of n elements representing his sins and virtue.
He has a magic stick and the power of magic stick is defined below :

You can Choose 2 adjacent elements and flip both of their signs. In other words choose 
an index `i` such that 1≤i≤n−1 and assign a[i] = −a[i] and a[i+1] = −a[i+1].
He wants to maximize the count of his sins and virtue i.e. the sum of the array.

He needed your help in this problem.

Note : You just need to complete Solve() function.

Input Format
First line contains an integer n .

Second line contains an integer array a of size n.

Output Format
Print the maximum possible sum the array can have after performing the described operation any number of times.

Example 1
Input

3
-1 -1 -1

Output

1

Explanation

By performing the operation on the first two elements, we can change the array from [−1,−1,−1] to [1,1,−1]
and it can be proven this array obtains the maximum possible sum which is 1+1+(−1)=1.

Example 2
Input

5
1 5 -5 0 2

Output


13
Explanation

By performing the operation on −5 and 0 , we change the array from [1,5,−5,0,2] to [1,5,−(−5),−0,2] =[1,5,5,0,2]
which has the maximum sum since all elements are non-negative. So, the answer is 1+5+5+0+2=13. 
