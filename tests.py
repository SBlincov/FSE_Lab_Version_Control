from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    
    # Test One
    key = 'c'
    value = 3
    result = st.add(key, value)
    assert result == 0, "The function did not return a 'success' code"
    val = st.get(key)
    assert val != None, "The added key does not exist in the storage"
    assert val == value, "Value for the key {} is not eqial to expected".format(key)
    
    # Test Two
    key = 'b'
    value = 4
    result = st.add(key, value)
    assert result == 404, "The function did not return an 'unsuccess' code"

def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.remove(key)
    assert st.get(key) is None, 'Expected no key {} in storage'.format(key)

    st = Storage({'a': 1, 'b': 2})

    was_exception = False
    key = 'c'
    try:
        st.remove(key)
    except:
        was_exception = True

    assert was_exception == False, 'Remove of unknown key shouldnt raise exception'
    assert st.get('a') == 1, 'Remove of unknown key shouldnt change Storage'
    assert st.get('b') == 2, 'Remove of unknown key shouldnt change Storage'

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'a'
    value = 3
    st.set(key, value)
    assert st.get(key) == value, "Value for the key {} not equal that has been set {}".format(key, value)
    key = 'c'
    st.set(key, value)
    assert st.get(key) != value, "Value for an unexisting key was set"

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
