import pandas as pd
import rpa as r

arq = "D:\\Downloads\\challenge.xlsx"
xlsx = pd.read_excel(arq, sheet_name = "Sheet1")

#Open Website #RPA
r.init()
r.url("http://www.rpachallenge.com/")
#Wait
r.wait(10)




#stop the tagui process
r.close()
