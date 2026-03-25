from rdflib import Graph


QS = {
    1: ("35000", "23000"),
    2: ("15",),
    3 : ("1240", "SHOPPING", "Milan", "LUMEN_Meet1", "2025-09-23", "2025-09-24"),
    4: ('0'),
    5: ('31',), 
    6: ('15.35', 'Yann', '38.37', '50cent', '59.3', 'Zidane'),
    7: ('28400',),
    8: ('50cent',),
    9: ('50cent', 'Yann', 'Zidane',),
    10: ("32",),
    11: ('10000',),
    12: ("26400",),
    13: ("1720",),
    14: ("2",),
    15: ('RP3', 'RP1', 'P1', 'RP2',),
    16: ('143.3333333333333333333333333',),
    17: ('WP4', 'WP2', 'WP3',),
    18: ('LUMEN_Meet1', 'LUMEN_Meet3'),
    19: ('1240',),
    20: ("Milan",),
    21: ('10', '50', '32',),
    22: ("SHOPPING",),
    23: ("LUMEN_Meet1",),
    24: ("P1", "RP1", "RP2", "RP3"),
    25: ("2000",),
    26: ("200",),
    27: ("Yann", "50cent", "Zidane"),
}

g = Graph()
g.parse("test.ttl", format="turtle")

for i in range(1, 27):
    with open(f'query/Q{i}_sparql.txt', 'r', encoding='utf-8') as f:
        query = f.read()

    responses = set()
    for row in g.query(query):
        for value in row:
            responses.add(str(value))

    print("EXPECT:", QS[i])
    print("RESPONSE:", responses)

    if all(v in responses for v in QS[i]):
        print(f"QS numero {i} est OK")
    else:
        print(f"QS numero {i} est KO")
    print()
