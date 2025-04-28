import linkedlist


def test_build_node():
    x = linkedlist.build_node([1, 2, 3, 4])

    assert x is not None

    z = x.find_deepest_value()
    assert z == 4


def test_build_linkedlist_should_insert_correctly():
    ll = linkedlist.SortedLinkedList()
    ll.insert(1)
    ll.insert(4)
    ll.insert(5)

    assert ll.head.depth == 2
    assert ll.head.find_deepest_value() == 5


def test_linkedlist_should_put_number_before():
    ll = linkedlist.SortedLinkedList()
    ll.insert(4)
    ll.insert(1)

    assert ll.head.depth == 1
    assert ll.head.find_deepest_value() == 4


def test_linkedlist_should_put_value_in_the_middle():
    ll = linkedlist.SortedLinkedList()
    ll.insert(1)
    ll.insert(4)
    ll.insert(5)

    # this should be inserted on the head (first next value)
    ll.insert(2)


def test_linkedlist_should_convert_to_list_with_no_head():
    ll = linkedlist.SortedLinkedList()
    result = ll.to_list()
    assert result == []


def test_linkedlist_should_work_with_depth1():
    ll = linkedlist.SortedLinkedList()
    ll.insert(1)

    assert ll.to_list() == [1]


def test_linkedlist_should_work_with_multiple_values():
    ll = linkedlist.SortedLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(4)
    ll.insert(5)

    assert ll.to_list() == [1, 2, 4, 5]


def test_linkedlist_delete_no_data():
    ll = linkedlist.SortedLinkedList()
    assert ll.delete_value(1) == 0


def test_delete_with_direct_match_no_next_value():
    ll = linkedlist.SortedLinkedList()
    ll.insert(2)

    ll.delete_value(2)

    assert ll.head is None


def test_delete_with_direct_match_next_value():
    ll = linkedlist.SortedLinkedList()
    ll.insert(2)
    ll.insert(3)

    ll.delete_value(2)

    print(1)

    # assert ll.head is None
