FROM joyzoursky/python-chromedriver

WORKDIR clicker_lb
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Settings logging
ENV LEVEL="INFO"
ENV GURU="True"
ENV TRACEBACK="false"

# Settings Clicker
# The data is hidden so as not to compromise the resource
ENV BASE_URL=""
ENV LOGIN_URL=""
ENV CHANGE_PASS_URL=""
ENV SEPARATOR_B=""
ENV SEPARATOR_OOP="\n"
ENV DB_B="b.txt"
ENV DB_OOP="oop.txt"
ENV TEST_ID_B=""
ENV TEST_ID_OOP=""
ENV BASE_PASS=""

# Building
RUN pip install --upgrade pip  --no-cache-dir
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY clicker_lb .

CMD python main.py
