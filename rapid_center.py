import os
import psutil
import json

class RapidCenter:
    def __init__(self):
        self.storage_data = {}

    def gather_storage_info(self):
        """Gather information about all disk partitions and their usage."""
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                self.storage_data[partition.device] = {
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percent': usage.percent
                }
            except PermissionError:
                continue

    def analyze_storage(self):
        """Analyze storage data to find partitions with critical usage levels."""
        critical_partitions = {}
        for device, data in self.storage_data.items():
            if data['percent'] > 90:  # Consider 90% as critical usage level
                critical_partitions[device] = data
        return critical_partitions

    def manage_storage(self):
        """Placeholder for storage management logic."""
        critical_partitions = self.analyze_storage()
        if critical_partitions:
            print("Critical storage levels detected in the following partitions:")
            for device, data in critical_partitions.items():
                print(f"Device: {device}, Usage: {data['percent']}%")
        else:
            print("All partitions are within safe usage levels.")

    def save_report(self, filename='storage_report.json'):
        """Save the current storage analysis report to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.storage_data, file, indent=4)
        print(f"Storage report saved as {filename}")

    def run(self):
        """Execute the main program logic."""
        self.gather_storage_info()
        self.manage_storage()
        self.save_report()

if __name__ == "__main__":
    rc = RapidCenter()
    rc.run()