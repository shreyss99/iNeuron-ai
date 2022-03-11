## DATA COMPRESSION

- This project contains simple data compression process for different file formats using the data compression algorithms.
- We have many data compression algorithms which can be used to compress files of types like .txt files, .png files, .wav files, .pdf files, .mp4 files.

***

### Tools

- Install [Python 3.5+]

***

### Overview:

- The project is a Python script which accepts the input file to be compressed, the algorithm to be used for compression and the output path to store the compressed file.
- These 3 parameters are input to the script as command-line arguments using parseArgs module.
- Once these are selected, the compressed file is placed at the output path.
- For checking the accuracy, we will be displaying certain file properties:
  - The size of original uncompressed file
  - The size of compressed file
  - The compression ratio for the file based on the algorithm.

### Usage:

- To compress a file and store it in a path, run `compress.py` script. To show help, enter `./compress.py -h` command:
