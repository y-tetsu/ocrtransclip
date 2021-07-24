"""ocrtransclip
"""
import os
import pathlib
from PIL import Image
import pyocr


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


if __name__ == '__main__':
    ocrtool = OcrTool('C:\\Program Files\\Tesseract-OCR')

    # test01
    path = pathlib.Path('.\\tests\\test01.png')
    output = ocrtool.image_to_string(str(path))
    expected = """Home

stefan Weiledited this page 26 days ago・70 revisions

Tesseract at UB Mannheim

The Mannheim University Librar (UB Mannheim) uses Tesseract to perform OCR (optical character recognition) of historical
German newspapers (Allgemeine PreuBische Staatszeituno, Deutscher Reichsanzeige. The latest results with OCR from more

than 360,000 scans are available online."""
    print(output)
    assert output == expected, '*** Error : output is not match. ***\n(expected)\n---\n' + expected + '\n---\n'
