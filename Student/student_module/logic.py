def check_pass_status(subjects, pass_mark=40):
    failed_subjects = [(subject, mark) for subject, mark in subjects.items() if mark < pass_mark]

    if failed_subjects:
        return "FAILED", failed_subjects
    else:
        return "PASSED", []
