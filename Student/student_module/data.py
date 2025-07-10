def get_student_data():
    name = input("Enter the name of the student: ")
    num_subjects = 5
    subjects = {}

    for i in range(num_subjects):
        subject = input(f"Enter the name of subject {i + 1}: ")
        while True:
            try:
                marks = int(input(f"Enter marks for {subject}: "))
                break
            except ValueError:
                print("Please enter valid integer marks.")
        subjects[subject] = marks

    return name, subjects
