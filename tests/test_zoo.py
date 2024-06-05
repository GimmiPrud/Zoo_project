import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence  # src.zoo = cartella.file e si importano le funzioni di zoo

class Testzoo(TestCase):

    def setUp(self) -> None: # la funzione setup esiste nella classe Testcase di unittest.
                             # questa funzione però è vuota e serve per inizializzare degli oggetti e variabili che verranno utilizzati per tutti i test 
        pass

    # però è più consigliato utilizzare variabili locali allinterno delle funzoini per i test, invece di variabili globali come quelle della funzione setup
    # Questo perchè durante i test sulle funzionni le variabili potrebbero modificarsi e i test successivi potrebbero essere fallati 

    # Test sul progetto zoo.py:

    def test_animal_dimension(self):

        zookeeper1: ZooKeeper = ZooKeeper(name="Alessio",surname="Carlini",id=379)
        fence1: Fence = Fence(area=100, temperature=21.0,habitat="Savanna")
        animal1: Animal = Animal(name="Bill",species="Felide", age=2, height=10.0,width=20.0, preferred_habitat="Savanna")
        zookeeper1.add_animal(animal1,fence1)
        result: int = len(fence1.animals)
        message: str = f"Error: the function add_animal should not add self.animal1 into self.fence1"

        self.assertEqual(result, 0, message)


    def test_animal_habitat(self):

        zookeeper1: ZooKeeper = ZooKeeper(name="Alessio",surname="Carlini",id=379)
        fence1: Fence = Fence(area=300, temperature=21.0,habitat="jungle")
        animal1: Animal = Animal(name="Bill",species="Felide", age=2, height=10.0,width=1.50, preferred_habitat="Savanna")
        zookeeper1.add_animal(animal1,fence1)
        result: int = len(fence1.animals)
        message: str = f"Error: the function add_animal should not add self.animal1 into self.fence1"

        self.assertEqual(result, 0, message)


    def test_remove_animal(self):
        
        zookeeper1: ZooKeeper = ZooKeeper(name="Alessio",surname="Carlini",id=379)
        fence1: Fence = Fence(area=300, temperature=21.0,habitat="jungle")
        animal1: Animal = Animal(name="Bill",species="Felide", age=2, height=10.0,width=1.50, preferred_habitat="Savanna")
        zookeeper1.remove_animal(animal1,fence1)
        result: int = len(fence1.animals)
        message: str = f"Error: the function remove_animal should not remove self.animal1 into self.fence1"

        self.assertEqual(result, 0, message)
    



if __name__=="__main__":
    unittest.main()

