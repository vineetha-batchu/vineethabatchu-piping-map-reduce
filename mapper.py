
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 11) : 
    Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales = datalist
    # print intermediate key-value pairs to standard output
    print(Genre,"\t",Global_Sales)