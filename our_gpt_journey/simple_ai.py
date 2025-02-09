# Project here is to build our own AI
# First we will get some text to learn from

import random  # Add this at the top with other imports

def read_story():
    # We'll start with a simple story
    story = """Once upon a time, there was a person who wanted to build AI and learn new skills. 
    With AI help they started small, learning step by step, and grew more confident each day. 
    Soon they were building amazing things they never thought possible before."""
    return story

def analyze_patterns(text):
    # Dictionary to store our patterns
    patterns = {}
    
    # Look at each character and what comes next
    for i in range(len(text) - 1):
        current_char = text[i]
        next_char = text[i + 1]
        
        # Create new dictionary for new characters
        if current_char not in patterns:
            patterns[current_char] = {}
        
        # Initialize count for new pairs
        if next_char not in patterns[current_char]:
            patterns[current_char][next_char] = 0
        
        # Count this pair
        patterns[current_char][next_char] += 1
    
    return patterns

def generate_text(patterns, start_char, length=100):
    # Start with our first character
    current_char = start_char
    result = start_char
    
    # Generate one character at a time
    for _ in range(length):
        # If we haven't seen this character before, pick a random one
        if current_char not in patterns:
            current_char = random.choice(list(patterns.keys()))
            continue
        
        # Get the possible next characters and their counts
        next_chars = patterns[current_char]
        
        # Convert counts to a list of choices (more common = appears more times)
        choices = []
        for char, count in next_chars.items():
            choices.extend([char] * count)  # Add char 'count' times
        
        # Pick the next character
        current_char = random.choice(choices)
        result += current_char
    
    return result

if __name__ == "__main__":
    # Get the story
    story = read_story()
    print("\nOriginal story:")
    print(story)
    
    # Generate some text
    print("\nGenerated text:")
    # Add any generation functions you want to test here
