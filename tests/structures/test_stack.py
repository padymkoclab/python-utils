"""Test for stack implementation."""


import pytest

from utils.structures.stack import Stack, StackEmptyError


stack = Stack()


def test_create_empty_stack():

    assert str(stack) == '[]'
    assert repr(stack) == 'Stack([])'
    assert stack.length == 0
    assert stack.isEmpty is True

    with pytest.raises(StackEmptyError):
        stack.pop()

    with pytest.raises(StackEmptyError):
        stack.head

    with pytest.raises(StackEmptyError):
        stack.tail


def test_push_to_empty_stack():

    stack.push(-2321.21)

    assert str(stack) == '[-2321.21]'
    assert repr(stack) == 'Stack([-2321.21])'
    assert stack.length == 1
    assert stack.isEmpty is False
    assert stack.head == -2321.21
    assert stack.tail == -2321.21


def test_push_second_item_to_stack():

    stack.push(True)

    assert str(stack) == '[-2321.21, True]'
    assert repr(stack) == 'Stack([-2321.21, True])'
    assert stack.length == 2
    assert stack.isEmpty is False
    assert stack.head is True
    assert stack.tail == -2321.21


def test_push_third_item_to_stack():

    stack.push(())

    assert str(stack) == '[-2321.21, True, ()]'
    assert repr(stack) == 'Stack([-2321.21, True, ()])'
    assert stack.length == 3
    assert stack.isEmpty is False
    assert stack.head == ()
    assert stack.tail == -2321.21


def test_push_fourth_item_to_stack():

    stack.push({})

    assert str(stack) == '[-2321.21, True, (), {}]'
    assert repr(stack) == 'Stack([-2321.21, True, (), {}])'
    assert stack.length == 4
    assert stack.isEmpty is False
    assert stack.head == {}
    assert stack.tail == -2321.21


def test_pop_item_from_stack():

    assert stack.pop() == {}
    assert str(stack) == '[-2321.21, True, ()]'
    assert repr(stack) == 'Stack([-2321.21, True, ()])'
    assert stack.length == 3
    assert stack.isEmpty is False
    assert stack.head == ()
    assert stack.tail == -2321.21


def test_pop_item_again_from_stack():

    assert stack.pop() == ()

    assert str(stack) == '[-2321.21, True]'
    assert repr(stack) == 'Stack([-2321.21, True])'
    assert stack.length == 2
    assert stack.isEmpty is False
    assert stack.head is True
    assert stack.tail == -2321.21


def test_clear_stack():

    stack.clear()

    assert str(stack) == '[]'
    assert repr(stack) == 'Stack([])'
    assert stack.length == 0
    assert stack.isEmpty is True

    with pytest.raises(StackEmptyError):
        stack.pop()

    with pytest.raises(StackEmptyError):
        stack.head

    with pytest.raises(StackEmptyError):
        stack.tail
