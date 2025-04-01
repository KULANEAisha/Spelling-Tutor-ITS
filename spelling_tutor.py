import random
import matplotlib.pyplot as plt

# Step 3: Define words
easy_words = [
    {"word": "cat", "hint": "A small pet animal", "masked": "c_t"},
    {"word": "dog", "hint": "A loyal pet", "masked": "d_g"},
    {"word": "fish", "hint": "An animal that lives in water", "masked": "f_sh"},
    {"word": "house", "hint": "A place where people live", "masked": "h_ _ se"},
    {"word": "elephant", "hint": "A large animal with a trunk", "masked": "e_ _ phant"}
]

hard_words = [
    {"word": "giraffe", "hint": "A tall animal", "masked": "g_ _ affe"},
    {"word": "bicycle", "hint": "A two-wheeled vehicle", "masked": "b_ _ ycle"},
    {"word": "pyramid", "hint": "A triangular structure", "masked": "p_ _ amid"},
    {"word": "calendar", "hint": "Used to track days", "masked": "c_ _ endar"}
]

# Step 4: Student Model
student_model = {"correct": 0, "incorrect": 0}

def update_student_model(is_correct):
    """Updates the student progress tracker."""
    if is_correct:
        student_model["correct"] += 1
    else:
        student_model["incorrect"] += 1

# Step 5:  Teaching Model
def get_next_word():
    """Dynamically selects words, ensuring variety and difficulty scaling."""
    if student_model["correct"] > student_model["incorrect"]:
        # Shuffle hard words and return one
        random.shuffle(hard_words)
        return random.choice(hard_words)
    else:
        # Shuffle easy words and return one
        random.shuffle(easy_words)
        return random.choice(easy_words)

# Step 6: Interface
def ask_question():
    """Displays a word with missing letters and checks the student's response."""
    question = get_next_word()
    print("\nFill in the missing letters:")
    print(f" Word: {question['masked']}")
    print(f" Hint: {question['hint']}")

    # User input
    answer = input("Your answer: ").strip().lower()

    # Check answer
    if answer == question["word"]:
        print("✅ Correct!")
        update_student_model(True)
    else:
        print(f"❌ Incorrect! The correct answer was '{question['word']}'.")
        update_student_model(False)

# Run the tutor
for _ in range(5):
    ask_question()

# Step 7: Performance Summary
attempts = list(range(1, student_model["correct"] + student_model["incorrect"] + 1))
correct_answers = [1 if i < student_model["correct"] else 0 for i in attempts]

plt.plot(attempts, correct_answers, marker='o', linestyle='-', color='b')
plt.title('Student Performance Over Time')
plt.xlabel('Attempt Number')
plt.ylabel('Correct/Incorrect')
plt.grid(True)
plt.show()

# Step 8: Adaptive Feedback
def give_feedback():
    """Provides feedback based on student performance."""
    if student_model["correct"] > student_model["incorrect"]:
        print("\n Great job! Let's try some harder words!")
    else:
        print("\n Keep practicing! Let's try some easier ones.")

give_feedback()


