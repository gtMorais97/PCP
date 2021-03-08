import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

with open('pcp/comite_central_pcp.json') as f:
    membros = json.load(f)
    ocupacoes = [membro['ocupacao'] for membro in membros]
    ocupacoes_count = Counter(ocupacoes)
    ocupacoes_count = dict(sorted(ocupacoes_count.items(), key=lambda item: item[1]))
    '''
    ocupacoes_count['Outro'] = 0
    for ocupacao in ocupacoes_count.keys():
        if ocupacoes_count[ocupacao] < 3:
            ocupacoes_count['Outro'] += ocupacoes_count[ocupacao]
    '''
    ocupacoes_count_final = {k: int(v) for k, v in ocupacoes_count.items() if v>=3}

    print(ocupacoes_count_final)
    fig = plt.figure(figsize=(20,10))
    labels = [k for k in ocupacoes_count_final.keys()]
    values = [int(v) for v in ocupacoes_count_final.values()]
    plt.bar(labels, values)
    plt.title('Ocupações do comité central do PCP (mínimo de 3 elementos por ocupação)')

    for i, v in enumerate(values):
        x = i-.06 if v>9 else i-.03
        plt.text( x,
                  v+0.5,
                  str(v),
                  fontsize=18,
                  color='tab:blue')

    plt.savefig("pcp_ocupacoes_hist")
