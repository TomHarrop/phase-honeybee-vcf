#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_resources import resource_filename
import argparse
import logging
import snakemake


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='phase_honeybee_vcf')
    parser.add_argument(
        '-n',
        help='Dry run',
        dest='dry_run',
        action='store_true')
    default_threads = 4
    parser.add_argument(
        '--threads',
        help=('Number of threads. Default: %i' % default_threads),
        metavar='int',
        type=int,
        dest='threads',
        default=default_threads)
    parser.add_argument(
        '--restart_times',
        required=False,
        help='number of times to restart failing jobs (default 0)',
        type=int,
        dest='restart_times',
        default=0)
    parser.add_argument(
        '--ref',
        required=True,
        help='Reference genome in uncompressed fasta',
        type=str,
        dest='ref')
    parser.add_argument(
        '--vcf',
        required=True,
        help='Filtered, compressed vcf from honeybee_genotype_pipeline',
        type=str,
        dest='vcf')
    parser.add_argument(
        '--bam',
        required=True,
        help='Indexed, merged bamfile from honeybee_genotype_pipeline',
        type=str,
        dest='bam')
    parser.add_argument(
        '--samples_csv',
        required=True,
        help='Sample csv (see README)',
        type=str,
        dest='samples_csv')
    parser.add_argument(
        '--outdir',
        required=True,
        help='Output directory',
        type=str,
        dest='outdir')

    args = vars(parser.parse_args())
    return(args)

def main():
    # set up log
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)

    # get the snakefile
    snakefile = resource_filename(__name__, 'Snakefile')
    logging.debug(f'Using snakefile {snakefile}')

    # get args
    args = parse_arguments()
    logging.debug(f'Entrypoint args\n{args}')

    snakemake.snakemake(
        snakefile=snakefile,
        config=args,
        cores=args['threads'],
        lock=False,
        printreason=True,
        printshellcmds=True,
        dryrun=True if args['dry_run'] else False,
        restart_times=args['restart_times'])

