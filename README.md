# 機車駕照初考名額通知

每次都搶不到機車駕照考試，一怒之下寫了這個

僅提供教材，禁止各種非法用途

---

# 功能

* 發現名額透過discord通知
* 切記！！！沒有搶名額的功能，當然你有想法可以嘗試

---

# 執行環境

作業系統：

* linux
* 當然你想用windows也行，步驟不太一樣但我懶得寫

---

# 安裝步驟

## 1. 下載專案

```bash
git clone https://github.com/lcytot211226/taiwan-scooter-license-notifier.git
cd taiwan-scooter-license-notifier.git
```

---

## 2. 建立 Python 虛擬環境

建立虛擬環境：

```bash
python3 -m venv .venv
```

啟用虛擬環境：

```bash
source .venv/bin/activate
```

成功後前面會出現：

```bash
(.venv)
```

代表已進入虛擬環境。

---

## 3. 安裝所有需要的套件

```bash
pip install -r requirements.txt
```

程式會自動安裝所有依賴套件。

---

## 4. 建立 Discord Webhook

進入自己的 Discord 伺服器。

選擇要接收通知的頻道：

右鍵頻道 → 編輯頻道

進入：

```text
整合 → Webhook
```

建立新的 Webhook。

複製 Webhook URL。

格式類似：

```text
https://discord.com/api/webhooks/xxxxxxxxxxxxxxxx
```

---

## 5. 建立設定檔

編輯：

```bash
nano .env
```

填入自己的設定。

範例：

```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxxxxxx
```

儲存離開：

```text
Ctrl + O
Enter
Ctrl + X
```

注意！千萬別洩漏這個連結

---

# 啟動程式

執行：

```bash
python bot.py
```
---

# 停止程式

按下：

```bash
Ctrl + C
```

即可停止。

---

# 通知間隔

bot.py 的第16.17行，單位是秒

會程式的就隨便改，教學用途嘛

---


# 注意事項

本工具僅協助監控公開可報名之考照名額。

請遵守監理站相關規定與網站使用條款。

若程式有任何問題，請直接將錯誤訊息複製貼上給 ChatGPT 詢問，通常能快速找到解決方法。

祝大家順利搶到理想的考照時段！
