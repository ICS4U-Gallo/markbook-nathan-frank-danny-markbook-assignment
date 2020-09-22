import pytest

import markbook


def test_create_assigment():
    assignment1 = markbook.create_assignment(name="Assignment One",
                                            due="2019-09-21",
                                            points=100)
    expected = {
        "name": "Assignment One",
        "due": "2019-09-21",
        "points": 100
    }
    assert assignment1 == expected

    assignment2 = markbook.create_assignment(name="Assignment Two",
                                             due=None,
                                             points=1)
    assert assignment2["name"] == "Assignment Two"
    assert assignment2["due"] is None
    assert assignment2["points"] == 1


def test_create_classroom():
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")

    assert classroom["course_code"] == "ICS4U"
    assert classroom["course_name"] == "Computer Science"
    assert classroom["period"] == 2
    assert classroom["teacher"] == "Mr. Gallo"
    # The classroom needs to be created with
    # empty lists for students and assignments
    assert classroom["student_list"] == []
    assert classroom["assignment_list"] == []


@pytest.mark.skip
def test_calculate_average_mark():
    student = {
        "marks": [50, 100]
    }
    assert markbook.calculate_average_mark(student) == 75.0


@pytest.mark.skip
def test_add_student_to_classroom():
    """
    Dependencies:
        - create_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    assert len(classroom["student_list"]) == 0
    markbook.add_student_to_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 1


@pytest.mark.skip
def test_remove_student_from_classroom():
    """
    Dependencies:
        - create_classroom()
        - add_student_to_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    markbook.add_student_to_classroom(student, classroom)
    assert len(classroom["student_list"]) == 1
    markbook.remove_student_from_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 0


@pytest.mark.skip
def test_edit_student():
    student = {"first_name": "John", "last_name": "Smith", "grade": 10}
    markbook.edit_student(student, first_name="Frank", last_name="Bell")
    assert student["first_name"] == "Frank"
    assert student["last_name"] == "Bell"
    assert student["grade"] == 10
