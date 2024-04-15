# TODO: Add the test cases that you'll be submitting to this file!
#       Make sure your test cases are all named starting with
#       test_ and that they have unique names.

# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA

import course
import survey
import criterion
import grouper
import pytest
###############################################################################
# Task 2 Test cases
###############################################################################


def test_has_answer_yes_no_question() -> None:
    """Test that YesNoQuestion has appropriate answer for student."""
    student = course.Student(1, 'Alex')
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    answer = survey.Answer(True)
    student.set_answer(question, answer)
    actual = True
    assert actual == student.has_answer(question)


def test_set_answer_changes_already_answer() -> None:
    """Test that method changes already had answer into new answer for question.
    """
    student = course.Student(1, 'Alex')
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    answer = survey.Answer(False)
    student.set_answer(question, answer)
    answer2 = survey.Answer(True)
    student.set_answer(question, answer2)
    actual = survey.Answer(True)
    assert actual.content == student.get_answer(question).content


def test_get_answer_yes_for_yes_no_answer_question() -> None:
    student = course.Student(1, 'Alex')
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    answer = survey.Answer(True)
    student.set_answer(question, answer)
    actual = survey.Answer(True)
    assert actual.content == student.get_answer(question).content

###############################################################################
# Task 3 Test cases
###############################################################################


def test_enroll_students_unsuccessfully() -> None:
    """Test that students have been enrolled cannot be enrolled twice."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student_list = [student, student2]
    cs_course = course.Course('cs')
    cs_course.enroll_students(student_list)
    cs_course.enroll_students(student_list)
    actual = list(cs_course.get_students())
    expected = student_list
    assert actual == expected


def test_students_all_answered_questions() -> None:
    """Test that the function return True iff students have answered all
    questions."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student_list = [student, student2]
    answer = survey.Answer(True)
    cs_course = course.Course('cs')
    cs_course.enroll_students(student_list)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    question_list = [question]
    cs_survey = survey.Survey(question_list)
    student.set_answer(question, answer)
    student2.set_answer(question, answer)
    actual = cs_course.all_answered(cs_survey)
    expected = True
    assert actual == expected


def test_get_students_in_order() -> None:
    """Test that get students method can sort all students in order."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'hooxi')
    student_list = [student4, student2, student, student3]
    cs_course = course.Course('cs')
    cs_course.enroll_students(student_list)
    expected = (student, student2, student4, student3)
    actual = cs_course.get_students()
    assert expected == actual


###############################################################################
# Task 4 Test cases
###############################################################################


def test_validate_answer_to_question() -> None:
    """Test that method return False if answer is invalid to Question."""
    answer = survey.Answer(5)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    actual = question.validate_answer(answer)
    expected = False
    assert actual == expected


def test_get_similarity_successfully() -> None:
    """Test that get similarity method return 1.0 for same answer."""
    answer1 = survey.Answer(True)
    answer2 = survey.Answer(True)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    actual = question.get_similarity(answer1, answer2)
    expected = 1.0
    assert actual == expected
###############################################################################
# Task 5 Test cases
###############################################################################


def test_answer_is_valid() -> None:
    """Test that the answer is valid."""
    answer = survey.Answer(False)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    actual = answer.is_valid(question)
    expected = True
    assert actual == expected
###############################################################################
# Task 6 Test cases
###############################################################################


def test_homogeneous_criterion_score_answer() -> None:
    """Test homogeneous criterion score students successfully."""
    answer1 = survey.Answer(False)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    answer_list = [answer1]
    expected = 1.0
    criteria = criterion.HomogeneousCriterion()
    actual = criteria.score_answers(question, answer_list)
    assert expected == actual
###############################################################################
# Task 7 Test cases
###############################################################################


def test_len_successfully() -> None:
    """Test __len__ method could return number of members."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'hooxi')
    members = [student, student2, student3, student4]
    group = grouper.Group(members)
    actual = group.__len__()
    expected = 4
    assert actual == expected


