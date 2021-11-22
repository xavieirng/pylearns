# 导入必要库
import requests
import json
from openpyxl import load_workbook
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map  # 为了可以绘制省市地图

# 原链接为“https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34108598287336549535_1600250300529&_=1600250300530”
# 在“&”之后的可以删掉
china_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

# 创建请求头，防止被认定为爬虫,并且将格式设置成字典
# 注意！此处字典要求使用双引号""而不是单引号''，否则报错
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

# 获取到了json数据
# 查看网页后，发现是“Request Method: GET”，故使用GET请求而不是POST
response = requests.get(url=china_url,headers=headers).json()
#print(response)

data = json.loads(response['data'])

# 保存数据
with open('data_covid_19.json','w',encoding='utf-8') as file:
	# 再把字典改成json字符串，利用dumps
	# 参数indent代表缩进字符个数
	# 为了输出中文，还需要加入一个参数ensure_ascii,并且指定为False
	file.write(json.dumps(data,ensure_ascii=False,indent=2))

# 获取国内的所有数据
chinaAreaDict = data['areaTree'][0]
# 获取国内所有省份的数据
provinceList = chinaAreaDict['children']
# print(provinceList)

# 构思如何制作Excel表头来存放数据
''' 省份 城市 之类的
 1  广东 广州 
 2  广东 珠海
 3  ........
 '''
# 构造这样一个列表，里面存放字典数据：[{广东，广州},{广东，珠海}]
china_citylist = []
for x in range(len(provinceList)):
 #      每一个省份的数据，一个字典就是一个城市的数据
 	province = provinceList[x]['name']
 #	print(province)  # 输出每个省份名字
 	province_list = provinceList[x]['children']
 #	print(province_list)  # 输出每个省份名字

 	for y in range(len(province_list)):
 		# 每一个城市的数据，对应同一个省份
 		city = province_list[y]['name']
 		today = province_list[y]['today']
 		total = province_list[y]['total']
 		city_list = {'province':province,
 					'city':city,
 					'today':today,
 					'total':total
 					}
 		china_citylist.append(city_list)
# print(china_citylist)

# 显示所有列
pd.set_option('display.max_columns',None)
# 显示所有行
pd.set_option('display.max_rows',None)
# 设置value的显示长度为100，默认的是50
pd.set_option('max_colwidth',100)
# 设置每行的长度为100，避免换行，其实要设置成200左右，不过Subline放不下
pd.set_option('display.width',200)

chinaTotalData = pd.DataFrame(china_citylist)
#print(chinaTotalData)

# chinaTotalData 中的today和total数据拆开添加到DataFrame中
nowConfirmlist = []
confirmlist = []
suspectlist = []
deadlist = []
deadRatelist = []
heallist = []
healRatelist = []

# 将chinaTotalData中的字典数据转化成列表
for value in chinaTotalData['total'].values.tolist():
	# 原理：先把字典数据中的如confirm放到事先建好的空列表中
	nowConfirmlist.append(value['nowConfirm'])
	confirmlist.append(value['confirm'])
	suspectlist.append(value['suspect'])
	deadlist.append(value['dead'])
	deadRatelist.append(value['deadRate'])
	heallist.append(value['heal'])
	healRatelist.append(value['healRate'])

# 原理：再把装好数据的列表重新放回chinaTotalData
chinaTotalData['nowConfirm'] = nowConfirmlist
chinaTotalData['confirm'] = confirmlist
chinaTotalData['suspect'] = suspectlist
chinaTotalData['dead'] = deadlist
chinaTotalData['deadRate'] = deadRatelist
chinaTotalData['heal'] = heallist
chinaTotalData['healRate'] = healRatelist

# 同上边拆分total，再来拆分today数据
today_confirmlist = []
today_confirmCutslist = []

for value in chinaTotalData['today'].values.tolist():  # 将chinaTotalData中的字典数据转化成列表
	today_confirmlist.append(value['confirm'])
	today_confirmCutslist.append(value['confirmCuts'])

chinaTotalData['today_confirm'] = today_confirmlist
chinaTotalData['today_confirmCuts'] = today_confirmCutslist

# 删除total，today列,"True"要开头大写
chinaTotalData.drop(['total','today'],axis=1,inplace=True)
#print(chinaTotalData)

# 将其保存到Excel中

book = load_workbook('data_covid_19.xlsx')
writer = pd.ExcelWriter('data_covid_19.xlsx',engine='openpyxl')
writer.book = book
# 以上三行为了保证旧数据不被新数据覆盖,但是此种写法必须事先在文件夹存有“data_covid_19.xlsx”文档
writer.sheets = dict((ws.title,ws) for ws in book.worksheets)
chinaTotalData.to_excel(writer,index=False)

writer.save()
writer.close()



# 利用pandas读取Excel文件，此处需要安装第三方库xlrd:pip install xlrd
df = pd.read_excel('data_covid_19.xlsx')
# 绘制国内确诊总疫情图
# groupby表示分组，按省份分组，并且省内求和
# 此时数据格式为dataframe数据
data = df.groupby(by='province',as_index = False).sum()
# 再把dataframe数据转化成形如[(广东,224),(福建,345)]之类，好符合接下来的使用
data_list = list(zip(data['province'].values.tolist(),data['confirm'].values.tolist()))

# 绘制中国地图
def map_china()->Map:
	map = (
		Map()
		.add(series_name="确诊病例",data_pair=data_list,maptype='china')
		.set_global_opts(
			title_opts=opts.TitleOpts(title="疫情地图"),
			visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
				pieces=[{"max":9,"min":0,"label":"0-9","color":"#FFE4E1"},
					{"max":99,"min":10,"label":"10-99","color":"#FF7F50"},
					{"max":499,"min":100,"label":"100-499","color":"#F08080"},
					{"max":999,"min":500,"label":"500-999","color":"#CD5C5C"},
					{"max":9999,"min":1000,"label":"1000-9999","color":"#990000"},
					{"max":99999,"min":10000,"label":">=10000","color":"#660000"}]
						)
		)
	)
	map.render("map_china.html")
map_china()  # 调用函数