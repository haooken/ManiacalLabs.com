import toml
import yaml
import sys


if __name__ == '__main__':
    in_file = sys.argv[0]
    with open(in_file, 'r') as f:
        data = f.read()

    data = toml.loads(data)

    print(yaml.dump(data, default_flow_style=False))
