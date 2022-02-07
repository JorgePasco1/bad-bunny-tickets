"""Entry file of the program."""


from config import NUMBER_OF_QUEUES
from ticket_queue_service import multiple_queueing


def run():
    """
    This is the main function of the program.
    """
    multiple_queueing(NUMBER_OF_QUEUES)


if __name__ == "__main__":
    run()
