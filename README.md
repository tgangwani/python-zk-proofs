This repository contains the code for the paper - ["Distributed and Secure ML with Self-tallying Multi-party Aggregation"](https://arxiv.org/abs/1811.10296), presented at the NeurIPS Workshop on Privacy Preserving Machine Learning, [PPML 2018](https://ppml-workshop.github.io/ppml/).

The project consists of:

- an Elgamal Encryption library implemented over elliptic curves (elgamal.py)
- ZKPoK libraries and test codes  (zkplib/, tests/)
- a Zorro client (zorro.py)
- a test application for cumulative voting (test.py)
- a ledger class simulating the blockchain (ledger.py)

Instruction:
- Python Environment: Python 3.5.2
- To run the test application, use command: python test.py

Acknowledgments:
- https://github.com/j2kun/elliptic-curves-finite-fields
- https://github.com/amiller/python-zk-proofs
