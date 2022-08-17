#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Class Cache
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        # key = self.redis.get("key")
        # if key is None:
        #     key = self.redis.set("key", data)
        return rand_key

    def get(self, key):
        """
        Get data from redis
        """
        value = self._redis.get(key)
        return value.decode('utf-8')
