# Score-IA-py

## Descrição
Sistema de análise e previsao de score de crédito utilizando Machine Learning. O projeto processa dados financeiros de clientes e treina modelos para classificar o score de crédito em categorias (Good, Standard, Poor).

## Funcionalidades
- **Análise de dados**: Processamento de dataset com 100.000 registros de clientes
- **Pré-processamento**: Codificação de variáveis categóricas (profissão, mix de crédito, comportamento de pagamento)
- **Modelos ML**: Implementação de Random Forest e K-Nearest Neighbors
- **Avaliação**: Comparação de performance entre diferentes algoritmos

## Dataset
O dataset contém 25 variáveis incluindo:
- Dados pessoais (idade, profissão, salário)
- Histórico financeiro (contas, cartões, empréstimos)
- Comportamento de pagamento
- Score de crédito (variável target)

## Tecnologias
- **Python 3.12+**
- **pandas**: Manipulação de dados
- **scikit-learn**: Machine Learning
- **Jupyter Notebook**: Desenvolvimento interativo

## Resultados
O sistema compara a performance de dois algoritmos:
- **Random Forest**: Modelo ensemble baseado em árvores de decisão
- **K-Nearest Neighbors**: Classificação baseada em proximidade

As métricas de acurácia são exibidas para comparação e seleção do melhor modelo.
