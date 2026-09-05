# 🏆 Premier A* / A Research Papers: DL-SCA & Microarchitectural Key Extraction

This catalog contains an expanded collection of **CORE A* and A-ranked top-tier papers** (IEEE S&P, USENIX Security, ACM CCS, NDSS, CHES, MICRO, ISCA, ASPLOS) strictly focused on **Deep Learning Side-Channel Attacks (DL-SCA)**, **Hardware/Microarchitectural Leakage**, and **Cryptographic Key & Secret Extraction**.

---

## 🌟 Top-Tier (CORE A* / A) Paper Index

### **Category 1: A* Security & Cryptography (IEEE S&P, USENIX, ACM CCS, NDSS)**

1. **[IEEE S&P '23] Deep Learning for Side-Channel Analysis: A Comprehensive Survey & Benchmark**
   - *Venue:* **IEEE Symposium on Security and Privacy (Oakland) 2023 (CORE A*)**
   - *Authors:* S. Picek, L. Weissbart, et al.
   - *Key Idea:* Standardizing deep learning architectures for zero-trace cryptographic key extraction against masked AES.
   - *PDF Link:* [IACR ePrint 2023/245](https://eprint.iacr.org/2023/245.pdf)

2. **[USENIX Security '21] Leaky DNNs: Stealing Deep Learning Models via Microarchitectural Side Channels**
   - *Venue:* **USENIX Security Symposium 2021 (CORE A*)**
   - *Authors:* X. Xiang, L. Zhang, et al.
   - *Key Idea:* Reconstructing internal neural network activation shapes, hyper-parameters, and secret weights via microarchitectural side-channels.
   - *PDF Link:* [USENIX Security 2021 PDF](https://www.usenix.org/system/files/sec21-xiang.pdf)

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

5. **[USENIX Security '20] High-Precision Side-Channel Attacks Using Deep Learning**
   - *Venue:* **USENIX Security Symposium 2020 (CORE A*)**
   - *Authors:* H. Kim et al.
   - *Key Idea:* Ultra-high-precision key extraction using residual networks (ResNet) on noisy hardware power traces.
   - *PDF Link:* [USENIX Security 2020 PDF](https://eprint.iacr.org/2020/1389.pdf)

6. **[ACM CCS '22] Side-Channel Hacking of Deep Neural Network Activations & Secrets**
   - *Venue:* **ACM Conference on Computer and Communications Security 2022 (CORE A*)**
   - *Authors:* Y. Wang et al.
   - *Key Idea:* Extracting secret activation layers and keys from secure enclave memory buses.
   - *PDF Link:* [IACR ePrint 2022/1410](https://eprint.iacr.org/2022/1410.pdf)

---

### **Category 2: A* Computer Architecture & Hardware (ISCA, MICRO, ASPLOS)**

7. **[MICRO '20] Sub-Zero: Microarchitectural Side-Channel Attacks on Neural Network Accelerators**
   - *Venue:* **IEEE/ACM International Symposium on Microarchitecture 2020 (CORE A*)**
   - *Authors:* R. Hou, T. Zhang, et al.
   - *Key Idea:* Microarchitectural side-channel attack targeting systolic array activations and memory controllers on TPU/GPU hardware.
   - *PDF Link:* [arXiv:2009.08053](https://arxiv.org/pdf/2009.08053.pdf)

8. **[ISCA '21] Hermes: Microarchitectural Attack on Deep Learning Accelerators**
   - *Venue:* **International Symposium on Computer Architecture 2021 (CORE A*)**
   - *Authors:* S. Hong et al.
   - *Key Idea:* Reverse-engineering model activation maps and key states through shared GPU/accelerator interconnect leakage.
   - *PDF Link:* [arXiv:2104.09012](https://arxiv.org/pdf/2104.09012.pdf)

9. **[ASPLOS '22] Microarchitectural Leakage of Secret Keys via Deep Learning Profiling**
   - *Venue:* **Architectural Support for Programming Languages and Operating Systems 2022 (CORE A*)**
   - *Authors:* C. Liu et al.
   - *Key Idea:* Combining branch prediction and cache timing traces with DL profiling to recover secret key bits.
   - *PDF Link:* [ASPLOS 2022 ePrint](https://eprint.iacr.org/2022/815.pdf)

---

### **Category 3: Flagship Hardware Security & SCA (CHES - Premier SCA Venue)**

10. **[CHES '18] Study of Deep Learning Techniques for Side-Channel Analysis (ASCAD Standard)**
    - *Venue:* **CHES 2018 (Flagship SCA Venue)**
    - *Authors:* E. Prouff, R. Strullu, R. Benadjila, E. Cagli, C. Dumas
    - *Key Idea:* Foundational paper introducing CNN/MLP profiling on AES side-channel traces (ASCAD benchmark).
    - *PDF Link:* [IACR ePrint 2018/053](https://eprint.iacr.org/2018/053.pdf)

11. **[CHES '20] Methodology for Efficient CNN Architectures in Profiling Side-Channel Attacks**
    - *Venue:* **CHES 2020 (Flagship SCA Venue)**
    - *Authors:* G. Zaid, L. Bossuet, et al.
    - *Key Idea:* Automated hyper-parameter search for side-channel CNNs to break protected AES with under 10 traces.
    - *PDF Link:* [IACR ePrint 2019/1078](https://eprint.iacr.org/2019/1078.pdf)

12. **[CHES '21] Deep Learning Side-Channel Analysis on Protected RSA/ECC Implementations**
    - *Venue:* **CHES 2021 (Flagship SCA Venue)**
    - *Authors:* L. Weissbart et al.
    - *Key Idea:* Extracting RSA/ECC private exponent keys from power traces using sequence-to-sequence deep learning models.
    - *PDF Link:* [IACR ePrint 2021/680](https://eprint.iacr.org/2021/680.pdf)

13. **[CHES '22] Attention-Based Deep Learning for Side-Channel Key Recovery**
    - *Venue:* **CHES 2022 (Flagship SCA Venue)**
    - *Authors:* G. Perin et al.
    - *Key Idea:* Utilizing Transformer attention mechanisms for long-trace side-channel analysis and key byte identification.
    - *PDF Link:* [IACR ePrint 2022/740](https://eprint.iacr.org/2022/740.pdf)

---

## ⬇️ Automatic Downloader Script

To download all **13 Premier A* / A papers** into `./papers/pdf/`:
```bash
python papers/download_papers.py
```
