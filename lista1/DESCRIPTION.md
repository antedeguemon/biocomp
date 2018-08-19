### 1.d
O arquivo eh lido e todas suas linhas sao reunidas em uma soh string.
Existe uma hash com 4 contadores para cada letra que jah sao conhecidas do arquivo.
Sempre que uma letra ja existente eh encontrada, o seu contador eh aumentado. Caso nao seja conhecida,
ela eh adicionada na array unknown.
Assim, varre-se todas as `letras` do arquivo, incrementando um contador quando sao encontradas letras
conhecidas ou adicionando em uma array quando nao sao.
```
Contadores: {'A': 17146584, 'C': 11918693, 'T': 17132531, 'G': 11909449}
Sim, caracteres diferentes encontrados: ['N']
```

### 1.c
Por ser intensivo, nao consigo usar um modo direto de executar este algoritmo, pois
nao tenho memoria o suficiente para armazenar tudo.
Como o arquivo tem 58109653 caracteres, foi possivel dividi-lo por 7 partes iguais,
ficando cada parte com 8301379 caracteres. 
