from copy import deepcopy

from functions.merged import merged

A, B, C, D = 'abcd'


def test_merged():

    assert merged() == {}

    assert merged({}, {}) == {}

    assert merged(
        {A: 1},
        {B: 2},
        {C: 3},
    ) == {
        A: {1},
        B: {2},
        C: {3},
    }

    assert merged(
        {A: 1},
        {A: 2},
        {A: 3},
    ) == {
        A: {1, 2, 3},
    }

    assert merged(
        {A: 1, B: 2},
        {B: 3, C: 4},
        {C: 5, D: 6},
    ) == {
        A: {1},
        B: {2, 3},
        C: {4, 5},
        D: {6},
    }

    dict1 = {A: 1, B: 2}
    dict2 = {B: 3, C: 4}
    dict1_copy = deepcopy(dict1)
    dict2_copy = deepcopy(dict2)
    assert merged(
        dict1, dict2,
    ) == {
        A: {1},
        B: {2, 3},
        C: {4},
    }
    assert dict1 == dict1_copy
    assert dict2 == dict2_copy
