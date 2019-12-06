from web3 import Web3
from web3.gas_strategies.time_based import fast_gas_price_strategy
import json
import time
web3 = Web3(Web3.HTTPProvider('your http web provider here'))
web3.eth.setGasPriceStrategy(fast_gas_price_strategy)

ETH_SCALE = 1000000000000000000

ADDRESS = "your address here"
KEY = "your key here"

CHIEF = '0x9eF05f7F6deB616fd37aC3c959a2dDD25A54E4F5'
SLATE = '0xF267EFDDA842539a2cAff990259395188a86b813'
ZEROS = '000000000000000000000000'
APPROVAL_8 = '0000000000000000000000000000000000000000000000000000000000000008'

SLATE_185 = '0xb5010b4bc4e506b933c2f0aca7b8214089167e33'
SLATE_205 = '0x606395f1b167aa73134b8a2b34c25bb7d0564920'
SLATE_225 = '0xa3104af92f7c996f7fd73f6b87f16be420d76c71'
SLATE_185_2 = '0xde4000cb884b237efbd6f793584701230e1c45b3'
SLATE_195 = '0x30899738762d84343f615de62c8d1283cc3364da'
SLATE_165 = '0x79ba240edc34f81dd56ff153470e2be3da91e88a'
SLATE_145 = '0x4c3c8aca2758799d697ce83e63fdcce0d52b3cd9'
SLATE_125 = '0x1ead8a37d189a67b1736020131d4890833cf9103'
SLATE_105 = '0x414c6e043c8580ca077250045a1c04b4745ac236'
SLATE_085 = '0x4436a797f8e1cd87f3c674865bc3ea1474c3b0b2'
SLATE_095 = '0x043c52c8ff76c088646c8d2630eddf1a8e33ba4c'
SLATE_055 = '0x168da8afc9d925456c087999ed0f8041a2b7defa'
SLATE_050 = '0xFA635D9093C2dd637CF19d48Df6EA1DBde56DDB1'
SLATE_MCD = '0xF44113760c4f70aFeEb412C63bC713B13E6e202E'
SLATE_040 = '0xF3aB5E963E7c09E205927b9ba498Bb09afe3BC22'
SLATE_OSM = '0x902f009d4dE4a7828284B04b364dD43F00E51A02'
SLATE_DSR_4 = '0xF267EFDDA842539a2cAff990259395188a86b813'

STORAGE_ADDRESS_185 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_185[2:] + APPROVAL_8))
STORAGE_ADDRESS_205 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_205[2:] + APPROVAL_8))
STORAGE_ADDRESS_225 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_225[2:] + APPROVAL_8))
STORAGE_ADDRESS_185_2 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_185_2[2:] + APPROVAL_8))
STORAGE_ADDRESS_195 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_195[2:] + APPROVAL_8))
STORAGE_ADDRESS_165 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_165[2:] + APPROVAL_8))
STORAGE_ADDRESS_145 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_145[2:] + APPROVAL_8))
STORAGE_ADDRESS_125 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_125[2:] + APPROVAL_8))
STORAGE_ADDRESS_105 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_105[2:] + APPROVAL_8))
STORAGE_ADDRESS_085 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_085[2:] + APPROVAL_8))
STORAGE_ADDRESS_095 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_095[2:] + APPROVAL_8))
STORAGE_ADDRESS_055 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_055[2:] + APPROVAL_8))
STORAGE_ADDRESS_050 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_050[2:] + APPROVAL_8))
STORAGE_ADDRESS_MCD = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_MCD[2:] + APPROVAL_8))
STORAGE_ADDRESS_040 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_040[2:] + APPROVAL_8))
STORAGE_ADDRESS_OSM = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_OSM[2:] + APPROVAL_8))
STORAGE_ADDRESS_DSR_4 = web3.toHex(web3.sha3(hexstr='0x' + ZEROS + SLATE_DSR_4[2:] + APPROVAL_8))


CHIEF_ABI = json.loads('[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]')
SLATE_ABI = json.loads('[{"constant":true,"inputs":[],"name":"data","outputs":[{"name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"cast","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"done","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"mana","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"whom","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"whom_","type":"address"},{"name":"mana_","type":"uint256"},{"name":"data_","type":"bytes"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"}]')
SPECIAL_ABI = json.loads('[{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"guy","type":"address"},{"indexed":true,"internalType":"bytes32","name":"foo","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"bar","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"CAP","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MOM","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"cast","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"done","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]')
chief_contract = web3.eth.contract(address=CHIEF, abi=CHIEF_ABI)
slate_contract = web3.eth.contract(address=SLATE, abi=SLATE_ABI)
special_contract = web3.eth.contract(address=SLATE_050, abi=SPECIAL_ABI)

