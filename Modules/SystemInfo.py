import platform, socket, uuid, psutil, datetime, json

class SystemInfo:
    def __init__(self) -> None:
        pass

    def get_info():
        info = platform.uname()
        system_info = {
            "system": info.system,
            "node": info.node,
            "release": info.release,
            "version": info.version,
            "machine": info.machine,
            "processor": info.processor,
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
            "mac_address": hex(uuid.getnode()),
            "ram": str(psutil.virtual_memory().total) + " KB",
            "boot_time": str(datetime.datetime.fromtimestamp(psutil.boot_time())),
            "disk_info": str(psutil.disk_partitions()),
        }
        return json.dumps(system_info, indent=4)