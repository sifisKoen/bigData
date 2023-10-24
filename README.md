# bigData


## Create Docker network

`docker network create ehealth-net`

## Sensors

For sensors we used Go lang. And encapsulated them in Docker containers. Each Sensor is in a separate directory for better organize. In each directory there is a `Dockerfile` for the sensors so to create our containers.

### Docker containers

To build your `Docker container` you need to move into the sensor directory.

For example:

```cmd
cd Sensors/bodyTempSensor
```

Then you just need to build and run the `Dockerfile`

Run:

`sudo docker build -t body-temp-app  .`

**Perfect now you have your container image build on your Docker**

Run this command to see your images:

`sudo docker images`

You will see something like this:

```
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
body-temp-app            latest    2d53db058525   8 minutes ago    842MB
```

If you see something like this that means you have your image.

To run your image you just need:

## Run docker under network 

`sudo docker run --network=ehealth-net body-temp-app`


## Run rubbitMQ

```cmd
docker run -d --name my-rabbitmq \
    --network ehealth-net \
    -p 5672:5672 \
    -p 15672:15672 \
    -e RABBITMQ_DEFAULT_USER=guest \
    -e RABBITMQ_DEFAULT_PASS=guest \
    rabbitmq:management
```

## Run Python

`sudo docker build -t ehealth-backend  .`
`sudo docker run -d --name ehealth-backend --network ehealth-net ehealth-backend`

## Argo Workflow and Kubernetes

First we need to instal **minikube** and then to install **kubectl**.

* Install minikube: [https://minikube.sigs.k8s.io/docs/start/]

After installation of minikube you need to install **kubectl**

`minikube kubectl -- get pods -A`

### Argo Workflow

#### Create Argocd namespace

`kubectl create namespace argocd`
`kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`

#### Forward the port

`kubectl get svc -n argocd`

`kubectl port-forward -n argocd svc/argocd-server 8080:443`

From this command you will see something like:

`Forwarding from 127.0.0.1:8080 -> 8080`

Now if you go to your browser and copy the `127.0.0.1:8080` you should be able to see the **Argo Flow UI**. From there you just need to add the user name and the password. The default username is: `admin`

For the password you need to:

`kubectl -n argocd get secret argocd-initial-admin-secret -o yaml`

And from this you will take the default hashed password for the admin user. So you need to decode this password.

`echo RzUzVlp0V0daclJlZXJrRQ== | base64 --decode`
