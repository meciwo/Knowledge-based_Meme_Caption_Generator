import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from collections import defaultdict
import os

LOAD_URL = "https://bokete.jp/odai/"
SAVE_PATH = "../../../../Volumes/my_strage/data/images/"
OUTPUT_PATH = "data/relation/"
d = defaultdict(list)
missed_img_num = 0
download_num = 100000
# texts = []
# Webページを取得して解析する
# 4.4MB/100毎
for page in tqdm(range(download_num)):
    # batch_df = pd.DataFrame([])
    page_url = LOAD_URL + "1" + str(page).zfill(6)
    try:
        html = requests.get(page_url)
        soup = BeautifulSoup(html.content, "html.parser")
        try:
            img_path = soup.find("div", class_="photo-content").find("img").get("src")
            img_id = img_path.split("/")[-1]
            save_img = False
            for boke in soup.find_all("div", class_="boke"):
                text = boke.find("a", class_="boke-text")
                star = boke.find("div", class_="boke-stars")
                if text is not None and star is not None:
                    d[img_id].append([text.get_text().strip(), star.get_text().strip()])
                    save_img = True
                # texts.append(text.get_text().strip())
            if save_img:
                # 存在するならsaveしない
                if not os.path.exists(SAVE_PATH + img_id):
                    re = requests.get("https:" + img_path)
                    with open(SAVE_PATH + img_id, "wb") as f:
                        f.write(re.content)

            # batch_df["image"] = [img_id] * len(texts)
            # batch_df["text"] = texts
            # main_df = pd.concat([main_df, batch_df], axis=0)

        except AttributeError:
            missed_img_num += 1
    except ConnectionError:
        print("http connection error happened")

    if (page + 1) % (download_num // 10) == 0:
        main_df = pd.DataFrame(
            [
                [image, text, star]
                for image, text_star in d.items()
                for text, star in text_star
            ],
            columns=["image", "text", "star"],
        )
        main_df.to_csv(
            OUTPUT_PATH + str(page // (download_num // 10)) + ".csv", index=False
        )
        d = defaultdict(list)
print(f"missed {missed_img_num}imges")
print("scraping done")
