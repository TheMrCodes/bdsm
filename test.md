# Musternotebook: Klassifizierung

Das Ziel dieses Notebooks ist es eine Musterlösung für die Aufbereitung eines Klassifikationsproblems bereitzustellen.
Hierzu werden zuerst die Schritte erläutert und diese dann auf ein Beispiel Datenset angewendet.

**Disclaimer:**
In diesem Notebook werden einige Werte und Verfahren mit mehreren Worten, die sich in der Bedeutung kaum,
bis gar nicht unterscheiden, aber in ihrem Context Variieren beschrieben. Weiteres werden Verfahren teils in ihrer 
englischen wie auch in ihrer deutschen Beschreibung benamst. Dies beruht darauf, dass das Notebook
auf Verständnis und nicht perfekte Genauigkeit in der Wortwahl ausgelegt ist. Ich bitte um ihr Verständnis. <br/>
Beispiele:
 - Dataset / DataFrame / Datensatz
 - Spalte (eines Datasets) / Feature / Dimension


## Struktur
### Imports, Variables & Settings
 - Random Seed
 - Seaborn/Matplot Color schema
 - Sonstige Configs (np, pandas, etc)
 - Helper Functions / imports für utilities

### Daten Laden / Migrieren
Daten von verschiedenen Datenquellen laden / importieren und migrieren (zusammenführen)

### Vorverarbeitung
#### Data Cleaning / Daten Bereinigung
 - Datentypen konvertieren
 - Auffällige Werte löschen
 - Null Values entfernen / ausfüllen / interpolieren etc.
 - Explorative Dataanalysis (EDA) Kennzeichen, Verteilungen, Wertebereiche anschauen (auch Grafisch)


#### Feature Reduction / Dimension-reduktion
 - Bestimmen des / der Labels und Teilen in Input (x) und Output (y) Dataset. <br/>
    **Notiz:** Alle folgende Schritte die auf die Selection von Features aus sind,
    werden nur auf das Input Dataset angewendet.
 - 'Feature selection' in Form manuellem aussortieren von unnützen Spalten (tB. zu viele NaN Werte, nichts aussagend)
 - Correlations-Matrix und Variance Inflation Factor (VIF) Analyse <br/>
   **Notiz:** Alle Features mit einem VIF Wert von über 10 haben eine hohe Multikollinearität und sollten entfernt werden.
 - Weitere Feature selection Verfahren.

 **Wichtig:** Aufschreiben der reduzierten features, nachdem diese bei neuen Echtdaten auch entfernt werden müssen.


### Train / Validation / Test Datasets
  #### Test - Dataset
  Das Test Dataset ist ein set das dazu verwendet wird das finale Model zu validieren und mit anderen Modelen vergleichbar zu machen.
  In einem Kaggle Wettbewerb zB. wird das Testset bis nach Ende geheim gehalten und dient zum Vergleich der Modelle und zur Erstellung der Rangliste.

  #### Train / Validation Split
  Train- und Validationset dienen zur Modellierung, Testen und Hyperparameter tuning.
  Deren Verhältnis (Ratio) liegt je nach dataset und model größe zwischen 70/30 und 80/20.


### Transformierung / Dimension-reduktion
   - Ausreißer analyse nach Train/Test-Split (Nicht immer möglich / gewünscht)
      wegen
       - Verzerrung der Standardisierung / Normalisierung
       - Test der Robustheit des Models gegen Ausreißer
   - Standardisierung / Normalisierung
   - LDA / PCA
   - VIF Dimension-reduktion


### Modelle für Klassifikationsprobleme:

#### Logistische Regression
 - VIF notwendig
 - Nummerischer Input
 - Kategoriale unabhängige Variable
 - Standardisierung: Empfohlen

#### kNN
 - Standardisierung: ja
 - LDA/PCA: ja - bei vielen Dimensionen notwendig
 - Kategoriale unabhängige Variable möglich
 - Abhängige Variablen encodieren: ja
 - möglichst wenige Dimensionen

#### Decision Tree
 - Nullable
 - Standardisierung: nein, Interpretierbarkeit geht dadurch verloren
 - LDA/PCA: ja wenn die Beschreibbarkeit nicht wichtig ist
 - Kategoriale unabhängige Variable möglich (scikit-learn encoding)
 - Abhängige Variablen encodieren: nein (scikit-learn encoding)

#### SVC
 - Standardisierung: ja
 - bei nicht linearen Trennungen richtigen Kernel wählen (rbf, ..)
 - Kategoriale UV möglich (scikit-learn encoding)
 - AV encodieren: ja
 - Parameter C - Breite der Trennung (wie viel Ungenauigkeit wird zugelassen)


### Kombinierte Klassifikatoren:

  #### Bagging (= B ootstrap Agg regation) / Pasting
  Kern Verfahren des Random Forest es selektiert jeweils nur ein Subset (teil der Sätze) und trainiert damit Decision Trees. Dieses Verfahren kann mit (Bagging) und ohne Zurücklegen (Pasting) erfolgen. Danach wird über einen Mehrheitsbeschluss da Ergebnis geschlossen.

  **Out-Of-Bag Score:**
  Der OoB Score kann beim Bagging berechnet werden hierbei werden alle nach der beim Subset auswahl über bleibenden Datensätze verwendet um einen Accuracy Score zu berechnen. Sie werden somit als Extra (Validation Set verwendet)

  #### Random Forest
   - Bagging ist das Kernverfahren des Random Forest als Model wird hierbei Decision Tree verwendet.
   - Deshalb: Selbe Eigenschaften wie Decision Tree

  #### Voting Classifier
  Beim Voting Classifier werden mehrere Modele verwendet um die Klassification zu berechnen dabei wird ein Mehrheitsentschluss der Ergebnisse aller Modele verwendet.

### Regression:
Für so ziemlich allen oben genannten Klassifikatoren gibt es eine Regressions-Variante hier sind ein paar davon:

#### Linear Regression
 - VIF notwendig (Feature selection)
 - Nummerischer Input
 - Unabhängige Variable möglich
 - Standardisierung: nein, da sonst die Interpretierbarkeit verloren geht (bei binär) | mehrere Klassen evtl.

#### Decision Tree regression
Selbe Eigenschaften wie der Decision Tree Classifier jedoch werden nummerische / ordinal skalierte Daten vorhergesagt.

#### SVR - Support Vector Regression
Selbe Eigenschaften wie der Support Vector Classifier jedoch werden nummerische Daten vorhergesagt.


### Hyperparameter Tuning
   #### Grid Search (Scikit-learn GridSearchCV)
   Grid Search probiert alle ihm übergebenen Parameter eines Modells aus und returniert diejenigen die das beste Ergebnis liefern. Um das Ergebnis zu erhalten, muss `gs.best_params_` aufgerufen werden.

   #### Randomized Parameter Optimization (Scikit-learn RandomizedSearchCV)
   Randomized Parameter Optimization

   **Notiz:** Grid und Randomized Search verwenden intern eine Cross validation, um die Ergebnisse zu verbessern, die Anzahl


## Unsupervised

### Modelle
#### K-Means Clustering
 - Eigenschaften:
    - Distanzbasiert
    - Künstliche Labels
    - Stark abhängig von Startposition
 - k - Anzahl der Cluster
 - Wird verwendet um: Zusammengehörigkeit erklären
 - Ellbogen-Methode: mehrere k ausprobieren und nach k / Durchschnittliche Cluster Streuung Plotten und nach dem "Knick" der Ellboge suchen.

