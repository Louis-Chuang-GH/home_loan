# 房貸試算

# 房貸金額
principal = 10000 * int(input("請輸入房貸金額 [整數] 萬: "))

# 年利率
apr = 0.01 * float(input("請輸入年利率 [小數] %: "))

# 借款期限
freq = 12 * int(input("請輸入借款期限 [整數] 年: "))

# 寬限期
g_period = 12 * int(input("請輸入寬限期 [整數] 年: 若無則輸入0 "))

# 總利息
g_interest = 0

# 每月還款金額計算
avg = round(principal/(freq-g_period))

print()

if g_period > 0:
    g = round(principal*apr/12)
    print("寬限期每月應償還利息:",g,"元")
    print("寬限期後，", end="")
    g_interest = g_interest + g * g_period

while True:
    total = principal
    total_g = g_interest

    
    for i in range(freq-g_period):
        total_g = round(total_g + total*apr/12)
        total = total - (avg - round(total*apr/12))
    else:
        if total <= 0:
            print("每月應還款:", avg, "元")
            break
        else:
            avg = avg + 1

print("總利息為:",total_g,"元")

"""
GPT 寫法
# 標準公式 等額本息（本息平均攤還）
# 房貸試算（等額本息）


# A 每月應付金額
P = 10000000           # 本金
r = 0.02275 / 12       # 月利率
n = 480                # 總期數（月）

A = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
print(f"每月應付金額：約 {round(A)} 元")
"""
