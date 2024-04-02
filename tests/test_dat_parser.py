from io import StringIO
from ammm_project.parsers.dat import parse


def test_parse_dat():
    content = """x =  5;
y =  7;
c =  5;

n =  5;

// Let's index products with letters: A, B, C, ...

//     A  B  C  D  E  
p = [  4  3  1  3  2  ];
w = [  3  2  1  2  1  ];
s = [  4  4  2  2  2  ];
"""

    dat_file = StringIO(content)

    assignments = parse(dat_file)

    assert assignments == {
        "x": 5,
        "y": 7,
        "c": 5,
        "n": 5,
        "p": [4, 3, 1, 3, 2],
        "w": [3, 2, 1, 2, 1],
        "s": [4, 4, 2, 2, 2],
    }
