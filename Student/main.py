from student_module.data import get_student_data
from student_module.logic import check_pass_status
from student_module.display import display_student_info, display_result

def main():
    student_name, subjects = get_student_data()
    display_student_info(student_name, subjects)
    result, failed_subjects = check_pass_status(subjects)
    display_result(result, failed_subjects)

if __name__ == "__main__":
    main()
