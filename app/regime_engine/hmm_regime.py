import numpy as np
from hmmlearn.hmm import GaussianHMM

class HMMRegime:

    def train(self, returns, n_states=3):

        model = GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=1000)
        model.fit(returns.reshape(-1, 1))

        self.model = model
        return model

    def detect(self, returns):

        hidden_states = self.model.predict(returns.reshape(-1, 1))
        return hidden_states
