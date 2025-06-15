import grpc
import university_pb2
import university_pb2_grpc
from google.protobuf import empty_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = university_pb2_grpc.BookServiceStub(channel)

        print("📚 Kitap Listesi:")
        response = stub.ListBooks(empty_pb2.Empty())
        for book in response.books:
            print(f"- {book.title} by {book.author} (Stock: {book.stock})")

if __name__ == "__main__":
    run()
