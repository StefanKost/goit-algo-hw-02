import queue
import time
import random

# Create a request queue
request_queue = queue.Queue()

# Unique ID counter
request_id = 1


def generate_request():
    """Generates a new request and adds it to the queue"""
    global request_id
    request = {
        'id': request_id,
        'description': f"Request {request_id}: data {random.randint(100, 999)}"
    }
    request_queue.put(request)
    print(f"New request added to queue: {request}")
    request_id += 1


def process_request():
    """Processes a request from the queue if any exist"""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing request: {request}")
    else:
        print("Queue is empty, nothing to process.")


def main():
    try:
        # Generate several request
        for _ in range(2):
            generate_request()

        while True:
            # Generate a new request randomly
            if random.randint(0, 1) == 1:
                generate_request()
                time.sleep(1)
            else:
                print('Skip request generation')

            # Process a request
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
