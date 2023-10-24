FROM golang:latest 
WORKDIR /bodyTempSensor
COPY . .

COPY  go.mod go.sum ./
RUN go mod download

RUN go build -o bodyTempApp .
CMD ["./bodyTempApp"]
