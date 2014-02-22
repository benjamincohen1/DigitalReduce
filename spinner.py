import digitalocean
from dop.client import Client


def main():
    client_id = 'ce302478afc77902c6fb05ba4ca5683e'
    api_key = 'e4a865a093fe5c2f704c194e91135b74'


    client = Client(client_id, api_key)
    images = client.images()
    sizes = client.sizes()

    job_id = 'testjob'
    for x in range(3):
        drop_name = job_id + '-' + str(x)
        client.create_droplet(name=drop_name)

def kill_all_droplets():
    for x in client.show_active_droplets():
        client.power_off_droplet(x.id)


def destroy_all_droplets():
    for x in client.show_active_droplets():
        client.destroy_droplet(x.id)

def print_sizes():
    for x in client.sizes():
        print x.to_json()

def print_regions():
    for x in client.regions():
        print x.to_json()

def print_images():
    for x in client.images():
        print x.to_json()

if __name__ == "__main__":
    client_id = 'ce302478afc77902c6fb05ba4ca5683e'
    api_key = 'e4a865a093fe5c2f704c194e91135b74'


    client = Client(client_id, api_key)

    # destroy_all_droplets()
    # main()
    # print_sizes()

    print_images()
    print_sizes()
    print_regions()