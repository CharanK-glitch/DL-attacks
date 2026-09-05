import os
from google.cloud import storage

def upload_dataset_to_gcs(local_path: str, bucket_name: str, gcs_destination: str):
    """Uploads local dataset directory or archive to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    if os.path.isfile(local_path):
        blob = bucket.blob(gcs_destination)
        print(f"[*] Uploading {local_path} -> gs://{bucket_name}/{gcs_destination}...")
        blob.upload_from_filename(local_path)
        print("[+] Upload complete!")
    elif os.path.isdir(local_path):
        for root, _, files in os.walk(local_path):
            for file in files:
                full_local_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_local_path, local_path)
                gcs_path = os.path.join(gcs_destination, rel_path)
                blob = bucket.blob(gcs_path)
                print(f"[*] Uploading {full_local_path} -> gs://{bucket_name}/{gcs_path}...")
                blob.upload_from_filename(full_local_path)
        print("[+] Directory sync complete!")

def download_dataset_from_gcs(bucket_name: str, gcs_source: str, local_destination: str):
    """Downloads dataset from Google Cloud Storage to local disk fast."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    os.makedirs(local_destination, exist_ok=True)
    blobs = bucket.list_blobs(prefix=gcs_source)

    for blob in blobs:
        rel_path = os.path.relpath(blob.name, gcs_source)
        local_file_path = os.path.join(local_destination, rel_path)
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        print(f"[*] Downloading gs://{bucket_name}/{blob.name} -> {local_file_path}...")
        blob.download_to_filename(local_file_path)
    print("[+] GCS Download complete!")
