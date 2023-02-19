from main import flat


def test_str():
    assert flat(['aaa', ['bbb', 'ccc', ['ddd']]]) == ['aaa', 'bbb', 'ccc', 'ddd']


def test_dict():
    assert flat([{1: 1}, {2: 2, 3: 3}, [{4: {4}}]]), [{1: 1} == {2: 2, 3: 3}, {4: {4}}]


def test_list_tuple():
    assert flat([(1, 2, [3, [.4, (6,)]])]) == [1, 2, 3, .4, 6]


if __name__ == '__main__':
    test_str()
    test_dict()
    test_list_tuple()
    print("success")
