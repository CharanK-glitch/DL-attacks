# 📚 Research Literature: Deep Learning Side-Channel & Processor Attacks

This directory contains a curated repository of peer-reviewed and open-access research papers on **Deep Learning-based Side-Channel Analysis (SCA)**, **Processor Microarchitectural Leaks**, and **Cryptographic Key / Secret Extraction**.

---

## 📑 Curated Paper Index

### **Category 1: Deep Learning for Side-Channel Analysis (SCA & Key Recovery)**
1. **Study of Deep Learning Techniques for Side-Channel Analysis (ASCAD Benchmark)**
   - *Authors:* E. Prouff, R. Strullu, R. Benadjila, E. Cagli, C. Dumas
   - *Venue:* CHES / IACR Cryptology ePrint Archive (2018/053)
   - *Focus:* Profiling AES-128 implementations using 1D-CNNs and MLPs; establishing the ASCAD dataset standard for key extraction.
   - *PDF:* [IACR ePrint 2018/053](https://eprint.iacr.org/2018/053.pdf)

2. **Deep Learning Side-Channel Analysis: Good, Bad, and Ugly**
   - *Authors:* H. Maghrebi, T. Portigliatti, E. Prouff
   - *Venue:* Security, Privacy, and Applied Cryptography Engineering (SPACE 2016)
   - *Focus:* Comparing Random Forests, Autoencoders, and CNNs against template attacks for extracting cryptographic keys from hardware power traces.
   - *PDF:* [HAL open science 01344400](https://hal.archives-ouvertes.fr/hal-01344400/document)

3. **Methodology for Efficient CNN Architectures in Profiling Side-Channel Attacks**
   - *Authors:* G. Zaid, L. Bossuet, A. Habrard, H. Venelli
   - *Venue:* CHES 2020 / IACR ePrint (2019/1078)
   - *Focus:* Designing optimal compact CNNs for side-channel key extraction with low trace counts.
   - *PDF:* [IACR ePrint 2019/1078](https://eprint.iacr.org/2019/1078.pdf)

---

### **Category 2: Processor Microarchitecture & Hardware Leaks using ML**
4. **Deep Learning-based Microarchitectural Side-Channel Attacks**
   - *Authors:* M. Mushtaq et al.
   - *Venue:* IEEE Transactions on Computers / arXiv
   - *Focus:* Utilizing deep neural networks to classify CPU cache states, branch predictor traces, and instruction execution patterns to extract secrets.
   - *PDF:* [arXiv:2002.04692](https://arxiv.org/pdf/2002.04692.pdf)

5. **NN-SCA: Neural Network-Assisted Side-Channel Attack on Embedded Hardware**
   - *Authors:* L. Weissbart et al.
   - *Venue:* Journal of Cryptographic Engineering (2021)
   - *Focus:* Deep learning power trace extraction on modern microcontrollers running RSA/ECC signatures and symmetric ciphers.
   - *PDF:* [arXiv:1906.07632](https://arxiv.org/pdf/1906.07632.pdf)

---

### **Category 3: Model Activation Leaks & Reverse Engineering**
6. **Stealing Machine Learning Models via Prediction APIs**
   - *Authors:* F. Tramèr, F. Zhang, N. Juels, M. Reiter, T. Ristenpart
   - *Venue:* USENIX Security Symposium (2016)
   - *Focus:* Reconstructing internal neural network activations, hyper-parameters, and secret model weights via output queries.
   - *PDF:* [USENIX Security 2016](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_tramer.pdf)

---

## ⬇️ How to Download PDF Papers Automatically

Run the helper script:
```bash
python papers/download_papers.py
```
This will fetch open-access PDFs directly into the `./papers/pdf/` folder.
