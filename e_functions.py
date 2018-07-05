

#  we want to check for paired boards
#  1. Check for 2 cards in board - flop


def flop_check_for_board_pair(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF]
    if len(set(board_ranks)) == 2:
        return True
    else:
        return False

        #  2. Check for 2 cards in board - turn


def turn_check_for_board_pair(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF]
    if len(set(board_ranks)) == 3:
        return True
    else:
        return False

        #  3. Check for 2 cards in board - river


def river_check_for_board_pair(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF,
                   (board[4] >> 8) & 0xF]
    if len(set(board_ranks)) == 4:
        return True
    else:
        return False

        #  2. Check for 2 pairs in board - turn - can result in hero having air/pair/top pair/overpairf/two pair


def turn_check_for_board_two_pairs(hand, board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF]
    board_uniques_len = len(set(board_ranks))
    if board_uniques_len == 4:  # board all uniques
        return "two_pair"

    elif board_uniques_len == 3:  # board has one pair
        player_ranks = [(hand[0] >> 8) & 0xF, (hand[1] >> 8) & 0xF]
        if player_ranks[0] == player_ranks[1]:
            if player_ranks[0] > max(board_ranks):
                return "overpair"
            else:
                return "pair"
        else:
            total_pairs = len(set(board_ranks + player_ranks))
            if total_pairs == 2:
                top_card_board = max(board_ranks)
                if player_ranks.count(top_card_board) == 1:
                    return "top_pair"
                else:
                    return "pair"
            elif total_pairs == 3:
                if min(player_ranks) == min(board_ranks):
                    return "pair"
                else:
                    return "two_pair"

    elif board_uniques_len == 2:
        player_ranks = [(hand[0] >> 8) & 0xF, (hand[1] >> 8) & 0xF]
        if player_ranks[0] == player_ranks[1]:
            if player_ranks[0] > max(board_ranks):
                return "overpair"
            elif player_ranks[0] > min(board_ranks):
                return "pair"
            else:
                return "air"
    else:
        return "air"


def check_for_two_pairs_river(hand, board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF,
                   (board[4] >> 8) & 0xF]
    board_uniques = set(board_ranks)
    board_uniques_len = len(board_uniques)
    if board_uniques_len == 5:
        return "two_pair"

    elif board_uniques_len == 4:
        # board has one pair - hand must be a pair or be a pair with the other two board hands (so two pair is completed) - check firstly for pocket pair
        top_card_board = max(board_ranks)
        player_ranks = [(hand[0] >> 8) & 0xF, (hand[1] >> 8) & 0xF]
        if player_ranks[0] == player_ranks[1]:  # hand has a pair
            if player_ranks[0] > top_card_board:
                return "overpair"
            else:
                return "pair"
        else:
            if player_ranks.count(top_card_board) == 1:
                return "top_pair"
            else:
                return "pair"

    elif board_uniques_len == 3:  # board has two pairs - need to check whether hand is a pair and where it stands relatively.
        player_ranks = [(hand[0] >> 8) & 0xF, (hand[1] >> 8) & 0xF]
        if player_ranks[0] == player_ranks[1]:
            board_dupslist = list(set(i for i in board_ranks if board_ranks.count(i) > 1))
            top_card_board = max(board_ranks)
            bottom_card_board_dups = min(board_dupslist)
            if player_ranks[0] > top_card_board:
                return "overpair"
            elif player_ranks[0] > bottom_card_board_dups:
                return "pair"
            else:
                return "air"
    else:
        return "air"


# 1. Check for 2 cards in board - flop
def flop_check_for_board_trips(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF]
    if len(set(board_ranks)) == 1:
        return True
    else:
        return False

def turn_check_for_board_trips(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF]
    if len(set(board_ranks)) == 2:
        return True
    else:
        return False

def river_check_for_board_trips(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF,
                   (board[4] >> 8) & 0xF]
    if len(set(board_ranks)) == 3:
        return True
    else:
        return False

def river_check_for_board_quads(board):
    board_ranks = [(board[0] >> 8) & 0xF, (board[1] >> 8) & 0xF, (board[2] >> 8) & 0xF, (board[3] >> 8) & 0xF,
                   (board[4] >> 8) & 0xF]
    if len(set(board_ranks)) == 2:
        return True
    else:
        return False


# def check_five_card_hands(board, actual_rank):  # check for full house/flush/straight
#     if get_rank(board) == actual_rank:  # need to change this get_rank
#         return False
#     else:
#         return True
