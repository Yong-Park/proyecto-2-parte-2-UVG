#codigo obtenido de https://neo4j.com/docs/api/python-driver/current/
from neo4j import GraphDatabase
import logging
import csv
from csv import writer
from neo4j.exceptions import ServiceUnavailable
from neo4j.work.simple import Query
import pandas as pd

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    #para los platillos
    def add_Platillos(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Platillos,message)
            

    @staticmethod
    def _create_and_return_Platillos(tx,message):
        result = tx.run("CREATE (a:Platillos) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)

     #para los tiempos
    def add_Time(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Time,message)
            

    @staticmethod
    def _create_and_return_Time(tx,message):
        result = tx.run("CREATE (a:Tiempo) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        

     #para el contenido nutricional
    def add_Nutricion(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Nutricion,message)
            

    @staticmethod
    def _create_and_return_Nutricion(tx,message):
        result = tx.run("CREATE (a:Nutricion) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)


    #para los precios de los platillos
    def add_Precio(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Precio,message)
            

    @staticmethod
    def _create_and_return_Precio(tx,message):
        result = tx.run("CREATE (a:Precio) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)

    #para los relacion de los platillos
    def add_Relacion(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Relacion,message)
            

    @staticmethod
    def _create_and_return_Relacion(tx,message):
        result = tx.run("CREATE (a:Relacion) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)

    #para realizar la relacion entre paltillo y tiempo
    def add_time_relation(self, message1, message2):
        with self.driver.session() as session:
            session.write_transaction(self.create_time_relation,message1,message2)

    def add_row(filename, listofelement):
        with open(filename, 'a', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(listofelement)

    @staticmethod
    def create_time_relation(tx, message1, message2):
        query = (
            "MATCH (p1:Tiempo {message : $message1}), (p2:Platillos {message: $message2})"
            "CREATE (p1)-[:tiempo]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, message1=message1, message2=message2)

    #para realizar la relacion entre paltillo y precio
    def add_price_relation(self, message1, message2):
        with self.driver.session() as session:
            session.write_transaction(self.create_price_relation,message1,message2)

    @staticmethod
    def create_price_relation(tx, message1, message2):
        query = (
            "MATCH (p1:Precio {message : $message1}), (p2:Platillos {message: $message2})"
            "CREATE (p1)-[:precio]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, message1=message1, message2=message2)

    #para realizar la relacion entre paltillo y nutricion
    def add_nutricion_relation(self, message1, message2):
        with self.driver.session() as session:
            session.write_transaction(self.create_nutricion_relation,message1,message2)

    @staticmethod
    def create_nutricion_relation(tx, message1, message2):
        query = (
            "MATCH (p1:Nutricion {message : $message1}), (p2:Platillos {message: $message2})"
            "CREATE (p1)-[:nutricion]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, message1=message1, message2=message2)

    #para realizar la relacion entre paltillo y relacion
    def add_relation_relation(self, message1, message2):
        with self.driver.session() as session:
            session.write_transaction(self.create_relation_relation,message1,message2)

    @staticmethod
    def create_relation_relation(tx, message1, message2):
        query = (
            "MATCH (p1:Relacion {message : $message1}), (p2:Platillos {message: $message2})"
            "CREATE (p1)-[:ingrediente]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, message1=message1, message2=message2)

    def delete_relationship(self, message):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._delete_and_return_relationship, message)

    # Eliminación de relación
    @staticmethod
    def _delete_and_return_relationship(tx, message):
        query = (
            "MATCH (p1:Platillos {message: $message}) "
            "DETACH DELETE p1"
        )
        result = tx.run(query, message=message)
        try:
            return [{"p1": row["p1"]["message"]}
                    for row in result]
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
    
    @staticmethod
    def delete_platillo(nombre):
        updatedlist=[]
        with open("export.csv",newline="") as platillos:
            reader = csv.reader(platillos)
            platillo_eliminar = nombre

        for row in reader: #for every row in the file
            
            if row[0]!=platillo_eliminar: #as long as the username is not in the row .......
                updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      
        print(updatedlist)
        updatefileDeleted(updatedlist)

    def updatefileDeleted(updatedlist):
        with open("export.csv","w",newline="") as platillos:
            Writer=csv.writer(platillos)
            Writer.writerows(updatedlist)
    
    
    #buscar y mostrar las relaciones que tiene el nodo
    def find_node(self, node):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_node, node)
            #for record in result:
                #print("Found person: {record}".format(record=record))

    @staticmethod
    def _find_and_return_node(tx, node):
        query = (
            "Match (n)-[r]->(m:Platillos{message:'$node'})"
            "Return n"
        )
        result = tx.run(query, node=node)
        properties = result.values()
        print(properties)
        #return [record["message"] for record in result]


    #para agregar al neo4j el data que el usuario desea
    def add_newPlatillo(self,message,price,time,nutrition,relation,base):
        with self.driver.session() as session:
            result = session.write_transaction(self._add_and_return_node,message,price,time,nutrition,relation,base)

    @staticmethod
    def _add_and_return_node(tx,message,price,time,nutrition,relation,base):
        #creara el nodo
        result = tx.run("CREATE (a:Platillos) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        #realizar la relacion entre el nodo y su precio
        if(price==("alto")):
            query = (
            "MATCH (p1:Precio {message : $price}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:precio]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, price=price, message=message)
        elif(price==("medio")):
            query = (
            "MATCH (p1:Precio {message : $price}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:precio]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, price=price, message=message)
        elif(price==("bajo")):
            query = (
            "MATCH (p1:Precio {message : $price}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:precio]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, price=price, message=message)

        #realizar la relacion entre el nodo y su tiempo
        if(time==("rapido")):
            query = (
            "MATCH (p1:Tiempo {message : $time}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:tiempo]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, time=time, message=message)
        elif(time==("medio")):
            query = (
            "MATCH (p1:Tiempo {message : $time}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:tiempo]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, time=time, message=message)
        elif(time==("lento")):
            query = (
            "MATCH (p1:Tiempo {message : $time}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:tiempo]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, time=time, message=message)

        #realizar la relacion entre el nodo y su nutricion
        if(nutrition==("alta")):    
            query = (
            "MATCH (p1:Nutricion {message : $nutrition}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:nutricion]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, nutrition=nutrition, message=message)
        elif(nutrition==("media")):
            query = (
            "MATCH (p1:Nutricion {message : $nutrition}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:nutricion]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, nutrition=nutrition, message=message)
        elif(nutrition==("baja")):
            query = (
            "MATCH (p1:Nutricion {message : $nutrition}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:nutricion]->(p2) "
            "RETURN p1, p2"
            )
            result = tx.run(query, nutrition=nutrition, message=message)
        
        #realizar la relacion entre el nodo y su relacion
        query = (
            "MATCH (p1:Relacion {message : $relation}), (p2:Platillos {message: $message})"
            "CREATE (p1)-[:ingrediente]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, relation=relation, message=message)
        

    #para generar los nodos del export.csv
    def Constructor(self,url,password):
        greeter = HelloWorldExample(url, "neo4j", password)
        df = pd.read_csv("export.csv")
        transaction_list = df.values.tolist()
        transaction_execution_commands = []
        #para agregar los platillos a los nodos
        for i in transaction_list:
            greeter.add_Platillos(str(i[0]))

        #agregar los tiempos a los nodos
        greeter.add_Time("rapido")
        greeter.add_Time("medio")
        greeter.add_Time("lento")

        #agregar los tipos de nutricio
        greeter.add_Nutricion("alta")
        greeter.add_Nutricion("media")
        greeter.add_Nutricion("baja")

        #agregar los precios 
        greeter.add_Precio("alto")
        greeter.add_Precio("medio")
        greeter.add_Precio("bajo")


        #agregar las relaciones de los alimentos
        relacion =[]
        for i in transaction_list:
            data = str(i[4]).split()
            for j in data:
                if(not relacion.__contains__(j)):
                    relacion.append(j)

        #agregar las relaciones como nodos al neo4j
        for i in relacion:
            greeter.add_Relacion(i)       

        #para realizar la relacion entre platillo y tiempo        
        for i in transaction_list:
            lista = str(i[2]).split()
            for j in lista:
                if(j==("rapido")):
                    greeter.add_time_relation("rapido",str(i[0]))
                elif(j==("medio")):
                    greeter.add_time_relation("medio",str(i[0]))
                elif(j==("lento")):
                    greeter.add_time_relation("lento",str(i[0]))

        #para realizar la relacion entre platillo y precio
        for i in transaction_list:
            lista = str(i[1]).split()
            for j in lista:
                if(j==("alto")):
                    greeter.add_price_relation("alto",str(i[0]))
                elif(j==("medio")):
                    greeter.add_price_relation("medio",str(i[0]))
                elif(j==("bajo")):
                    greeter.add_price_relation("bajo",str(i[0]))


        #para realizar la relacion entre platillo y nutricion
        for i in transaction_list:
            lista = str(i[3]).split()
            for j in lista:
                if(j==("alta")):
                    greeter.add_nutricion_relation("alta",str(i[0]))
                elif(j==("media")):
                    greeter.add_nutricion_relation("media",str(i[0]))
                elif(j==("baja")):
                    greeter.add_nutricion_relation("baja",str(i[0]))

            #para realizar la relacion entre platillo y relacion
        for i in transaction_list:
            lista = str(i[4]).split()
            for j in lista:
                for k in relacion:
                    if(j==k):
                        greeter.add_relation_relation(j,str(i[0]))

        return greeter