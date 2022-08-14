from random import random
import pandas as pd
import matplotlib.pyplot as plt
import os.path
from random import randrange


class classPandas:

    def createDataFrame(arrayList: list, headers: list ):
        return pd.DataFrame(arrayList,columns=headers)

    def dataFrametoExcel(dataFrame: pd.DataFrame ,fileName: str, sheetName: str = str(randrange(100))):
        if(os.path.exists(fileName)):
            print("Archivo existente")
            with pd.ExcelWriter(r''+fileName, engine='openpyxl', mode='a') as writer:  
                dataFrame.to_excel(writer, sheet_name=sheetName)
        else:
            print("Creando Archivo")
            dataFrame.to_excel(fileName, index = False, header=True)

    def graficBar(dataFrame: pd.DataFrame, nameRow:str, nameCol: str):
        namesRow = list(dataFrame[nameRow])
        valuesCols = list()
        for i in range(len(dataFrame[nameCol])):
            valuetemp = dataFrame[nameCol][i].replace(',', '')
            valuesCols.append(float(valuetemp))
        plt.bar(namesRow, valuesCols)
        plt.show() 