import pytest

from Chapter3 import stack_class
from Chapter3 import check_parantheses


class TestStackWithLength:

    @pytest.fixture
    def s1(self):
        s1 = stack_class.Stack()
        return s1

    def test_empty_stack(self, s1):
        assert s1.its_empty() is True

    def test_stack_methods(self, s1):
        s1.push('Elvis')
        s1.push('Alexandra')
        assert s1.its_empty() is False
        assert s1.height() == 2
        assert s1.top_stack() == 'Alexandra'
        assert s1.pop() == 'Alexandra'

    def test_check_parentheses(self):
        assert check_parantheses.check_parentheses('((() (())))') is True
        assert check_parantheses.check_parentheses('((() ())))') is False

