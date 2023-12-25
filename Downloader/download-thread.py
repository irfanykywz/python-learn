# https://www.blackbox.ai/
# download multi thread python

import threading
import requests

def download_chunk(url, start, end, file_path):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 206:
        with open(file_path, 'wb+') as f:
            f.seek(start)
            f.write(response.content)
            f.flush()
    else:
        print(f"Error {response.status_code} downloading chunk")

def download_file(url, num_threads=4):
    response = requests.head(url)
    file_size = int(response.headers.get('content-length', 0))
    

    if file_size <= 0:
        print("Cannot download file")
        return
    
    chunk_size = file_size // num_threads
    threads = []
    file_path = 'asu.mp4'

    for i in range(num_threads):
        start = i * chunk_size
        end = (i+1) * chunk_size - 1 if i < num_threads - 1 else file_size
        thread = threading.Thread(target=download_chunk, args=(url, start, end, file_path))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print(f"Download complete: {file_path}")

url = "https://scontent-xsp1-1.xx.fbcdn.net/o1/v/t2/f1/m69/GGlZyBbDBk2Q7FkIAMHp3pO7v8lcbmdjAAAF.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ht=scontent-xsp1-1.xx.fbcdn.net&_nc_cat=104&_nc_eui2=AeGlIge-wiu39cDyr9_a8FU7XGU9VBs0S5VcZT1UGzRLlUP_4FVLfBAULhcGMTdbRvENyEOXfhojEk-y3DjP47k4&strext=1&vs=a0a77228e5e91cbf&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR2xaeUJiREJrMlE3RmtJQU1IcDNwTzd2OGxjYm1kakFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dJZ3k1eFEtdzJnUjhBQUJBRWk3Wl8zV2VPNXhidjRHQUFBRhUCAsgBAEsHiBJwcm9ncmVzc2l2ZV9yZWNpcGUBMQ1zdWJzYW1wbGVfZnBzABB2bWFmX2VuYWJsZV9uc3ViACBtZWFzdXJlX29yaWdpbmFsX3Jlc29sdXRpb25fc3NpbQAoY29tcHV0ZV9zc2ltX29ubHlfYXRfb3JpZ2luYWxfcmVzb2x1dGlvbgAddXNlX2xhbmN6b3NfZm9yX3ZxbV91cHNjYWxpbmcAEWRpc2FibGVfcG9zdF9wdnFzABUAJQAcjBdAAAAAAAAAABERAAAAJrSPx7vI5qMEFQIoAkMzGAt2dHNfcHJldmlldxwXQFHxBiTdLxsYIWRhc2hfZ2VuMmh3YmFzaWNfaHEyX2ZyYWdfMl92aWRlbxIAGBh2aWRlb3MudnRzLmNhbGxiYWNrLnByb2Q4ElZJREVPX1ZJRVdfUkVRVUVTVBsKiBVvZW1fdGFyZ2V0X2VuY29kZV90YWcGb2VwX2hkE29lbV9yZXF1ZXN0X3RpbWVfbXMBMAxvZW1fY2ZnX3J1bGUHdW5tdXRlZBNvZW1fcm9pX3JlYWNoX2NvdW50BjI0NTE2OBFvZW1faXNfZXhwZXJpbWVudAAMb2VtX3ZpZGVvX2lkEDE2NzIwODI2NjMyNDI1MDkSb2VtX3ZpZGVvX2Fzc2V0X2lkDzkyMzM1NjY5NTQxODU4NBVvZW1fdmlkZW9fcmVzb3VyY2VfaWQQMTIwNDYyNzc5MzU2ODczMBxvZW1fc291cmNlX3ZpZGVvX2VuY29kaW5nX2lkEDEzOTY4MDQ0Njc5MDg2NDAOdnRzX3JlcXVlc3RfaWQAJQIcACW%2BARsHiAFzBDExMDICY2QKMjAyMy0wNi0wNQNyY2IGMjQ1MTAwA2FwcBRGYWNlYm9vayBmb3IgQW5kcm9pZAJjdA5GQl9TSE9SVFNfUE9TVBNvcmlnaW5hbF9kdXJhdGlvbl9zBjcxLjc3MwJ0cxVwcm9ncmVzc2l2ZV9lbmNvZGluZ3MA&ccb=9-4&oh=00_AfDNjFVWGS0s2zeQI7P6GvrwcGa4bSFHZevwZq9lL9UUVQ&oe=6580C9D6&_nc_sid=1d576d&_nc_rid=117835399270092&_nc_store_type=1"
download_file(url)