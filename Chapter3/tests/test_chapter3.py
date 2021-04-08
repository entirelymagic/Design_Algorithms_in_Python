import pytest

from Chapter3 import stack_class
from Chapter3 import check_parentheses
from Chapter3 import queue_class
from Chapter3 import iosif_flavius_problem


class TestStackWithLength:

    @pytest.fixture
    def s1(self):
        s1 = stack_class.Stack()
        return s1

    @pytest.fixture
    def q1(self):
        q1 = queue_class.Queue()
        return q1

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
        assert check_parentheses.check_parentheses('((() (())))') is True
        assert check_parentheses.check_parentheses('((() ())))') is False

    def test_queue_methods(self, q1):
        assert q1.its_empty() is True
        q1.add('RED')
        q1.add('YELLOW')
        q1.add('GREEN')
        assert q1.its_empty() is False
        assert q1.length() == 3
        assert q1.remove() == 'RED'
        assert q1.remove() == 'YELLOW'
        assert q1.remove() == 'GREEN'
        assert q1.its_empty() is True

    def test_iosif_flavius_game(self):
        list_of_names = ['Ana', 'Madalina', 'Cecilia', 'Elvis', 'Alex', 'Dan']
        steps = 6
        x = iosif_flavius_problem.game(list_of_names, steps)
        assert str(x) == "['Alex']"