def test_member_contains_in_group() -> None:
    """Test __contains__ return True for members in group."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'hooxi')
    members = [student, student2, student3, student4]
    group = grouper.Group(members)
    actual = group.__contains__(student)
    expected = True
    assert actual == expected


def test_get_members_return_groups_of_members() -> None:
    """Test get members method return members of group"""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'hooxi')
    members = [student, student2, student3, student4]
    group = grouper.Group(members)
    group_copy = group.get_members()
    for i in range(len(group_copy)):
        assert group_copy[i] == members[i]


###############################################################################
# Task 8 Test cases
###############################################################################


def test_add_group() -> None:
    """Test add group method runs properly."""
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'hooxi')
    members1 = [student, student2]
    members2 = [student3, student4]
    group1 = grouper.Group(members1)
    group2 = grouper.Group(members2)
    grouping = grouper.Grouping()
    grouping.add_group(group1)
    grouping.add_group(group2)
    actual = [group1, group2]
    for i in range(len(grouping.get_groups())):
        assert grouping.get_groups()[i] == actual[i]
###############################################################################
# Task 9 Test cases
###############################################################################


def test_get_questions() -> None:
    """Test get questions method get questions in survey."""
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    expected = questions
    actual = sample.get_questions()
    assert expected == actual


def test_get_criterion() -> None:
    """Test get questions method get criterion in survey."""
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    expected = sample._get_criterion(question)
    actual = criterion.HomogeneousCriterion()
    assert type(expected) == type(actual)


def test_get_weight() -> None:
    """Test get weight method get weight in survey."""
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    expected = sample._get_weight(question)
    actual = 1
    assert expected == actual


def test_set_weight_successfully() -> None:
    """Test set weight for question successfully."""
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    sample.set_weight(2, question)
    expected = 2
    actual = sample._get_weight(question)
    assert expected == actual


def test_set_criterion_successfully() -> None:
    """Test set criterion for question successfully."""
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    sample.set_criterion(criterion.HeterogeneousCriterion(), question)
    expected = criterion.HeterogeneousCriterion()
    actual = sample._get_criterion(question)
    assert type(expected) == type(actual)


def test_score_students() -> None:
    """Test score students method return right score."""
    student = course.Student(1, 'Alex')
    answer1 = survey.Answer(False)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    student.set_answer(question, answer1)
    students = [student]
    actual = sample.score_students(students)
    expected = 1.0
    assert actual == expected


def test_score_grouping() -> None:
    """Test score grouping method return right score."""
    student = course.Student(1, 'Alex')
    answer1 = survey.Answer(False)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    questions = [question]
    sample = survey.Survey(questions)
    student.set_answer(question, answer1)
    students = [student]
    group = grouper.Group(students)
    grouping = grouper.Grouping()
    grouping.add_group(group)
    expected = 1.0
    actual = sample.score_grouping(grouping)
    assert expected == actual
###############################################################################
# Task 10 Test cases
###############################################################################


def test_alpha_grouper() -> None:
    """Test alpha grouper divides groups appropriately."""
    lst_grouper = grouper.AlphaGrouper(2)
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'Hooxi')
    student_list = [student, student2, student3, student4]
    answer = survey.Answer(True)
    cs_course = course.Course('cs')
    cs_course.enroll_students(student_list)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    question_list = [question]
    cs_survey = survey.Survey(question_list)
    student.set_answer(question, answer)
    student2.set_answer(question, answer)
    student3.set_answer(question, answer)
    student4.set_answer(question, answer)
    actual = lst_grouper.make_grouping(cs_course, cs_survey).get_groups()
    grouping = grouper.Grouping()
    members1 = [student, student4]
    members2 = [student3, student2]
    group1 = grouper.Group(members1)
    group2 = grouper.Group(members2)
    grouping.add_group(group1)
    grouping.add_group(group2)
    expected = grouping.get_groups()
    for i in range(len(expected)):
        actual_group = actual[i]
        expected_group = actual[i]
        for j in range(len(actual_group.get_members())):
            actual_student = actual_group.get_members()[j]
            expected_student = expected_group.get_members()[j]
            assert actual_student == expected_student


def test_greedy_grouper() -> None:
    """Test greedy grouper divides groups appropriately."""
    lst_grouper = grouper.GreedyGrouper(2)
    student = course.Student(1, 'Alex')
    student2 = course.Student(2, 'Swenni')
    student3 = course.Student(666, 'Steven')
    student4 = course.Student(9, 'Hooxi')
    student_list = [student, student2, student3, student4]
    answer1 = survey.Answer(True)
    answer2 = survey.Answer(False)
    cs_course = course.Course('cs')
    cs_course.enroll_students(student_list)
    question = survey.YesNoQuestion(1, 'is a1 difficult?')
    question_list = [question]
    cs_survey = survey.Survey(question_list)
    student.set_answer(question, answer1)
    student2.set_answer(question, answer2)
    student3.set_answer(question, answer1)
    student4.set_answer(question, answer2)
    actual = lst_grouper.make_grouping(cs_course, cs_survey).get_groups()
    grouping = grouper.Grouping()
    members1 = [student, student3]
    members2 = [student2, student4]
    group1 = grouper.Group(members1)
    group2 = grouper.Group(members2)
    grouping.add_group(group1)
    grouping.add_group(group2)
    expected = grouping.get_groups()
    for i in range(len(expected)):
        actual_group = actual[i]
        expected_group = actual[i]
        for j in range(len(actual_group.get_members())):
            actual_student = actual_group.get_members()[j]
            expected_student = expected_group.get_members()[j]
            assert actual_student == expected_student
