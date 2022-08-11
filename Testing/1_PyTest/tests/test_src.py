import pytest
import functionality.src
from functionality.src import *


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [[]])
def test_should_return_exception_when_todos_list_is_empty(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    with pytest.raises(Exception) as exc_info:
        check_pos(2)

    assert exc_info.type is Exception
    assert exc_info.value.args[0] == "No more todos!"


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_when_todos_list_isnt_empty(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    check_pos(2)


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_return_exception_for_negative_value(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    with pytest.raises(Exception) as exc_info:
        check_pos(-1)

    assert exc_info.type is Exception
    assert exc_info.value.args[0] == "No such item number!"


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_return_exception_for_value_equal_len_of_todos(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    with pytest.raises(Exception) as exc_info:
        check_pos(len(todos))

    assert exc_info.type is Exception
    assert exc_info.value.args[0] == "No such item number!"


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_return_exception_for_value_greater_than_len_of_todos(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    with pytest.raises(Exception) as exc_info:
        check_pos(len(todos) + 1)

    assert exc_info.type is Exception
    assert exc_info.value.args[0] == "No such item number!"


@pytest.mark.check_pos
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_value_lesser_than_len_of_todos(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    check_pos(len(todos) - 1)


@pytest.mark.add_todo
@pytest.mark.parametrize("content", [5])
def test_should_pass_for_int_value(content):
    add_todo(content)


@pytest.mark.add_todo
@pytest.mark.parametrize("content", ["str"])
def test_should_pass_for_str_value(content):
    add_todo(content)



