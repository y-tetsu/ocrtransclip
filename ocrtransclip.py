"""ocrtransclip
"""
import os
import pathlib
import re

from PIL import Image
import pyocr
import googletrans
import pyperclip


class OcrTool:
    def __init__(self, ocr_tool_path, layout=3, lang='jpn'):
        self.path = self._add_tesseract_path(ocr_tool_path)
        self.tool = self._select_tesseract_for_ocr_tool()
        self.builder = self._setup_tesseract_builder(layout)
        self.lang = lang

    def _add_tesseract_path(self, tool_path):
        path = pathlib.Path(tool_path)
        os.environ['PATH'] += ';' + str(path)
        return path

    def _select_tesseract_for_ocr_tool(self):
        print(pyocr.get_available_tools())
        return pyocr.get_available_tools()[0]

    def _setup_tesseract_builder(self, layout):
        return pyocr.builders.TextBuilder(tesseract_layout=layout)

    def image_to_string(self, image_file):
        img = Image.open(image_file)
        return self.tool.image_to_string(img, lang=self.lang, builder=self.builder)


class Translator:
    def __init__(self):
        self.translator = googletrans.Translator()

    def _pre_format(self, text, src, dest):
        if src == 'en':
            # format sentence
            text = re.sub(r'\n(\w)', r' \1', text)
            text = re.sub(r'(\.[^\.]+)\n', r'\1', text)
            # format period
            text = re.sub(r'\.', r'.\n', text)
            # remove space
            text = re.sub(r'\n\s+', r'\n', text)
            text = re.sub(r'\s+\n', r'\n', text)
        return text

    def run(self, text):
        detect = self.translator.detect(text)
        src, dest = ('ja', 'en') if detect.lang == 'ja' else ('en', 'ja')
        text = self._pre_format(text, src, dest)
        translated = self.translator.translate(text, src=src, dest=dest).text
        pyperclip.copy(translated)
        return translated


if __name__ == '__main__':
    ocrtool = OcrTool('C:\\Program Files\\Tesseract-OCR')
    translator = Translator()

    # test01
    path = pathlib.Path('.\\tests\\test01.png')

    # OCR
    ocr_text = ocrtool.image_to_string(str(path))
    expected = """Home

stefan Weiledited this page 26 days ago・70 revisions

Tesseract at UB Mannheim

The Mannheim University Librar (UB Mannheim) uses Tesseract to perform OCR (optical character recognition) of historical
German newspapers (Allgemeine PreuBische Staatszeituno, Deutscher Reichsanzeige. The latest results with OCR from more

than 360,000 scans are available online."""
    print(ocr_text)
    assert ocr_text == expected, '*** Error : ocr_text is not match. ***\n(expected)\n---\n' + expected + '\n---\n'

    # translation
    trans_text = translator.run(ocr_text)
    expected = """家
Stefan weilileedこのページ26日前・70リビジョン
UBマンハイムのテッセサクト
Mannheim University Librar（UB Manheim）はTesseractを使用して歴史的なドイツの新聞のOCR（Optical Character認識）を実行します（Allgemeine Preubische Staatszeituno、Deutscher Reichsanzeige。
360,000以上のスキャンからOCRを持つ最新の結果がオンラインで入手可能です。"""
    print(trans_text)
    assert trans_text == expected, '*** Error : trans_text is not match. ***\n(expected)\n---\n' + expected + '\n---\n'
