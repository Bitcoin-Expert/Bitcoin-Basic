from Classes.client import Client
from Classes.transaction import Transaction
from Classes.block import Block

from Classes.utils import display_transaction

last_block_hash = ""
TPCoins = []

Dinesh = Client()
t0 = Transaction(
    "Genesis",
    Dinesh.identity,
    500.0
)

block0 = Block()

block0.previous_block_hash = None
block0.Nonce = None
block0.verified_transactions.append(t0)

digest = hash(block0)
last_block_hash = digest

TPCoins.append(block0)


def dump_blockchain (self):
   print ("Number of blocks in the chain: " + str(len (self)))
   for x in range (len(TPCoins)):
      block_temp = TPCoins[x]
      print ("block # " + str(x))
      for transaction in block_temp.verified_transactions:
         display_transaction (transaction)
         print ('--------------')
      print ('=====================================')
      
dump_blockchain(TPCoins)