import asyncio
import logging

import grpc
import GreetingService_pb2_grpc
import GreetingService_pb2


async def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = GreetingService_pb2_grpc.GreetingServiceStub(channel)
        response: GreetingService_pb2.HelloResponse = stub.greeting(GreetingService_pb2.HelloRequest(name='John'))
        print("Greeter client received: " + response.greeting)
        response: GreetingService_pb2.HelloResponse  = stub.greeting(GreetingService_pb2.HelloRequest(name='Jenny'))
        print("Greeter client received: " + response.greeting)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
