import joblib

def test_that_for_set_input_feature_returns_label_with_class_zero():

    model = joblib.load('model/logistic_model.pkl')

    input_feature_1 = [[17.99, 10.38, 122.8, 1001.]]
    input_feature_2 = [[7.76, 24.54, 47.92, 181.]]

    assert model.predict(input_feature_1) == 0
    assert model.predict(input_feature_2) == 1