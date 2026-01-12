class GameCharacter:
    """Represents a game character and manages character stats."""
    
    def __init__(self, name):
        """
        Initialize a new GameCharacter.
        
        Args:
            name (str): The name of the character
        """
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        """Read-only property for the character's name."""
        return self._name
    
    @property
    def health(self):
        """Getter for the character's health."""
        return self._health
    
    @health.setter
    def health(self, value):
        """Setter for health that prevents values below 0 and caps at 100."""
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value
    
    @property
    def mana(self):
        """Getter for the character's mana."""
        return self._mana
    
    @mana.setter
    def mana(self, value):
        """Setter for mana that prevents values below 0 and caps at 50."""
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value
    
    @property
    def level(self):
        """Getter for the character's level."""
        return self._level
    
    def level_up(self):
        """Increase the character's level by 1 and reset health and mana."""
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
    
    def __str__(self):
        """Return a formatted string with the character's stats."""
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"


# Usage example
if __name__ == "__main__":
    hero = GameCharacter('Kratos')  # Creates a new character named Kratos
    print(hero)  # Displays the character's stats
    print()
    
    hero.health -= 30  # Decreases health by 30
    hero.mana -= 10    # Decreases mana by 10
    print(hero)  # Displays the updated stats
    print()
    
    hero.level_up()  # Levels up the character
    print(hero)  # Displays the stats after leveling up