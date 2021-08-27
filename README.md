# Mahjong_Calculator
The python file is the Mahjong Calculator for Winning Tiles on "Pure Concealed Hand".

For winning rules for general Mahjong, you can refer to https://en.wikipedia.org/wiki/Mahjong

For simplicity and ease, some important terms are discribed below:
1. Tile = Mahjong card 
2. Suit = The catogory of each tile (Dots/Bamboo/Characters)
3. Rank = The point of each tile (1 to 9)
4. Pure hand = All tiles on hand have the same suit
5. Concealed hand = All tiles on hand can be composed to any meld(s) whatever you want
6. Meld = a composition of tiles on hand (inclusing eye, pong and chow)
7. Eye = a pair of two identical tiles (e.g. [Dot 1, Dot 1], [Bamboo 4, Bamboo 4])
8. Pong = a composition of three identical tiles (e.g. [Character 2, Character 2, Character 2]) 
9. Chow = a composition of three consecutive tiles (e.g. [Character 2, Character 3, Character 4])
10. Win = 14 cards on hand with exactly 1 eye and 4 (Pongs or Chows or Both), in other words, 14=2+3+3+3+3


For this program, we assume you want to achieve a winning hand on "Pure Concealed Hand", which means all tiles have the same suit and can combine to any meld. 
Therefore, we mark each tile only using its rank (i.e. 1-9)
Now you have 13 tiles on hand and we are waiting for the 14th tile, so this program is used to analyze which rank can lead to a win.

For example,
If we have [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6] (Notice that we have assumed all have the same suit, so we do not need to mark the suit):
1. The 14th tile can be 1, winning melds are [[2, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
2. The 14th tile can be 3, winning melds are [[3, 3], [2, 2, 2], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
3. The 14th tile can be 4, winning melds are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
4. The 14th tile can be 6, winning melds are [[3, 3], [2, 2, 2], [2, 3, 4], [4, 5, 6], [4, 5, 6]]
5. The 14th tile can be 7, winning melds are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [5, 6, 7]]

Developed by Haofeng Jiang
2021/08/27


本python程序用于计算麻将门前清清一色的听牌。
麻将详细介绍请参阅 https://zh.wikipedia.org/wiki/麻将

为了便于理解，以下为一些麻将术语的简单解释：
1. 麻将牌 = 打麻将使用的牌
2. 花色 = 麻将牌的种类，这里我们只考虑万、条、筒
3. 点数 = 麻将牌上的点数，这里我们只考虑1-9
4. 清一色 = 每张手牌的花色相同
5. 门前清 = 手牌可以任意组合
6. 组 = 两张或三张麻将牌的组合
7. 雀头 = 一组两张完全一样的牌（如【一筒，一筒】，【四条，四条】）
8. 刻子 = 一组三张完全一样的牌（如【二万，二万，二万】）
9. 顺子 = 一组三张连续的牌（如【二万，三万，四万】）
10. 胡牌 = 手上14张牌刚好可以组成1个雀头和4个（刻子或顺子），即14=2+3+3+3+3

假设你想要做成门前清的清一色胡牌，所以在本程序里，所有的麻将牌只用点数代表（因为清一色代表花色相同）。
现在你手上有13张牌，正在等着第14张牌（即听牌），那么本程序可以告诉你哪张牌可以让你胡牌。

例如：
如果我们手牌是[2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6] （注意我们已经假设所有花色相同了，所以就不写花色只写点数）：
1. 第14张牌可以是 1, 胡牌组合为 [[2, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
2. 第14张牌可以是 3, 胡牌组合为 [[3, 3], [2, 2, 2], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
3. 第14张牌可以是 4, 胡牌组合为 [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
4. 第14张牌可以是 6, 胡牌组合为 [[3, 3], [2, 2, 2], [2, 3, 4], [4, 5, 6], [4, 5, 6]]
5. 第14张牌可以是 7, 胡牌组合为 [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [5, 6, 7]]

开发者：蒋浩锋
2021/08/27
