import scrapy
from unidecode import unidecode

class ComiteCentralSpider(scrapy.Spider):
    name = "comite_central"

    def start_requests(self):
        urls = [
            'https://www.pcp.pt/comite-central-do-pcp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        membros = response.css('div.membro')
        for membro in membros:
            nome = unidecode(membro.css("p.nome::text").get())
            ocupacao = unidecode(membro.css("p.desc::text").get().split('.')[0])
            tokens = ocupacao.split(' ')
            if tokens[0][-1] == 'a' and tokens[0] != 'Economista':
                index_to_replace = len(tokens[0])-1
                ocupacao_list = list(ocupacao)
                if ocupacao_list[index_to_replace-1] == 'r':
                    del ocupacao_list[index_to_replace]
                else:
                    ocupacao_list[index_to_replace] = 'o'
                ocupacao = ''.join(ocupacao_list)

            tokens = ocupacao.split(' ')
            if tokens[0] in ('Licenciado', 'Operario'):
                ocupacao = tokens[0]



            yield {
                'nome': nome,
                'ocupacao': ocupacao
            }
