import time
import requests
from bs4 import BeautifulSoup
import urllib3
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
URL = "https://www.mvdis.gov.tw/m3-emv-trn/exm/locations"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# You can adjust these sleep times as needed
NORMAL_SLEEP_TIME = 60
SLOW_SLEEP_TIME = 300
############################################

session = requests.Session()

while True:
    try:
        today = datetime.now()
        today_str = f"{today.year - 1911:03d}{today.month:02d}{today.day:02d}"
        r = session.post(
            URL,
            data={
                "method": "query",
                "licenseTypeCode": "3",
                "expectExamDateStr": max(today_str, "1150617"),
                "dmvNoLv1": "40",
                "dmvNo": "43"
            },
            timeout=10,
            verify=False
        )

        soup = BeautifulSoup(r.text, "html.parser")

        rows = soup.select("#trnTable tbody tr")

        if not rows:
            print("查不到場次")
            time.sleep(NORMAL_SLEEP_TIME)
            continue

        available = False

        for row in rows:
            cols = row.find_all("td")

            if len(cols) < 4:
                continue

            date_text = cols[0].get_text(" ", strip=True)
            desc_text = cols[1].get_text(" ", strip=True)
            count_text = cols[2].get_text(" ", strip=True)

            if "重考生" in desc_text:
                continue

            short_desc = desc_text[:4] + "..." if len(desc_text) > 4 else desc_text
            # print(f"[{date_text}] [{short_desc}] [{count_text}]")

            if "額滿" in count_text:
                continue

            available = True

            print("=" * 80)
            print("發現空位！")
            print(date_text)
            print(desc_text)
            print("剩餘名額:", count_text)
            print("=" * 80)

            requests.post(
                WEBHOOK_URL,
                json={
                    "content": f"🚨 五結監理站有位置！\n日期：{date_text}\n場次：{desc_text}\n剩餘名額：{count_text}"
                },
                timeout=10
            )

            print("Discord通知已送出")

        if available:
            time.sleep(SLOW_SLEEP_TIME)
        else:
            print(f"超可憐沒位置 at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(NORMAL_SLEEP_TIME)

        

    except Exception as e:
        print("錯誤:", e)
        requests.post(
            WEBHOOK_URL,
            json={
                "content": f"錯誤訊息：{str(e)}"
            },
            timeout=10
        )
        time.sleep(NORMAL_SLEEP_TIME)