# 📚 Guia COMPLETO: Criar o Workflow KNIME Manualmente

## ⏱️ Tempo Total: ~15 minutos

---

## 🎯 PASSO 1: Abrir KNIME e Criar Novo Workflow

1. **Abra o KNIME**
   ```bash
   open /Applications/KNIME\ 5.8.3.app
   ```

2. **Crie um novo workflow**
   - **File** → **New** → **KNIME Workflow**
   - Nome: `VitorHugoVasconcelosdeLima_ProjetoFinal`
   - Local: `/Users/vitorlima/knime-workspace/Trabalho Final/`
   - Clique **Finish**

---

## 📝 PASSO 2: Adicionar o Primeiro Bloco (Informações)

### Adicionar Nó de Anotação/Texto

1. No painel esquerdo, procure por **"Annotation"** ou **"Note"**
2. Arraste para o canvas
3. **Clique duas vezes** e adicione o texto:
   ```
   PROJETO FINAL - DETECÇÃO DE NOTAS FALSAS
   
   Aluno: Vitor Hugo Vasconcellos de Lima
   Email: vitor.hugo.9999@gmail.com
   Dataset: fake_bills.csv
   
   Objetivo: Classificar notas como falsas ou genuínas
   usando Redes Neurais Artificiais
   ```
4. Clique **OK**

---

## 🗂️ PASSO 3: Carregar os Dados (CSV Reader)

### Adicionar CSV Reader

1. **Procure por "CSV Reader"** (Ctrl+F no painel de nós)
2. **Arraste para o canvas** (embaixo do bloco anterior)
3. **Clique duas vezes** para configurar:
   ```
   - File:  /Users/vitorlima/knime-workspace/Trabalho Final/fake_bills.csv
   - Column delimiter: ; (semicolon)
   - First row contains column names: ✓ (marcado)
   ```
4. Clique **OK**

**Resultado esperado:** 1500 linhas, 7 colunas

---

## 🔧 PASSO 4: Tratar Valores Faltantes

### Adicionar Missing Value Node

1. **Procure por "Missing Value"**
2. **Arraste para o canvas**
3. **Conecte:** CSV Reader (saída) → Missing Value (entrada)
   - Clique na saída (porta direita) do CSV Reader
   - Arraste até a entrada (porta esquerda) do Missing Value
4. **Configure:**
   - Coluna: `margin_low`
   - Método: `Mean` (média)
5. Clique **OK**

---

## 📊 PASSO 5: Normalizar os Dados

### Adicionar Normalizer

1. **Procure por "Normalizer"**
2. **Arraste para o canvas**
3. **Conecte:** Missing Value → Normalizer
4. **Configure:**
   - Selecione todas as colunas EXCETO `is_genuine`
   - Modo: `Z-Score`
5. Clique **OK**

---

## ✂️ PASSO 6: Dividir em Treino e Teste

### Adicionar Partitioner

1. **Procure por "Partitioner"**
2. **Arraste para o canvas**
3. **Conecte:** Normalizer → Partitioner
4. **Configure:**
   - Partition size: `0.8` (80% treino)
   - Random seed: `42`
   - ✓ Stratify
   - Stratification column: `is_genuine`
5. Clique **OK**

**Resultado:** 2 saídas (treino e teste)

---

## 🧠 PASSO 7: Treinar a Rede Neural

### Adicionar Deep Learning Node

1. **Procure por "DL Python Network Learner"** (ou "Keras Network Learner")
2. **Arraste para o canvas** (lado direito)
3. **Conecte:** Partitioner (saída 1 - treino) → DL Learner (entrada)

#### Configure a ARQUITETURA:

4. **Clique duas vezes** no nó
5. **Network Configuration:**
   - Clique em **"New"** para criar uma rede nova
   - Adicione as camadas:
     ```
     Camada 1: 64 neurônios, ativação ReLU
     Camada 2: 32 neurônios, ativação ReLU
     Camada 3: 16 neurônios, ativação ReLU
     ```
   - Camada de Saída: 1 neurônio, ativação Sigmoid

#### Configure o TREINAMENTO:

6. **Training Configuration:**
   - Epochs: `50`
   - Batch size: `32`
   - Optimizer: `Adam`
   - Loss function: `Binary Crossentropy`
   - ✓ Early stopping (paciência: 20)
   - Validation split: `0.2`

7. **Target column:** `is_genuine`

8. Clique **OK**

---

## 🎯 PASSO 8: Fazer Predições

### Adicionar DL Network Executor

1. **Procure por "DL Python Network Executor"**
2. **Arraste para o canvas** (lado direito do learner)
3. **Conecte TWO entradas:**
   - DL Learner (saída do modelo) → DL Executor (porta esquerda)
   - Partitioner (saída 2 - teste) → DL Executor (porta direita)
4. Deixe as configurações padrão
5. Clique **OK**

---

## 📈 PASSO 9: Calcular Métricas

### Adicionar Scorer

1. **Procure por "Scorer"**
2. **Arraste para o canvas** (embaixo do executor)
3. **Conecte:** DL Executor → Scorer
4. **Configure:**
   - Target column: `is_genuine`
5. Clique **OK**

---

## 📊 PASSO 10: Matriz de Confusão

### Adicionar Confusion Matrix

