from shared_memory_dict import SharedMemoryDict
from time import sleep
# from multiprocessing.shared_memory import SharedMemory

smd_config1 = SharedMemoryDict(name='config', size=1024)
existing_smd = SharedMemoryDict(name='tokens', size=1024)

# abbMsg_Dict = SharedMemoryDict(name='config', size=1024)
# msg_from_abb = SharedMemoryDict(name='msg_from_abb', size=1024)
# smd_config = SharedMemoryDict(name='config', size=1024)
# smd_config2 = SharedMemoryDict(name='config2', size=1024)
# shared_mem1 = SharedMemory(name='MyMemory', create=False)

while True:
    print(smd_config1[0])
    existing_smd[0] = "hello from halcon"

    sleep(1)