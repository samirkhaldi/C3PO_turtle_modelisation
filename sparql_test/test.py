from rdflib import Graph

QS = {
    1: ('3002.790697674418604651162790',),
    2: ("0.2930232558139534883720930232",),
    3 : ('2025-11-20', 'WP2', '3045', 'Stockholm', 'LUMEN_Meet3', '2025-11-30'),
    4: ('3045',),
    5: ('https://www.turtle_tutorial.com/WP4', '0.2232558139534883720930232558',), 
    6: ('15.35', 'Yann', '38.37', '50cent', '59.3', 'Zidane'),
    7: ('P1','4129.186046511627906976744186','RP3','1918.604651162790697674418604'),
    8: ('50cent',),
    9: ('50cent', 'Yann', 'Zidane',),
    10: ("32",),
    11: ('Zidane', '59.3'),
    12: ("26400",),
    13: ("1720",),
    14: ("2",),
    15: ('RP3', 'RP1', 'P1', 'RP2',),
    16: ('143.3333333333333333333333333',),
    17: ('WP4', 'WP2', 'WP3',),
    18: ('LUMEN_Meet1', 'LUMEN_Meet3'),
    19: ('3045',),
    20: ("Milan",),
    21: ('10', '50', '32',),
    22: ("SHOPPING",),
    23: ("LUMEN_Meet1",),
    24: ("P1", "RP1", "RP2", "RP3"),
    25: ("2000",),
    26: ("200",),
    27: ("Yann", "50cent", "Zidane"),
    28: ('0.2232558139534883720930232558',),
    29: ('3002.790697674418604651162790',),
    30: ('3045',),
    31: ('3000', '45'),
    32: ('15.34883720930232558139534884',),
    33: ('491.1627906976744186046511629',)
}

g = Graph()
g.parse("test.ttl", format="turtle")

for i in range(1, 34):
    with open(f'query/Q{i}_sparql.txt', 'r', encoding='utf-8') as f:
        query = f.read()

    responses = set()
    for row in g.query(query):
        for value in row:
            responses.add(str(value))

    print("EXPECT:", QS[i])
    print("RESPONSE:", responses)

    if all(v in responses for v in QS[i]):
        print(f"Request : {i} ✅")
    else:
        print(f"Request : {i} ❌")
    print()
