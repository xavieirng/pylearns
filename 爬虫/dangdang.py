from time import sleep

import requests
from bs4 import BeautifulSoup

cookies = {
    'Qs_lvt_411649': '1640854201',
    'Hm_lvt_1f19c27e7e3e3255a5c79248a7f4bdf1': '1640854202',
    'XSRF-TOKEN': 'eyJpdiI6IkZHakw2SFZtMEl2OHNJOVNReEN6M1E9PSIsInZhbHVlIjoiV0dXMGp5aGNkWmhvR2c0ZTBUdzJid2xIYUFyWEdxNVZEWjYzYTZMVjIzWk8wRjFUVkhLdmVRTmNWTGhONGlHZ29ZdVVSZTYxNEx1U2ZNRTBJSW5TYnc9PSIsIm1hYyI6ImRmZjA2MGYzMDY3ZWIyZDliYjIxMDMxN2UzMDgzNGM5NTNmN2M3MmZiNDVjMmQ0MGVlYzk4Y2JhNDRhN2ZlMGMifQ%3D%3D',
    'laravel_session': 'eyJpdiI6InFqWG1HOSs4a2VGWkR6NVpPelJINkE9PSIsInZhbHVlIjoiNUIwelNxandVSmVmMVBDTmZRQmFrS2xkT1wvY1F0YjhrZ2JzdGpKVVE2N3hhSjJUMmREQVlmZHZSZTBYVjB3OFFteEludWhRWVlnbXM0SUdSb3JDRDhRPT0iLCJtYWMiOiI4N2JkZWI5OGMzNzEwNjEwNWE3YjRiMTVhZWZkODJjZTg5M2NjMjI4ODBjMzRkMDQzMDU5YmM4MTRiNThiNTQ4In0%3D',
    'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImV4cGlyZV90aW1lIjoxNjQxNDA5MjAwLCJpYXQiOjE2NDA4NTQzMTYsImlkIjoyOTc2MTQ2fQ.0107HOHwYM2c21dgEgu5StRWG2Ba1EYBVs1PCkQjTIY',
    'UM_distinctid': '17e0a8d6e8736f-0dc22cb83b0423-4c607a68-1fa400-17e0a8d6e88367',
    'mediav': '%7B%22eid%22%3A%221090564%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22LM9wyh34)I8ifXqH%3C40%5B%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22LM9wyh34)I8ifXqH%3C40%5B%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A1%7D',
    'Hm_lpvt_1f19c27e7e3e3255a5c79248a7f4bdf1': '1640858413',
    'Qs_pv_411649': '3776992973475732000%2C1511680491504983300%2C2915640072245289500%2C3610981674982469000%2C317525044407294300',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}


Big_category=['食品饮料']
Subcategory=[['零食/坚果/特产',"酒水/饮料","茶","粮油米面/南北干货/调味品", "乳品/咖啡/冲调","方便速食/速冻食品","其他"],
             ["生活日用","家庭清洁","口腔护理","头发洗护/造型","身体清洁/护理","收纳整理","女性护理","五金工具","其他"],
             ["护肤品","彩妆/香水","美妆工具/美容仪器","其他"],
             ["潮流饰品","黄金钻石","翡翠玉石","珍珠","其他"],
             ["婴童用品","纸尿裤","奶粉/辅食/零食/营养品","孕产妇用品/营养品","其他"],
             ["水果","海鲜水产","蔬菜","肉/蛋/禽类","其他"],
             ["儿童读物","教材教辅","其他书刊","育儿百科","电子教育"],
             ["箱包", "男鞋","女鞋","婴童鞋/亲子鞋","其他"],
             ["床上用品","家居饰品","居家布艺","其他"],
             ["鲜花速递","绿植园艺","其他"],
             ["运动鞋","运动服","运动/户外/骑行用品","运动包/户外包/配件","其他"],
             ["钟表","眼镜","配饰","其他"],
             ["手机","电脑/平板/服务器","数码配件","数码相机/单反相机/摄像机","智能设备","影音娱乐","商务办公","话费/宽带/流量","其他"],
             ["文具","创意礼品","婚庆节庆","书法绘画","古董文玩","办公耗材","其他"],
             ["住宅家具","灯饰照明","家装材料","厨房卫浴","商业/办公家具","五金建材","装修设计","其他","全屋定制"],
             ["餐饮具","厨具","生活电器","大家电","个护电器","其他"],
             ["玩具/童车/益智/积木/模型","动漫/周边/cos/桌游","乐器/配件","其他"],
             ["宠物用品/服饰","宠物食品","水族类","宠物保健","其他"],
             ["滋补品","护理护具","医疗器械","保健品","医药","其他"],
             ["旅游度假","虚拟卡券","医疗服务","装修服务","汽车服务","其他生活服务"],
             ["维修保养/清洗/美容","电子导航/车载电器","汽车/摩托车配件","汽车装饰","汽车/摩托车整车","其他"],
             ["机械设备","农资农具","其他"]]


