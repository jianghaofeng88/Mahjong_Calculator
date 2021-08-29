# Mahjong_Calculator
The python file is the Mahjong Calculator for Winning Tiles on "Pure Concealed Hand".

Below is the simple introduction of how the program works. For detailed info related to Mahjong game, please refer to detail_info.txt.

Input: 13 integers (from 1 to 9 inclusive）

Output: The 14th integer which will make all 14 integers be able to split into exactly 1 pair and 4 triplets (In other words, 14=2+3+3+3+3). 

Reqiurements:
1. The pair must be two identical integers. (E.g. [1,1], [3,3], [6,6]).
2. The triplet must be either three identical integers or three consecutive integers. (E.g. [2,2,2], [2,3,4], [3,4,5], [8,8,8], [7,8,9]).
3. All individual integer can appear at most 4 times (i.e. we do not allow the same integer appear 5 times or more). For example, if there have been already four "2"s in the input, the program will not output "2". 
4. Output all possible integers from 1 to 9 inclusive.

For example,
If we have [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6],
1. The output integer can be 1, valid splits are [[2, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
2. The output integer can be 3, valid splits are [[3, 3], [2, 2, 2], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
3. The output integer can be 4, valid splits are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
4. The output integer can be 6, valid splits are [[3, 3], [2, 2, 2], [2, 3, 4], [4, 5, 6], [4, 5, 6]]
5. The output integer can be 7, valid splits are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [5, 6, 7]]

Developed by Haofeng Jiang

2021/08/27




本python程序用于计算麻将门前清清一色的听牌。

以下为本程序用法的简单介绍，如果想详细了解如何应用于麻将，请参阅detailed_info.txt。

输入：13个整数（必须为1-9之间的整数）

输出：第14个整数使得这14个数可以刚好分成1个对子和4个三数小组（即14=2+3+3+3+3）。

要求：
1. 对子必须是2个相同的数。（例如 [1,1], [3,3], [6,6]）
2. 三数小组必须是3个相同的数或者3个连续的数。（例如 [2,2,2], [2,3,4], [3,4,5], [8,8,8], [7,8,9]）
3. 每个数只能最多出现4次（即不能出现5个一样的数），比方说如果已经输入了四个2，则程序不会输出2。
4. 本程序会输出1-9之间所有符合条件的整数。

实例：
如果我们输入[2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]，
1. 输出可以是 1, 把14个数分成 [[2, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
2. 输出可以是 3, 把14个数分成 [[3, 3], [2, 2, 2], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
3. 输出可以是 4, 把14个数分成 [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
4. 输出可以是 6, 把14个数分成 [[3, 3], [2, 2, 2], [2, 3, 4], [4, 5, 6], [4, 5, 6]]
5. 输出可以是 7, 把14个数分成 [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [5, 6, 7]]

开发者：蒋浩锋

2021/08/27
