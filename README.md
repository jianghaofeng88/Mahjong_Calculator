# Mahjong_Calculator
The python file is the Mahjong Calculator for Winning Tiles on "Pure Concealed Hand".

For winning rules for general Mahjong, you can refer to https://en.wikipedia.org/wiki/Mahjong

For simplicity and ease, some important terms are discribed below:
1. Tile = Mahjong card 
2. Suit = The catogory of each tile (Dots/Bamboo/Characters)
3. Rank = The point of each tile (1 to 9)
4. Pure hand = All tiles on hand has the same suit
5. Concealed hand = All tiles on hand can be composed whatever you want
6. Meld = a composition of tiles on hand (inclusing eye, pong and chow)
7. Eye = a pair of two identical tiles (e.g. [Dot 1, Dot 1], [Bamboo 4, Bamboo 4])
8. Pong = a composition of three identical tiles (e.g. [Character 2, Character 2, Character 2]) 
9. Chow = a composition of three consecutive tiles (e.g. [Character 2, Character 3, Character 4])
10. Win = 14 cards on hand with exactly 1 eye and 4 (Pongs or Chows or Both)


For this program, we assume you want to achieve a winning hand on "Pure Concealed Hand", which means all tiles have the same suit and can combine to any meld. 
Therefore, we mark each tile only using its rank (i.e. 1-9)
Now we have 13 tiles on hand and we are waiting for the 14th tile, so this program is used to analyze which rank can lead to a win.

For example,
If we have [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6] (Notice that we have assumed all have the same suit, so we do not need to mark the suit):
the 14th tile can be 1, winning melds are [[2, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
the 14th tile can be 3, winning melds are [[3, 3], [2, 2, 2], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
the 14th tile can be 4, winning melds are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
the 14th tile can be 6, winning melds are [[3, 3], [2, 2, 2], [2, 3, 4], [4, 5, 6], [4, 5, 6]]
the 14th tile can be 7, winning melds are [[2, 2], [2, 3, 4], [2, 3, 4], [3, 4, 5], [5, 6, 7]]

