import MeCab
mecab = MeCab.Tagger("-Ochasen")

tokenized_text = mecab.parse('ハリーポッターと賢者の石').split('\n')[0:-2]
surfaces = [t.split('\t')[0] for t in tokenized_text]
poses = [t.split('\t')[3].split('-')[0] for t in tokenized_text]
morphs = [{"surface":s, "pos":p} for (s,p) in zip(surfaces,poses)]
for m in morphs:
  print(m)
  
# {'surface': 'ハリーポッター', 'pos': '名詞'}
# {'surface': 'と', 'pos': '助詞'}
# {'surface': '賢者', 'pos': '名詞'}
# {'surface': 'の', 'pos': '助詞'}
# {'surface': '石', 'pos': '名詞'}
