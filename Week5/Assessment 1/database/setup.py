#! /usr/bin/env python3
from data.schema import schema
from data.seed import seed

def run():
    schema()
    seed()


if __name__ == "__main__":
    run()