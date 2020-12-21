from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Sorry to hear about your breakup with docker );"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# RUN with docker:
# docker run -p 5001:5000 natelliu/k8_flask:v1

# RUN with kubernetes
# minikube start
# kubectl apply -f deployment.yaml

"""
kubernetes_flask % kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
hello-python-6c7b478cf5-45lkg   1/1     Running   0          39h
hello-python-6c7b478cf5-hkpqv   1/1     Running   0          39h
hello-python-6c7b478cf5-jfdxw   1/1     Running   0          39h
hello-python-6c7b478cf5-p99cq   1/1     Running   0          39h
kubernetes_flask % curl localhost:6000             

Sorry to hear about your breakup with docker );
"""

# for debugging https://kubernetes.io/docs/tasks/debug-application-cluster/debug-service/
