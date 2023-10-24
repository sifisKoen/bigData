# bigData


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

`sudo docker run body-temp-app`


## Run docker under network 

`sudo docker run --network=ehealth-net body-temp-app`