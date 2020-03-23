import block
import wallet
import json
import requests

MINING_DIFFICULTY = 5
CAPACITY = 5 # run capacity=1, 5, 10
init_count = -1 #initial id count, accept ids <= 10

class Node:
	def __init__(self,NUM_OF_NODES=None):
		print('node_init')
		self.NBC=100;
		self.wallet=wallet.Wallet()
		self.id=-1 # bootstrap will send the node's final ID
		self.valid_chain=None
		self.ring={} #here we store information for every node, as its id, its address (ip:port) its public key and its balance 


	def broadcast(message,url):
		m = json.dump(message)
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		for other in self.ring:
			requests.post(other+"/"+url, data = m, headers = headers)
		return

	def create_new_block():
		print("create_block")
	
	# def create_wallet():
	# 	#create a wallet for this node, with a public key and a private key
		# print("create_wallet")
		
	
	#add this node to the ring, only the bootstrap node can add a node to the ring after checking his wallet and ip:port address
	#bottstrap node informs all other nodes and gives the request node an id and 100 NBCs
	def register_node_to_ring(self, nodeID, ip, port, public_key):
		if self.id == 0:
			print(self.id)
			self.ring[nodeID] = {'ip': ip,'port': port,'public_key': public_key}
			print('register_node')
		else:
			print('cannot register node')


	def create_transaction(sender, receiver, signature):
		#remember to broadcast it
		print("create_transaction")
		

	def broadcast_transaction(trans):
		print("broadcast_transaction")
		url = "broadcst_trans"
		message = trans.__dict__ #returns attributes as keys, and their values as value
		broadcast(message,url)
		return


	def validate_transaction():
		#use of signature and NBCs balance
		print("validate_transaction")

	def add_transaction_to_block():
		#if enough transactions  mine
		print("add_transaction_to_block")


	def mine_block():
		print("mine_block")


	def broadcast_block(block):
		print("broadcast_block")
		url = "broadcst_block"
		message = block.__dict__
		return

	
	def validate_block(self,block):
		print("validate_block\n")
		return

	def valid_proof(other_parameters, difficulty=MINING_DIFFICULTY):
		print("valid_proof")



	#concencus functions

	def valid_chain(self, chain):
		#check for the longer chain accroose all nodes
		print("valid_chain")

	def resolve_conflicts(self):
		#resolve correct chain
		print("resolve_conflicts")

