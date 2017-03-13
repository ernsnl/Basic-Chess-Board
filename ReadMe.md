# Basic Chess Board

This is a program for creating and displaying movements for the given chess board string and player in this board.

It takes two input:
1. Chess Board String (Please look below for format of the string)
2. Color for the player (0 for the Black and 1 for the White Player)


## Requirements

This project is developed in Python 3.5.2

## Format of the chess board string

This project follows the formatting that is used in the [lichess]('https://en.lichess.org/editor')
Lichess provides free online chess board editor. Using that online tool will help to generate and visualize the chess board.

Under the editor, there is a segment called FEN. This is format used in this project. Symbol representation is
given below.

1. r/R ==> Black/White ROOK
2. n/N ==> Black/White NIGHT
3. b/B ==> Black/White BISHOP
4. q/Q ==> Black/White QUEEN
5. k/K ==> Black/White KING
6. p/P ==> Black/White PAWN

## Sample Input

Structure of input string as follows:

```
python3 run.py '{your_custom_design_chess_board}' {0 or 1}
```

![alt text](http://imgur.com/a/qoN2U "Main Board")

For example; To display initial start of a chess game (picture above) with white player having the turn run the following command(1):

```
python3 run.py 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -' 1
```


## Sample Output

Output of the project as follows:

```
{Chess Board in Ascii}
----
{Type of the piece} at {Location of that particular piece}
{Possible Movement available to that particular piece in chess notation}
----
```

For the initial start command(1) output will be as follows
```
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟




♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 

PAWN at a2
Pa3 Pa4
----
PAWN at b2
Pb3 Pb4
----
PAWN at c2
Pc3 Pc4
----
PAWN at d2
Pd3 Pd4
----
PAWN at e2
Pe3 Pe4
----
PAWN at f2
Pf3 Pf4
----
PAWN at g2
Pg3 Pg4
----
PAWN at h2
Ph3 Ph4
----
NIGHT at b1
Na3 Nc3
----
NIGHT at g1
Nf3 Nh3
----
```
