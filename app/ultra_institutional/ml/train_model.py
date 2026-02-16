from sklearn.ensemble import RandomForestClassifier
import joblib

class InstitutionalML:

    def train(self, X, y):
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=6,
            random_state=42
        )
        model.fit(X, y)
        joblib.dump(model, "institutional_model.pkl")
        return model
