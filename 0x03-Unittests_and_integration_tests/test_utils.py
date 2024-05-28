#!/usr/bin/env python3
"""
Parameterize a unit test
"""

from unittest import TestCase
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
)
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """A test class for Nestedmap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> Any:
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
