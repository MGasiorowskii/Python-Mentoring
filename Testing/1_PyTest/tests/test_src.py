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
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_int_value(mocker, content, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    add_todo(content)

    assert content in todos


@pytest.mark.add_todo
@pytest.mark.parametrize("content", ["value"])
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_str_value(mocker, content, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    add_todo(content)

    assert content in todos


@pytest.mark.remove_todo
@pytest.mark.parametrize("pos", [2])
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_int_value(mocker, pos, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    expected = todos[pos]
    remove_todo(pos)

    assert expected not in todos


@pytest.mark.edit_todo
@pytest.mark.parametrize("pos", [2])
@pytest.mark.parametrize("content", [5])
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_int_value(mocker, pos, content, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    edit_todo(pos, content)

    expected = content
    result = todos[pos]

    assert expected == result


@pytest.mark.edit_todo
@pytest.mark.parametrize("pos", [2])
@pytest.mark.parametrize("content", ["value"])
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_str_value(mocker, pos, content, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    edit_todo(pos, content)

    expected = content
    result = todos[pos]

    assert expected == result


@pytest.mark.remove_all
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_todos_list_with_elements(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    remove_all()

    expected = []
    result = todos

    assert expected == result


@pytest.mark.remove_all
@pytest.mark.parametrize("todos", [["a", "b", "c"]])
def test_should_pass_for_empty_todos_list(mocker, todos):
    mocker.patch.object(functionality.src, 'todos', todos)
    remove_all()

    expected = []
    result = todos

    assert expected == result
