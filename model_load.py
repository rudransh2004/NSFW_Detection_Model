import gradio as gr
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models, transforms
import torch.nn as nn

# Load the trained model
model = models.resnet50(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 3)  # Assuming 3 classes
model.load_state_dict(torch.load("NSFW_Model.pth", map_location=torch.device('cpu')))
model = model.to("cpu")  # Move the model to the CPU
model.eval()

# Define the image transformations
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)

# Function to predict the image
def predict_image(image):
    image = Image.fromarray(image.astype("uint8"), "RGB")
    image = transform(image).unsqueeze(0)
    image = image.to("cpu")  # Move the image to the CPU

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        predicted_class = predicted.item()
        
    return f"Predicted class: {predicted_class}"

# Create a Gradio interface
iface = gr.Interface(fn=predict_image, inputs="image", outputs="text")

# Launch the interface
iface.launch(server_name="0.0.0.0")
