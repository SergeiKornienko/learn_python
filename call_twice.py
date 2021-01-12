def call_twice(func, *args, **kwargs):
    return (func(*args, **kwargs), func(*args, **kwargs))


if __name__ == '__main__':
    def push_and_count(target, *, value):
        target.append(target)
        return len(target)


    def shoot():
        return 'Bang!'


    def test_call_twice():
        assert call_twice(push_and_count, [], value=42) == (1, 2), (
            "Function should be called twice with same arguments!"
        )
        assert call_twice(shoot) == ('Bang!', 'Bang!')
    print(call_twice(shoot))
