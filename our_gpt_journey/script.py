from transformers import pipeline
import os

# Initialize the pipeline
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    generated_texts = generator(prompt, max_length=100, truncation=True)
    return generated_texts[0]['generated_text']

def save_story(prompt, story):
    # Get current directory
    current_dir = os.getcwd()
    print(f"\nSaving stories in: {current_dir}/stories")
    
    # Create a stories folder if it doesn't exist
    if not os.path.exists('stories'):
        os.makedirs('stories')
        print("Created new stories folder!")
    
    # Save the story to a file
    with open('stories/generated_story.txt', 'a') as f:
        f.write(f"\nPrompt: {prompt}\n")
        f.write(f"Generated Story: {story}\n")
        f.write("-" * 50 + "\n")

if __name__ == "__main__":
    print("Welcome to the AI Story Generator!")
    print("Type your story starter below (or 'quit' to exit)")
    
    while True:
        user_prompt = input("\nYour story starter: ")
        if user_prompt.lower() == 'quit':
            break
            
        result = generate_text(user_prompt)
        print("\nGenerated story:", result)
        print("-" * 50)
        
        # Save the story
        save_story(user_prompt, result)
