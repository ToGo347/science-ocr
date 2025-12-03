from science_ocr import ScienceOCR
from difflib import SequenceMatcher

def test_ocr():
	socr = ScienceOCR()
	with open('tests/fixtures/573_574BSEA44NBSharpiarubida_300dpi.txt', 'r') as f:
		og_text = f.read()
		for dpi in range(96, 300, 16):
			text = socr.parse_text('tests/fixtures/573_574BSEA44NBSharpiarubida.pdf', dpi=dpi)
			score = SequenceMatcher(None, text, og_text).ratio()
			print(dpi, score)
			assert score > 0.9
