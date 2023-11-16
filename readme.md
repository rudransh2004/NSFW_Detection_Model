# NSFW Detection Model for EmeraldChat

## Step 1: Clone the GitHub Repo

```bash
git clone https://github.com/Aqua-123/NSFW_Detection_Model.git
```
```bash
cd NSFW_Detection_Model
```

## Step 2: Create a Python Virtual Environment

1. **Install Python**: Ensure you have Python 3.x installed on your system. You can download it from the official Python website (https://www.python.org/downloads/) or use your system's package manager.

2. **Install Virtualenv (if not already installed)**: Virtualenv is a tool to create isolated Python environments. You can install it using pip, which is the Python package manager. Open your terminal and run:

```bash
   pip install virtualenv
```

3. **Create a Virtual Env**: 

```bash
python3 -m venv /root/venv/NSFW_Detection
```

4. **Activate Virtual Enviorment**:

```bash
source /root/venv/NSFW_Detection/bin/activate
```


## Step 3: Install pip requirements:

```bash
pip3 install -r requirements.txt
```

### Step 4: Run the python script

```bash
python model_load.py
```