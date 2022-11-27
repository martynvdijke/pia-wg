

__version__ = "0.1.0"
__author__ = "Martyn van Dijke"
__copyright__ = "Martyn van Dijke"
__license__ = "GPL License"

from . import piawg
from . import generate_config
import argparse
import logging

_logger = logging.getLogger(__name__)


def parse_args(args):
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Generate PIA wireguard config')
    parser.add_argument('-u', '--username', dest=username,
                        help="PIA username to use", required=False)
    parser.add_argument('-p', '--password', dest=password,
                        help="PIA password to use", required=False)
    parser.add_argument('-r', '--region', dest='region', choices=[
                        "auto"]+regions, help='Allowed values are '+', '.join(regions), metavar='')
    parser.add_argument('--sort-latency', action='store_true',
                        help='Display lowest latency regions first (requires root)')
    args = parser.parse_args()
