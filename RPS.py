import random

def player(prev_play, opponent_history=[], transition_counts={}):
    # Store opponent moves
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)

    # Initialize transition_counts dict on first call
    # Format: { 'R': {'R': count, 'P': count, 'S': count}, ... }
    if not transition_counts:
        transition_counts.update({m: {'R':0, 'P':0, 'S':0} for m in ['R','P','S']})

    # Update transition counts from opponent history
    if len(opponent_history) >= 2:
        prev = opponent_history[-2]
        curr = opponent_history[-1]
        transition_counts[prev][curr] += 1

    # First move: random
    if not opponent_history:
        return random.choice(['R', 'P', 'S'])

    # Small randomness to avoid being predictable
    if random.random() < 0.1:
        return random.choice(['R', 'P', 'S'])

    # Pattern detection: check if last 3 moves repeat
    if len(opponent_history) >= 6:
        if opponent_history[-3:] == opponent_history[-6:-3]:
            # Opponent is cycling a pattern
            predicted = opponent_history[-1]
            # Return the move that beats predicted
            return {'R':'P', 'P':'S', 'S':'R'}[predicted]

    last_move = opponent_history[-1]

    # Use transition probabilities to predict next opponent move
    next_moves = transition_counts[last_move]
    predicted = max(next_moves, key=next_moves.get)  # move with highest count after last_move

    # If no transitions recorded yet, fallback to frequency analysis
    if sum(next_moves.values()) == 0:
        count_R = opponent_history.count('R')
        count_P = opponent_history.count('P')
        count_S = opponent_history.count('S')
        if count_R >= count_P and count_R >= count_S:
            predicted = 'R'
        elif count_P >= count_R and count_P >= count_S:
            predicted = 'P'
        else:
            predicted = 'S'

    # Return the move that beats predicted opponent move
    return {'R':'P', 'P':'S', 'S':'R'}[predicted]
