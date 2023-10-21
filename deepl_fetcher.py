import deepl 
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

auth_key = os.environ.get("AUTH_KEY")
print(auth_key)
translator = deepl.Translator(auth_key)
text = "ライトフライヤースタジオ × Keyが贈る、ドラマチックRPG『ヘブンバーンズレッド（ヘブバン）』の公式Twitter。🎫ヘブバンライブ2024抽選先行チケット受付中！👉http://eplus.jp/hbrlive2024/ ⏰11/5（日）23:59まで" 
target_language = "EN-US"
result = translator.translate_text(text, target_lang=target_language) 
translated_text = result.text
print(f"DeepL: {translated_text}")