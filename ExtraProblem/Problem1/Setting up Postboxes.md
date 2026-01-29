Setting up Postboxes
You work in a post office and you have been assigned to allocate postboxes in a new locality. The new locality has n number of houses and their x-coordinates are represented by the array locations.

You only have k number of postboxes for this locality. You need to distribute them in such a way that sum of all the distances from a house to its nearest postbox is minimum.

Input Format
The first line consists of an integer n, representing the number of houses

The second line consists of n spaced integers representing the coordinates of the houses on the street

The third line consists of an integer k, the number of postboxes you have to allocate

Output Format
Print the least possible sum of all the distances from a house to its nearest postbox

Example 1
Input

5
1 4 8 10 20
3
Output

5
Explanation

Allocate mailboxes in position 3, 9 and 20.

Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5

Example 2
Input

5
2 3 5 12 18
2
Output

9
Explanation

Allocate mailboxes in position 3 and 14.

Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Constraints
1 <= k <= coordinates.length <= 100

1 <= coordinates[i] <= 10^4

All the integers of houses are unique
