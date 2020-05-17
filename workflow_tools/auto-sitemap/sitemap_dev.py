# --- IMPORT --- #
import os
import glob
import json
import datetime

# --- "sitemap" ディレクトリがなければ作成 --- #
if not os.path.exists("sitemap"):
  os.mkdir("sitemap")
  print('Directory "sitemap" created')

# --- 変数定義 --- #
CHECK_DIR = ["data"]
ENCODING = "UTF-8"
JSON_FILES = ["data.json"]
HOST = "https://covid19-ibk-dev.netlify.app"
data_json = {}
posRate_json = {}

# --- data.jsonを開く --- #
with open("data/data.json", encoding=ENCODING) as file:
  data_json = json.load(file)
  print('Loaded data.json')

# --- positive_rate.jsonを開く --- #
with open("data/positive_rate.json", encoding=ENCODING) as file:
  posRate_json = json.load(file)
  print('Loaded positive_rate.json')

# --- パスおよび変更日時の指定 --- #
PATHS = {
  "/": data_json["lastUpdate"],
  "/cards/details-of-confirmed-cases": data_json["main_summary"]["children"][0]["date"],
  "/cards/number-of-confirmed-cases": data_json["patients"]["date"],
  "/cards/attributes-of-confirmed-cases": data_json["patients"]["date"],
  "/cards/number-of-reports-to-covid19-telephone-advisory-center": data_json["contacts"]["date"],
  "/cards/number-of-inspection-persons": data_json["inspection_persons"]["date"],
  "/cards/ibaraki-city-table": data_json["patients"]["date"],
  "/cards/ibaraki-city-map-table": data_json["patients"]["date"],
  "/cards/number-of-recovered": data_json["recovered_summary"]["date"],
  "/cards/number-of-deaths": data_json["deaths_summary"]["date"],
  "/cards/ibaraki-colona-next": data_json["ibk_colona_next"]["date"],
  "/cards/positive-rate": posRate_json["date"],
  "/about": "2020/05/15 18:00",
  "/contacts": "2020/05/15 18:00",
  "/flow": "2020/05/15 18:00",
  "/helpus": "2020/05/15 18:00",
  "/otherpref": "2020/05/15 18:00",
  "/parent": "2020/05/15 18:00",
  "/worker": "2020/05/15 18:00"
}

# --- Sitemap.xmlの作成部分 --- #
for lang in ("ja", "en", "ja-basic"):
  print('----------')
  print("Lang: {}".format(lang))
  # --- なければ作成 --- #
  if not os.path.exists("sitemap/{}".format(lang)):
    os.mkdir("sitemap/{}".format(lang))
    print('Language directory created')
  # --- なければ自動生成される。あればそれを開く --- #
  with open("sitemap/{}/sitemap.xml".format(lang), mode="a", encoding=ENCODING) as result:
    result.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    for path, updatedAt in PATHS.items():
      if lang == "ja":
        result.write('<url><loc>{}{}</loc>'.format(HOST,path))
      else:
        result.write('<url><loc>{}/{}{}</loc>'.format(HOST, lang, path))
      result.write('<lastmod>{}</lastmod>'.format(datetime.datetime.strptime(updatedAt, "%Y/%m/%d %H:%M").strftime("%Y-%m-%d")))
      result.write('<changefreq>daily</changefreq>')
      result.write('<mobile:mobile />')
      result.write('</url>')
      print("Path: {} (Updated at {}) ...done!".format(path, updatedAt))
    result.write('</urlset>')

print('----------')
print('All done!')
