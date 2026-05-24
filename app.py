# define functions

# function to summarize provided policy text
def summarize(policy):
    return policy[:150]

# function to find impacted users based on keywords in the policy text
def find_impacted_users(policy):
    impacted = []
    policy_lower = policy.lower()

    if "employee" in policy_lower:
        impacted.append("Employees")
    if "manager" in policy_lower:
        impacted.append("Managers")
    if "contractor" in policy_lower:
        impacted.append("Contractors")
    if not impacted:
        impacted.append("Unknown - No specific user groups identified")

    return impacted

# function to identify action items based on keywords in the policy text
def generate_action_items(policy):
    action_items = []
    policy_lower = policy.lower()

    if "submit" in policy_lower:
        action_items.append("Submit required documents")
    if "review" in policy_lower:
        action_items.append("Review required documents")
    if "approve" in policy_lower:
        action_items.append("Obtain necessary approvals")
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
