FROM python:3.9

WORKDIR src/my_plotting_utils

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "testing.py"]