import threading
import time
import queue

class Channel:
    def __init__(self):
        self.lock = threading.Lock()
        self.message = None
        self.empty = True

    def send(self, message):
        while not self.empty:
            time.sleep(0.1)
        self.message = message
        self.empty = False

    def receive(self):
        with self.lock:
            while self.empty:
                time.sleep(0.1)
            message = self.message
            self.empty = True
            return message

class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def send(self, message):
        self.queue.put(message)

    def receive(self):
        message = self.queue.get()
        self.queue.task_done()
        return message

def message_handler_using_channel(channel):
    while True:
        message = channel.receive()  # 从通道接收消息
        if message == 'quit':
            break
        # 处理消息的逻辑
        print("Channel: Processing message:", message)
        time.sleep(1)  # 模拟处理消息的耗时操作

def message_handler_using_message_queue(message_queue):
    while True:
        message = message_queue.receive()  # 从消息队列接收消息
        if message == 'quit':
            break
        # 处理消息的逻辑
        print("Message Queue: Processing message:", message)
        time.sleep(1)  # 模拟处理消息的耗时操作

def run_channel_example():
    channel = Channel()

    # 创建多个消息处理线程，使用通道处理消息
    num_threads = 4
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=message_handler_using_channel, args=(channel,))
        t.start()
        threads.append(t)

    # 发送消息到通道
    for i in range(10):
        channel.send(f'Message {i}')

    # 等待所有消息处理线程完成
    for _ in range(num_threads):
        channel.send('quit')

    # 等待所有线程结束
    for t in threads:
        t.join()

    print("Channel: All messages processed")

def run_message_queue_example():
    message_queue = MessageQueue()

    # 创建多个消息处理线程，使用消息队列处理消息
    num_threads = 4
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=message_handler_using_message_queue, args=(message_queue,))
        t.start()
        threads.append(t)

    # 发送消息到队列
    for i in range(10):
        message_queue.send(f'Message {i}')

    # 等待所有消息处理线程完成
    for _ in range(num_threads):
        message_queue.send('quit')

    # 等待所有线程结束
    for t in threads:
        t.join()

    print("Message Queue: All messages processed")

run_channel_example()
run_message_queue_example()

