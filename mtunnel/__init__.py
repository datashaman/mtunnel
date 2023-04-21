#!/usr/bin/env python3

import bgtunnel
import click
import time
import yaml


@click.command()
@click.pass_context
@click.argument('stage')
@click.option('--config', default='mtunnel.yml')
def main(ctx: click.Context, stage: str, config: str):
    with open(config, 'r') as f:
        config = yaml.safe_load(f)

    if stage not in config['tunnels']:
        click.echo('Stage not found in tunnels')
        ctx.exit(1)

    for tunnel_id, tunnel in config['tunnels'][stage].items():
        if tunnel.pop('enabled', True):
            connection['forwarder'] = bgtunnel.open(**{
                **config['jumpbox'],
                **tunnel,
            })

    while True:
        time.sleep(0.5)
