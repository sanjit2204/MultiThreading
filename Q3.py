import os
import time
import threading
import requests
from urllib.parse import urlparse

def download_file(url, output_dir="downloads"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = f"file_{int(time.time())}.dat"
        
        filepath = os.path.join(output_dir, filename)

        start = time.time()
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        duration = time.time() - start
        print(f"[✔] Downloaded {filename} ({total_size/1024:.1f} KB) in {duration:.2f} seconds")
        return True

    except Exception as e:
        print(f"[✖] Failed to download {url}: {e}")
        return False

def sequential_download(urls, output_dir="downloads"):
    print("\n Starting sequential download...")
    start_time = time.time()
    success = 0

    for url in urls:
        if download_file(url, output_dir):
            success += 1

    elapsed = time.time() - start_time
    print(f"\n Sequential completed: {success}/{len(urls)} files in {elapsed:.2f} seconds")
    return elapsed

def threaded_download(urls, output_dir="downloads", max_threads=5):
    print(f"\n🧵 Starting threaded download with {max_threads} threads...")
    start_time = time.time()
    success_count = [0]
    semaphore = threading.Semaphore(max_threads)
    threads = []

    def task(url):
        with semaphore:
            if download_file(url, output_dir):
                success_count[0] += 1

    for url in urls:
        thread = threading.Thread(target=task, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    print(f"\n Threaded completed: {success_count[0]}/{len(urls)} files in {elapsed:.2f} seconds")
    return elapsed

def main():
    print(" Concurrent File Downloader (Sample URLs Only)")
    print("===============================================")

    sample_urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.netflix.com"
    ]

    print("\nSample URLs to be downloaded:")
    for url in sample_urls:
        print(f"- {url}")

    output_dir = "downloads"
    max_threads = 5

    seq_time = sequential_download(sample_urls, output_dir)
    thd_time = threaded_download(sample_urls, output_dir, max_threads)

    speedup = seq_time / thd_time if thd_time > 0 else 0
    print("\n Performance Comparison:")
    print(f"- Sequential time: {seq_time:.2f} sec")
    print(f"- Threaded time:   {thd_time:.2f} sec")
    print(f"- Speedup:         {speedup:.2f}x")

    print("\n Finished downloading files.")

if __name__ == "__main__":
    main()
