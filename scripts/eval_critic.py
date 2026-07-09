# scripts/eval_critic.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.critic.feynman_analyst import feynman_analyst_node

test_cases = [
    # Original 8
    {"current_answer": "A random variable is a function that maps outcomes in a sample space to real numbers, allowing us to work numerically with random outcomes.", "has_gap": False},
    {"current_answer": "A random variable is just a variable that changes randomly with no real definition.", "has_gap": True},
    {"current_answer": "The sample space is the set of all possible outcomes of a random experiment, and every event is a subset of it.", "has_gap": False},
    {"current_answer": "Sample space just means the space where samples are stored.", "has_gap": True},
    {"current_answer": "The expectation of a random variable is its long-run average value, calculated as the weighted sum (or integral) of its possible values, weighted by their probabilities.", "has_gap": False},
    {"current_answer": "Expectation just means what you expect to happen next.", "has_gap": True},
    {"current_answer": "For a continuous random variable, expectation is computed by integrating the variable's value times its probability density function over its entire range.", "has_gap": False},
    {"current_answer": "Expectation for continuous variables works exactly the same as for discrete ones, just add up all the values.", "has_gap": True},

    # New: variance (near-certain to follow expectation in a probability unit)
    {"current_answer": "Variance measures how spread out a random variable's values are around its mean, calculated as the expected value of the squared deviation from the mean.", "has_gap": False},
    {"current_answer": "Variance just means how different the numbers are from each other.", "has_gap": True},

    # New: conditional probability
    {"current_answer": "Conditional probability P(A|B) is the probability that event A occurs given that event B has already occurred, calculated as P(A and B) divided by P(B).", "has_gap": False},
    {"current_answer": "Conditional probability just means the probability changes depending on the situation.", "has_gap": True},

    # New: independence
    {"current_answer": "Two events are independent if the occurrence of one does not affect the probability of the other, meaning P(A and B) equals P(A) times P(B).", "has_gap": False},
    {"current_answer": "Independent events just means events that have nothing to do with each other in real life.", "has_gap": True},

    # New: discrete vs continuous distinction
    {"current_answer": "A discrete random variable takes on a countable set of distinct values, while a continuous random variable can take any value within a range, described by a probability density function rather than individual probabilities.", "has_gap": False},
    {"current_answer": "Discrete and continuous random variables are basically the same thing, just different names.", "has_gap": True},
]

correct = 0
for case in test_cases:
    output = feynman_analyst_node({"current_answer": case["current_answer"]})
    feedback = output["analyst_feedback"].strip()
    predicted_gap = not feedback.upper().startswith("PASS")
    is_correct = predicted_gap == case["has_gap"]
    correct += is_correct
    print(f"[{'✓' if is_correct else '✗'}] expected_gap={case['has_gap']} predicted_gap={predicted_gap} -> {feedback[:100]}")

print(f"\nAccuracy: {correct}/{len(test_cases)} = {correct/len(test_cases)*100:.1f}%")