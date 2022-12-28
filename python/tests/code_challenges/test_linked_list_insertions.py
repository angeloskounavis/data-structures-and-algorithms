import pytest
from data_structures.linked_list import LinkedList, TargetError


@pytest.mark.skip("TODO")
def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_exists():
    assert LinkedList


def test_instantiate():
    assert LinkedList()


def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


def test_to_string_empty():
    linked_list = LinkedList()
    assert str(linked_list) == "NULL"


def test_to_string_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{'apple'} -> NULL"


def test_to_string_double():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{'apple'} -> NULL"
    linked_list.insert("banana")
    assert str(linked_list) == "{'banana'} -> {'apple'} -> NULL"


def test_includes_true():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    assert linked_list.includes("apple")


def test_includes_false():
    linked_list = LinkedList()
    linked_list.insert("apple")

