# define functions

# function to summarize provided policy text
def summarize(policy):
    return policy[:150]

# function to find impacted users based on keywords in the policy text
def find_impacted_users(policy):
    impacted = []
    policy_lower = policy.lower()

    if "employees" in policy_lower:
        impacted.append("Employees")
    if "managers" in policy_lower:
        impacted.append("Managers")
    if "contractors" in policy_lower:
        impacted.append("Contractors")

    return impacted

# start of main program
print("--- Welcome to PlainPath! ---")

# get policy text input from user
policy = input("\nPaste Policy Text Here\n")

print("\nProcessing...\n")

# define variables to hold summary and impacted users
summary = summarize(policy)
impacted_users = find_impacted_users(policy)

# print summary and impacted users
print("--- SUMMARY ---")
print(summary)

print("\n--- IMPACTED USERS ---")
for user in impacted_users:
    print(f"- {user}")
