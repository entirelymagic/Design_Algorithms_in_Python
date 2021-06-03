import pytest

from Chapter7.search_algorithms.unordered_liniar_search import search_unordered_list


class TestUnorderedListSearch:

    @pytest.fixture
    def ul1(self):
        list1 = [-10, 14, -21, 43, 15, 2, 432]
        return list1

    def test_finding_element_in_unordered_list(self, ul1):
        assert search_unordered_list(ul1, 14) == 1
        assert search_unordered_list(ul1, 500) is None


class TestOrderedListSearch:

    @pytest.fixture
    def ol1(self):
        list1 = [-21, -10, 2, 14, 15, 43, 432]
        return list1

    def test_finding_element_in_ordered_list(self, ol1):
        assert search_unordered_list(ol1, 14) == 3
        assert search_unordered_list(ol1, 432) == 6
        assert search_unordered_list(ol1, 500) is None
