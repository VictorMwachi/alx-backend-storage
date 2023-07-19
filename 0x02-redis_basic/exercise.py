#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from Typing import Union


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
