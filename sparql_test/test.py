from rdflib import Graph

for i in range(16,33):
 with open(f'query/QS{i}_sparql.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

    filename = "test.ttl" 

    g = Graph()
    g.parse(filename, format="turtle")

    query = contenu
    for row in g.query(query):
          print(i)
          print(row)



