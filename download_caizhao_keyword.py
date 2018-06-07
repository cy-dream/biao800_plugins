import requests
from lxml import etree

def get_data():
	response = requests.get('https://www.chinabidding.cn/cha/A/7.html', verify=False)
	if response.status_code == 200:
		html = etree.HTML(response.text)
		tag_lis = html.xpath('//ul[@class="dq_rmc"]/li/a')
		key_word = list()
		for li in tag_lis:
			key_word.extend(li.xpath('./text()'))
		print(key_word)

def create_url():
	letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
					 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for le in letter:
		num = 1
		while True:
			# https://www.chinabidding.cn/cha/A/1.html
			url = 'https://www.chinabidding.cn/cha/{}/{}.html'.format(le,num)
			# 禁止报https verify error
			requests.packages.urllib3.disable_warnings()
			# allow_redirects=False 禁止重定向
			response = requests.get(url, verify=False, allow_redirects=False)
			if response.status_code == 200:
				num += 1
				get_keyword(response.text)
			else:
				print('字母: {}；共{}页'.format(le, str(num-1)))
				break


def get_keyword(html):
		html = etree.HTML(html)
		tag_lis = html.xpath('//ul[@class="dq_rmc"]/li/a')
		keyword_list = list()
		for li in tag_lis:
			keyword_list.extend(li.xpath('./text()'))
			write_data(keyword_list)


def write_data(keyword_list):
	keyword_str = '\n'.join(keyword_list)
	with open('keyword.txt', 'a+', encoding='utf-8') as f:
		f.write(keyword_str)
		f.close()

if __name__ == '__main__':
	create_url()