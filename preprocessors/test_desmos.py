import unittest

import desmos

MOCK_CONTENT = """
# Chapter 1

Something here.

```desmos
{
    "expression": "x"
}
```

```desmos
{
    "expression": "x^2"
}
```

And here maybe?
"""


class TestDesmos(unittest.TestCase):
    def test_add_desmos(self):
        desmos.add_desmos(MOCK_CONTENT)


if __name__ == "__main__":
    unittest.main()
