python -m grpc_tools.protoc -I../src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../src/main/proto/GreetingService.proto
