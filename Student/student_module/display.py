def display_student_info(name, subjects):
    print("\n--- Student Information ---")
    print(f"Name: {name}")
    print("Subjects and Marks:")
    for subject, mark in subjects.items():
        print(f"{subject}: {mark}")

def display_result(result, failed_subjects):
    print(f"\nResult: {result}")
    if result == "FAILED":
        print("Failed in:")
        for subject, mark in failed_subjects:
            print(f" - {subject}: {mark}")
    else:
        print("✅ Student passed all subjects.")
