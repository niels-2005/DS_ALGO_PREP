import pytest

# Question
# Three in One: Describe how you could use a single array to implement three stacks.


class MultiStack:
    pass


def test_multistack():
    num_stacks = 3
    stack_size = 6
    s = MultiStack(stack_size=stack_size, number_of_stacks=num_stacks)

    for stack_num in range(num_stacks):
        assert s.is_empty(stack_num)
        assert not s.is_full(stack_num)
        with pytest.raises(StackEmptyError):
            s.pop(stack_num)

        for i in range(stack_size - 1):
            s.push(i, stack_num=stack_num)
            assert s.peek(stack_num) == i
            assert not s.is_empty(stack_num)
            assert not s.is_full(stack_num)

        s.push(999, stack_num=stack_num)
        with pytest.raises(StackFullError):
            s.push(777, stack_num=stack_num)

        assert not s.is_empty(stack_num)
        assert s.is_full(stack_num)

        assert s.peek(stack_num) == 999
        assert s.pop(stack_num) == 999
        assert not s.is_empty(stack_num)
        assert not s.is_full(stack_num)

        for i in range(stack_size - 2, 0, -1):
            assert s.peek(stack_num) == i
            assert s.pop(stack_num) == i
            assert not s.is_empty(stack_num)
            assert not s.is_full(stack_num)

        assert s.peek(stack_num) == 0
        assert s.pop(stack_num) == 0
        assert s.is_empty(stack_num)
        assert not s.is_full(stack_num)

        with pytest.raises(StackEmptyError):
            s.peek(stack_num)
        with pytest.raises(StackEmptyError):
            s.pop(stack_num)


def test_stack_does_not_exist():
    s = MultiStack(stack_size=3, number_of_stacks=1)
    with pytest.raises(StackDoesNotExistError):
        s.push(1, 1)
