# Rock Paper Scissors AI Player

This project implements an AI player for the Rock-Paper-Scissors game using machine learning techniques.

## Project Overview

The goal is to create a program that plays Rock-Paper-Scissors against multiple bots and wins at least 60% of the games against each.

## Strategy

- Uses a Markov Chain to model the opponent’s move transitions.
- Detects repeating patterns (cycles) in the opponent’s moves.
- Employs frequency analysis as a fallback prediction.
- Adds controlled randomness to avoid being predictable.
- Selects the move that beats the predicted opponent move.

## Results

- Achieved consistent win rates above 60% against all four test bots.
- Peak win rate observed: 81%.

## How to Run

1. Run `main.py` to simulate matches against bots:

    ```bash
    python3 main.py
    ```

2. Uncomment interactive lines in `main.py` to play against the AI manually.

## Further Improvements

- Extend pattern detection to longer sequences.
- Use more sophisticated prediction algorithms.
- Analyze opponent strategies dynamically.

---

Happy coding and learning!
