from rdflib import Graph


QS = {
    1: ("35000", "23000"),
    2: ("15",),
    3 : ("1240", "SHOPPING", "Milan", "LUMEN_Meet1", "2025-09-23", "2025-09-24"),
    4: ("0",),
    5: ("31"),
    6: ("100", "1000", "10000",),
    7: ("31",),
    8: ("100", "Yann", "1000", "50cent", "10000", "Zidane"),
    9: ("36240", "24240"),
    16: ("Yann",),
    17: ("32",),
    18: ("10000",),
    19: ("26400",),
    20: ("1720",),
    21: ("2",),
    22: ("P1", "RP1", "RP2"),
    23: ("143.3333333333333333333333333",),
    24: ("WP2", "WP3", "WP4"),
    25: ("LUMEN_Meet1", "LUMEN_Meet3"),
    26: ("1240",),
    27: ("Milan",),
    28: ("SHOPPING",),
    29: ("LUMEN_Meet1",),
    30: ("P1", "RP1", "RP2", "RP3"),
    31: ("2000",),
    32: ("200",),
    33: ("Yann", "50cent", "Zidane"),
}

g = Graph()
g.parse("test.ttl", format="turtle")

for i in range(1, 19):
    with open(f'query/Q{i}_sparql.txt', 'r', encoding='utf-8') as f:
        query = f.read()

    responses = set()
    for row in g.query(query):
        for value in row:
            responses.add(str(value))

    print("EXPECT:", QS[i])
    print("REPONSE:", responses)

    if all(v in responses for v in QS[i]):
        print(f"QS numero {i} est OK")
    else:
        print(f"QS numero {i} est KO")
    print()
