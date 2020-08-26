from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from impyute.imputation.cs import mice

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
#Estandarizo las notas promedio de los estudiantes.
class ScaleColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        min_max_scaler = MinMaxScaler()
        for i in range(3):
            data[self.columns] = min_max_scaler.fit_transform(data[self.columns])
        return data

class MiceImputation(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        data = mice(data)
        return data   
    
 class UnderOverSampling(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        count_class_acep, count_class_sosp = data.OBJETIVO.value_counts()
        df_class_acep = data[data['OBJETIVO'] == 'Aceptado']
        df_class_sosp = data[data['OBJETIVO'] == 'Sospechoso']
        
        #Random under-sampling
        df_class_acep_under = df_class_acep.sample(count_class_sosp*3)
        df_test_under = pd.concat([df_class_acep_under, df_class_sosp], axis=0)
        
        #Random over-sampling
        df_class_sosp_over = df_class_sosp.sample(count_class_sosp*3, replace=True)
        df_test_over = pd.concat([df_class_acep, df_class_sosp_over], axis=0)
        
        df_acep = pd.DataFrame(
        df_test_under[df_test_under['OBJETIVO'] == 'Aceptado']
        )
        df_sosp = pd.DataFrame(
        df_test_over[df_test_over['OBJETIVO'] == 'Sospechoso']
        )

        frames = [df_acep, df_sosp]
        df_result = pd.concat(frames)
        return df_result
