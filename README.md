# ocrtransclip
OCRで翻訳ツール

## 使い方
1. コマンドプロンプトで以下を実行してツール起動
```
$ py -3.9 ocrtransclip.py
```
2. 翻訳したい部分を[Windowロゴ]キー + [Shift]キー + [S]キー ショートカットを使ってキャプチャ
3. OCRと翻訳(英語⇒日本語)が実施され、翻訳結果のテキストをクリップボードに送る

## 動作環境
- Windows10 64bit<br>
- [Python 3.9.6](https://www.python.org/downloads/release/python-396/)<br>
    - Pillow      8.3.1<br>
    - pyocr       0.8<br>
    - googletrans 4.0.0rc1<br>
    - pyperclip   1.8.2<br>
    - numpy       1.21.1<br>
- [Tesseract v5.0.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)<br>

## pipインストール
```
$ py -3.9 -m pip install pyocr
$ py -3.9 -m pip install googletrans==4.0.0-rc1
$ py -3.9 -m pip install pyperclip
$ py -3.9 -m pip install numpy
```
## 注意事項
本ツールはTesseractが'C:\\Program Files\\Tesseract-OCR'にインストールされている前提で動作します。

## 参考サイト
- 「Python＋Tesseractによる画像処理でOCRを試してみた！」https://rightcode.co.jp/blog/information-technology/python-tesseract-image-processing-ocr
- 「【python】googletransの『AttributeError: 'NoneType' object has no attribute 'group'』対策【2021/01/12追記】」https://qiita.com/_yushuu/items/83c51e29771530646659