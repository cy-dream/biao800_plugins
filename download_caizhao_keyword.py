import requests
from lxml import etree

def get_data():
	response = requests.get('https://www.chinabidding.cn/cha/A/', verify=False)
	html = etree.HTML(response.text)
	print(html)
	

if __name__ == '__main__':
	get_data()