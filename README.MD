# About
This project recreates the mobile game Blockudoku and implements various players that each use different rules and techniques to play the game. 

The reason for creating this project is to be able to explore and gain proficiency in techniques used while handling lots of data.

# How Blockudoku Works

Blockudoku consists of a 9 by 9 grid onto which you place shapes. When a section is complete (either a verticle/horizontal line or a 3 by 3 square like in tradiational sudoku) the section will disappear, awarding the player points. The aim of the game is to gain the most number of points before the board gets filled to a point where no further shapes can be placed down.

The core gameplay loop consists of the player being presented 3 shapes from a bank of available shapes which must all be placed until another 3 shapes are given.

Blockudoku can be found [here](https://play.google.com/store/apps/details?id=com.easybrain.block.puzzle.games) on the Google Play Store


# How to Run

# Players
Each player is extended from a base class which defines general attributes and methods
## Dumb Player
The Dumb player will look for the first valid place it can put down each available shape (starting from top left of board and working down, then left). The move that will garner the highest immediate score will be played.
## MidLow Player
The MidLow player employs two main tactics when making its decision. The player will search through the whole board looking for each vaild move of each available shape. The move giving the highest immediate score will be selected. However if there are multiple moves tha give the same score then it will assess the board as if the move had been palyed to determin how favourable it is.

It does this by counting the number of empty tiles per section (every verticle/hhorizontal and 3 by 3 square). Each section is then rated using this conversion:


|Empty tiles|0|1|2|3|4|5|6|7|8|9|
|-----------|-|-|-|-|-|-|-|-|-|-|
|Rating|0|1|2|3|4|4|3|2|1|0|

By using this weighting system, the player will favour a board which has sections that are more empty or more full. This wanted as it means the sections are open for more shapes to be placed (high number of empty tiles) or nearly complete and therefore soon to be cleared (low number of empty tiles)

The rating for each section across the board is then summed and normalised the highest rating you could get (108). When the player is making a move and multiple moves give the same immediate score, the one resulting in the lowest rating (as lower is better) from this evaluation is chosen.
<!-- Add visual example -->

## MidHigh Player
MidHigh player is an extension of the MidLow player class. It uses the same system to evaluate the state of a board but with the addition of another evaluation check.

For each potential move, it counts how large the areas of empty tiles are. A high number of empty tiles together is favourable as it allows for a larger number of shapes to be placed within it. Once it finds all the areas of empty tiles, it counts how many in each, sqares that number and then sums them all together. By doing this, you weight the player to produce boards with a fewer empty areas but of high number of empty tiles. As with the rating in MidLow player, these ratings are normalised in comparison to the max number a board can achieve (8561).

<!-- Add visual example -->

# Results
