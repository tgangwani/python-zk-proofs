#!/usr/bin/env python
# a test application 

from ledger import Ledger
from zorro import Zorro

def test_app():
    l = Ledger()
    g1 = [2, 3, 3]
    g2 = [1, 2, 2]
    g3 = [1, 1, 1]
    gmax = 5   # range of each element 
    g_length = 3    # length of the vector
    total_bound = 10 # range of the vector

    # Phase 0: initiate
    z1 = Zorro(l, 0, g_length, gmax, total_bound)
    z2 = Zorro(l, 1, g_length, gmax, total_bound)
    z3 = Zorro(l, 2, g_length, gmax, total_bound)

    print("Phase 1: commit...")
    # Phase 1: commit 
    if(l.phase('c') == 1):
        z1.commit(g1)
        z2.commit(g2)
        z3.commit(g3)
    else:
        print("Phase 1 failed!")

    print("Phase 2: proof...")
    # Phase 2: generate zkp proofs
    if(l.phase('p') == 1):
        z1.prove()
        z2.prove()
        z3.prove()
    else:
        print("Phase 2 failed!")

    print("Phase 3: results...")
    # Phase 3: get results
    if(l.phase('r') == 1):
        print(z1.results())
        #z2.results()
        #z3.results()
    else:
        print("Phase 3 failed!")

if __name__=="__main__":
    test_app()
