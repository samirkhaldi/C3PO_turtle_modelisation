import sys
sys.stdout.reconfigure(encoding='utf-8')

from rdflib import Graph

QS = {
    1: ('1918.604651162790697674418604',),
    2: ("0.2930232558139534883720930232",),
    3 : ('Milan', 'LUMEN_Meet1', '2027-11-20', '2025-09-24', '2027-11-30', '3045.0', '0', 'LUMEN_Meet3', 'Stockholm', 'WP2', 'SHOPPING', '2025-09-23'),
    4: ('3045.0',),
    5: ('https://www.turtle_tutorial.com/WP4', '0.2232558139534883720930232558',), 
    6: ('15.35', 'Yann', '38.37', '50cent', '59.3', 'Zidane'),
    7: ('RP3', '0', 'RP1', 'P1', '159.8837209302325581395348837', '6270.697674418604651162790698', 'RP2'),
    8: ('50cent',),
    9: ('50cent', 'Yann', 'Zidane',),
    10: ("32",),
    11: ('Zidane', '59.3'),
    12: ("26400",),
    13: ("1720",),
    14: ("P1Y",),
    15: ('RP3', 'RP1', 'P1', 'RP2',),
    16: ('143.3333333333333333333333333',),
    17: ('WP4', 'WP2', 'WP3',),
    18: ('LUMEN_Meet2', 'LUMEN_Meet1', 'LUMEN_Meet3',),
    19: ('3045.0',),
    20: ("Milan",),
    21: ('SHOPPING',),
    22: ("LUMEN_Meet1",),
    23: ('P1', 'RP1',),
    24: ("2000",),
    25: ("200",),
    26: ("Yann", "50cent", "Zidane",),
    27: ('https://www.turtle_tutorial.com/LUMEN',),
    28: ('10', 'Yann', 'Zidane', '32',),
    29: ('0.2232558139534883720930232558',),
  #  30: ('3000', '45',),
   # 31: ('15.34883720930232558139534884',),
    #32: ('491.1627906976744186046511629',),
}

g = Graph()
g.parse("testV3.ttl", format="turtle")

for i in range(1, 30):
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