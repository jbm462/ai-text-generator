import random

def read_story():
    # Our training text
    story = """Once upon a time, there was a early thirties man who wanted to learn coding. 
    He started with Python and found it fun. Each day he learned something new."""
    return story

def analyze_pairs(text):
    # Store patterns of character pairs
    pairs = {}
    
    # Look through the text, but stop 2 characters before the end
    for i in range(len(text) - 2):
        two_chars = text[i:i+2]     # Like 'th' or 'in'
        next_char = text[i+2]       # What comes after those two
        
        if two_chars not in pairs:
            pairs[two_chars] = {}
        
        if next_char not in pairs[two_chars]:
            pairs[two_chars][next_char] = 0
        pairs[two_chars][next_char] += 1
    
    return pairs

def generate_text(patterns, start="th", length=100):
    current = start
    result = start
    
    for _ in range(length):
        if current not in patterns:
            next_char = random.choice('abcdefghijklmnopqrstuvwxyz ')
            result += next_char
            current = current[1] + next_char
            continue
            
        possibilities = patterns[current]
        choices = []
        for char, count in possibilities.items():
            choices.extend([char] * count)
            
        next_char = random.choice(choices)
        result += next_char
        current = current[1] + next_char
    
    return result

if __name__ == "__main__":
    story = read_story()
    print("Original story:\n")
    print(story)
    
    patterns = analyze_pairs(story)
    
    print("\nGenerating new text:\n")
    for start in ["th", "in", "on"]:
        generated = generate_text(patterns, start=start, length=50)
        print(f"\nStarting with '{start}':")
        print(generated) 