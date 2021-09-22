inputMoney = int(input("请输入消费金额"))
if inputMoney > 0:
    print("消费金额为：" + str(inputMoney))
    print("支付成功，对方已经收款")
else:
    print("支付失败")
