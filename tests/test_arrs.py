from utils import arrs, dicts

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([], -2) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]

def test_get_val():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs") == 'mercurial'
    assert dicts.get_val(data, "abc") == 'git'
    assert dicts.get_val(data, "vcs", "git") == 'mercurial'
    assert dicts.get_val(data, "vcs", "test") == 'mercurial'
    assert dicts.get_val(data, "abc", "test") == 'test'
    data = {}
    assert dicts.get_val(data, "vcs") == 'git'
    assert dicts.get_val(data, "vcs", "git") == 'git'
    assert dicts.get_val(data, "vcs", "bazaar") == 'bazaar'
