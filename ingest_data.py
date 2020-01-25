import wget

outDir = './data/'

#driving licenses in current issue for each category and county:
drv_license_distrib = 'https://www.rsa.ie/Documents/Road%20Safety/Licence_stats/Full%20Licences%20Current%20on%2031st%20December%202016_%20by%20Licence%20Category%20County.pdf


#https://www.rsa.ie/en/RSA/Road-Safety/RSA-Statistics/

data_sources = [
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/January/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative%20)%20January%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/February/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-(Cumulative)%20February%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/March/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative)%20March%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/April/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative)%20April%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/May/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative)%20May%20%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/June/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20_%20County%20-%20(Cumulative)%20June%20%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/July/Penalty%20points%20Issued%20-%20Stats%20for%20June%202017.xlsx',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/August/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20(Cumulative)%20August%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/September/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20(Cumulative)%20September%202017.xls',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/October/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative)%20October%202017.xlsx',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/November/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-%20(Cumulative)%20November%202017.xlsx',
'https://www.rsa.ie/Documents/PenaltyPointsStats/2017/December/Penalty%20Point%20Offences%20broken%20down%20by%20Type%20and%20County%20-(Cumulative)%20December%202017.xls',
]



for url in data_sources:
 wget.download(url, out=outDir)

#fetch number of registered licenses:
wget.download(drv_license_distrib, out=outDir)


