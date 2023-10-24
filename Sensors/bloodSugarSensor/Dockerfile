FROM golang:latest 
WORKDIR /bloodSugarSensor
COPY . .
RUN go build -o bloodSugarApp bloodSugarSensor.go
CMD ["./bloodSugarApp"]
