# UBike Outdoor E-Paper Display Project
## 核心技術規格 (Technical Specifications)

### 1. 能源收支平衡公式 (Energy Balance Equation)
為了確保系統在不拉市電的情況下永不斷電，必須滿足以下物理限制：

$$P_{solar} \times \eta \times T_{sun} > (E_{wake} \times N_{refresh}) + (P_{sleep} \times 24h)$$

* $P_{solar}$: 太陽能板額定功率
* $\eta$: 轉換效率 (含 MPPT 損耗)
* $T_{sun}$: 平均每日有效日照時數
* $E_{wake}$: 單次喚醒更新功耗
* $N_{refresh}$: 每日更新次數
* $P_{sleep}$: 深層睡眠功耗

### 2. 硬體選型準則
* **SOC**: Rockchip RV1106 (支援 Fastboot，降低 $E_{wake}$)
* **Display**: Kaleido 3 Color E-Ink
* **Battery**: LiFePO4 10Ah (耐高溫，循環壽命長)
