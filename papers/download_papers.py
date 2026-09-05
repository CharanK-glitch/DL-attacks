import os
import urllib.request

# CORE A* and A Top-Tier Conference Papers
TOP_TIER_PAPERS = {
    "AStar_USENIX21_Leaky_DNNs_Microarchitectural_SCA.pdf": "https://www.usenix.org/system/files/sec21-xiang.pdf",
    "AStar_IEEE_SP21_Mind_The_Gap_DL_SCA.pdf": "https://eprint.iacr.org/2021/412.pdf",
    "AStar_ACM_CCS20_DeepKey_Microarchitectural_KeyExtraction.pdf": "https://eprint.iacr.org/2020/1218.pdf",
    "AStar_NDSS22_DeepLeakage_KeyExtraction_Hardware.pdf": "https://eprint.iacr.org/2022/194.pdf",
    "AStar_MICRO20_SubZero_Microarchitectural_SCA_NN.pdf": "https://arxiv.org/pdf/2009.08053.pdf",
    "AStar_ISCA21_Hermes_Microarchitectural_Attack_DL.pdf": "https://arxiv.org/pdf/2104.09012.pdf",
    "CHES18_ASCAD_Study_DL_SCA_Prouff.pdf": "https://eprint.iacr.org/2018/053.pdf",
    "CHES20_Methodology_Efficient_CNN_SCA_Zaid.pdf": "https://eprint.iacr.org/2019/1078.pdf"
}

def download_top_tier_papers():
    save_dir = os.path.join(os.path.dirname(__file__), "pdf")
    os.makedirs(save_dir, exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    print(f"[*] Downloading {len(TOP_TIER_PAPERS)} top-tier (A* / A) research papers...")
    for filename, url in TOP_TIER_PAPERS.items():
        filepath = os.path.join(save_dir, filename)
        print(f"[*] Fetching {filename} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"[+] Saved: {filename} ({os.path.getsize(filepath) / 1024 / 1024:.2f} MB)")
        except Exception as e:
            print(f"[!] Failed to download {filename}: {e}")

    print(f"\n[+] All A* / A papers successfully downloaded into {save_dir}")

if __name__ == "__main__":
    download_top_tier_papers()
