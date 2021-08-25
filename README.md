# monoDiKGap
## monoDiKGap Theoretical Description
When -kgap=n then the (20) × (20 × 20) × n features will exist for protein.  
When -kgap=1, feature structure will be X_XX.  
When -kgap=2, feature structure will be X_XX, and X_ _XX.  
When -kgap=3, feature structure will be X_XX, X_ _ XX, and X_ _ _ XX.  
## Command for generate dataset only monoDiKGap method  
### run command  
python main.py -seq=Protein -fa=/home/gongxiaodou/data/GA.fasta  -la=/home/gongxiaodou/data/label.txt   -full=1  -optimum=1 -f12=1 -kgap=2
### parameter description
full = 1 where the parameters that do not want to save the complete set of data, optimum = 1 that do not want to save the best data set and the generated f12 = 1 generates monoDiKGap features.
# CC  
## usage  
python cc.py F:/DrugHybrid/data/ip.fasta Protein CC -out F:/DrugHybrid/result/CC/ip_CC  
python cc.py F:/DrugHybrid/data/in.fasta Protein CC -out F:/DrugHybrid/result/CC/in_CC
## feature description  
The CC variable describes the average interaction between two fragments with different physical and chemical properties separated by lag fragments.  The maximum lag in this study was set to 2, considering the three physical and chemical properties of hydrophobicity values,hydrophilicity values and side chain mass of the amino acid R.  
# GAAC  
## usgae  
python  iFeature.py --file F:/DrugHybrid/data/ip.fasta  --type GAAC --out F:/DrugHybrid/result/GAAC/GAAC(1).tsv  
python  iFeature.py --file F:/DrugHybrid/data/in.fasta  --type GAAC --out F:/DrugHybrid/result/GAAC/GAAC(2).tsv  
copy *.tsv all-groups.tsv  
## feature description  
GAAC divides amino acids into aliphatic, aromatic, positively charged, negatively charged and uncharged groups.  
The features extracted by GAAC describe the frequency of each amino acid family.
