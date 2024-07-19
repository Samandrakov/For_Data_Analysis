url_list = ["https://www.globo.com", "https://www.gazetadopovo.com.br/", "https://www.firjan.com.br/noticias/", "https://www.estadao.com.br/", "https://www.em.com.br", "https://www.diariodocentrodomundo.com.br/", "https://www.correiobraziliense.com.br/", "https://www.campograndenews.com.br/", "https://www.brasildefato.com.br/english/", "https://www.brasil247.com/", "https://www.amcham.com.br", "https://www.agoramt.com.br/mundo/", "https://veja.abril.com.br", "https://valor.globo.com/", "https://revistaforum.com.br/", "https://jornalggn.com.br/", "https://brazilian.report", "https://apexbrasil.com.br/br/pt/conteudo/noticias.html", "https://agenciabrasil.ebc.com.br/en/geral", "https://oglobo.globo.com/", "https://www.vermelho.org.br", "https://www.uol.com.br/", "https://www.terra.com.br/", "https://www.riotimesonline.com/", "https://www.pragmatismopolitico.com.br/", "https://www.jornaldocomercio.com/", "https://www.jb.com.br", "https://www.ig.com.br/", "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias-2", "https://www.gov.br/mre", "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias", "https://www.gov.br/casacivil/pt-br/assuntos/noticias", "https://www.gov.br"]

with open('alt_urls.txt','w') as f:
    f.write('(')
    for i in range(len(url_list)):
        f.write(f"doc.external_url LIKE '{url_list[i]}%' OR\n")

