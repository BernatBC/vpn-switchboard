# VPN Switchboard
VPN Switchboard is a desktop application written in Python that enables users to manage and switch between multiple VPN providers seamlessly. With an intuitive interface, it simplifies connecting, disconnecting, and monitoring VPN connections from a single place.

## Features

- Manage multiple VPN providers from one app
- Easy connect/disconnect functionality
- Status monitoring for active VPN connections
- Cross-platform support
- CLI and GUI

## Supported VPN Services

| VPN Service        | Status |
|--------------------|--------|
| ProtonVPN          | ✅     |
| WireGuard          | WIP    |
| Cloudflare WARP    | WIP    |
| OpenVPN            | WIP    |

## Installation

Comming soon

## Development instructions
You'll need to have `python` installed.

### Setting up the environment
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Building and running
```sh
pip install -e .
```

## Usage

### Setting up a service
```sh
vpn-switchboard setup $service
```

### Connect to a vpn
```sh
vpn-switchboard connect $service
```

### Disconnect a vpn
```sh
vpn-switchboard disconnect $service
```

### List of services
```sh
warp # Cloudflare warp
protonvpn # ProtonVPN
openvpn # OpenVPN
wireguard # Wireguard
```
