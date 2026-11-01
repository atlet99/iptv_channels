[![Channels](https://img.shields.io/badge/channels-1100%2B-blue)](#-quick-start)
[![EPG](https://img.shields.io/badge/EPG-XMLTV-green)](#-quick-start)
[![Update](https://img.shields.io/badge/auto--update-every%206h-orange)](../../actions)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

# iptv_channels

> Ready-to-use IPTV playlist files for players (M3U / XMLTV EPG / XSPF).

## :rocket: Quick Start

Add a playlist to your player (Televizo, VLC, Kodi, OTT Navigator, …) by URL:

| File | Purpose | URL |
|------|---------|-----|
| `lgiptv.m3u8` | Channel playlist (M3U, UTF-8) | [raw](https://raw.githubusercontent.com/atlet99/iptv_channels/main/lgiptv.m3u8) |
| `lgiptv-epg.xml.gz` | Program guide (XMLTV, gzip) | [raw](https://raw.githubusercontent.com/atlet99/iptv_channels/main/lgiptv-epg.xml.gz) |
| `lgiptv-epg.xml` | Program guide (XMLTV, plain) | [raw](https://raw.githubusercontent.com/atlet99/iptv_channels/main/lgiptv-epg.xml) |
| `lgiptv.xspf` | Same channels in XSPF (VLC) format | [raw](https://raw.githubusercontent.com/atlet99/iptv_channels/main/lgiptv.xspf) |

**EPG in the player:** the playlist header already carries the `url-tvg` link —
players that read it (e.g. Televizo) set up EPG automatically. Otherwise point
the player's EPG source at `lgiptv-epg.xml.gz`.

> [!NOTE]
> The playlist refreshes automatically every 6 hours
> ([Actions](../../actions)), so simply keep your player pointed at the URL.
> Stream links upstream are time-limited — if a channel does not play,
> refresh the playlist before assuming it is dead.

## :tv: What's inside

- **1100+ channels**: RU / KZ / UZ federals, news, sports, movies, kids, music, regional
- **XMLTV EPG**: ~250 channels with a program grid, `tvg-id` matched exactly
- **Logos**: bundled in [`assets/`](assets/) and referenced per channel
- **Groups**: one clean category per channel (Федеральные, Новости, Спорт, Кино, …)
- Channels from public sources only; dead links are filtered automatically

## :page_facing_up: Disclaimer

<details>
<summary>Legal notice — click to expand</summary>

**:warning: Caution:** Everything in this repository was found in open sources.
Every channel link and piece of metadata was collected solely from **publicly
accessible, unauthenticated endpoints** that third-party services themselves
expose on the open internet. Nothing was hacked, cracked, bypassed or paid for.

- The channel **logos in `assets/` were collected from openly available
  sources** (official channel sites, public channel databases and public
  playlists). The author **does not own these logos and has no connection
  to the channels or their owners**; all trademarks and logos belong to
  their respective owners and are used solely for channel identification
  in a playlist. If you are the owner of a logo and want it removed, open
  an issue and it will be **taken down promptly**.
- The author **is not affiliated with** any of the services or applications
  referenced here, in any way — no partnership, sponsorship, endorsement or
  other connection. Names and trademarks belong to their respective owners
  and are mentioned for identification only.
- The author **does not host, store, retransmit, own or operate** any
  stream. Every link points to a server controlled by a third party whose
  content the author neither selects nor can control.
- The author **does not verify and cannot verify** the legality, origin,
  licensing or availability of any stream, and claims no rights to any of
  it.
- This repository is provided **"AS IS", WITHOUT WARRANTY OF ANY KIND**,
  express or implied — including accuracy, availability, fitness for a
  particular purpose or non-infringement. It is published **for
  informational purposes only**. It is not a service, not an offer, and no
  support is provided.
- **Use at your own risk and be careful.** You are solely responsible for
  compliance with the laws of your jurisdiction and with the terms of
  service of any third party. The author accepts **no liability** for any
  direct or indirect damage arising from the use of this repository —
  including, but not limited to, consequences for your accounts with the
  services in question, legal exposure or data charges.
- Channel availability, geo-restrictions and the legal status of the
  streams may change **at any time and without notice**.
- No credentials, private keys, paid-subscription content or DRM-protected
  material are included. Anything that requires a paid subscription is left
  out on purpose.
- If you are a rights holder and believe something here should not be
  published, open an issue and the referenced material will be **removed
  promptly**.

</details>

## :page_with_curl: License

[MIT](LICENSE)
