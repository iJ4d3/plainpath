# define functions

# function to summarize provided policy text
def summarize(policy):
    return policy[:150]

# function to find impacted users based on keywords in the policy text
def find_impacted_users(policy):
    impacted = []
    policy_lower = policy.lower()

    user_groups = {
        "employee": "Employees",
        "manager": "Managers",
        "contractor": "Contractors"
    }

    for keyword in user_groups:
        if keyword in policy_lower:
            impacted.append(user_groups[keyword])
        if not impacted:
            impacted.append("No specific user groups identified")

    return impacted

# function to identify action items based on keywords in the policy text
def generate_action_items(policy):
    action_items = []
    policy_lower = policy.lower()

    action_keywords = {
        "submit": "Submit required documentation",
        "update": "Update existing records",
        "review": "Review documentation",
    }

    for keyword in action_keywords:
        if keyword in policy_lower:
            action_items.append(action_keywords[keyword])
    if not action_items:
        action_items.append("No specific action items identified")

    return action_items

# start of main program
print("--- Welcome to PlainPath! ---")

# get policy text input from user
policy = input("\nPaste Policy Text Here\n")

print("\nProcessing...\n")

# define variables to hold summary and impacted users
summary = summarize(policy)
impacted_users = find_impacted_users(policy)
action_items = generate_action_items(policy)

# print summary and impacted users
print("--- SUMMARY ---")
print(summary)

print("\n--- IMPACTED USERS ---")
for user in impacted_users:
    print(f"- {user}")

print("\n--- ACTION ITEMS ---")
for item in action_items:
    print(f"- {item}")
