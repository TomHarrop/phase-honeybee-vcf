#!/usr/bin/env python3

import logging
import pysam
import pandas
from pathlib import Path

alignment_file = 'output/010_genotypes/merged.bam'
fai_file = 'data/GCF_003254395.2_Amel_HAv3.1_genomic.fna.fai'
outdir = 'test/split'

# set up log
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename=snakemake.log[0],
    level=logging.INFO)

# read files
bamfile = pysam.AlignmentFile(alignment_file, 'rb')

all_chrs = sorted(set(pandas.read_csv(fai_file, sep='\t', header=None)[0]))
all_samples = sorted(set(x['ID'] for x in bamfile.header.get('RG')))

# generate paths
logging.info(f'Generating paths')
all_paths = {(chrom, sample): Path(outdir, sample, f'{chrom}.bam')
             for chrom in all_chrs for sample in all_samples}
for path in all_paths.values():
    if not path.parent.is_dir():
        path.parent.mkdir(parents=True)

# open file_handles
logging.info(f'Opening file handles')
handles = {
    (chrom, sample):
    pysam.AlignmentFile(Path(outdir, sample, f'{chrom}.bam'),
                        'wb',
                        template=bamfile)
    for chrom in all_chrs for sample in all_samples}

logging.info(f'Opened {len(handles)} file handles')

# write each read to the appropriate file
logging.info(f'Looping over BAM records')
i = 1
for read in bamfile:
    handles[(read.reference_name, read.get_tag('RG'))].write(read)
    if i % 1e6 == 0:
        logging.info(f'Processed {int(i / 1e6)} million records')
    i += 1

# close all the handles
logging.info(f'Closing file handles')
i = 1
total = len(handles.keys())
for handle in handles.values():
    handle.close()
    if i % 100 == 0:
        print(f'Closed {i} of {total} handles')
    i += 1

