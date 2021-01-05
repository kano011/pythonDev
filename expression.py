import codecs
from janome.tokenizer import Tokenizer

# pn_ja.dicファイルから、単語をキー、極性値を値とする辞書を得る
def load_pn_dict():
    dic = {}
    
    with codecs.open('data/pn_ja.dic', 'r', 'utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            columns = line.split(':')
            dic[columns[0]] = float(columns[3])
            
    return dic


# トークンリストから極性値リストを得る
def get_pn_scores(tokens, pn_dic):

    for surface in [t.surface for t in tokens if t.part_of_speech.split(',')[0] in ['動詞','名詞', '形容詞', '副詞']]:
        textArray = []
        numArray = []
        if surface in pn_dic:
            textArray.append(surface)
            numArray.append(pn_dic[surface])
        if not textArray:
            continue
        print(textArray, numArray)


def returnExpressionScore(texts):
    naive_tokenizer = Tokenizer()
    pn_dic = load_pn_dict()

    for tweet in texts:
        token = naive_tokenizer.tokenize(tweet)
        point = get_pn_scores(token, pn_dic)

t = input()

print(returnExpressionScore(t))
