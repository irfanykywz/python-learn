import requests
from tqdm import tqdm


def download(url: str, fname: str, chunk_size=1024):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)


download('https://scontent-cgk1-2.xx.fbcdn.net/o1/v/t2/f1/m69/GEK31Rfas6DsZ1MCAMkfbYkLrB0bbmdjAAAF.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ht=scontent-cgk1-2.xx.fbcdn.net&_nc_cat=101&_nc_eui2=AeFcoB2BOVj4ziaD-lzn-yIpF94RBK5mF9AX3hEErmYX0EgBk30_KePLHxz7STmKdDKyLlYY1GlgLFY8HhydAbqc&strext=1&vs=f7d087de45181eae&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRUszMVJmYXM2RHNaMU1DQU1rZmJZa0xyQjBiYm1kakFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dBd1IxaGZhWmphVWNPMEVBRk5TR2tTOWVGNUZidjRHQUFBRhUCAsgBAEsHiBJwcm9ncmVzc2l2ZV9yZWNpcGUBMQ1zdWJzYW1wbGVfZnBzABB2bWFmX2VuYWJsZV9uc3ViACBtZWFzdXJlX29yaWdpbmFsX3Jlc29sdXRpb25fc3NpbQAoY29tcHV0ZV9zc2ltX29ubHlfYXRfb3JpZ2luYWxfcmVzb2x1dGlvbgAddXNlX2xhbmN6b3NfZm9yX3ZxbV91cHNjYWxpbmcAEWRpc2FibGVfcG9zdF9wdnFzABUAJQAcjBdAAAAAAAAAABERAAAAJq76xoX%2FofwEFQIoAkMzGAt2dHNfcHJldmlldxwXQGaDMzMzMzMYIWRhc2hfZ2VuMmh3YmFzaWNfaHEyX2ZyYWdfMl92aWRlbxIAGBh2aWRlb3MudnRzLmNhbGxiYWNrLnByb2Q4ElZJREVPX1ZJRVdfUkVRVUVTVBsKiBVvZW1fdGFyZ2V0X2VuY29kZV90YWcGb2VwX2hkE29lbV9yZXF1ZXN0X3RpbWVfbXMBMAxvZW1fY2ZnX3J1bGUHdW5tdXRlZBNvZW1fcm9pX3JlYWNoX2NvdW50BDk2NTIRb2VtX2lzX2V4cGVyaW1lbnQADG9lbV92aWRlb19pZA8yODQ3OTcxMTExOTMxNDkSb2VtX3ZpZGVvX2Fzc2V0X2lkEDEwMjQ0NjIwOTg4Nzk2NjYVb2VtX3ZpZGVvX3Jlc291cmNlX2lkEDEzOTkxNjI3Nzc2ODk3NTEcb2VtX3NvdXJjZV92aWRlb19lbmNvZGluZ19pZBAyMjMxMjM1NTkwNDAxNzQwDnZ0c19yZXF1ZXN0X2lkACUCHAAlxAEbB4gBcwQ0MTk1AmNkCjIwMjMtMTEtMDcDcmNiBDk2MDADYXBwBVZpZGVvAmN0GUNPTlRBSU5FRF9QT1NUX0FUVEFDSE1FTlQTb3JpZ2luYWxfZHVyYXRpb25fcwYxODAuMTMCdHMVcHJvZ3Jlc3NpdmVfZW5jb2RpbmdzAA%3D%3D&ccb=9-4&oh=00_AfCGbgKC7jwysP-NTYtf1uqmq_vee7WFYWDVJC8mb-Nh9Q&oe=657C5B8D&_nc_sid=1d576d&_nc_rid=065245760745760&_nc_store_type=1', 'jncuq.mp4')