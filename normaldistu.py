import csv
import pandas as pd
import statistics  

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  height_weight_data = list(reader)


df = pd.read_csv("data.csv") 
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

hmean=statistics.mean(height_list)
hmode=statistics.mode(height_list)
hmedian=statistics.median(height_list)
hstdev=statistics.stdev(height_list)


wmode=statistics.mode(weight_list)
wmean=statistics.mean(weight_list)
wmedian=statistics.median(weight_list)
wstdev=statistics.stdev(weight_list)


hstdev1_start,hstdev1_end  =  hmean-hstdev,hmean+hstdev
hstdev2_start,hstdev2_end=hmean-2*hstdev,hmean+2*hstdev
hstdev3_start,hstdev3_end=hmean-3*hstdev,hmean+3*hstdev

wstdev1_start,wstdev1_end=wmean-wstdev,wmean+wstdev
wstdev2_start,wstdev2_end=wmean-2*wstdev,wmean+2*wstdev
wstdev3_start,wstdev3_end=wmean-3*wstdev,wmean+3*wstdev

hstdev1_data=[a for a in height_list if a>hstdev1_start and a<hstdev1_end]
hstdev2_data=[b for b in height_list if b>hstdev2_start and b<hstdev2_end]
hstdev3_data=[c for c in height_list if c>hstdev3_start and c<hstdev3_end]



wstdev1_data=[d for d in weight_list if d>wstdev1_start and d<wstdev1_end]
wstdev2_data=[e for e in weight_list if e>wstdev2_start and e<wstdev2_end]
wstdev3_data=[f for f in weight_list if f>wstdev3_start and f<wstdev3_end]
print (len(hstdev1_data))
print (len(hstdev2_data))
print (len(hstdev3_data))