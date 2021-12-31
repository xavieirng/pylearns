def fun_bmr(name,gender,weight,height,age):
    if gender == '男':
        bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    print('您的姓名：{},性别：{},体重:{}公斤，身高:{}厘米，年龄：{}岁'.format(name,gender,weight,height,age))
    print('您的基础代谢率{}卡路里'.format(bmr))
fun_bmr('李平','男',60,175,15)
fun_bmr('周虹','女',50,155,14)
