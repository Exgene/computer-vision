# Define the knowledge base as a dictionalry of rules
knowledge_base = {
    "rule1": {
        "if": ["A", "B"],
        "then": "C"
    },
    "rule2": {
        "if": ["D"],
        "then": "A"
    },
    "rule3": {
        "if": ["E"],
        "then": "B"
    },
    "rule4": {
        "if": ["F"],
        "then": "D"
    },
    "rule5": {
        "if": ["G"],
        "then": "E"
    },
}

# Define a function to perform backward chaining


def backward_chaining(goal, known_facts):
    if goal in known_facts:
        return True

    for rule, value in knowledge_base.items():
        if goal in value["if"]:
            all_conditions_met = all(
                condition in known_facts for condition in value["if"])
            if all_conditions_met and backward_chaining(value["then"], known_facts):
                return True
            return False


goal = "C"
known_facts = ["G", "F", "E"]

# Check if the goal can be reached using backwards chaining
if backward_chaining(goal, known_facts):
    print(f"The goal '{goal}' can be reached.")
else:
    print(f"The goal '{goal}' cannot be reached.")
