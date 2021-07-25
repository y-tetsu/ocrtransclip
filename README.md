# ocrtransclip
OCRで翻訳ツール


## 使い方
1. コマンドプロンプトで以下を実行してツールを起動して下さい。
```
$ py -3.9 ocrtransclip.py
```
2. 翻訳したい部分を[Windowロゴ]キー + [Shift]キー + [S]キー ショートカットを使ってキャプチャして下さい。
3. OCRと翻訳(英語⇒日本語)が実施され、結果がコマンドプロンプトに表示されます。
4. また、翻訳結果のテキストがクリップボードに送られます。
5. 必要に応じて、お好きな場所に貼り付けてください。


## 動作環境
- Windows10 64bit<br>
- [Python 3.9.6](https://www.python.org/downloads/release/python-396/)<br>
    - Pillow      8.3.1<br>
    - pyocr       0.8<br>
    - googletrans 4.0.0rc1<br>
    - pyperclip   1.8.2<br>
    - numpy       1.21.1<br>
- [Tesseract v5.0.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)<br>


## インストール
1. 任意の場所にコードを[ダウンロード](https://github.com/y-tetsu/ocrtransclip/archive/refs/heads/main.zip)してzipを解凍してください。
2. 以下を実施して必要なライブラリを全てインストールしてください。
```
$ py -3.9 -m pip install pyocr
$ py -3.9 -m pip install googletrans==4.0.0-rc1
$ py -3.9 -m pip install pyperclip
$ py -3.9 -m pip install numpy
```
3. [Tesseract v5.0.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)をインストールしてください。([Python＋Tesseractによる画像処理でOCRを試してみた！](https://rightcode.co.jp/blog/information-technology/python-tesseract-image-processing-ocr)参照)


## 注意事項
本ツールはTesseractが'C:\\Program Files\\Tesseract-OCR'にインストールされている前提で動作します。
