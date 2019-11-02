# -*- coding: utf-8 -*-
"""DrugPredictablePropertiesAndActivityDeterminationNew.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0B47H2q-cUseAODVHczJkdEZScHFkUHF3OVhpS0t4cUluMF9z
"""

# Commented out IPython magic to ensure Python compatibility.
#importing of basic necessary properties
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# %matplotlib inline

!pip install chembl_webresource_client

from chembl_webresource_client.new_client import new_client

#rdkit installation
import sys
import os
import requests
import subprocess
import shutil
from logging import getLogger, StreamHandler, INFO


logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel(INFO)


def install(
        chunk_size=4096,
        file_name="Miniconda3-latest-Linux-x86_64.sh",
        url_base="https://repo.continuum.io/miniconda/",
        conda_path=os.path.expanduser(os.path.join("~", "miniconda")),
        rdkit_version=None,
        add_python_path=True,
        force=False):
    """install rdkit from miniconda
    ```
    import rdkit_installer
    rdkit_installer.install()
    ```
    """

    python_path = os.path.join(
        conda_path,
        "lib",
        "python{0}.{1}".format(*sys.version_info),
        "site-packages",
    )

    if add_python_path and python_path not in sys.path:
        logger.info("add {} to PYTHONPATH".format(python_path))
        sys.path.append(python_path)

    if os.path.isdir(os.path.join(python_path, "rdkit")):
        logger.info("rdkit is already installed")
        if not force:
            return

        logger.info("force re-install")

    url = url_base + file_name
    python_version = "{0}.{1}.{2}".format(*sys.version_info)

    logger.info("python version: {}".format(python_version))

    if os.path.isdir(conda_path):
        logger.warning("remove current miniconda")
        shutil.rmtree(conda_path)
    elif os.path.isfile(conda_path):
        logger.warning("remove {}".format(conda_path))
        os.remove(conda_path)

    logger.info('fetching installer from {}'.format(url))
    res = requests.get(url, stream=True)
    res.raise_for_status()
    with open(file_name, 'wb') as f:
        for chunk in res.iter_content(chunk_size):
            f.write(chunk)
    logger.info('done')

    logger.info('installing miniconda to {}'.format(conda_path))
    subprocess.check_call(["bash", file_name, "-b", "-p", conda_path])
    logger.info('done')

    logger.info("installing rdkit")
    subprocess.check_call([
        os.path.join(conda_path, "bin", "conda"),
        "install",
        "--yes",
        "-c", "rdkit",
        "python=={}".format(python_version),
        "rdkit" if rdkit_version is None else "rdkit=={}".format(rdkit_version)])
    logger.info("done")

    import rdkit
    logger.info("rdkit-{} installation finished!".format(rdkit.__version__))


if __name__ == "__main__":
    install()

import rdkit
from rdkit import Chem
generatedMol = ["PCPPOO","PPPCPCPO", "Cl.CNCN1C2CCCC2CCC2CCCCC12", "CCCPCPCO", "CNPCP=O", "CC1=C(CC(=O)O)c2cc(Cl)ccc2/C/1=C\c1ccc(cc1)F", "NC(=O)c1ccc(I)c(c1)F", "PPNCCCCPO", "CN1CCCC1c2cccnc2", "CC(C)[C@H](N)C(=O)N1CCC[C@H]1S(O)O"]
inputMols = []
inputMols = []
for smiles in generatedMol:
    inputMols.append(Chem.MolFromSmiles(smiles))
generatedMol = inputMols

#calculating molecular properties 

n = 10
from rdkit.Chem import Descriptors
properties = ["Mol_weight","FpDensityMorgan1","MaxAbsPartialCharge","NumHeavyAtoms","NumRotatableBonds","NumAromaticRings", "NumHBA", "NumHBD", "NumLipinskiHBA", "NumLipinskiHBD", "TPSA", "QED_CALC", "LOGP"]
propArr = {}
for factor in properties:
    propArr[factor] = []
