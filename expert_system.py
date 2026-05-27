# Rule-Based Expert System using Forward Chaining
rules = [
    (["fever", "cough"], "flu"),
    (["flu", "headache"], "viral infection"),
    (["sneezing", "runny_nose"], "cold"),
    (["fever", "body_pain"], "infection"),
    (["infection", "fatigue"], "weak immune system"),
    (["chest_pain", "breathing_problem"], "heart disease"),
]

# Take User Input

print("=== Medical Expert System ===")
print("Enter symptoms separated by space")
print("Example: fever cough headache")
print()
user_input = input("Enter symptoms: ").lower().split()

# Convert input into facts
facts = set(user_input)

# Store inference steps
inference_log = []

# Forward Chaining Function
def forward_chaining(facts, rules):

    inferred = True
    while inferred:
        inferred = False
        for conditions, conclusion in rules:
            # Check if all conditions exist in facts
            if all(condition in facts for condition in conditions):
                # Add new conclusion if not already present
                if conclusion not in facts:
                    facts.add(conclusion)
                    inference_log.append(
                        f"Rule Applied: {conditions} -> {conclusion}"
                    )
                    inferred = True
    return facts
# Run Expert System

final_facts = forward_chaining(facts, rules)

# Display Inference Steps

print("\n=== Inference Steps ===")

if inference_log:
    for step in inference_log:
        print(step)
else:
    print("No rules matched.")
# Display Final Conclusions
print("\n=== Final Facts / Diagnosis ===")

for fact in final_facts:
    print("-", fact)
# Detect Possible Diseases
diseases = [
    "flu",
    "viral infection",
    "cold",
    "infection",
    "weak immune system",
    "heart disease"
]

found = False

print("\n=== Possible Diseases ===")

for disease in diseases:
    if disease in final_facts:
        print("->", disease)
        found = True

if not found:
    print("No disease detected.")