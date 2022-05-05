'''
Создание таблицы из JSON
Перед работой необходимо в терминале 
установить бибилиотеку pandas командой
pip install pandas
'''
import pandas


data = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"image":
		{
			"url": "images/0001.jpg",
			"width": 200,
			"height": 200
		},
	"thumbnail":
		{
			"url": "images/thumbnails/0001.jpg",
			"width": 32,
			"height": 32
		}
}
            
df = pandas.DataFrame(data=data)
print(df)
# @endhmPythON