value = 0 
for i in range(0,n):
    for factor in properties:
        if factor == "Mol_weight":
            value = Descriptors.ExactMolWt(generatedMol[i])
            propArr[factor].append(value)
        if factor == "FpDensityMorgan1":
            value = Descriptors.FpDensityMorgan1(generatedMol[i])
            propArr[factor].append(value)
        if factor == "MaxAbsPartialCharge":
            value = Descriptors.MaxAbsPartialCharge(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumHeavyAtoms":
            value = Chem.Lipinski.HeavyAtomCount(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumRotatableBonds":
            value = Chem.rdMolDescriptors.CalcNumRotatableBonds(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumAromaticRings":
            value = Chem.rdMolDescriptors.CalcNumAromaticRings(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumHBA":
            value = Chem.rdMolDescriptors.CalcNumHBA(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumHBD":
            value = Chem.rdMolDescriptors.CalcNumHBD(generatedMol[i])
            propArr[factor].append(value) 
        if factor == "NumLipinskiHBA":
            value = Chem.rdMolDescriptors.CalcNumLipinskiHBA(generatedMol[i])
            propArr[factor].append(value)
        if factor == "NumLipinskiHBD":
            value = Chem.rdMolDescriptors.CalcNumLipinskiHBD(generatedMol[i])
            propArr[factor].append(value)
        if factor == "TPSA":
            value = Chem.rdMolDescriptors.CalcTPSA(generatedMol[i])
            propArr[factor].append(value) 
        if factor == "QED_CALC":
            value = Chem.QED.weights_mean(generatedMol[i])
            propArr[factor].append(value) 
        if factor == "LOGP":
            value = Chem.Crippen.MolLogP(generatedMol[i])
            propArr[factor].append(value)

for factor in properties:
    print(propArr[factor])

#place collected data in a DataFrame
import pandas as pd

data = pd.DataFrame(data = propArr, index = range(1,11))

#LinpinskiRuleCheck
check = [0]*10

for i in range(0,10):
    if propArr["Mol_weight"][i] > 500:
        check[i] += 1
    if propArr["NumLipinskiHBA"][i] > 10:
        check[i] += 1
    if propArr["NumLipinskiHBD"][i] > 5:
        check[i] += 1
    if propArr["LOGP"][i] > 5:
        check[i] += 1

#GeneralRo5Check

check0 = [0]*10

for i in range(0,10):
    if propArr["Mol_weight"][i] > 500:
        check0[i] += 1
    if propArr["NumHBA"][i] > 10:
        check0[i] += 1
    if propArr["NumHBD"][i] > 5:
        check0[i] += 1
    if propArr["LOGP"][i] > 5:
        check0[i] += 1

#ro3 check

check1 = [1]*10

for i in range(0,10):
    if propArr["Mol_weight"][i] > 300:
        check1[i] = 0
        break
    if propArr["NumHBA"][i] > 3:
        check1[i] = 0
        break
    if propArr["NumHBD"][i] > 3:
        check1[i] = 0
        break
    if propArr["LOGP"][i] > 3:
        check1[i] = 0
        break

#adding ro5 and ro3 results

addProps = ["num_lipinski_ro5_violations","num_ro5_violations", "ro3_pass"]

for prop in addProps:
    propArr[prop] = []
value = 0
for i in range(0,n):
    value = check[i]
    propArr["num_lipinski_ro5_violations"].append(value)
    value = check0[i]
    propArr["num_ro5_violations"].append(value)
    value = check1[i]
    propArr["ro3_pass"].append(value)

#collecting the lung carcinoma molecules
drug_indication = new_client.drug_indication
molecules = new_client.molecule
lung_cancer_ind = drug_indication.filter(efo_term__icontains="LUNG CARCINOMA")
lung_cancer_mols = molecules.filter(molecule_chembl_id__in=[x['molecule_chembl_id'] for x in lung_cancer_ind])

n_lung = 100
#creating a dataFrame. Note, these molecules are what we consider active (1)
import pandas as pd   
arr = lung_cancer_mols[0]['molecule_properties']

arr['active'] = 1
arr_labels = []
for key in arr.keys():
    arr_labels.append(key)
a = []
for i in range(23):
    a.append([])   
for q in range(0,23):
    a[q].append(arr[arr_labels[q]])
    
index = []
for p in range(1,n_lung):
    count = 1
    list1 = lung_cancer_mols[p]['molecule_properties']
    #print(list1)
    if list1 != None:
        list1['active'] = 1
        for j in range(0,23):
            a[j].append(list1[arr_labels[j]])
        count += 1

l1 = len(a[0])

def makeDict(list1, list2):
    new_Dict = {}
    for i in range(0,23):
        new_Dict[list1[i]] = list2[i]
    return new_Dict
for i in range(1,l1+1):
    index.append(i)

data2 = pd.DataFrame(data = makeDict(arr_labels, a),index = index, copy = True)
data2 = data2[arr_labels]
data2.info()

#viewing the top 5 entries
data2.head()

#some basic pre-processing

orig = len(data2)
y = []
for i in range (0,l1):
    y.append([])
predProps = {'acd_logd','acd_logp', 'mw_monoisotopic', 'mw_freebase'}
data2['acd_logd'] = data2['acd_logd'].apply(pd.to_numeric, errors = 'ignore')
data2['acd_logp'] = data2['acd_logp'].apply(pd.to_numeric, errors = 'ignore')
data2['mw_monoisotopic'] = data2['mw_monoisotopic'].apply(pd.to_numeric, errors = 'ignore')
data2['mw_freebase'] = data2['mw_freebase'].apply(pd.to_numeric, errors = 'ignore')
y[0] = data2['active'].values
y[1] = data2['acd_logd'].values
y[2] = data2['acd_logp'].values
y[3] = data2['mw_freebase'].values
y[4] = data2['mw_monoisotopic'].values

#too many missing values of 'acd_most_apka', 'acd_most_bpka' and they will not be predicted and used in further analysis

data2.drop(labels = ['active', 'acd_logd','acd_logp','mw_monoisotopic','mw_freebase','molecular_species', 'acd_most_apka', 'acd_most_bpka', 'full_molformula'], axis = 1, inplace = True)
data2['ro3_pass'].replace(to_replace=['Y'], value = 1,inplace=True)
data2['ro3_pass'].replace(to_replace = ['N'], value = 0, inplace=True)

data2 = data2.apply(pd.to_numeric, errors = 'ignore')

X = data2.iloc[::].values

from statistics import median
import numpy as np
import math
for i in range(0,orig):
    for j in range(0, len(X[i])):
        lst = []
        if math.isnan(X[i][j]):
            for b in range(0,orig):
                if math.isnan(X[b][j]) == False:
                    
                    lst.append(X[b][j])
            X[i][j] = median(lst)
            
for i in range(0,orig):
    for j in range(0, len(X[i])):
        X[i][j] = np.float32(X[i][j])
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

data2.info()

#placing all rdKit predicted values in a new dictionary with the same order as the chembl dictionary of molecular properties

data3 = {}  
for i in range(0,n):
    if i == 0:
        data3['alogp'] = []
        data3['aromatic_rings'] = []
        data3['full_mwt'] = []
        data3['hba'] = []
        data3['hba_lipinski'] = []
        data3['hbd'] = []
        data3['hbd_lipinski'] = []
        data3['heavy_atoms'] = []
        data3['num_lipinski_ro5_violations'] = []
        data3['num_ro5_violations'] = []
        data3['psa'] = []
        data3['qed_weighted'] = [] 
        data3['ro3_pass'] = []
        data3['rtb'] = []

    data3['alogp'].append(propArr["LOGP"][i])
    data3['aromatic_rings'].append(propArr["NumAromaticRings"][i])
    data3['full_mwt'].append(propArr["Mol_weight"][i])
    data3['hba'].append(propArr["NumHBA"][i])
    data3['hba_lipinski'].append(propArr["NumLipinskiHBA"][i])
    data3['hbd'].append(propArr["NumHBD"][i])
    data3['hbd_lipinski'].append(propArr["NumLipinskiHBD"][i])
    data3['heavy_atoms'].append(propArr["NumHeavyAtoms"][i])
    data3['num_lipinski_ro5_violations'].append(propArr["num_lipinski_ro5_violations"][i])
    data3['num_ro5_violations'].append(propArr["num_ro5_violations"][i])
    data3['psa'].append(propArr["TPSA"][i])
    data3['qed_weighted'].append(propArr["QED_CALC"][i])
    data3['ro3_pass'].append(propArr['ro3_pass'][i])
    data3['rtb'].append(propArr['NumRotatableBonds'][i])

index = [] 
for q in range(1,11):
    index.append(q)
      
X_test1 = pd.DataFrame(data = data3, index = index) 
X_test1 = X_test1.apply(pd.to_numeric, errors = 'ignore')
X_test1.head()

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel 
#Y will be used to collect the calculated properties for each of the 10 compounds
Y = {}
predProps2 = ['acd_logd','acd_logp', 'mw_monoisotopic', 'mw_freebase']
acc = []
for i in range(0,4):
    #division of main dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y[i+1], test_size = 0.3, random_state = 0)
    sel = SelectFromModel(RandomForestRegressor(n_estimators = 50))

    #Fitting the training datasets
    sel.fit(X_train,y_train)
    #transformation
    X_important_train = sel.transform(X_train)
    X_important_test = sel.transform(X_test)
    X_important_test1 = sel.transform(X_test1)
    #prediction
    clf_important = RandomForestRegressor(n_estimators=50)
    clf_important.fit(X_important_train, y_train)
    pred = clf_important.predict(X_important_test)
    print(pred)
    print(y_test)
    #properties for new generated compounds
    Y_test1 = clf_important.predict(X_important_test1)
    Y[predProps2[i]] = Y_test1

for predProps in predProps2:
    print(Y[predProps])

#adding 'mw_monoisotopic'and 'mw_freebase' into the dictionary of molecular properties (these two properties were predicted with higher accuracies than the other two 'acd_logd','acd_logp')

for i in range(0,n):
    if i == 0:
        data3['mw_monoisotopic'] = []
        data3['mw_freebase'] = []
    data3['mw_freebase'].append(Y[predProps2[2]][i])
    data3['mw_monoisotopic'].append(Y[predProps2[3]][i])
  
  
X_test1 = pd.DataFrame(data = data3, index = index)
X_test1 = X_test1.apply(pd.to_numeric, errors = 'ignore')
cols = X_test1.columns.tolist()
cols = cols[0:8] + cols[-2:] + cols [8:(len(cols)-2)]
X_test1 = X_test1[cols]

X_test1.head()

"""#### Activity Prediction"""

#Prediction of activity of generated molecules

import pandas as pd
arr = lung_cancer_mols[0]['molecule_properties']

arr['active'] = 1
arr_labels = []
for key in arr.keys():
    arr_labels.append(key)
a = []
for i in range(23):
    a.append([])   
for q in range(0,23):
    a[q].append(arr[arr_labels[q]])
    
index = []
for p in range(1,n_lung):
    count = 1
    list1 = lung_cancer_mols[p]['molecule_properties']
    #print(list1)
    if list1 != None:
        list1['active'] = 1
        for j in range(0,23):
            a[j].append(list1[arr_labels[j]])
            count += 1

l1 = len(a[0])
def makeDict(list1, list2):
    new_Dict = {}
    for i in range(0,23):
        new_Dict[list1[i]] = list2[i]
    return new_Dict
for i in range(1,l1+1):
    index.append(i)
    
dataLung = pd.DataFrame(data = makeDict(arr_labels, a),index = index, copy = True)
dataLung = dataLung[arr_labels]
#dataLung.info()

#tb_molecules: Activity = 0 
drug_indication = new_client.drug_indication
molecules = new_client.molecule
tb_ind = drug_indication.filter(efo_term__icontains="TUBERCULOSIS")
tb_mols = molecules.filter(molecule_chembl_id__in=[x['molecule_chembl_id'] for x in tb_ind])

n_tb = 100
import pandas as pd
arr = tb_mols[0]['molecule_properties']
arr['active'] = 0
arr_labels = []
for key in arr.keys():
    arr_labels.append(key)
a = []
for i in range(23):
    a.append([])   
for q in range(0,23):
    a[q].append(arr[arr_labels[q]])
    
index2 = []
for p in range(1,40):
    count = 1
    list1 = tb_mols[p]['molecule_properties']
    if list1 != None:
        list1['active'] = 0
    
        for j in range(0, n_tb):
            a[j].append(list1[arr_labels[j]])
            count += 1

l2 = len(a[0])
def makeDict(list1, list2):
    new_Dict = {}
    for i in range(0,23):
        new_Dict[list1[i]] = list2[i]
    return new_Dict

for i in range(l1+1, l1+l2+1):
    index2.append(i)
    
datatb = pd.DataFrame(data = makeDict(arr_labels, a), index = index2)
datatb = datatb[arr_labels]
datatb.head()

datatb.info()

frames = [dataLung, datatb]

dataComb = pd.concat(frames)

dataComb.to_csv("dataComb")

"""### Analysis and  preprocessing the data"""

#full_molformula will be unique for each molecule
dataComb.drop(labels = ['full_molformula'],axis = 1,inplace= True)

# categorical features treatment 
!pip install category-encoders

import category_encoders as ce

ce_OHE = ce.OneHotEncoder(cols = ['molecular_species',"ro3_pass"])
dataComb = ce_OHE.fit_transform(dataComb)

dataComb.head()

dataComb.info()

#converting the obejct types features to numeric
cat_labels = dataComb.select_dtypes(include = ["object"]).columns
dataComb[cat_labels] = dataComb[cat_labels].apply(pd.to_numeric)

dataComb.info()

dataComb.isnull().sum()
dataComb.head(10)

"""#### Analysing data"""

#these two properties were not predicted before for the generated compounds
df1 = dataComb.drop(labels=["acd_most_apka","acd_most_bpka", "acd_logp", "acd_logd"],axis = 1)

# SPLITING DATA INTO predictors/response variables 

X = df1.iloc[:,:-1]
y = df1.iloc[:,-1]

X.head()

#treating missing values 
from scipy.stats import mode
X= X.fillna({"psa":X.psa.median(),
             "num_ro5_violations":X.num_ro5_violations.mode(),
             "mw_monoisotopic":X.mw_monoisotopic.mean(),
             "mw_freebase": X.mw_freebase.mean(),
             "heavy_atoms": X.heavy_atoms.median(),
             "hbd_lipinski": X.heavy_atoms.median(),
             "hba_lipinski": X.heavy_atoms.median(),
             "alogp":X.alogp.mean(),
             "aromatic_rings":X.aromatic_rings.median(),
             "hba":X.hba.median(),
             "hbd":X.hbd.median(),
             "num_lipinski_ro5_violations": 0.0,
             "qed_weighted":X.qed_weighted.mean(),
             "rtb":X.rtb.median()})

"""### Skewness in data distribution of original dataset"""

X_skew = X.skew()
skewness = X_skew[abs(X_skew) > 0.5] 
skewed_features = skewness.index
print(skewed_features)
skewness

import numpy as np

#skewness treatment taking/trasnforming
xsk=X.iloc[:,:]
xsk[skewed_features] = np.log1p(xsk[skewed_features])
#xsk =
xsk.skew()

#removing highly skewed variables
X_skew_removed = xsk.drop(["num_lipinski_ro5_violations", "num_ro5_violations","molecular_species_1","molecular_species_2",
       "molecular_species_3","molecular_species_4","molecular_species_5","ro3_pass_1","ro3_pass_2"], axis = 1 )

X_skew_removed.skew()

import seaborn as sns 
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# visualising the distribution
sns.pairplot(X_skew_removed)
plt.show()

X_skew_removed.head(40)

X_skew_removed["alogp"] = X_skew_removed["alogp"].interpolate()

X_skew_removed.head(40)

"""#### Skewness in data distribution of generated molecules data."""

skewness = X_skew[abs(X_skew) > 0.5] 
skewed_features = skewness.index
X_skew1 = X_test1.skew()
xsk1 = X_test1.iloc[:,:]
xsk1[skewed_features] = np.log1p(xsk1[skewed_features])
#xsk =
xsk1.skew()

X_test1 = xsk1.drop(["num_lipinski_ro5_violations", "num_ro5_violations", "ro3_pass"],axis =1)

"""#### logistic regression"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
#Logistic regression 
def logistic_reg(a,b):
    """LogisticRegression classifier with optimised parameters ,
    stratifiedKfold is used for imbalance data  """ 
    import seaborn as sns 
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    #from sklearn.model_selection import KFold
    from sklearn.model_selection import StratifiedKFold 
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn import metrics
    
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.25, random_state=42)
    model_lr = LogisticRegression(penalty='l1',n_jobs=-1)
    model_lr.fit(X_train,y_train)
    y_pred=model_lr.predict(X_test)
    
    str_kfold = StratifiedKFold(n_splits=10, random_state=42)
    accuracy = cross_val_score(model_lr, a, b, cv=str_kfold,scoring='accuracy')
    print('cross_ validation Accuracy : ',np.mean(accuracy))
    
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    #print(confusion_matrix)
    sns.heatmap(confusion_matrix, annot=True)
    plt.show()
    return model_lr 
    

logistic_reg(X_skew_removed,y)

"""#### k-NN classifier"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
def knn_classifier(a,b):
    """K-nearest neighbour classifier with optimised parameters.
    """
    #Spliting data into train/validation sets 
    from sklearn.model_selection import train_test_split
    #from sklearn.model_selection import KFold
    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import GridSearchCV
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.25, random_state=42)
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    #y_pred=model.predict(X_test)
    
    #validating the model
    str_kfold = StratifiedKFold(n_splits=10, random_state=42) #giving better result
    
    param_grid = dict(n_neighbors=[3,4,5,6,7,8,9])
    grid_model = GridSearchCV(model, param_grid, scoring='accuracy', n_jobs=-1, cv=str_kfold)
    grid_result = grid_model.fit(a, b)
    y_pred = grid_model.predict(X_test)
    
    #print(a.columns)
    
    print(f"best parameters:{grid_result.best_params_ } , best accuracy:{grid_result.best_score_}")
    
    accuracy = cross_val_score(grid_model, a, b, cv=str_kfold,scoring='accuracy')
    print('cross_ validation Accuracy : ',np.mean(accuracy))
    return grid_model
    

knn_classifier(X_skew_removed,y)

"""#### Random-Forest classifier"""

#random forest
def rf_classifier(a,b):
    """RandomForest classifier with optimised parameters.
    """
    #Spliting data into train/validation sets 
    from sklearn.model_selection import train_test_split
    #from sklearn.model_selection import KFold
    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import GridSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.3, random_state=42)
    
    rf = RandomForestClassifier()
    str_kfold = StratifiedKFold(n_splits=10, random_state=42)
    param_grid = dict(n_estimators=np.arange(10,60,5),criterion=["gini","entropy"])
    
    grid_model = GridSearchCV(rf, param_grid, scoring='accuracy', n_jobs=-1, cv=str_kfold)
    grid_result = grid_model.fit(X_train, y_train)
    
    print(grid_result.best_params_ , grid_result.best_score_)
    
    accuracy = cross_val_score(grid_model, X_test, y_test, cv=str_kfold,scoring='accuracy')
    print('cross_ validation Accuracy : ',np.mean(accuracy))
    return grid_model

classifier = rf_classifier(X_skew_removed,y)

!pip install xgboost

"""#### XGBoost classifier"""

def xgb_classifier(a,b):
    """XGBoost classifier with optimised parameters.
    """
    #Spliting data into train/validation sets 
    from sklearn.model_selection import train_test_split
    #from sklearn.model_selection import KFold
    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import GridSearchCV
    from xgboost import XGBClassifier
    from sklearn import metrics
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.25, random_state=42)
    
    xgb = XGBClassifier()
    #xgb.fit(X_train, y_train)
    param_grid = dict(learning_rate=[0.01,0.05,0.10,0.2,0.3], 
                      n_estimators=np.arange(1,50,10), 
                      reg_alpha = np.arange(0.1,1,0.2),
                      max_depth=[2,4,6,8], 
                      gamma=[0,1,5])
    
    str_kfold = StratifiedKFold(n_splits=10, random_state=42)
    
    grid_model = GridSearchCV(xgb, param_grid, scoring='accuracy', n_jobs=-1, cv=str_kfold)
    grid_result = grid_model.fit(X_train,  y_train)
    
    print(grid_result.best_params_ , grid_result.best_score_)
    best_parm = grid_result.best_params_ 
    model = XGBClassifier(learning_rate=best_parm["learning_rate"],
                      objective="binary:logistic", 
                      n_estimators=best_parm["n_estimators"], 
                      reg_alpha = best_parm["reg_alpha"],
                      max_depth=best_parm["max_depth"], 
                      gamma=best_parm["gamma"])
    model.fit(X_train, y_train)
    accuracy = cross_val_score(model,  X_test, y_test, cv=str_kfold,scoring='accuracy')
    print('cross_ validation Accuracy : ',np.mean(accuracy))
    return model

model_xgb = xgb_classifier(X_skew_removed,y)

model_xgb.feature_importances_

"""#### Predicting the generated molecules"""

#Random forest and Xgboost models gave the same average accuracy; used Random Forest for this example
pred = classifier.predict(X_test1)

"""####Genetic Algorithm"""

#download the tpot classifier
!pip install tpot

from tpot import TPOTClassifier

def geneticModel(a,b):
  X_train, X_test, y_train, y_test = train_test_split(a, b,
  train_size=0.75, test_size=0.25)

  tpot = TPOTClassifier(generations=12, population_size=100, verbosity=2)
  tpot.fit(X_train,y_train)
  print(classifier.score(X_test, y_test))
  return tpot

classifier = geneticModel(X_skew_removed,y)

pred = classifier.predict(Xtest1)

pred