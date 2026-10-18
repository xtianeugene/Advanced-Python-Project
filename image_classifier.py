import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

transform = transforms.ToTensor()
train = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
loader = torch.utils.data.DataLoader(train, batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 128), nn.ReLU(),
    nn.Linear(128, 10)
)
opt = optim.Adam(model.parameters())
loss_fn = nn.CrossEntropyLoss()

for epoch in range(1):
    for x, y in loader:
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward(); opt.step()
    print(f"Epoch {epoch+1} done. | Loss: {loss.item():.4f}")