# game.py
"""
This module defines game objects for a No Limit Hold'em poker game,
designed to integrate with a computer vision system that inputs game data.
It leverages a circular linked list for player ordering so that we can 
establish dealer, big blind, and small blind positions. Players who are 
sitting out are skipped in the turn order. Individual game functions are 
provided, culminating in one large 'turn' function that processes the 
active player's turn.
"""

from enum import Enum
from typing import List, Optional


class Move(Enum):
    """Enumeration for a player's possible moves."""
    FOLD = "fold"
    CALL = "call"
    RAISE = "raise"
    CHECK = "check"


class Player:
    """
    Represents a poker player.
    
    Attributes:
        name (str): The player's name.
        chip_amount (int): The total chips the player has.
        bet (int): The current bet amount.
        last_move (Optional[Move]): The last move made by the player.
        is_active (bool): Whether the player is actively playing (True) or sitting out (False).
        next (Optional[Player]): The next player in the circular linked list.
    """
    def __init__(
        self,
        name: str,
        chip_amount: int = 0,
        bet: int = 0,
        last_move: Optional[Move] = None,
        is_active: bool = True
    ):
        self.name = name
        self.chip_amount = chip_amount
        self.bet = bet
        self.last_move = last_move
        self.is_active = is_active
        self.next: Optional['Player'] = None  # Pointer for the circular linked list

    def set_chip_amount(self, amount: int):
        """Sets the player's chip amount."""
        self.chip_amount = amount

    def set_bet(self, bet: int):
        """Sets the player's current bet amount."""
        self.bet = bet

    def set_last_move(self, move: Move):
        """Sets the player's last move."""
        self.last_move = move

    def set_active(self, active: bool):
        """
        Sets the player's active status.
        
        Args:
            active (bool): True if the player is actively playing; False if sitting out.
        """
        self.is_active = active

    def __repr__(self):
        return (f"Player({self.name}, chips={self.chip_amount}, bet={self.bet}, "
                f"move={self.last_move}, active={self.is_active})")


class Game:
    """
    Represents the state of a No Limit Hold'em poker game using a circular linked list.
    
    Attributes:
        players (List[Player]): The list of players in the game.
        community_cards (List[str]): The community cards on the table as string representations.
        dealer (Optional[Player]): The current dealer in the circular linked list.
        current_turn (Optional[Player]): The player whose turn it currently is.
    """
    def __init__(self, players: Optional[List[Player]] = None, community_cards: Optional[List[str]] = None):
        self.players: List[Player] = players if players is not None else []
        self.community_cards: List[str] = community_cards if community_cards is not None else []
        self.dealer: Optional[Player] = None
        self.current_turn: Optional[Player] = None
        self._initialize_circular_linked_list()

    def _initialize_circular_linked_list(self):
        """Initializes a circular linked list from the players list."""
        if not self.players:
            return

        n = len(self.players)
        # Link the players in the order provided.
        for i in range(n):
            self.players[i].next = self.players[(i + 1) % n]

        # Establish the dealer: choose the first active player in the list.
        self.dealer = self._find_next_active(self.players[0])
        # Set current turn pointer to the dealer.
        self.current_turn = self.dealer

    def _find_next_active(self, player: Player) -> Player:
        """
        Finds the next active player starting from the given player.
        If the given player is active, returns it immediately.
        """
        current = player
        for _ in range(len(self.players)):
            if current.is_active:
                return current
            current = current.next
        # If no active player is found (all players sitting out), return the original.
        return player

    def get_next_active_player(self, player: Player) -> Player:
        """
        Gets the next active player after the given player in the circular list,
        skipping players who are sitting out.
        """
        next_player = player.next
        # Loop until we find an active player or come back to the starting player.
        while next_player != player:
            if next_player.is_active:
                return next_player
            next_player = next_player.next
        # If all players are inactive or only one active exists, return the original player.
        return player

    def set_players(self, players: List[Player]):
        """
        Sets the players in the game and rebuilds the circular linked list.
        
        Args:
            players (List[Player]): A list of Player objects.
        """
        self.players = players
        self._initialize_circular_linked_list()

    def update_player(self, player: Player):
        """
        Updates a player's information in the game. If the player is not already present, adds them.
        
        Args:
            player (Player): The player object with updated information.
        """
        for i, p in enumerate(self.players):
            if p.name == player.name:
                self.players[i].chip_amount = player.chip_amount
                self.players[i].bet = player.bet
                self.players[i].last_move = player.last_move
                self.players[i].is_active = player.is_active
                return
        # If the player is not found, add them and reinitialize the linked list.
        self.players.append(player)
        self._initialize_circular_linked_list()

    def set_community_cards(self, card_strs: List[str]):
        """
        Sets the community cards based on a list of card string representations.
        
        Args:
            card_strs (List[str]): List of card representations (e.g., "As" for Ace of spades).
        """
        self.community_cards = card_strs

    def clear_community_cards(self):
        """Clears all community cards from the table."""
        self.community_cards = []

    def rotate_dealer(self):
        """
        Rotates the dealer position to the next active player.
        Also resets the current turn pointer to the new dealer.
        """
        if self.dealer:
            self.dealer = self.get_next_active_player(self.dealer)
            self.current_turn = self.dealer

    def assign_blinds(self):
        """
        Assigns the small blind and big blind positions based on the dealer.
        Returns:
            tuple: (small_blind, big_blind) as Player objects (or None if unavailable).
        """
        if not self.dealer:
            return (None, None)
        small_blind = self.get_next_active_player(self.dealer)
        big_blind = self.get_next_active_player(small_blind)
        return (small_blind, big_blind)

    def process_turn(self, player: Player):
        """
        Processes the turn for the given player.
        In an actual game, this would involve handling the player's actions 
        (which might be determined via computer vision inputs).
        Here, we simulate the turn with a placeholder action.
        
        Args:
            player (Player): The player whose turn is being processed.
        """
        print(f"Processing turn for {player.name}.")
        # Placeholder: mark the player's move as CHECK.
        player.set_last_move(Move.CHECK)
        # Additional logic (betting, chip updates, etc.) would be implemented here.
        return player

    def turn(self):
        """
        Processes the turn for the current active player in the circular linked list,
        then advances the turn to the next active player.
        
        Returns:
            Player: The next active player whose turn will be processed next.
        """
        if not self.current_turn:
            return None
        # Process the current player's turn.
        self.process_turn(self.current_turn)
        # Advance to the next active player.
        self.current_turn = self.get_next_active_player(self.current_turn)
        return self.current_turn

    def __repr__(self):
        players_repr = ', '.join([p.name for p in self.players])
        dealer_name = self.dealer.name if self.dealer else "None"
        current_turn_name = self.current_turn.name if self.current_turn else "None"
        return (f"Game(dealer={dealer_name}, current_turn={current_turn_name}, "
                f"players=[{players_repr}], community_cards={self.community_cards})")
