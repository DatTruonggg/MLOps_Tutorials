from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from prediction_model.config import config
from prediction_model.processing import preprocessing as pp

classification_pipeline = Pipeline(
    [
        ('MeanImputation', pp.MeanImputer(variables=config.NUM_FEATURES)),
        ('ModelImputation', pp.ModelImputer(variables=config.CAT_IMPUTATION)),
        ('DomainProcessing', pp.DomainProcessing(variable_to_modify=config.FEATURE_TO_MODIFY, variable_to_add=config.FEATURE_TO_ADD)),
        ('DropFeatures', pp.DropColumn(variables_to_drop=config.DROP_FEATURE)),
        ('LabelEncoder', pp.CustomLabelEncoder(variables=config.FEATURE_TO_ENCODE)),
        ('LogTransformation', pp.LogTransformation(variables=config.LOG_FEATURE)),
        ('MinMaxScaler', MinMaxScaler()),
        ('LogisticClassifier', LogisticRegression(random_state=0))
    ]
)
