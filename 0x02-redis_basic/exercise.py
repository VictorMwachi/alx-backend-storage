#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that
    key every time the method is called and returns the value
    returned by the original method.
    """
    @wraps(method)
    def caller(self, *args, **kwargs) -> Any:
        """calls the given method after incrementing its call counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return caller


def call_history(method: Callable) -> Callable:
    '''Tracks the call details of a method in a Cache class.
    '''
    @wraps(method)
    def caller(self, *args, **kwargs) -> Any:
        '''Returns the method's output after storing its inputs and output.
        '''
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return caller


def replay(fn: Callable) -> None:
    '''Displays the call history of a Cache class' method.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    func_name = fn.__qualname__
    in_key = '{}:inputs'.format(func_name)
    out_key = '{}:outputs'.format(func_name)
    func_call_count = 0
    if redis_store.exists(func_name) != 0:
        func_call_count = int(redis_store.get(func_name))
    print('{} was called {} times:'.format(func_name, func_call_count))
    func_inputs = redis_store.lrange(in_key, 0, -1)
    func_outputs = redis_store.lrange(out_key, 0, -1)
    for func_input, func_output in zip(func_inputs, func_outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            func_input.decode("utf-8"),
            func_output,
        ))


class Cache:
    """class cache"""
    def __init__(self) -> None:
        """initialize clas cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid)
        store the input data in Redis using the random key and
        return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[bytes, str, float, int]:
        """
        take a key string argument and an optional Callable argument named fn.
        This callable will be used to convert the data back
        to the desired format.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """will automatically parametrize Cache.get to str"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """will automatically parametrize Cache.get to int"""
        return self.get(key, lambda x: int(x))
