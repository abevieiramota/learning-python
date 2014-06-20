from nose.tools import *
from ex47.game import Room

def setup():
    print 'SETUP!'

def teardown():
    print 'TEAR DOWN!'

def test_room():
    gold = Room('Gold Room', 'Muito ouro')
    
    assert_equal(gold.name, 'Gold Room')
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room('center', 'no centro')
    north = Room('north', 'no norte')
    south = Room('south', 'no sul')

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


