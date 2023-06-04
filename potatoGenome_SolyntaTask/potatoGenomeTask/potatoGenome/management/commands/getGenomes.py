"""
Defining a Django custom command to call the getPotatoGenomes.py to fetch the requred potato genome data

Created_by : Samhita

Created_Date : 02.June.2023
"""

# Import necessary modules

from django.core.management.base import BaseCommand
from potatoGenome.models import genomeClass
from potatoGenome.getPotatoGenomes import getGenomeData

from datetime import datetime

class Command(BaseCommand):
    help = "Fetches the potato whole genomes and their (meta)data posted after 2018"
        
    def handle(self, *args, **kwargs):
                
        getGenomeData()


            
            
