def f(money, interest, month):
    result = 0
    for i in range(month):
        result += money  # 每個月存入的錢數加到result中
        result *= (100+interest)/100  # 計算利息並加到result中

    return round(result)  # 返回四捨五入後的結果

# 獲取用戶輸入
m = eval(input("請輸入每月存入的錢數："))
i = eval(input("請輸入每月的利率（%）："))
mon = eval(input("請輸入投資的月份數："))

# 計算並打印最終金額
print(f"最終金額是：{f(m, i, mon)}")

# 等待用戶輸入以防止窗口立即關閉
input("請按任意鍵退出...")
