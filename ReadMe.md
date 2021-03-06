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

![Screenshot](http://imgur.com/a/qoN2U)

If image is not showing, you find it on [here](http://imgur.com/a/qoN2U)

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

{And More}
```

## About this project

Displayed moves are possible moves in the chess board. In these possible moves, check, castling and "en passant" is ignored.


## Several Test Samples

[Double Horse](https://lichess.org/editor/8/8/8/2N2N2/8/8/8/8_w_-_-)
```
python3 run.py '8/8/8/2N2N2/8/8/8/8 w - -' 1
```
***
[Double King](https://lichess.org/editor/8/8/8/1K4k1/8/8/8/8_w_-_-)
```
python3 run.py '8/8/8/1K4k1/8/8/8/8 w - -' 1
```
***
[Rook on Each Corner](https://lichess.org/editor/r6R/8/8/8/8/8/8/R6r_w_-_-)
```
python3 run.py 'r6R/8/8/8/8/8/8/R6r w - -' 1
```
***
[Ruy Lopez](https://lichess.org/editor/r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R_b_KQkq_-)
```
python3 run.py 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -' 1
```
***
[Eight Queen Problem Solution 1](https://lichess.org/editor/3Q4/6Q1/2Q5/7Q/1Q6/4Q3/Q7/5Q2_w_-_-)
```
python3 run.py '3Q4/6Q1/2Q5/7Q/1Q6/4Q3/Q7/5Q2 w - -' 1
```
