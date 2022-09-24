import os
from web3 import Web3
from ens import ENS
from termcolor import colored
import random
os.system('color')

# Added multiple APIs to avoid request limitation
infuraProjectId = ["b7bc52eb73a7431e95ef7190a65ca32f", "a3d66728cec04581a14a2605f3209b14", "e95c2f334836431e8c1ae4ce892a9642"]



freeList = []

def get_Random_Api():
    randomize = random.randint(0, len(infuraProjectId) - 1)
    randomApi = infuraProjectId[randomize]
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + randomApi))
    ns = ENS.fromWeb3(w3)
    return ns


# Version 1 - Check from .txt file

with open("words.txt", "r") as file:
    cnt = 0
    for line in file:
        freeList.append(line.rstrip())
        print('Loading domains: [%d]\r'%(cnt), end="")
        cnt += 1

counter = 0
freeCounter = 0
lastFree = ""
for domain in freeList:
    ns = get_Random_Api()
    owner = ns.owner(domain)
    counter += 1

    if owner == "0x0000000000000000000000000000000000000000":
        with open('freeList.txt', "a", encoding='utf-8') as myfile:
            myfile.write(domain + "\n")
            freeCounter += 1
            lastFree = domain

    print('Checking domains: [%d]/[{}] - Owner: [%s] - - - Free: [%d] - - - Last free domain: [%s]\r'.format(len(freeList) - 1)%(counter,owner, freeCounter, lastFree), end="")
