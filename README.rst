phase honeybee vcf
==================

Preconfigured pipeline for converting the VCF and BAM output from
`honeybee_genotype_pipeline <https://github.com/tomharrop/honeybee-genotype-pipeline>`__
to a phased VCF.

For each hive, this pipeline:

1. Extracts the consensus sequence from the single drone and maps it
   back to the reference
2. Extracts the mapped reads and called variants for the pooled sample
3. Uses 1 & 2 as evidence for ``whatshap phase``

Install
-------

|https://www.singularity-hub.org/static/img/hosted-singularity–hub-%23e32929.svg|

Use the singularity container hosted on `Singularity
hub <https://singularity-hub.org/collections/5020>`__. The container
provides:

::

   whatshap
   samtools
   bcftools
   minimap2
   tabix

If you have the above dependencies installed, you can install the
pipeline with ``pip3``:

.. code:: bash

   pip3 install \
       git+git://github.com/tomharrop/phase-honeybee-vcf.git

Usage
-----

::

   phase_honeybee_vcf [-h] [-n] [--threads int] [--restart_times RESTART_TIMES]
                             --ref REF --vcf VCF --bam BAM --samples_csv SAMPLES_CSV
                             --outdir OUTDIR

   optional arguments:
     -h, --help            show this help message and exit
     -n                    Dry run
     --threads int         Number of threads. Default: 4
     --restart_times RESTART_TIMES
                           number of times to restart failing jobs (default 0)
     --ref REF             Reference genome in uncompressed fasta
     --vcf VCF             Filtered, compressed vcf from honeybee_genotype_pipeline
     --bam BAM             Indexed, merged bamfile from honeybee_genotype_pipeline
     --samples_csv SAMPLES_CSV
                           Sample csv (see README)
     --outdir OUTDIR       Output directory

-  The ``--vcf`` and ``--bam`` files should be output from
   `honeybee_genotype_pipeline <https://github.com/tomharrop/honeybee-genotype-pipeline>`__
-  ``--samples_csv`` should link the ``sample`` to the ``hive`` as
   follows:

::

   sample,hive,type
   BB34_drone,BB34,drone
   BB34_pool,BB34,pool
   BB42_drone,BB42,drone
   BB42_pool,BB42,pool

Graph
-----

|image1|

.. |https://www.singularity-hub.org/static/img/hosted-singularity–hub-%23e32929.svg| image:: https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg
   :target: https://singularity-hub.org/collections/5020
.. |image1| image:: graph.svg
