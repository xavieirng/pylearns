from idlelib.iomenu import encoding
from time import sleep
import openpyxl
import requests
from bs4 import BeautifulSoup
from pyasn1.compat.octets import null

cookies = {
    'laravel_session': 'eyJpdiI6InFqWG1HOSs4a2VGWkR6NVpPelJINkE9PSIsInZhbHVlIjoiNUIwelNxandVSmVmMVBDTmZRQmFrS2xkT1wvY1F0YjhrZ2JzdGpKVVE2N3hhSjJUMmREQVlmZHZSZTBYVjB3OFFteEludWhRWVlnbXM0SUdSb3JDRDhRPT0iLCJtYWMiOiI4N2JkZWI5OGMzNzEwNjEwNWE3YjRiMTVhZWZkODJjZTg5M2NjMjI4ODBjMzRkMDQzMDU5YmM4MTRiNThiNTQ4In0%3D',
    'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImV4cGlyZV90aW1lIjoxNjQxNDA5MjAwLCJpYXQiOjE2NDA4NTQzMTYsImlkIjoyOTc2MTQ2fQ.0107HOHwYM2c21dgEgu5StRWG2Ba1EYBVs1PCkQjTIY',
    'UM_distinctid': '17e0a8d6e8736f-0dc22cb83b0423-4c607a68-1fa400-17e0a8d6e88367',
    'Hm_lvt_1f19c27e7e3e3255a5c79248a7f4bdf1': '1640854202,1640925854',
    'Hm_lpvt_1f19c27e7e3e3255a5c79248a7f4bdf1': '1640925854',
    'Qs_lvt_411649': '1640854201%2C1640925853',
    'Qs_pv_411649': '3610981674982469000%2C317525044407294300%2C1373714792570628900%2C469213097273985600%2C1750045556357279200',
    'mediav': '%7B%22eid%22%3A%221090564%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22LM9wyh34)I8ifXqH%3C40%5B%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22LM9wyh34)I8ifXqH%3C40%5B%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A1%7D',
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
    'If-None-Match': 'W/"61ce7d0c-beb8"',
    'If-Modified-Since': 'Fri, 31 Dec 2021 03:46:20 GMT',
}



Big_category=["服饰内衣",'食品饮料',"日用百货","美妆护肤","珠宝饰品","母婴用品","生鲜蔬果","图书音像","鞋靴箱包","家居家纺","鲜花绿植","运动户外","钟表配饰","3C数码","礼品文创","家具建材","厨卫家电","玩具乐器","宠物用品","医药保健","本地生活","汽配摩托","其他"]
Subcategory=[["女装","男装","婴童装/亲子装","内衣/袜子","家居服","其他"],
            ["茶","粮油米面/南北干货/调味品", "乳品/咖啡/冲调","方便速食/速冻食品","其他"],
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

# Big_category=["服饰内衣"]
# Subcategory=[["女装","男装","婴童装/亲子装","内衣/袜子","家居服","其他"]]


for i, big in enumerate(Big_category):
    for category in Subcategory[i]:
        params = (
            ('keyword', ''),
            ('big_category', big),
            ('first_category', category),
        )
        for item in range(1,101,1):
            hhh=str(item)
            html='https://api-service.chanmama.com/v2/shop/search?page='+hhh+'&big_category='+str(big)+'&first_category='+str(category)+'&keyword=&sort=volume&orderby=desc&size=50&has_aweme=0&has_live=0&avg_price=&avg_amount=&expr_score='
            print(html)
            response = requests.post(html, headers=headers, cookies=cookies)

            response=response.json()

            getjson=response['data']['list']
            for item in getjson:
                c=big
                d=category.split('/')
                a=item['shop_name']
                b=item['shop_tel']

                name=str(c)+str(d)+"1.xls"
                with open('test.xls', 'a',encoding='utf-8-sig',  errors='ignore') as f:

                    f.write(c)
                    if(a!=null):
                        f.write(',')
                    f.write(d[0])
                    if(a!=null):
                        f.write(',')
                    f.write(a)
                    if(a!=null):
                        f.write(',')
                    f.write(b)
                    if(a!=null):
                        f.write(',')
                        f.write('\n')

                with open(name, 'a',encoding='utf-8-sig',  errors='ignore') as f:

                    f.write(c)
                    if(a!=null):
                        f.write(',')
                    f.write(d[0])
                    if(a!=null):
                        f.write(',')
                    f.write(a)
                    if(a!=null):
                        f.write(',')
                    f.write(b)
                    if(a!=null):
                        f.write(',')
                        f.write('\n')


        sleep(1)



