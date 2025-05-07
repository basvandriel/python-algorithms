from nonsorted_linkedlist import NonSortedLinkedList


def test_should_be_empty():
    result = NonSortedLinkedList().is_empty()
    assert result is True


def test_single_insert():
    ll = NonSortedLinkedList()
    ll.insert(1)

    assert ll.is_empty() is False
    assert ll.head.value == 1


def test_double_insert():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)

    assert ll.is_empty() is False
    assert ll.head.size == 2

    ll.head.find_deepest_node() == 2


def test_insert_with_5_and_should_find_deepest_value():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(5)
    ll.insert(1)
    ll.insert(90)

    ll.head.find_deepest_node().value == 90


def test_it_should_work_iterating():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(5)
    ll.insert(1)

    assert list(ll) == [1, 2, 5, 1]


def test_delete_on_empty_list():
    ll = NonSortedLinkedList()
    result = ll.delete(0)
    assert result == 0


def test_delete_on_size_1_list_with_matching_value():
    ll = NonSortedLinkedList()

    ll.insert(1)

    result = ll.delete(1)
    assert result == 1


def test_delete_on_size_1_list_with_nonmatching_value():
    ll = NonSortedLinkedList()
    ll.insert(1)

    result = ll.delete(9)
    assert result == 0


def test_delete_nested_value_in_next():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(9)
    result = ll.delete(9)
    assert result == 1

    assert list(ll) == [1]


def test_multidelete_not_in_head():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(9)
    ll.insert(9)
    ll.delete(9)

    assert list(ll) == [1, 2, 3]


def test_delete_multiple_one_in_head():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(1)
    ll.insert(1)

    result = ll.delete(1)

    assert result == 3
    assert list(ll) == [2]


def test_delete_last_node():
    ll = NonSortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    result = ll.delete(3)

    assert list(ll) == [1, 2]
