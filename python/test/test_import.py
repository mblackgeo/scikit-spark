def test_model_selection_import():
    from skspark.model_selection import RandomizedSearchCV, GridSearchCV
    assert RandomizedSearchCV is not None
    assert GridSearchCV is not None
