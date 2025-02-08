# Project here is to build our own AI
# First we will get some text to learn from

import random  # Add this at the top with other imports

def read_story():
    # We'll start with a simple story
    story = """Once upon a time, there was a early thirties man who wanted to build AI and overcome his lack of technical skills. With the AI help they started small, learning step by step, and grew more confident each day. Soon they were building amazing things they never thought possible before."""
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
    # Get our story
    training_text = read_story()
    print("Our AI will learn from this story:\n")
    print(training_text)
    
    # Analyze patterns
    patterns = analyze_patterns(training_text)
    
    # Print patterns we found - let's look at more letters and format nicely
    print("\n----- PATTERNS FOUND IN THE STORY -----")
    for char in ['t', 'h', 'a', 'i', 'e', 's']:  # Added more letters to check
        if char in patterns:
            print(f"\nAfter the letter '{char}', I found these next letters:")
            # Sort by most common
            sorted_patterns = sorted(patterns[char].items(), 
                                  key=lambda x: x[1], 
                                  reverse=True)
            # Show top 5 most common next letters
            for next_char, count in sorted_patterns[:5]:
                print(f"  '{next_char}' appears {count} times")

    print("\n----- GENERATING NEW TEXT -----")
    # Try generating text starting with different letters
    for start_char in ['t', 'a', 'i']:
        generated = generate_text(patterns, start_char, length=50)
        print(f"\nStarting with '{start_char}', AI wrote:")
        print(generated)
