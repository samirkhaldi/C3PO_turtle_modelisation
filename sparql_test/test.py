from rdflib import Graph


QS = {16:'Yann',17:"32",18:"10000"}

for i in range(16,19):
 with open(f'query/QS{i}_sparql.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

    filename = "test.ttl" 

    g = Graph()
    g.parse(filename, format="turtle")

    query = contenu
    for row in g.query(query):
          response = str(row[0])
        #   print("longueur row :",len(row))
        #   print("QS numero :",i)
        #   print("réponse :", response)
         
          if QS[i] in response :
             print(QS[i],"est OK")
          else:
             print(QS[i],"est KO")

