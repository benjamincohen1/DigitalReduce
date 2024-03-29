# import digitalocean
from dop.client import Client


def spawn(client, num_instances = 5):
    client_id = 'ce302478afc77902c6fb05ba4ca5683e'
    api_key = 'e4a865a093fe5c2f704c194e91135b74'


    client = Client(client_id, api_key)
    print "HERE"
    images = client.images()
    sizes = client.sizes()
    print 'before create'
    for x in client.show_active_droplets():
        print x.id
    print 'after create'
    job_id = 'job'
    for x in range(num_instances):
        drop_name = job_id + '-' + str(x)
        client.create_droplet(name=drop_name, image_id = 2393479, size_id=66)

def kill_all_droplets(client):
    for x in client.show_active_droplets():
        if x.id == 1195790 or x.id == str(1195790):
            pass
        else:
            client.power_off_droplet(x.id)

def turn_on_droplet(client, id):
    client.power_on_droplet(id)

    return True


def destroy_all_droplets(client):
    for x in client.show_active_droplets():
        if x.id == 1195790 or x.id == str(1195790):
            pass
        else:
            client.destroy_droplet(x.id)

def print_sizes(client):
    for x in client.sizes():
        print x.to_json()

def print_regions(client):
    for x in client.regions():
        print x.to_json()

def print_images(client):
    for x in client.images():
        print x.to_json()


def initialize(client_id = 'ce302478afc77902c6fb05ba4ca5683e',\
               api_key = 'e4a865a093fe5c2f704c194e91135b74'):
    client_id = client_id
    api_key = api_key


    client = Client(client_id, api_key)
    # if client != None:
    return client



if __name__ == "__main__":
    client_id = 'ce302478afc77902c6fb05ba4ca5683e'
    api_key = 'e4a865a093fe5c2f704c194e91135b74'


    client = Client(client_id, api_key)

    # destroy_all_droplets(client)
    #main()
    # for x in client.show_active_droplets():
    #     print x.name
        # print x.id
    # print_sizes(client)
    spawn(client, 4)
    # print_images()
    # print_sizes()
    # print_regions()
