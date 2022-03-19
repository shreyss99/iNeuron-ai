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
- Once these are selected, the file is compressed using the apecifiec algorithm and the compressed file is placed at the output path.
- For checking the accuracy, we will be displaying certain file properties:
  - The size of uncompressed file (in bytes)
  - The size of compressed file (in bytes)
  - The compression ratio = (size of uncompressed file) / (size of compressed file)

### Usage:

- To compress a file and store it in a path, run `compress.py` script. To show help, enter `./compress.py -h` command:

```sh
$ ./compress.py -h
usage: compress.py [-h] [--alg {huffman,shannon,lzw,image,zip,pdf,video,wav}] input_file output_path

Compress a file

positional arguments:
  input_file            input file to be compressed
  output_path           output path for storing compressed output file
  --alg 				{huffman,shannon,lzw,image,zip,pdf,video,wav}            

optional arguments:
  -h, --help            show this help message and exit
```

When run this script, you must choose one of available algorithms (`huffman`, `shannon`, `lzw`, `image`, `zip`, `pdf`, `video`, `wav`), pass an `input file` to be compressed and an `output path` for storing decompressed file.
Huffman algorithm will be default when run this script. To run with another algorithm, use option `--alg` to specify an algorithm you want. For example:

```
$ python compress.py --alg huffman "./Sample_Input/temp.txt" "./Sample_Output/"
Uncompressed size: 10033 bytes
===== Using HUFFMAN compression algorithm ======
Output file: ./Sample_Output/Compressed_temp.txt
Compressed size: 6065 bytes
Compression ratio = 10033 / 6065 = 1.654
```

### Output Interpretation:
	
	- We have 8 different files for - Huffman, LZW, Shannon-Fano, PDF, WAV, ZIP, Image and Video.
	- We have duplicated all of them. We will run each file using the ZIP algorithm and the corresponding individual algorithms.
	- In the output screenshots, we have stored the screenshots and compressed files foeach file using the ZIP algorithm and using the corresponding better algorithm.