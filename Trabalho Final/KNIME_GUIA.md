# 🎓 Guia: Como Abrir o Workflow no KNIME

## Opção 1: Abrir a Pasta do Workflow (Recomendado)

1. **Abra o KNIME**
   ```bash
   open /Applications/KNIME\ 5.8.3.app
   ```

2. **Configure o Workspace**
   - Quando abrir pela primeira vez, selecione um local para o workspace
   - Recomendo: `/Users/vitorlima/knime-workspace`
   - Clique **OK**

3. **Importe o Workflow**
   - **File** → **Import Workflow**
   - Navegue até: `/Users/vitorlima/knime-workspace/VitorHugoVasconcelosdeLima_ProjetoFinal/workflow`
   - Clique **Finish**

4. **Abra o Workflow**
   - No painel esquerdo (Explorer), clique em **VitorHugoVasconcelosdeLima_ProjetoFinal**
   - Clique duas vezes para abrir

## Opção 2: Abrir Manualmente via Terminal

```bash
cd /Users/vitorlima/knime-workspace

# Abrir KNIME no workspace
open /Applications/KNIME\ 5.8.3.app --args -workspacedata "/Users/vitorlima/knime-workspace"
```

## 📋 Passo a Passo Dentro do KNIME

### Configurar o CSV Reader (Nó 0)

1. Clique duas vezes no nó **CSV Reader**
2. Clique em **Browse** e selecione: `fake_bills.csv`
3. **Coluna do Delimitador**: Selecione `;` (semicolon)
4. Clique **OK**

### Configurar o Missing Value Handler (Nó 1)

1. Clique duas vezes no nó
2. Selecione a coluna `margin_low`
3. **Method**: Mean (Média)
4. Clique **OK**

### Configurar o Normalizer (Nó 2)

1. Clique duas vezes no nó
2. Selecione todas as features (não o target `is_genuine`)
3. **Normalization Mode**: Z-Score
4. Clique **OK**

### Configurar o Partitioner (Nó 3)

1. Clique duas vezes no nó
2. **Partition Size**: 0.8 (80% treino)
3. **Random Seed**: 42
4. **Stratify**: Marque a opção
5. **Target Column**: `is_genuine`
6. Clique **OK**

### Configurar a Rede Neural (Nó 4)

1. Clique duas vezes no nó **Deep Learning - Keras Network Learning**
2. **Network Configuration**:
   - Adicione 3 camadas:
     - Camada 1: 64 neurônios, ativação ReLU
     - Camada 2: 32 neurônios, ativação ReLU
     - Camada 3: 16 neurônios, ativação ReLU
   - Camada Saída: 1 neurônio, ativação Sigmoid

3. **Training Configuration**:
   - **Epochs**: 50
   - **Batch Size**: 32
   - **Optimizer**: Adam
   - **Loss Function**: Binary Crossentropy
   - **Early Stopping**: Ativado (paciência: 20)

4. **Target Column**: `is_genuine`

5. Clique **OK**

## ▶️ Executar o Workflow

### Executar Nó por Nó
1. Clique com botão direito em um nó
2. Selecione **Execute**
3. Aguarde a execução (barra azul no nó)

### Executar Todo o Workflow
1. Clique em **Workflow** → **Execute All** (ou `Ctrl+Shift+F11`)
2. Aguarde a execução de todos os nós

## 📊 Visualizar Resultados

### Ver Dados Após Cada Nó
1. Clique duas vezes em um nó executado
2. Clique em **Data** ou **View**
3. Veja os resultados

### Ver Métricas de Performance
1. Execute o nó **Scorer**
2. Clique duas vezes e vá em **View**
3. Veja Acurácia, Precisão, Recall, F1-Score

### Ver Matriz de Confusão
1. Execute o nó **Confusion Matrix**
2. Clique duas vezes e vá em **View**
3. Veja a matriz visualizada

### Ver Curva ROC
1. Execute o nó **ROC Curve**
2. Clique duas vezes e vá em **View**
3. Veja o gráfico ROC com AUC

## 🐍 Alternativa: Usar Script Python

Se preferir, você pode executar diretamente o script Python:

```bash
cd "/Users/vitorlima/knime-workspace/Trabalho Final"
python3 train_model.py
```

Isso gera:
- `performance_analysis.png` - Gráficos de análise
- `metrics_summary.txt` - Métricas em texto
- `neural_network_model.h5` - Modelo treinado

## ⚠️ Possíveis Problemas e Soluções

### Erro: "CSV Reader não encontra arquivo"
- Certifique-se que `fake_bills.csv` está na mesma pasta do workflow
- Ou use o caminho completo: `/Users/vitorlima/knime-workspace/Trabalho Final/fake_bills.csv`

### Erro: "Keras não está instalado"
- No KNIME: **Preferences** → **Python**
- Configure o Python 3 com TensorFlow/Keras instalado

### Erro: "Missing Value Handler não funciona"
- Certifique-se de que há valores faltantes (NaN) no dataset
- Se não houver, pule este nó

### Lento para treinar
- Reduza **Epochs** de 50 para 20-30
- Reduza o **Batch Size** de 32 para 16

## 📝 Estrutura do Workflow

```
CSV Reader (Carrega dados)
    ↓
Missing Value Handler (Trata NaNs)
    ↓
Normalizer (StandardScaler)
    ↓
Partitioner (80/20 split)
    ├─→ Treino (80%)
    │    ↓
    │    Deep Learning - Keras Learner (Treina modelo)
    │
    └─→ Teste (20%)
         ↓
         Deep Learning - Keras Executor (Predições)
         ↓
         Scorer (Métricas)
         Confusion Matrix (Matriz)
         ROC Curve (Curva ROC)
```

## 💡 Dicas

- **Executar um nó**: Clique direito → Execute
- **Ver entrada/saída**: Clique duas vezes no nó → Data/View
- **Resetar nó**: Clique direito → Reset
- **Deletar nó**: Selecione + Delete
- **Adicionar nó novo**: Clique no painel esquerdo e arraste

## 📚 Recursos

- Documentação KNIME: https://www.knime.com/docs
- Keras no KNIME: https://www.knime.com/deeplearning-keras

---

**Sucesso no projeto!** 🎉
