import torch
import torch.nn as nn

class MultiLinearRegression(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.linear(x)

def load_model(input_dim, path):
    model = MultiLinearRegression(input_dim)
    model.load_state_dict(torch.load(path))
    model.eval()
    return model
