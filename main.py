import time
import threading

from counter import secondary_counter, get_secondary_count

# Event to signal the secondary counter thread to stop
stop_event = threading.Event()

def start_secondary_counter():
    """Starts the secondary counter in a separate daemon thread."""
    thread = threading.Thread(target=secondary_counter, args=(stop_event,))
    thread.daemon = True
    thread.start()
    return thread  # Return the thread to optionally join it later

def main_counter_loop():
    """Main counter loop that prints both counters."""
    primary_counter = 1
    try:
        while True:
            print(f'Primary count: {primary_counter}')
            print(f'Secondary count: {get_secondary_count()}')
            primary_counter += 1
            time.sleep(2)
    except KeyboardInterrupt:
        stop_event.set()
        time.sleep(1.1)  # Wait a moment to let the thread print its stop message
        print('\nMain and second counter interrupted.')

def main():
    """Entry point of the program."""
        start_secondary_counter()
        main_counter_loop()      
        print('Program terminated.')

if __name__ == "__main__":
    main()
