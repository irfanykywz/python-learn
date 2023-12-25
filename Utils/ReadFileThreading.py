import threading

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def multi_threaded_file_reader(file_paths):
    threads = []
    results = {}

    # Define the worker function
    def read_file_thread(file_path):
        result = read_file(file_path)
        results[file_path] = result

    # Create and start threads
    for file_path in file_paths:
        thread = threading.Thread(target=read_file_thread, args=(file_path,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":
    file_paths = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    results = multi_threaded_file_reader(file_paths)
    separator_size = 50
    for file_path, content in results.items():
        print(f"Reading {file_path}:")
        print(content)
        print("-" * separator_size)        