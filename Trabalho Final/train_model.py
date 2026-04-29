"""
Projeto Final - Detecção de Notas Falsas com Redes Neurais
Aluno: Vitor Hugo Vasconcellos de Lima
Email: vitor.hugo.9999@gmail.com
Dataset: fake_bills.csv
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend não-interativo
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    confusion_matrix, classification_report, accuracy_score,
    precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc
)
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 80)
print("PROJETO FINAL - DETECÇÃO DE NOTAS FALSAS COM REDES NEURAIS")
print("=" * 80)

# 1. CARREGAMENTO DO DATASET
print("\n[1/6] Carregando Dataset...")
df = pd.read_csv('fake_bills.csv', sep=';')
print(f"✓ Dataset carregado: {df.shape[0]} registros, {df.shape[1]} colunas")
print(f"\nPrimeiras linhas:\n{df.head()}")
print(f"\nInformações do Dataset:\n{df.info()}")
print(f"\nEstatísticas descritivas:\n{df.describe()}")

# Verificar valores faltantes
print(f"\nValores faltantes: {df.isnull().sum().sum()}")

# Distribuição da classe alvo
print(f"\nDistribuição de Classes:")
print(df['is_genuine'].value_counts())
print(f"Proporção: {df['is_genuine'].value_counts(normalize=True)}")

# 2. PRÉ-PROCESSAMENTO E PREPARAÇÃO DOS DADOS
print("\n[2/6] Pré-processando dados...")

# Tratar valores faltantes (preencher com a média)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
df_filled = df.copy()
df_filled.iloc[:, 1:] = imputer.fit_transform(df.iloc[:, 1:])
print(f"✓ Valores faltantes tratados (preenchidos com média)")

# Separar features e target
X = df_filled.drop('is_genuine', axis=1).values
y = df_filled['is_genuine'].map({True: 1, False: 0}).values

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Dividir dados em treino e teste (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"✓ Dados divididos:")
print(f"  - Treino: {X_train.shape[0]} registros ({X_train.shape[0]/len(X)*100:.1f}%)")
print(f"  - Teste: {X_test.shape[0]} registros ({X_test.shape[0]/len(X)*100:.1f}%)")

# Normalizar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✓ Dados normalizados com StandardScaler")

# 3. CONSTRUÇÃO E CONFIGURAÇÃO DO MODELO DE REDE NEURAL
print("\n[3/6] Construindo modelo de Rede Neural...")

model = MLPClassifier(
    hidden_layer_sizes=(64, 32, 16),
    activation='relu',
    solver='adam',
    learning_rate='adaptive',
    max_iter=500,
    early_stopping=True,
    validation_fraction=0.2,
    n_iter_no_change=20,
    random_state=42,
    verbose=0
)

print("✓ Arquitetura da Rede Neural (MLPClassifier):")
print("  - Camada 1: 64 neurônios (ReLU)")
print("  - Camada 2: 32 neurônios (ReLU)")
print("  - Camada 3: 16 neurônios (ReLU)")
print("  - Camada Saída: 1 neurônio (Softmax - Classificação Binária)")

print("\nConfiguração do Treinamento:")
print("  - Otimizador: Adam")
print("  - Função de Ativação: ReLU")
print("  - Early Stopping: Sim (20 iterações sem melhoria)")
print("  - Validação: 20% do conjunto de treino")

# 4. TREINAMENTO DO MODELO
print("\n[4/6] Treinando modelo...")

model.fit(X_train_scaled, y_train)

print("✓ Treinamento concluído!")
print(f"  - Iterações realizadas: {model.n_iter_}")
print(f"  - Perda (Loss) final: {model.loss_:.6f}")

# 5. AVALIAÇÃO DO MODELO
print("\n[5/6] Avaliando modelo...")

# Predições
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
y_pred = model.predict(X_test_scaled)

# Métricas de performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print(f"\n✓ Métricas de Performance:")
print(f"  - Acurácia: {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"  - Precisão: {precision:.4f}")
print(f"  - Recall: {recall:.4f}")
print(f"  - F1-Score: {f1:.4f}")
print(f"  - ROC-AUC: {roc_auc:.4f}")

print(f"\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=['Falsa', 'Genuína']))

# Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
print(f"\nMatriz de Confusão:")
print(cm)

# 6. VISUALIZAÇÕES E GRÁFICOS
print("\n[6/6] Gerando visualizações...")

# Criar figura com múltiplos subplots
fig = plt.figure(figsize=(16, 10))

# 1. Perda no Treinamento (usando coef_ para demonstrar convergência)
ax1 = plt.subplot(2, 3, 1)
ax1.plot(model.loss_curve_, linewidth=2, color='#FF6B6B')
ax1.set_title('Loss durante o Treinamento', fontsize=12, fontweight='bold')
ax1.set_xlabel('Iterações')
ax1.set_ylabel('Loss')
ax1.grid(True, alpha=0.3)

# 2. Matriz de Confusão
ax2 = plt.subplot(2, 3, 2)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax2,
            xticklabels=['Falsa', 'Genuína'], yticklabels=['Falsa', 'Genuína'],
            cbar_kws={'label': 'Frequência'})
ax2.set_title('Matriz de Confusão - Conjunto de Teste', fontsize=12, fontweight='bold')
ax2.set_ylabel('Verdadeiro')
ax2.set_xlabel('Predito')

# 3. Curva ROC
ax3 = plt.subplot(2, 3, 3)
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc_val = auc(fpr, tpr)
ax3.plot(fpr, tpr, color='darkorange', lw=2.5, label=f'ROC (AUC = {roc_auc_val:.3f})')
ax3.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Aleatório')
ax3.set_xlim([0.0, 1.0])
ax3.set_ylim([0.0, 1.05])
ax3.set_xlabel('False Positive Rate')
ax3.set_ylabel('True Positive Rate')
ax3.set_title('Curva ROC', fontsize=12, fontweight='bold')
ax3.legend(loc="lower right")
ax3.grid(True, alpha=0.3)

# 4. Distribuição de Probabilidades
ax4 = plt.subplot(2, 3, 4)
ax4.hist(y_pred_proba[y_test == 0], bins=25, alpha=0.6, label='Notas Falsas', color='#FF6B6B', edgecolor='black')
ax4.hist(y_pred_proba[y_test == 1], bins=25, alpha=0.6, label='Notas Genuínas', color='#4ECDC4', edgecolor='black')
ax4.set_xlabel('Probabilidade de Ser Genuína')
ax4.set_ylabel('Frequência')
ax4.set_title('Distribuição de Probabilidades de Predição', fontsize=12, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

# 5. Métricas em Barplot
ax5 = plt.subplot(2, 3, 5)
metrics = ['Acurácia', 'Precisão', 'Recall', 'F1-Score', 'ROC-AUC']
values = [accuracy, precision, recall, f1, roc_auc]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars = ax5.bar(metrics, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
ax5.set_ylim([0, 1.1])
ax5.set_ylabel('Valor')
ax5.set_title('Resumo de Métricas de Performance', fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3, axis='y')

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height + 0.02,
             f'{height:.3f}', ha='center', va='bottom', fontweight='bold', fontsize=9)

# 6. Distribuição de Classes Original vs Predita
ax6 = plt.subplot(2, 3, 6)
labels = ['Falsa', 'Genuína']
original = [np.sum(y_test == 0), np.sum(y_test == 1)]
predicted = [np.sum(y_pred == 0), np.sum(y_pred == 1)]
x = np.arange(len(labels))
width = 0.35
ax6.bar(x - width/2, original, width, label='Original', color='#95E1D3', edgecolor='black')
ax6.bar(x + width/2, predicted, width, label='Predito', color='#F38181', edgecolor='black')
ax6.set_ylabel('Quantidade')
ax6.set_title('Distribuição: Original vs Predita', fontsize=12, fontweight='bold')
ax6.set_xticks(x)
ax6.set_xticklabels(labels)
ax6.legend()
ax6.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('performance_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Gráficos salvos em: performance_analysis.png")

# Salvar métricas em arquivo de texto
with open('metrics_summary.txt', 'w') as f:
    f.write("=" * 80 + "\n")
    f.write("RESUMO DE MÉTRICAS - PROJETO FINAL\n")
    f.write("=" * 80 + "\n\n")
    f.write(f"Acurácia: {accuracy:.4f} ({accuracy*100:.2f}%)\n")
    f.write(f"Precisão: {precision:.4f}\n")
    f.write(f"Recall (Sensibilidade): {recall:.4f}\n")
    f.write(f"F1-Score: {f1:.4f}\n")
    f.write(f"ROC-AUC: {roc_auc:.4f}\n\n")
    f.write("Matriz de Confusão:\n")
    f.write(f"Verdadeiros Negativos (TN): {cm[0,0]}\n")
    f.write(f"Falsos Positivos (FP): {cm[0,1]}\n")
    f.write(f"Falsos Negativos (FN): {cm[1,0]}\n")
    f.write(f"Verdadeiros Positivos (TP): {cm[1,1]}\n\n")
    f.write("Relatório de Classificação:\n")
    f.write(classification_report(y_test, y_pred, target_names=['Falsa', 'Genuína']))

print("✓ Métricas salvas em: metrics_summary.txt")

# Resumo Final
print("\n" + "=" * 80)
print("RESUMO DO PROJETO")
print("=" * 80)
print(f"\n✓ Dataset: {df.shape[0]} registros de notas (genuínas e falsas)")
print(f"✓ Features: {X.shape[1]} (diagonal, altura, margem, comprimento)")
print(f"✓ Arquitetura: 4 camadas (64 → 32 → 16 → Saída)")
print(f"✓ Treinamento: {model.n_iter_} iterações com early stopping")
print(f"✓ Split: 80% treino ({len(X_train)} registros), 20% teste ({len(X_test)} registros)")
print(f"✓ Acurácia Final no Teste: {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"✓ ROC-AUC: {roc_auc:.4f}")
print(f"✓ F1-Score: {f1:.4f}")
print("\nArquivos gerados:")
print("  - performance_analysis.png (gráficos de análise)")
print("  - metrics_summary.txt (resumo de métricas)")
print("=" * 80)
