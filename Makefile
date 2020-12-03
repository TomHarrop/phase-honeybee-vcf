graph: graph.svg

graph.svg: phase_honeybee_vcf/Snakefile
	snakemake \
	-n \
	-s phase_honeybee_vcf/Snakefile \
	--cores 8 \
	--dag \
	--forceall \
	--config \
	outdir=out \
	threads=8 \
	bam=data/gt_output/merged.bam \
	vcf=data/filtered.vcf.gz \
	samples_csv=data/samples.csv \
	ref=data/GCF_003254395.2_Amel_HAv3.1_genomic.fna \
	| dot -Tsvg \
	> graph.svg

# 	| grep -v "^[[:space:]+]0" | grep -v "\->[[:space:]]0" \

readme: README.rst

README.rst: README.md
	pandoc -f markdown -t rst README.md > README.rst
