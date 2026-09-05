import os
import urllib.request

PAPERS = {
    "ASCAD_Study_DL_SCA_Prouff_2018.pdf": "https://eprint.iacr.org/2018/053.pdf",
    "Deep_Learning_SCA_Good_Bad_Ugly_2016.pdf": "https://eprint.iacr.org/2017/974.pdf",
    "Methodology_Efficient_CNN_SCA_Zaid_2019.pdf": "https://eprint.iacr.org/2019/1078.pdf",
    "DL_Microarchitectural_SCA_Mushtaq_2020.pdf": "https://arxiv.org/pdf/2002.04692.pdf",
    "NN_SCA_Embedded_Hardware_Weissbart_2019.pdf": "https://arxiv.org/pdf/1906.07632.pdf",
    "Stealing_ML_Models_API_Tramer_2016.pdf": "https://eprint.iacr.org/2016/928.pdf"
}

def download_research_papers():
    save_dir = os.path.join(os.path.dirname(__file__), "pdf")
    os.makedirs(save_dir, exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    print(f"[*] Starting download of {len(PAPERS)} open-access research papers...")
    for filename, url in PAPERS.items():
        filepath = os.path.join(save_dir, filename)
        if os.path.exists(filepath):
            print(f"[=] Already exists: {filename}")
            continue

        print(f"[*] Downloading {filename} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"[+] Saved: {filename}")
        except Exception as e:
            print(f"[!] Failed to download {filename}: {e}")

    print(f"\n[+] All papers processed in {save_dir}")

if __name__ == "__main__":
    download_research_papers()
