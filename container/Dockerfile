FROM python:3.8.5
WORKDIR /C:\Users\aditd\OneDrive\Documents\My documents\sem7\project 1\Containerized-AI-for-Anomaly-Detection-master\container

COPY requirements.txt /C:\Users\aditd\OneDrive\Documents\My documents\sem7\project 1\Containerized-AI-for-Anomaly-Detection-master\container
RUN pip install -r ./requirements.txt

COPY app.py /C:\Users\aditd\OneDrive\Documents\My documents\sem7\project 1\Containerized-AI-for-Anomaly-Detection-master\container
COPY Cloud_model.h5 /C:\Users\aditd\OneDrive\Documents\My documents\sem7\project 1\Containerized-AI-for-Anomaly-Detection-master\container
COPY scaler_data /C:\Users\aditd\OneDrive\Documents\My documents\sem7\project 1\Containerized-AI-for-Anomaly-Detection-master\container

#ENV FLASK_DEBUG=1

CMD ["python", "app.py"]
