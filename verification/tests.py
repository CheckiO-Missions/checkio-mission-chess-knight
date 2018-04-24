"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['a1', 1],
            "answer": ['b3', 'c2']
        },
        {
            "input": ['h8', 2],
            "answer": ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
        }
    ],
    "Extra": [
        {
            "input": ['e5', 1],
            "answer": ['c4', 'c6', 'd3', 'd7', 'f3', 'f7', 'g4', 'g6']
        }
    ]
}
