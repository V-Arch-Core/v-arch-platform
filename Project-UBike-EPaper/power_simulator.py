# V-Arch Power Simulation Tool v1.0
def check_sustainability(battery_ah, solar_watt, refresh_per_day):
    # 簡化的能源平衡模型
    daily_consumption = (refresh_per_day * 0.05) + 0.12  # 每次刷新功耗 + 24h 待機
    daily_generation = solar_watt * 3.5 * 0.7  # 假設平均 3.5 小時有效日照，70% 效率
    
    balance = daily_generation - daily_consumption
    status = "✅ 能源正增長" if balance > 0 else "❌ 能源入不敷出"
    
    print(f"每日發電量: {daily_generation:.2f} Wh")
    print(f"每日消耗量: {daily_consumption:.2f} Wh")
    print(f"結論: {status}")

# 範例測試：10W 太陽能板, 每日更新 24 次
check_sustainability(10, 10, 24)
