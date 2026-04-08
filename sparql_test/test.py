from rdflib import Graph

QS = {
    1: ('1918.604651162790697674418604',),
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
    18: ('LUMEN_Meet1', 'LUMEN_Meet3',),
    19: ('3045',),
    20: ("Milan",),
    21: ('SHOPPING',),
    22: ("LUMEN_Meet1",),
    23: ('P1', 'RP1', 'RP3', 'RP2',),
    24: ("2000",),
    25: ("200",),
    26: ("Yann", "50cent", "Zidane",),
    27: ('0.2232558139534883720930232558',),
    28: ('3002.790697674418604651162790',),
    29: ('3045',),
    30: ('3000', '45',),
    31: ('15.34883720930232558139534884',),
    32: ('491.1627906976744186046511629',),
}

g = Graph()
g.parse("test.ttl", format="turtle")

for i in range(1, 33):
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
