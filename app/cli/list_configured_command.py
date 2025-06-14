from app.core.vpn_configurations import list_configurations

def list_configured(args):
    """Lists all configured VPNs."""
    configurations = list_configurations()
    if not configurations:
        print("No VPN configurations found.")
    else:
        print("Configured VPNs:")
        for config in configurations:
            print(config)