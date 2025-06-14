#!/usr/bin/env python3
import argparse
import sys
from app.cli.list_configured_command import list_configured
from app.cli.list_providers_command import list_providers
from app.cli.connect_command import connect_vpn
from app.cli.disconnect_command import disconnect_vpn
from app.cli.remove_command import remove_vpn
from app.cli.setup_command import setup_vpn

def main():
    parser = argparse.ArgumentParser(
        description="VPN Switchboard: Manage VPN connections.",
        prog="vpn-manager"
    )
    parser.set_defaults(func=lambda args: parser.print_help()) # Default action

    subparsers = parser.add_subparsers(title="Commands", dest="command", help="Available commands")

    # List providers command
    list_providers_parser = subparsers.add_parser("list-providers", help="List supported VPN providers")
    list_providers_parser.set_defaults(func=list_providers)

    # List configured VPNs command
    list_configs_parser = subparsers.add_parser("list-configs", help="List all configured VPN configurations")
    list_configs_parser.set_defaults(func=list_configured)

    # Connect command
    connect_parser = subparsers.add_parser("connect", help="Connect to a VPN")
    connect_parser.add_argument("vpn_name", help="Name of the VPN to connect to")
    connect_parser.set_defaults(func=connect_vpn)

    # Disconnect command
    disconnect_parser = subparsers.add_parser("disconnect", help="Disconnect from a VPN")
    disconnect_parser.add_argument("vpn_name", nargs='?', help="Name of the VPN to disconnect from (optional, defaults to current)")
    disconnect_parser.set_defaults(func=disconnect_vpn)

    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a VPN configuration")
    remove_parser.add_argument("vpn_name", help="Name of the VPN configuration to remove")
    remove_parser.set_defaults(func=remove_vpn)

    # Setup command
    setup_parser = subparsers.add_parser("setup", help="Setup a new VPN configuration")
    setup_parser.add_argument("vpn_name", help="Name of the VPN configuration to setup")
    setup_parser.set_defaults(func=setup_vpn)

    # If no arguments are provided (only script name), print help.
    # The `parser.set_defaults(func=lambda args: parser.print_help())` handles cases
    # where a command is not recognized or if no command is given.
    # However, to explicitly show help when *only* the script name is run,
    # we can check sys.argv length.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    # Call the function associated with the chosen subcommand
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # This case should ideally be covered by set_defaults on the main parser
        # or if a subcommand is required.
        parser.print_help(sys.stderr)


if __name__ == "__main__":
    main()