html='https://api-service.chanmama.com/v1/product/category?type=all'
print(html)
response='{"data":[{"id":"服饰内衣","cat_name":"服饰内衣","sub_categories":[{"id":"女装","cat_name":"女装","sub_categories":[]},{"id":"男装","cat_name":"男装","sub_categories":[]},{"id":"婴童装/亲子装","cat_name":"婴童装/亲子装","sub_categories":[]},{"id":"内衣/袜子","cat_name":"内衣/袜子","sub_categories":[]},{"id":"家居服","cat_name":"家居服","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"食品饮料","cat_name":"食品饮料","sub_categories":[{"id":"零食/坚果/特产","cat_name":"零食/坚果/特产","sub_categories":[]},{"id":"酒水/饮料","cat_name":"酒水/饮料","sub_categories":[]},{"id":"茶","cat_name":"茶","sub_categories":[]},{"id":"粮油米面/南北干货/调味品","cat_name":"粮油米面/南北干货/调味品","sub_categories":[]},{"id":"乳品/咖啡/冲调","cat_name":"乳品/咖啡/冲调","sub_categories":[]},{"id":"方便速食/速冻食品","cat_name":"方便速食/速冻食品","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"日用百货","cat_name":"日用百货","sub_categories":[{"id":"生活日用","cat_name":"生活日用","sub_categories":[]},{"id":"家庭清洁","cat_name":"家庭清洁","sub_categories":[]},{"id":"口腔护理","cat_name":"口腔护理","sub_categories":[]},{"id":"头发洗护/造型","cat_name":"头发洗护/造型","sub_categories":[]},{"id":"身体清洁/护理","cat_name":"身体清洁/护理","sub_categories":[]},{"id":"收纳整理","cat_name":"收纳整理","sub_categories":[]},{"id":"女性护理","cat_name":"女性护理","sub_categories":[]},{"id":"五金工具","cat_name":"五金工具","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"美妆护肤","cat_name":"美妆护肤","sub_categories":[{"id":"护肤品","cat_name":"护肤品","sub_categories":[]},{"id":"彩妆/香水","cat_name":"彩妆/香水","sub_categories":[]},{"id":"美妆工具/美容仪器","cat_name":"美妆工具/美容仪器","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"珠宝饰品","cat_name":"珠宝饰品","sub_categories":[{"id":"潮流饰品","cat_name":"潮流饰品","sub_categories":[]},{"id":"黄金钻石","cat_name":"黄金钻石","sub_categories":[]},{"id":"翡翠玉石","cat_name":"翡翠玉石","sub_categories":[]},{"id":"珍珠","cat_name":"珍珠","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"母婴用品","cat_name":"母婴用品","sub_categories":[{"id":"婴童用品","cat_name":"婴童用品","sub_categories":[]},{"id":"纸尿裤","cat_name":"纸尿裤","sub_categories":[]},{"id":"奶粉/辅食/零食/营养品","cat_name":"奶粉/辅食/零食/营养品","sub_categories":[]},{"id":"孕产妇用品/营养品","cat_name":"孕产妇用品/营养品","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"生鲜蔬果","cat_name":"生鲜蔬果","sub_categories":[{"id":"水果","cat_name":"水果","sub_categories":[]},{"id":"海鲜水产","cat_name":"海鲜水产","sub_categories":[]},{"id":"蔬菜","cat_name":"蔬菜","sub_categories":[]},{"id":"肉/蛋/禽类","cat_name":"肉/蛋/禽类","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"图书音像","cat_name":"图书音像","sub_categories":[{"id":"儿童读物","cat_name":"儿童读物","sub_categories":[]},{"id":"教材教辅","cat_name":"教材教辅","sub_categories":[]},{"id":"其他书刊","cat_name":"其他书刊","sub_categories":[]},{"id":"育儿百科","cat_name":"育儿百科","sub_categories":[]},{"id":"电子教育","cat_name":"电子教育","sub_categories":[]}]},{"id":"鞋靴箱包","cat_name":"鞋靴箱包","sub_categories":[{"id":"箱包","cat_name":"箱包","sub_categories":[]},{"id":"男鞋","cat_name":"男鞋","sub_categories":[]},{"id":"女鞋","cat_name":"女鞋","sub_categories":[]},{"id":"婴童鞋/亲子鞋","cat_name":"婴童鞋/亲子鞋","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"家居家纺","cat_name":"家居家纺","sub_categories":[{"id":"床上用品","cat_name":"床上用品","sub_categories":[]},{"id":"家居饰品","cat_name":"家居饰品","sub_categories":[]},{"id":"居家布艺","cat_name":"居家布艺","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"鲜花绿植","cat_name":"鲜花绿植","sub_categories":[{"id":"鲜花速递","cat_name":"鲜花速递","sub_categories":[]},{"id":"绿植园艺","cat_name":"绿植园艺","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"运动户外","cat_name":"运动户外","sub_categories":[{"id":"运动鞋","cat_name":"运动鞋","sub_categories":[]},{"id":"运动服","cat_name":"运动服","sub_categories":[]},{"id":"运动/户外/骑行用品","cat_name":"运动/户外/骑行用品","sub_categories":[]},{"id":"运动包/户外包/配件","cat_name":"运动包/户外包/配件","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"钟表配饰","cat_name":"钟表配饰","sub_categories":[{"id":"钟表","cat_name":"钟表","sub_categories":[]},{"id":"眼镜","cat_name":"眼镜","sub_categories":[]},{"id":"配饰","cat_name":"配饰","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"3C数码","cat_name":"3C数码","sub_categories":[{"id":"手机","cat_name":"手机","sub_categories":[]},{"id":"电脑/平板/服务器","cat_name":"电脑/平板/服务器","sub_categories":[]},{"id":"数码配件","cat_name":"数码配件","sub_categories":[]},{"id":"数码相机/单反相机/摄像机","cat_name":"数码相机/单反相机/摄像机","sub_categories":[]},{"id":"智能设备","cat_name":"智能设备","sub_categories":[]},{"id":"影音娱乐","cat_name":"影音娱乐","sub_categories":[]},{"id":"商务办公","cat_name":"商务办公","sub_categories":[]},{"id":"话费/宽带/流量","cat_name":"话费/宽带/流量","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"礼品文创","cat_name":"礼品文创","sub_categories":[{"id":"文具","cat_name":"文具","sub_categories":[]},{"id":"创意礼品","cat_name":"创意礼品","sub_categories":[]},{"id":"婚庆节庆","cat_name":"婚庆节庆","sub_categories":[]},{"id":"书法绘画","cat_name":"书法绘画","sub_categories":[]},{"id":"古董文玩","cat_name":"古董文玩","sub_categories":[]},{"id":"办公耗材","cat_name":"办公耗材","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"家具建材","cat_name":"家具建材","sub_categories":[{"id":"住宅家具","cat_name":"住宅家具","sub_categories":[]},{"id":"灯饰照明","cat_name":"灯饰照明","sub_categories":[]},{"id":"家装材料","cat_name":"家装材料","sub_categories":[]},{"id":"厨房卫浴","cat_name":"厨房卫浴","sub_categories":[]},{"id":"商业/办公家具","cat_name":"商业/办公家具","sub_categories":[]},{"id":"五金建材","cat_name":"五金建材","sub_categories":[]},{"id":"装修设计","cat_name":"装修设计","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]},{"id":"全屋定制","cat_name":"全屋定制","sub_categories":[]}]},{"id":"厨卫家电","cat_name":"厨卫家电","sub_categories":[{"id":"餐饮具","cat_name":"餐饮具","sub_categories":[]},{"id":"厨具","cat_name":"厨具","sub_categories":[]},{"id":"生活电器","cat_name":"生活电器","sub_categories":[]},{"id":"大家电","cat_name":"大家电","sub_categories":[]},{"id":"个护电器","cat_name":"个护电器","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"玩具乐器","cat_name":"玩具乐器","sub_categories":[{"id":"玩具/童车/益智/积木/模型","cat_name":"玩具/童车/益智/积木/模型","sub_categories":[]},{"id":"动漫/周边/cos/桌游","cat_name":"动漫/周边/cos/桌游","sub_categories":[]},{"id":"乐器/配件","cat_name":"乐器/配件","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"宠物用品","cat_name":"宠物用品","sub_categories":[{"id":"宠物用品/服饰","cat_name":"宠物用品/服饰","sub_categories":[]},{"id":"宠物食品","cat_name":"宠物食品","sub_categories":[]},{"id":"水族类","cat_name":"水族类","sub_categories":[]},{"id":"宠物保健","cat_name":"宠物保健","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"医药保健","cat_name":"医药保健","sub_categories":[{"id":"滋补品","cat_name":"滋补品","sub_categories":[]},{"id":"护理护具","cat_name":"护理护具","sub_categories":[]},{"id":"医疗器械","cat_name":"医疗器械","sub_categories":[]},{"id":"保健品","cat_name":"保健品","sub_categories":[]},{"id":"医药","cat_name":"医药","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"本地生活","cat_name":"本地生活","sub_categories":[{"id":"旅游度假","cat_name":"旅游度假","sub_categories":[]},{"id":"虚拟卡券","cat_name":"虚拟卡券","sub_categories":[]},{"id":"医疗服务","cat_name":"医疗服务","sub_categories":[]},{"id":"装修服务","cat_name":"装修服务","sub_categories":[]},{"id":"汽车服务","cat_name":"汽车服务","sub_categories":[]},{"id":"其他生活服务","cat_name":"其他生活服务","sub_categories":[]}]},{"id":"汽配摩托","cat_name":"汽配摩托","sub_categories":[{"id":"维修保养/清洗/美容","cat_name":"维修保养/清洗/美容","sub_categories":[]},{"id":"电子导航/车载电器","cat_name":"电子导航/车载电器","sub_categories":[]},{"id":"汽车/摩托车配件","cat_name":"汽车/摩托车配件","sub_categories":[]},{"id":"汽车装饰","cat_name":"汽车装饰","sub_categories":[]},{"id":"汽车/摩托车整车","cat_name":"汽车/摩托车整车","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]},{"id":"其他","cat_name":"其他","sub_categories":[{"id":"机械设备","cat_name":"机械设备","sub_categories":[]},{"id":"农资农具","cat_name":"农资农具","sub_categories":[]},{"id":"其他","cat_name":"其他","sub_categories":[]}]}],"errCode":0}'
response=response.json()

getjson=response['data']['id']
for item in getjson:
    print(item['id'])


    sleep(1)



