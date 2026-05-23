print("--- Welcome to PlainPath! ---")

policy = input("\nPaste Policy Text Here\n")

print("\nProcessing...\n")

summary = policy[:150]

print("--- SUMMARY ---")
print(summary)

print("\n--- Action Items ---")
print("- Review Policy")
print("- Determine Applicability")

print("\n--- Impacted Users ---")

impacted = []
policy_lower = policy.lower()

if "employees" in policy_lower:
    impacted.append("Employees")
if "managers" in policy_lower:
    impacted.append("Managers")
if "contractors" in policy_lower:
    impacted.append("Contractors")

for group in impacted:
    print(f"- {group}")