import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class Testzoo(TestCase):

    def setUp(self) -> None: # la funzione setup esiste nella classe Testcase di unittest.
                             # questa funzione però è vuota e serve per inizializzare degli oggetti e variabili che verranno utilizzati per tutti i test 
        pass

    # però è più consigliato utilizzare variabili locali allinterno delle funzoini per i test, invece di variabili globali come quelle della funzione setup