

# Part 1: Define the Functions
def welcome_developer(name, role):
    badge = role.upper()

    print("=" * 42)
    print(f"Welcome {name} to MediaWiki!")
    print(f"Role : {role}")
    print(f"Badge : {badge}")
    print("=" * 42)


def assign_task(role, project="MediaWiki"):
    match role:
        case "Junior Developer":
            task = "Fix a typo or formatting error in the codebase"
        case "Active Developer":
            task = "Review and test an open pull request"
        case "Senior Developer":
            task = "Fix a reported bug in the software"
        case "Lead Developer":
            task = "Design and lead a new feature development"
        case _:
            task = "Read the CONTRIBUTING file on GitHub"

    print(f"Project : {project}")
    print(f"Task : {task}")
    return task


def check_skills(*skills):
    print("Skills registered:")
    for skill in skills:
        print(f" - {skill}")
    print(f"Total skills: {len(skills)}")


# Part 4 Function
def generate_report(project, *developers):
    print("=" * 42)
    print(" MEDIAWIKI COMMUNITY REPORT")
    print("=" * 42)
    print(f"Project : {project}")
    print(f"Total : {len(developers)} developers joined")
    print("-" * 42)
    print("Developer List:")

    for developer in developers:
        print(f" - {developer}")

    print("=" * 42)

# Part 2: Accept New Developers


print("=" * 42)
print(" MEDIAWIKI — COMMUNITY MANAGER")
print("=" * 42)
print("Project : MediaWiki")
print("GitHub : github.com/wikimedia/mediawiki")
print("Stars : 4,200+")
print("Contributors: 1,000+ software developers")
print("=" * 42)

joined_developers = []

while True:
    name = input("Enter developer name : ").strip()
    experience = input("Enter experience level : ").strip().lower()

    match experience:
        case "beginner":
            role = "Junior Developer"
        case "intermediate":
            role = "Active Developer"
        case "advanced":
            role = "Senior Developer"
        case "expert":
            role = "Lead Developer"
        case _:
            role = "Observer"

    welcome_developer(name, role)
    assign_task(role)

    joined_developers.append(name)

    again = input("Add another developer? (yes/no): ").strip().lower()
    if again == "no":
        break


# Part 3: Scan the Developer List
joined_developers.append("Anonymous")
joined_developers.append("Vandal")
joined_developers.append("Sara")

print("-" * 42)
print("Scanning developer list...")
print("-" * 42)

for developer in joined_developers:
    if developer == "Anonymous":
        print(f"Skipping {developer} — anonymous not allowed")
        continue

    if developer == "Vandal":
        print("WARNING: Vandal detected! Stopping scan.")
        break

    print(f"Developer verified: {developer}")

print("-" * 42)
print("Project name characters:")

for character in "MediaWiki":
    print(character)



# Part 4: Generate the Final Report
generate_report("MediaWiki", *joined_developers)
check_skills("PHP", "JavaScript", "MediaWiki API")