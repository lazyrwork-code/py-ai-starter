import asyncio
import time

# Versi BIASA (synchronous) - blocking
def fetch_job_sync(job_title):
    print(f"Fetching {job_title}...")
    time.sleep(1)  # simulasi network request
    return f"{job_title} — Remote — Rp 15jt/bulan"

# Versi ASYNC (asynchronous) - non-blocking
async def fetch_job_async(job_title):
    print(f"Fetching {job_title}...")
    await asyncio.sleep(1)  # simulasi network request
    return f"{job_title} — Remote — Rp 15jt/bulan"

async def main():
    jobs_to_fetch = [
        "Backend Developer",
        "Go Engineer", 
        "AI Engineer"
    ]

    # SYNC — jalan satu per satu
    print("=== SYNC (lambat) ===")
    start = time.time()
    for job in jobs_to_fetch:
        result = fetch_job_sync(job)
        print(result)
    print(f"Total waktu: {round(time.time() - start, 1)} detik\n")

    # ASYNC — jalan bersamaan
    print("=== ASYNC (cepat) ===")
    start = time.time()
    results = await asyncio.gather(*[fetch_job_async(job) for job in jobs_to_fetch])
    for result in results:
        print(result)
    print(f"Total waktu: {round(time.time() - start, 1)} detik")

if __name__ == "__main__":
    asyncio.run(main())