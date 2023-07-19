#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """class cache"""
    def __init__(self) -> None:
        """initialize clas cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

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
