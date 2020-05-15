import twitter
import os
import glob
import json

auth = twitter.OAuth(consumer_key=os.environ['API_KEY'],
consumer_secret=os.environ['API_SECRET'],
token=os.environ['ACCESS_TOKEN'],
token_secret=os.environ['ACCESS_SECRET'])

CHECK_DIR = ["data"]
ENCODING = "UTF-8"
JSON_FILES = ["data.json"]
lastUpdate = ""

t = twitter.Twitter(auth=auth)

for cdir in CHECK_DIR:
  cdir = os.path.join(os.pardir, os.pardir, cdir)

  json_files = glob.glob(cdir + os.sep + "**" + os.sep + "*.json", recursive=True)
  # 各jsonファイルについて処理
  for path in json_files:
    file_name = os.path.basename(path)
    # jsonファイルが調べるべきjsonであるか
    if file_name in JSON_FILES:
      with open(path, encoding=ENCODING) as file:
        # jsonを読み込み
        json_content = json.load(file)
        # タグリストを生成
        if file_name == JSON_FILES[0]:  # data.jsonの場合
          lastUpdate = json_content["lastUpdate"]
          print("更新日時: "+lastUpdate+"\n")

msg = str(os.environ['MSG'])
msgJson = json.loads(msg)
commitMsg = msgJson[len(msgJson)-1]["message"].splitlines()
print("Commit Message:\n----------")
print(msg)
print("----------\n")

updContent = ""
for i in range(len(commitMsg)):
  if i<1: continue
  txt = commitMsg[i]
  updContent += txt
  updContent += "\n"

print("LAST COMMIT MESSAGE")
print(updContent)

status="【 #茨城県 版 #新型コロナウイルス 対策サイト 更新情報】\nhttps://ibaraki.stopcovid19.jp/\n"+lastUpdate+"更新\n\n更新内容\n"+updContent+"\n※反映に時間がかかることがあります。\n#StayHome #家で過ごそう"

print("TWEET MESSAGE\n----------\n"+status+"\n----------")

t.statuses.update(status=status)