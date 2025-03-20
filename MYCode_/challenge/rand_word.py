import random
import string

class RandomWordGenerator:
    def __init__(self):
        self.alphabet = string.ascii_lowercase 
    
   
    def generate_word(self, length: int):
        """Generate a single random word of a given length."""
        return ''.join(random.choices(self.alphabet, k=length))
    
   
    def generate_multiple_words(self, num_words: int, min_len: int, max_len: int):
        """Generate multiple random words with lengths between min_len and max_len."""
        return [self.generate_word(random.randint(min_len, max_len)) for _ in range(num_words)]