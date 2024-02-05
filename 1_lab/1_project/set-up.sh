#!/bin/bash
echo "Start"
# Наступна команда буде створювати віртульне середовище
python -m venv ./project_requests
# далі нам потрібно встановити всі бібліотеки, всередині нашого віртуального середовища
source project_requests/Scripts/activate
pip install requests
deactivate
echo "Finish"