import json

from create import vultr_call
if __name__ == '__main__':

    #
    # plans = vultr_call("GET", "plans/list")
    #
    # for key in plans:
    #     print(plans[key])
    #
    # regions = vultr_call("GET", "regions/list")
    #
    # for key in regions:
    #     print(regions[key])
    #
    oss = vultr_call("GET", "os/list")
    for key in oss:
        print(oss[key])

    with open("data/os.json", "w") as f:
        f.write(json.dumps(oss, indent=4))

    apps = vultr_call("GET", "app/list")

    for key in apps:
        print(apps[key])

    with open("data/app.json", "w") as f:
        f.write(json.dumps(apps, indent=4))
