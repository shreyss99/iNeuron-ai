import Code.huffman.compressor
import Code.lzw.compressor
import Code.shannon.compressor
import Code.zip.compressor
import Code.image.compressor
import Code.wav_mp3.compressor
import Code.pdf.compressor
import Code.video.compressor
import os
import argparse
import sys


'''
This script is used for executing compression
via command line interface
'''
# Command line parser

parser = argparse.ArgumentParser(description='Compress a file')
parser.add_argument('input_file', type=str, help='Input file to be compressed')
parser.add_argument('output_path', type=str, help='Output path for storing compressed output file')
parser.add_argument('--alg', help='Choose an algorithm, default is huffman', choices=['huffman', 'shannon', 'lzw', 'zip', 'image', 'wav', 'pdf', 'video'])
args = parser.parse_args()


# Main script

input_file = args.input_file
output_path = args.output_path
alg = args.alg

if not os.path.isfile(input_file):
    print("ERROR: {} isn't a file or doesn't exist".format(input_file))
    sys.exit(1)

if not os.path.isdir(output_path):
    print("ERROR: {} isn't a path or doesn't exist.".format(output_path))
    sys.exit(1)
    
    
uncompressed_size = os.stat(input_file).st_size
print('Uncompressed size: {} bytes'.format(uncompressed_size))

print('===== Using {} compression algorithm ======'.format(alg.upper()))
output_file = ''

if alg == 'huffman':
    output_file = Code.huffman.compressor.compress(input_file, output_path)
elif alg == 'lzw':
    output_file = Code.lzw.compressor.compress(input_file, output_path)
elif alg == 'shannon':
    output_file = Code.shannon.compressor.compress(input_file, output_path)
elif alg == 'zip':
    output_file = Code.zip.compressor.compress(input_file, output_path)
elif alg == 'image':
    output_file = Code.image.compressor.compress(input_file, output_path)
elif alg == 'wav':
    output_file = Code.wav_mp3.compressor.compress(input_file, output_path)
elif alg == 'pdf':
    output_file = Code.pdf.compressor.compress(input_file, output_path)
elif alg == 'pdf':
    output_file = Code.pdf.compressor.compress(input_file, output_path)
elif alg == 'video':
    output_file = Code.video.compressor.compress(input_file, output_path)
    
    
# Print some compression information

compressed_size = os.stat(output_file).st_size
print('Output file: {}'.format(output_file))
print('Compressed size: {} bytes'.format(compressed_size))
print('Compression ratio = {0} / {1} = {2:.3f}'.format(uncompressed_size, compressed_size, uncompressed_size / compressed_size))
sys.exit(0)