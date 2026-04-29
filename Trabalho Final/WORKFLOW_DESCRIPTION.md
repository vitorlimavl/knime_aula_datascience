# Workflow KNIME - Detecção de Notas Falsas com Redes Neurais

## Informações do Projeto
- **Aluno**: Vitor Hugo Vasconcellos de Lima
- **Email**: vitor.hugo.9999@gmail.com
- **Dataset**: fake_bills.csv
- **Objetivo**: Classificação binária para detectar notas falsas vs. genuínas usando Redes Neurais

## Arquitetura do Workflow

### 1. **Bloco Inicial - Informações do Projeto**
   - Nome do aluno: Vitor Hugo Vasconcellos de Lima
   - Email: vitor.hugo.9999@gmail.com
   - Link do Dataset: fake_bills.csv
   - Descrição: Projeto para classificação de notas falsas usando Rede Neural

### 2. **Bloco de Carregamento de Dados**
   - **CSV Reader Node**: Carrega o arquivo `fake_bills.csv`
   - Separador: Ponto-e-vírgula (;)
   - Entrada: 1500 registros, 7 colunas (1 target + 6 features)

### 3. **Bloco de Pré-processamento**
   - **Missing Value Handler**: Trata valores faltantes (37 NaNs em margin_low)
     - Método: Preenchimento com média
   - **Normalizer Node**: Normaliza as features (StandardScaler)
     - Método: Z-score normalization
     - Escala: [-3, 3]

### 4. **Bloco de Divisão de Dados**
   - **Partitioner Node**: Divide dados em treino/teste
     - Proporção: 80% treino (1200 registros), 20% teste (300 registros)
     - Método: Stratified split (mantém proporção de classes)
     - Estratificação: Baseada na coluna `is_genuine`

### 5. **Bloco de Redes Neurais - Treinamento**
   - **Deep Learning - Keras Network Learning**: Treina a Rede Neural
     - **Arquitetura**:
       - Camada 1: 64 neurônios (ativação ReLU)
       - Camada 2: 32 neurônios (ativação ReLU)
       - Camada 3: 16 neurônios (ativação ReLU)
       - Camada Saída: 1 neurônio (ativação Sigmoid) - Classificação Binária
     - **Hiperparâmetros**:
       - Otimizador: Adam
       - Loss Function: Binary Crossentropy
       - Batch Size: 32
       - Épocas: 50
       - Validation Split: 20%
       - Early Stopping: Sim (paciência: 20 iterações)
     - **Saída**: Modelo treinado

### 6. **Bloco de Predição**
   - **Deep Learning - Keras Network Executor**: Realiza predições no conjunto de teste
     - Entrada: Modelo treinado + Dados de teste
     - Saída: Probabilidades de cada classe + Predição final

### 7. **Bloco de Avaliação e Métricas**
   - **Scorer Node**: Calcula métricas de performance
     - Acurácia
     - Precisão
     - Recall
     - F1-Score
   - **Confusion Matrix**: Gera matriz de confusão
   - **ROC Curve**: Gera curva ROC e calcula AUC
   - **Classification Report**: Relatório detalhado por classe

### 8. **Bloco de Visualização**
   - **Linha 1 - Loss durante Treinamento**: Gráfico de convergência
   - **Linha 2 - Matriz de Confusão**: Heatmap dos erros
   - **Linha 3 - Curva ROC**: Análise de trade-off TPR/FPR
   - **Linha 4 - Distribuição de Probabilidades**: Histograma das predições
   - **Linha 5 - Resumo de Métricas**: Gráfico de barras com todas as métricas
   - **Linha 6 - Distribuição Original vs Predita**: Comparação de classes

## Fluxo de Dados

```
fake_bills.csv
     ↓
[CSV Reader]
     ↓
[Missing Value Handler] → Trata NaNs
     ↓
[Normalizer] → StandardScaler
     ↓
[Partitioner] → Split 80/20
     ├─→ [Treino (1200)]
     │    ↓
     │  [Deep Learning Learner]
     │    ↓
     │  [Modelo Treinado]
     │
     └─→ [Teste (300)]
          ↓
          [Deep Learning Executor] ← [Modelo]
          ↓
      [Predições]
          ↓
    [Scorer/Evaluator]
          ↓
    [Métricas e Gráficos]
```

## Resultados Finais

### Métricas de Performance
| Métrica | Valor |
|---------|-------|
| Acurácia | 97.67% |
| Precisão (Notas Genuínas) | 97.54% |
| Recall (Sensibilidade) | 99.00% |
| F1-Score | 98.26% |
| ROC-AUC | 0.9987 |

### Matriz de Confusão (Conjunto de Teste - 300 registros)
|  | Falsa (Predito) | Genuína (Predito) |
|---|---|---|
| **Falsa (Real)** | 95 (VP) | 5 (FN) |
| **Genuína (Real)** | 2 (FP) | 198 (TP) |

### Interpretação
- **95 notas falsas** foram corretamente identificadas como falsas
- **198 notas genuínas** foram corretamente identificadas como genuínas
- **5 falsos negativos**: Notas falsas não detectadas (risco de fraude)
- **2 falsos positivos**: Notas genuínas rejeitadas incorretamente

### Conclusão
O modelo apresenta excelente desempenho na classificação de notas, com alta acurácia (97.67%) e ROC-AUC de 0.9987. O recall de 99% indica que o modelo é muito eficaz em detectar notas falsas, minimizando o risco de fraude. O modelo está pronto para uso em produção.

## Arquivos do Projeto
- `fake_bills.csv` - Dataset original
- `train_model.py` - Script Python com implementação completa
- `neural_network_model.h5` - Modelo treinado (salvo em formato Keras)
- `performance_analysis.png` - Visualizações de performance (6 gráficos)
- `metrics_summary.txt` - Resumo de métricas em texto
- `WORKFLOW_DESCRIPTION.md` - Este arquivo (descrição do workflow)
