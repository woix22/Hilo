import random

class Card:
    """A card with a number between 1 and 13.    
   
    Attributes:
        actual_card (int): The number of the actual card.
        next_card (int): The number of the next card.
    """
    
    def __init__(self):
        """Constructs a new instance of Card without any number.

        Args:
            self (Card): An instance of Card.
        """

        self.actual_card = 0
        self.next_card = 0

    def randomize(self):
        """Generates a new random value between 1 and 13 for both cards.
        
        Args:
            self (Card): An instance of Card.
        """
    
        self.actual_card = random.randrange(1, 14, 1)
        self.next_card = random.randrange(1, 14, 1)
        
        

        


