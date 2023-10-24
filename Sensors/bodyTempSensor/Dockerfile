FROM golang:latest 
WORKDIR /bodyTempSensor
COPY . .
RUN go build -o bodyTempApp bodyTempSensor.go
CMD ["./bodyTempApp"]
