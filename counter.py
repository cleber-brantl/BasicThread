import time

# Global variable to hold the secondary counter value
secondary_count = 0

def secondary_counter(stop_event):
    """
    Continuously increments and prints the secondary counter every second,
    until the stop_event is set.
    """
    global secondary_count
    while not stop_event.is_set():
        secondary_count += 1
        print(f'Secondary count (from thread): {secondary_count}')
        time.sleep(1)
    print('Secondary counter stopped.')

def get_secondary_count():
    """Returns the current value of the secondary counter."""
    return secondary_count
