Q1
Merge Sort algorithm implemented with a multi-threaded version to divide the task of sorting across threads.
Benchmarking compares single-threaded and multi-threaded performance.
Includes speedup calculation for various input sizes (e.g., 1000, 10000, 100000 elements).
Sample array: [12, 4, 56, 17, 8, 99, 23, 1, 45] Sorted array: [1, 4, 8, 12, 17, 23, 45, 56, 99] 
Array size: 1000 Thread count: 4 Single-threaded time: 0.0020 seconds Multi-threaded time: 0.0060 seconds Results match: True Speedup: 0.34x ---------------------------------------- 
Array size: 10000 Thread count: 4 Single-threaded time: 0.0273 seconds Multi-threaded time: 0.0377 seconds Results match: True Speedup: 0.72x ---------------------------------------- 
Array size: 100000 Thread count: 4 Single-threaded time: 0.3708 seconds Multi-threaded time: 0.3887 seconds Results match: True Speedup: 0.95x

Q2
Quick Sort algorithm optimized with multi-threading, using depth-limited threading to prevent excessive overhead.
Benchmarking compares single-threaded and multi-threaded performance.
Automatically adjusts for small partitions by switching to single-threaded mode.
Original array: [21, 5, 17, 8, 99, 33, 1, 76] Sorted array: [1, 5, 8, 17, 21, 33, 76, 99] 
Array size: 1000 Max thread depth: 3 Single-threaded time: 0.0010 seconds Multi-threaded time: 0.0021 seconds Results match: True Speedup: 0.48x ---------------------------------------- 
Array size: 10000 Max thread depth: 3 Single-threaded time: 0.0174 seconds Multi-threaded time: 0.0216 seconds Results match: True Speedup: 0.81x ---------------------------------------- 
Array size: 100000 Max thread depth: 3 Single-threaded time: 0.2534 seconds Multi-threaded time: 0.2746 seconds Results match: True Speedup: 0.92x ... 
Results match: True Speedup: 0.99x --------------------

Q3
Concurrently downloads multiple files from the internet using Python’s threading module.
Supports both sequential and multi-threaded downloading.
Displays download statistics and computes speedup for each approach.
Concurrent File Downloader (Sample URLs Only) =============================================== 
Sample URLs to be downloaded: 
- https://www.example.com 
- https://www.google.com 
- https://www.wikipedia.org 
- https://www.python.org 
- https://www.netflix.com 
Starting sequential download... 
[✔] Downloaded file_1745949286.dat (0.6 KB) in 0.65 seconds 
[✔] Downloaded file_1745949286.dat (0.0 KB) in 0.64 seconds 
[✔] Downloaded file_1745949287.dat (21.6 KB) in 0.71 seconds 
[✔] Downloaded file_1745949288.dat (11.6 KB) in 0.58 seconds 
[✔] Downloaded file_1745949288.dat (0.0 KB) in 2.68 seconds 
Sequential completed: 5/5 files in 5.28 seconds 
Starting threaded download with 5 threads... 
[✔] Downloaded file_1745949291.dat (11.6 KB) in 1.01 seconds 
[✔] Downloaded file_1745949291.dat (0.6 KB) in 1.08 seconds 
[✔] Downloaded file_1745949291.dat (0.0 KB) in 1.15 seconds 
[✔] Downloaded file_1745949291.dat (21.6 KB) in 1.25 seconds 
[✔] Downloaded file_1745949291.dat (0.0 KB) in 3.19 seconds ... 
- Threaded time: 3.20 sec - Speedup: 1.65x 
Finished downloading files.
