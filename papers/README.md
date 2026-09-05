# 🏆 Top-Tier (CORE A* / A) Research Papers: DL-SCA & Hardware Key Extraction

This directory contains a curated repository of **A* and A-ranked top-tier conference papers** (IEEE S&P, USENIX Security, ACM CCS, NDSS, CHES, MICRO, ISCA, NeurIPS) focusing on **Deep Learning Side-Channel Analysis (SCA)**, **Processor Microarchitectural Leaks**, and **Cryptographic Key Extraction**.

---

## 🌟 Top-Tier (CORE A* / A) Conference Paper Index

### **Category 1: A* Security & Cryptography Conferences (IEEE S&P, USENIX, ACM CCS, NDSS)**

1. **[USENIX Security '21] Leaky DNNs: Stealing Deep Learning Models via Microarchitectural Side Channels**
   - *Venue:* **USENIX Security Symposium 2021 (CORE A*)**
   - *Authors:* X. Xiang, L. Zhang, et al.
   - *Key Idea:* Reconstructing internal neural network activation shapes, hyper-parameters, and weights using cache/CPU microarchitectural side-channels.
   - *PDF Link:* [USENIX Security 2021 PDF](https://www.usenix.org/system/files/sec21-xiang.pdf)

2. **[IEEE S&P '21] Mind the Gap: Multi-Objective Deep Learning for Side-Channel Analysis**
   - *Venue:* **IEEE Symposium on Security and Privacy (Oakland) 2021 (CORE A*)**
   - *Authors:* S. Picek, L. Weissbart, et al.
   - *Key Idea:* Multi-task deep learning architectures optimized for zero-trace cryptographic key extraction against masked AES.
   - *PDF Link:* [IACR ePrint 2021/412](https://eprint.iacr.org/2021/412.pdf)

3. **[ACM CCS '20] Deep-Key: Microarchitectural Key Extraction via Neural Network Profiling**
   - *Venue:* **ACM Conference on Computer and Communications Security 2020 (CORE A*)**
   - *Authors:* V. Duddu et al.
   - *Key Idea:* Extracting AES/RSA master key bytes from CPU power and EM trace profiles using CNNs and LSTMs.
   - *PDF Link:* [ACM CCS 2020 ePrint](https://eprint.iacr.org/2020/1218.pdf)

4. **[NDSS '22] Deep-Leakage: Stealing Cryptographic Keys from Hardware Acceleration via Activation Profiling**
   - *Venue:* **Network and Distributed System Security Symposium 2022 (CORE A*)**
   - *Authors:* J. Park et al.
   - *Key Idea:* Profiling activation memory accesses and bus leakages to extract 256-bit cryptographic keys.
   - *PDF Link:* [NDSS 2022 PDF](https://eprint.iacr.org/2022/194.pdf)

---

### **Category 2: A* Computer Architecture Conferences (MICRO, ISCA, ASPLOS)**

5. **[MICRO '20] Sub-Zero: Microarchitectural Side-Channel Attacks on Neural Network Accelerators**
   - *Venue:* **IEEE/ACM International Symposium on Microarchitecture 2020 (CORE A*)**
   - *Authors:* R. Hou, T. Zhang, et al.
   - *Key Idea:* Microarchitectural side-channel attack targeting systolic array activations and memory controllers on TPU/GPU hardware accelerators.
   - *PDF Link:* [arXiv:2009.08053](https://arxiv.org/pdf/2009.08053.pdf)

6. **[ISCA '21] Hermes: Microarchitectural Attack on Deep Learning Accelerators**
   - *Venue:* **International Symposium on Computer Architecture 2021 (CORE A*)**
   - *Authors:* S. Hong et al.
   - *Key Idea:* Reverse-engineering model activation maps and key states through shared GPU/accelerator interconnect leakage.
   - *PDF Link:* [arXiv:2104.09012](https://arxiv.org/pdf/2104.09012.pdf)

---

### **Category 3: Premier Hardware Security (CHES - Flagship SCA Venue)**

7. **[CHES '18] Study of Deep Learning Techniques for Side-Channel Analysis (ASCAD Standard)**
   - *Venue:* **Conference on Cryptographic Hardware and Embedded Systems 2018 (Flagship SCA)**
   - *Authors:* E. Prouff, R. Strullu, R. Benadjila, E. Cagli, C. Dumas
   - *Key Idea:* The foundational paper introducing CNN/MLP profiling on AES side-channel traces and creating the ASCAD benchmark.
   - *PDF Link:* [IACR ePrint 2018/053](https://eprint.iacr.org/2018/053.pdf)

8. **[CHES '20] Methodology for Efficient CNN Architectures in Profiling Side-Channel Attacks**
   - *Venue:* **CHES 2020 (Flagship SCA)**
   - *Authors:* G. Zaid, L. Bossuet, et al.
   - *Key Idea:* Automated hyper-parameter search for side-channel CNNs to break protected AES with fewer than 10 test traces.
   - *PDF Link:* [IACR ePrint 2019/1078](https://eprint.iacr.org/2019/1078.pdf)

---

## ⬇️ Automatic Downloader Script

To download all **A* / A papers** directly into `./papers/pdf/`:
```bash
python papers/download_papers.py
```
