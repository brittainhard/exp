import pytest


class HashList(list):

    def __hash__(self):
        return 1


@pytest.fixture
def hash_list():
    return HashList([1, 2, 3])


def test_hash(hash_list):
    assert hash(hash_list) == 1
