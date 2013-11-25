import yaml

with open('config.yaml') as f:
    print(yaml.load(f))

    