1. **Procure por "Confusion Matrix"**
2. **Arraste para o canvas**
3. **Conecte:** DL Executor → Confusion Matrix
4. **Configure:**
   - Target column: `is_genuine`
5. Clique **OK**

---

## 📉 PASSO 11: Curva ROC

### Adicionar ROC Curve

1. **Procure por "ROC Curve"**
2. **Arraste para o canvas**
3. **Conecte:** DL Executor → ROC Curve
4. **Configure:**
   - Positive class: `1` (ou verdadeiro)
5. Clique **OK**

---

## ▶️ PASSO 12: Executar o Workflow

### Executar os Nós

**Opção 1: Nó por Nó**
```
1. Clique direito em "CSV Reader" → Execute
2. Aguarde (bola verde indica sucesso)
3. Clique direito em "Missing Value" → Execute
4. Continue para cada nó...
```

**Opção 2: Executar Tudo (Recomendado)**
```
1. Clique em "Workflow" (menu superior)
2. Selecione "Execute All"
3. Ou pressione: Ctrl+Shift+F11
```

---

## 📊 PASSO 13: Ver os Resultados

### Visualizar cada resultado:

**CSV Reader:**
- Clique 2x → Aba "Data" → Ver 1500 linhas

**Scorer (Métricas):**
- Clique 2x → Aba "View" → Ver acurácia, precisão, recall

**Confusion Matrix:**
- Clique 2x → Aba "View" → Ver matriz visual

**ROC Curve:**
- Clique 2x → Aba "View" → Ver gráfico ROC com AUC

---

## 💾 PASSO 14: Salvar o Workflow

1. **Ctrl+S** ou **File** → **Save**
2. Workflow salvo em: `/Users/vitorlima/knime-workspace/Trabalho Final/VitorHugoVasconcelosdeLima_ProjetoFinal/`

---

## 📤 PASSO 15: Exportar para GitHub

1. Clique direito no workflow (no Explorer)
2. **Export as KAR** (arquivo comprimido)
3. Salve em: `/Users/vitorlima/knime-workspace/Trabalho Final/`

**Ou simples:**
```bash
# No terminal
cd /Users/vitorlima/knime-workspace/"Trabalho Final"
# Copie a pasta do workflow para GitHub
git add VitorHugoVasconcelosdeLima_ProjetoFinal/
git commit -m "Add: Workflow KNIME completo"
git push
```

---

## ✅ ESTRUTURA VISUAL FINAL

```
┌──────────────────────────────────────────────────────┐
│ INFORMAÇÕES DO PROJETO (Anotação/Note)               │
│ - Aluno, Email, Dataset                              │
└─────────┬────────────────────────────────────────────┘
          │
┌─────────▼──────────┐
│   CSV Reader       │ → Carrega fake_bills.csv (1500 registros)
└─────────┬──────────┘
          │
┌─────────▼──────────────────────┐
│ Missing Value Handler           │ → Trata 37 NaNs (média)
└─────────┬──────────────────────┘
          │
┌─────────▼──────────┐
│   Normalizer       │ → StandardScaler (Z-score)
└─────────┬──────────┘
          │
┌─────────▼────────────────────────────────┐
│ Partitioner (80/20 estratificado)         │
└──────┬──────────────────────────┬─────────┘
       │                          │
    TREINO (80%)              TESTE (20%)
    1200 registros            300 registros
       │                          │
       ▼                          ▼
┌──────────────────┐      ┌──────────────────┐
│ DL Keras Learner │      │ DL Keras Executor│
│ (Treina)         │      │ (Predições)      │
└──────────────────┘      └─────┬────┬───┬───┘
                                │    │   │
                    ┌───────────▼┐ ┌──┴──▼────┐ ┌──────────┐
                    │  Scorer    │ │Confusion │ │ROC Curve │
                    │ (Métricas) │ │ Matrix   │ │          │
                    └────────────┘ └──────────┘ └──────────┘
```

---

## 🎓 RESULTADOS ESPERADOS

| Nó | Resultado |
|----|-----------|
| CSV Reader | 1.500 registros |
| Missing Value | 37 valores preenchidos |
| Normalizer | Dados normalizados |
| Partitioner | 1.200 treino, 300 teste |
| DL Learner | Modelo treinado |
| DL Executor | 300 predições |
| Scorer | Acurácia ~97.67% |
| Confusion Matrix | 95 TN, 198 TP, 2 FP, 5 FN |
| ROC Curve | AUC ~0.9987 |

---

## ⚠️ SE TIVER ERRO

### "CSV Reader não encontra arquivo"
→ Use o caminho completo: `/Users/vitorlima/knime-workspace/Trabalho Final/fake_bills.csv`

### "DL Keras não está disponível"
→ **File** → **Preferences** → **KNIME** → **Python**
→ Configure Python com TensorFlow/Keras instalado

### "Missing Value Handler não funciona"
→ Certifique-se que há NaN na coluna (`margin_low`)

### Demora muito para treinar
→ Reduza Epochs de 50 para 20-30 no DL Learner

---

## 🎉 Pronto!

Quando terminar:
1. ✓ Workflow KNIME pronto
2. ✓ PDF com documentação
3. ✓ Gráficos de performance
4. ✓ Métricas calculadas
5. ✓ Tudo no GitHub

**Tempo total:** ~15 minutos

**Bom trabalho!** 🚀
