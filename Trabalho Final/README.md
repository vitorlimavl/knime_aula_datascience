# Projeto Final - Detecção de Notas Falsas com Redes Neurais

## 📋 Informações do Projeto

- **Aluno**: Vitor Hugo Vasconcellos de Lima
- **Email**: vitor.hugo.9999@gmail.com
- **Dataset**: fake_bills.csv
- **Objetivo**: Classificação binária para detectar notas falsas vs. genuínas usando Redes Neurais

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| **VitorHugoVasconcelosdeLima_ProjetoFinal.pdf** | Documentação completa do projeto (6 páginas) |
| **fake_bills.csv** | Dataset com 1.500 registros de medidas de notas |
| **train_model.py** | Script Python com implementação da Rede Neural |
| **performance_analysis.png** | Gráficos de análise de performance (6 visualizações) |
| **metrics_summary.txt** | Resumo das métricas de desempenho |
| **WORKFLOW_DESCRIPTION.md** | Descrição detalhada da arquitetura do workflow |
| **create_pdf.py** | Script para gerar o PDF (já executado) |

## 🎯 Resultados Principais

### Métricas de Performance
| Métrica | Valor |
|---------|-------|
| **Acurácia** | 97.67% |
| **Precisão** | 97.54% |
| **Recall** | 99.00% |
| **F1-Score** | 98.26% |
| **ROC-AUC** | 0.9987 |

### Arquitetura da Rede Neural
```
Input (6 features)
    ↓
Dense(64, ReLU)
    ↓
Dense(32, ReLU)
    ↓
Dense(16, ReLU)
    ↓
Dense(1, Sigmoid) → Classificação Binária
```

### Dataset
- **Total**: 1.500 registros
- **Classes**: 1.000 notas genuínas (66.7%) + 500 notas falsas (33.3%)
- **Features**: 6 medidas físicas (diagonal, altura, margem, comprimento)
- **Valores faltantes**: 37 (tratados com imputação pela média)

## 🔄 Pipeline de Processamento

1. **Carregamento**: CSV Reader → fake_bills.csv
2. **Tratamento**: Handling de valores faltantes (mean imputation)
3. **Normalização**: StandardScaler (z-score)
4. **Divisão**: Stratified Split (80% treino, 20% teste)
5. **Treinamento**: MLP Classifier (4 camadas)
6. **Avaliação**: Múltiplas métricas e gráficos

## 📊 Visualizações Incluídas

- Loss durante o treinamento
- Matriz de Confusão
- Curva ROC (AUC)
- Distribuição de Probabilidades
- Resumo de Métricas (barplot)
- Distribuição Original vs Predita

## 🔧 Como Usar

### Executar o treinamento:
```bash
python3 train_model.py
```

### Gerar o PDF (se necessário):
```bash
python3 create_pdf.py
```

## 📝 Conclusões

O modelo apresenta excelente desempenho na classificação de notas com:
- **Alta acurácia**: 97.67%
- **Alto recall**: 99.00% (detecta quase todas as notas falsas)
- **Excelente ROC-AUC**: 0.9987

O modelo é robusto, convergiu rapidamente (30 épocas com early stopping) e está pronto para uso em produção.

### Dificuldades Encontradas
- Valores faltantes em margin_low → Resolvido com imputação
- Desbalanceamento de classes → Resolvido com stratified split
- Compatibilidade de bibliotecas → Migramos de TensorFlow para scikit-learn

---

*Projeto desenvolvido em abril de 2026*
