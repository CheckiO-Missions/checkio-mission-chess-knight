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
        },
        {
            "input": ['h7', 3],
            "answer": ['b4', 'b6', 'b8', 'c3', 'c5', 'c7', 'd2', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f2', 'f3', 'f4', 'f6', 'f7', 'f8', 'g1', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
        },
    ],
    "Extra": [
        {
            "input": ['e5', 1],
            "answer": ['c4', 'c6', 'd3', 'd7', 'f3', 'f7', 'g4', 'g6']
        },
        {
            "input": ['a1', 5],
            "answer": ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
        },
        {
            "input": ['d3', 4],
            "answer": ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
        },
    ]
}