#print('special cap: {0}'.format(special_contract.functions.CAP().call()))

def main():
	previous_bn = web3.eth.blockNumber
	while (True):
		current_bn = web3.eth.blockNumber
		if (previous_bn != current_bn):
			previous_bn = current_bn
			print('\nlift&cast checking block {0}'.format(current_bn))

			# count_185 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_185))))[2:66].lstrip('0'), 16)
			# count_205 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_205))))[2:66].lstrip('0'), 16)
			# count_225 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_225))))[2:66].lstrip('0'), 16)			
			# count_185_2 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_185_2))))[2:66].lstrip('0'), 16)
			# count_165 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_165))))[2:66].lstrip('0'), 16)
			# count_145 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_145))))[2:66].lstrip('0'), 16)
			# count_125 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_125))))[2:66].lstrip('0'), 16)
			# count_105 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_105))))[2:66].lstrip('0'), 16)
			# count_085 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_085))))[2:66].lstrip('0'), 16)
			# count_095 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_095))))[2:66].lstrip('0'), 16)
			# count_055 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_055))))[2:66].lstrip('0'), 16)
			# count_050 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_050))))[2:66].lstrip('0'), 16)
			count_mcd = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_MCD))))[2:66].lstrip('0'), 16)
			count_040 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_040))))[2:66].lstrip('0'), 16)
			count_osm = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_OSM))))[2:66].lstrip('0'), 16)
			count_dsr_4 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_DSR_4))))[2:66].lstrip('0'), 16)

			# print('18.5 count: {0}'.format(count_185 / ETH_SCALE))
			# print('20.5 count: {0}'.format(count_205 / ETH_SCALE))
			# print('22.5 count: {0}'.format(count_225 / ETH_SCALE))
			# print('18.5 count: {0}'.format(count_185_2 / ETH_SCALE))
			# print('16.5 count: {0}'.format(count_165 / ETH_SCALE))
			# print('14.5 count: {0}'.format(count_145 / ETH_SCALE))
			# print('12.5 count: {0}'.format(count_125 / ETH_SCALE))
			# print('10.5 count: {0}'.format(count_105 / ETH_SCALE))
			# print('09.5 count: {0}'.format(count_095 / ETH_SCALE))
			# print('08.5 count: {0}'.format(count_085 / ETH_SCALE))
			# print('05.5 count: {0}'.format(count_055 / ETH_SCALE))
			# print('05.0 count: {0}'.format(count_050 / ETH_SCALE))
			print('MCD  count: {0}'.format(count_mcd / ETH_SCALE))
			print('04.0 count: {0}'.format(count_040 / ETH_SCALE))
			print('OSM  count: {0}'.format(count_osm / ETH_SCALE))
			print('DSR4 count: {0}'.format(count_dsr_4 / ETH_SCALE))
			if ((count_dsr_4 > count_osm) and (count_dsr_4 > count_mcd)):
				do_it()
				exit()

		time.sleep(10)

def do_it():
	previous_bn = web3.eth.blockNumber
	lift_hash = lift_it()
	pending_send_flag = True
	confs = 2
	while(pending_send_flag):
		current_bn = web3.eth.blockNumber
		if (previous_bn != current_bn):
			previous_bn = current_bn
			tx_rec = web3.eth.getTransactionReceipt(lift_hash)
			if(tx_rec is None):
				pending_send_flag = True
			elif(tx_rec['status'] == 1):
				confs -= 1
			elif(tx_rec['status'] == 0):
				print('something went wrong. lift failed')
				pending_send_flag = False
				exit()

			if(confs <= 0):
				cast_it()

		time.sleep(1)


def lift_it():
	nonce = web3.eth.getTransactionCount(ADDRESS)
	gp = web3.eth.generateGasPrice()
	trans = chief_contract.functions.lift(SLATE).buildTransaction({'gas':200000,'gasPrice': gp, 'nonce':nonce })
	signed_trans = web3.eth.account.signTransaction(trans, private_key=KEY)
	trans_hash = web3.eth.sendRawTransaction(signed_trans.rawTransaction)
	print('lifted: {0}'.format(trans_hash.hex()))
	return trans_hash

def cast_it():
	nonce = web3.eth.getTransactionCount(ADDRESS)
	gp = web3.eth.generateGasPrice()
	trans = slate_contract.functions.cast().buildTransaction({'gas':200000,'gasPrice': gp, 'nonce':nonce })
	signed_trans = web3.eth.account.signTransaction(trans, private_key=KEY)
	trans_hash = web3.eth.sendRawTransaction(signed_trans.rawTransaction)
	print('casted: {0}'.format(trans_hash.hex()))
	exit()


if __name__ == "__main__":
	main()
