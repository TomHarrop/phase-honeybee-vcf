#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


# load README.rst
def readme():
    with open('README.rst') as file:
        return file.read()

setup(
    name='phase_honeybee_vcf',
    version='0.0.1',
    description='python3 wrapper for phasing pools with single drone',
    long_description=readme(),
    url='https://github.com/tomharrop/phase-honeybee-vcf',
    author='Tom Harrop',
    author_email='twharrop@gmail.com',
    license='GPL-3',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.4',
        'snakemake>=5.30.1'
    ],
    entry_points={
        'console_scripts': [
            'phase_honeybee_vcf = phase_honeybee_vcf.__main__:main'
            ],
    },
    # scripts={
    #     'csdemux/src/calculate_hamming_distance.R',
    #     'csdemux/src/combine_step_logs.R',
    #     'csdemux/src/plot_adaptor_content.R',
    #     'csdemux/src/plot_barcode_content.R',
    #     'csdemux/src/plot_barcode_distance.R',
    # },
    package_data={
        'phase_honeybee_vcf': [
            'Snakefile',
            'README.rst'
        ],
    },
    zip_safe=False)
