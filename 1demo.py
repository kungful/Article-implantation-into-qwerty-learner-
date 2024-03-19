import requests
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import json
import nltk
from nltk.corpus import cmudict
import re
from googletrans import Translator as GoogleTranslator
import pronouncing

class ArticleTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文章植入qwerty")
        self.root.configure(bg="black")

        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="输入文章:", bg="black", fg="white")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.text_area = scrolledtext.ScrolledText(self.frame, width=40, height=10)
        self.text_area.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.translate_button = tk.Button(self.frame, text="翻译", command=self.translate_article)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text="保存", command=self.save_json)
        self.save_button.grid(row=2, column=1, padx=5, pady=5)

        self.api_label = tk.Label(self.frame, text="选择翻译API:", bg="black", fg="white")
        self.api_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.api_var = tk.StringVar()
        self.api_var.set("谷歌")
        self.api_menu = tk.OptionMenu(self.frame, self.api_var, "谷歌", "必应")
        self.api_menu.grid(row=3, column=1, padx=5, pady=5)

        self.word_per_line_label = tk.Label(self.frame, text="每行翻译单词数量:", bg="black", fg="white")
        self.word_per_line_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.word_per_line_scale = tk.Scale(self.frame, from_=1, to=10, orient="horizontal")
        self.word_per_line_scale.set(1)  # 默认为每行翻译一个单词
        self.word_per_line_scale.grid(row=4, column=1, padx=5, pady=5)

        self.result_label = tk.Label(self.frame, text="翻译结果:", bg="black", fg="white")
        self.result_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.result_text = scrolledtext.ScrolledText(self.frame, width=40, height=10)
        self.result_text.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

        self.usage_label = tk.Label(self.frame, text="使用说明:\n1. 翻译后请保存到qwerty-learner\\public\\dicts目录进行替换。\n2. 如果qwerty没有显示，需在qwerty-learner\\src\\resources\\dictionary.ts中添加索引。\n3. 关于qwerty添加词典的教程请参考：https://github.com/RealKai42/qwerty-learner/blob/master/docs/toBuildDict.md", bg="black", fg="white")
        self.usage_label.grid(row=7, column=0, padx=5, pady=5, columnspan=2)

        self.d = cmudict.dict()

    def translate_article(self):
        article = self.text_area.get("1.0", tk.END)
        word_per_line = self.word_per_line_scale.get()
        filtered_article = self.filter_non_english_words(article)
        translated_article = self._translate_text(filtered_article, word_per_line)
        result_json = json.dumps(translated_article, ensure_ascii=False, indent=4)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_json)

        self.result_label.config(text="翻译结果:")

    def save_json(self):
        json_data = self.result_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(json_data)

    def _translate_text(self, text, word_per_line, dest='zh-CN'):
        api = self.api_var.get()
        if api == "谷歌":
            translator = GoogleTranslator()
            translated_article = []
            words = text.split()
            for i in range(0, len(words), word_per_line):
                chunk = " ".join(words[i:i+word_per_line])
                translation = translator.translate(chunk, dest=dest)
                word_dict = {
                    "name": chunk,
                    "trans": [translation.text],
                    "usphone": self.get_phonetic(chunk),
                    "ukphone": ""
                }
                translated_article.append(word_dict)
            return translated_article
        elif api == "必应":
            translated_article = []
            words = text.split()
            for i in range(0, len(words), word_per_line):
                chunk = " ".join(words[i:i+word_per_line])
                translation = self.translate_text_bing(chunk, dest)
                word_dict = {
                    "name": chunk,
                    "trans": [translation],
                    "usphone": self.get_phonetic(chunk),
                    "ukphone": ""
                }
                translated_article.append(word_dict)
            return translated_article
        else:
            messagebox.showerror("错误", "选择的翻译API无效")
            return []

    def get_phonetic(self, word):
        word = word.lower()
        phones_list = pronouncing.phones_for_word(word)
        if phones_list:
            phonetic = " , ".join(phones_list)
            return phonetic
        else:
            return "Unknown"

    def filter_non_english_words(self, text):
        # 使用正则表达式匹配非英文单词和标点符号
        english_words = re.findall(r'\b[A-Za-z]+\b', text)
        return " ".join(english_words)

    def translate_text_bing(self, text, dest):
        url = 'https://api.cognitive.microsofttranslator.com/translate'
        payload = [{'text': text, 'to': dest}]
        headers = {
            'Ocp-Apim-Subscription-Key': 'your_subscription_key',  # 替换为你的订阅密钥
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            translation = response.json()[0]['translations'][0]['text']
            return translation
        else:
            print("Translation failed with status code:", response.status_code)
            return None

if __name__ == "__main__":
    nltk.download('cmudict')
    root = tk.Tk()
    app = ArticleTranslatorApp(root)
    root.mainloop()
