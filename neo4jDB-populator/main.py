import random
import time
import numpy as np
import pandas as pd
from neo4j import GraphDatabase
from random_italian_person import RandomItalianPerson


class PopulateDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.people = []

    def close(self):
        self.driver.close()

    def create_people(self):
        with self.driver.session() as session:
            for i in range(100):
                person = RandomItalianPerson()
                ssn_created = session.write_transaction(self._create_person, person.name, person.surname,
                                                        person.data["codice_fiscale"], person.birthdate, person.sex,
                                                        person.birthplace)
                self.people.append(ssn_created)
                print(ssn_created + " created")
            # print(greeting1)

    def create_family(self, towns, addresses, num_family):
        with self.driver.session() as session:
            for i in range(num_family):
                town = random.choice(towns)
                address = random.choice(addresses)
                id_house = session.write_transaction(self._create_house, town[0], address[0])
                ssn_family = []
                for j in range(random.randint(1, 6)):
                    person = RandomItalianPerson()
                    ssn_family_member = session.write_transaction(self._create_person, person.name, person.surname,
                                                                  person.data["codice_fiscale"], person.birthdate,
                                                                  person.sex,
                                                                  person.birthplace)
                    ssn_family.append(ssn_family_member)

                session.write_transaction(self._create_lives, ssn_family, id_house)

    def clear_db(self):
        with self.driver.session() as session:
            session.write_transaction(self._clear_db)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    @staticmethod
    def _create_person(tx, name, surname, ssn, birth, sex, birthplace):
        result = tx.run("CREATE (a:Person {"
                        "name : $name,"
                        "surname : $surname,"
                        "ssn : $ssn, "
                        "birthdate : $birth,"
                        "sex : $sex,"
                        "birthplace : $birthplace"
                        "}) "
                        "RETURN a.ssn", name=name, surname=surname, ssn=ssn, birth=birth, sex=sex,
                        birthplace=birthplace)
        return result.single()[0]

    @staticmethod
    def _create_house(tx, town, address):
        result = tx.run("CREATE (a:House {"
                        "town : $town,"
                        "address : $address"
                        "}) "
                        "RETURN id(a)", town=town, address=address)
        return result.single()[0]

    @staticmethod
    def _create_lives(tx, ssn_family, id_house):
        for ssn in ssn_family:
            result = tx.run("MATCH (a:Person), (b:House) "
                            "WHERE a.ssn = $ssn AND id(b) = $id_house "
                            "CREATE (a)-[r:LIVES]->(b)"
                            "RETURN r ", ssn=ssn, id_house=id_house)
        return result.single()[0]

    @staticmethod
    def _clear_db(tx):
        result = tx.run("MATCH (n) DETACH DELETE n")
        result_summary = result.consume()
        print("Deleted " + str(result_summary.counters.nodes_deleted) + " nodes")


if __name__ == "__main__":
    """
    txt_parser = NameParser()
    names = pd.read_csv('nomi.txt', sep='\n')
    surnames = pd.read_csv('cognomi.txt', sep='\n', header=None)
    """
    towns = pd.read_csv('comuni.csv', header=None)
    addresses = pd.read_csv('addresses.csv', header=None)
    """
    sex = ["M", "F"]
    """
    populator = PopulateDB("bolt://localhost:7687", "neo4j", "neo4jnew")
    populator.clear_db()
    # populator.create_people()
    populator.create_family(towns.values.tolist(), addresses.values.tolist(), 5)
    populator.close()