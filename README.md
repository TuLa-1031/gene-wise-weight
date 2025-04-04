# gene-wise-weight

Data: DNA Methylation 450 và Gene expression RNAseq FPKM được lấy từ [https://xenabrowser.net/datapages/?cohort=GDC%20TCGA%20Lung%20Adenocarcinoma%20(LUAD)&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443]

Các bước preprocessing:
1. Loại bỏ đi features DNA Methylation bị thiếu 20% giá trị
2. Fill các giá trị còn thiếu của feature DNAmethylation bằng KNNimpute từ package sklearn
