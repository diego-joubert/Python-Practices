class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")


with HelloContextManager() as hello:
    h = hello
    print(f"Recurso alojado en {h=}")
