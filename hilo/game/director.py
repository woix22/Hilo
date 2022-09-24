from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Card): A card nstance
        hilo (string): h or l.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.hilo = ""
        self.is_playing = True
        self.score = 0
        self.total_score = 300       

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to choose higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        self.card.randomize()
        print(f"The card is: {self.card.actual_card}")
        
        
        while True:
            try:
                self.hilo = input("Higher or lower? [h/l] ")
            except ValueError:
                print("\nInvalid input\n")
                continue
            
            if self.hilo not in ["h","l"]:
                print("\nInvalid input\n") 
                continue
            
            else: break        
   
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.score = 0
        if(self.card.next_card == self.card.actual_card):
            self.score = 0
        elif(self.card.next_card > self.card.actual_card and self.hilo == "h"):
            self.score = 100
        elif(self.card.next_card < self.card.actual_card and self.hilo == "l"):
            self.score = 100
        else:
            self.score = -75

        self.total_score += self.score
        

        

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was: {self.card.next_card}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.total_score > 0)
        
        while True:
            try:
                keep_playing = input("Play again? [y/n] ")
            except ValueError:
                print("\nInvalid input\n")
                continue
            
            if keep_playing not in ["y","n"]:
                print("\nInvalid input\n") 
                continue
            
            else: break        
        self.is_playing = (keep_playing == "y")
        if not self.is_playing:
            return 

        