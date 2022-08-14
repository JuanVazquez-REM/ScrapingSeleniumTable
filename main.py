from classSelenium import classSelenium
from classJson import classJson
from classPandas import classPandas

data = classJson.readJson('config')

webDriver = classSelenium(data['driver']['path'])
webDriver.setPage(data['driver']['page'])

#Tomamos los datos de la tabla
arrayList, headers = webDriver.getTable(data['table']['xpath'])

#Crear dataFrame
dataFrame = classPandas.createDataFrame(arrayList, headers)

#Crear Excel
classPandas.dataFrametoExcel(dataFrame,data['file']['fileName'],data['file']['sheetName'])

#Listar campos para la grafica
#Graficando
classPandas.graficBar(dataFrame,data['table']['graphBar']['namesRow'],data['table']['graphBar']['valuesCol'])
print("Fin")

