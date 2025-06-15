from concurrent import futures
from grpc_reflection.v1alpha import reflection
import grpc
import uuid
import university_pb2
import university_pb2_grpc
from google.protobuf import empty_pb2

# Mock veri ile çalışan Book servisi
class BookServiceServicer(university_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.books = [
            university_pb2.Book(
                id=str(uuid.uuid4()),
                title="1984",
                author="George Orwell",
                isbn="9780451524935",
                publisher="Penguin",
                pageCount=328,
                stock=3
            ),
            university_pb2.Book(
                id=str(uuid.uuid4()),
                title="Sapiens",
                author="Yuval Noah Harari",
                isbn="9780062316097",
                publisher="Harper",
                pageCount=498,
                stock=5
            )
        ]

    def ListBooks(self, request, context):
        return university_pb2.BookList(books=self.books)

    def GetBook(self, request, context):
        for book in self.books:
            if book.id == request.id:
                return book
        context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

    def CreateBook(self, request, context):
        new_book = university_pb2.Book(
            id=str(uuid.uuid4()),
            title=request.title,
            author=request.author,
            isbn=request.isbn,
            publisher=request.publisher,
            pageCount=request.pageCount,
            stock=request.stock
        )
        self.books.append(new_book)
        return new_book

    def UpdateBook(self, request, context):
        for i, book in enumerate(self.books):
            if book.id == request.id:
                self.books[i] = request
                return request
        context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

    def DeleteBook(self, request, context):
        self.books = [book for book in self.books if book.id != request.id]
        return empty_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(), server)

    from grpc_reflection.v1alpha import reflection
    SERVICE_NAMES = (
        university_pb2.DESCRIPTOR.services_by_name['BookService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    print("🚀 Server running at port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
