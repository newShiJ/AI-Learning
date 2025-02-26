## 自动求导

import torch

x = torch.arange(4.0)
print(x)

# 标记跟踪 后续操作 可以进行求导
x.requires_grad_(True)  # 等价于x=torch.arange(4.0,requires_grad=True)
x.grad  # 默认值是None