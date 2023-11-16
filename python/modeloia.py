import torch
from torchvision import transforms
from torchvision.models import densenet121
from PIL import Image

# Carregue o modelo DenseNet121 pré-treinado
model = densenet121(pretrained=False)
model_path = "C:/Users/vinicius/PycharmProjects/script-logo/ia/densenet121-idenprof-test_acc_0.82550_epoch-95.pt"  # Caminho para o seu modelo

# Modifique o classificador para corresponder ao número de classes desejado (10 classes)
num_ftrs = model.classifier.in_features
model.classifier = torch.nn.Linear(num_ftrs, 10)

model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Carregue e pré-processe a imagem
image_path = "screenshot.png"  # Caminho para a imagem
image = Image.open(image_path)
preprocess = transforms.Compose([transforms.Resize(256),
                                 transforms.CenterCrop(224),
                                 transforms.ToTensor(),
                                 transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
image = preprocess(image)
image = image.unsqueeze(0)  # Adicione uma dimensão para corresponder à entrada do modelo

# Faça a inferência
with torch.no_grad():
    output = model(image)

# Carregue os rótulos da classe
class_labels_path = "C:/Users/vinicius/PycharmProjects/script-logo/labels.txt"  # Caminho para o arquivo de rótulos
with open(class_labels_path) as f:
    class_labels = f.read().splitlines()

# Obtenha a classe prevista
_, predicted_class = output.max(1)
class_label = class_labels[predicted_class]

print("Classe prevista:", class_label)
